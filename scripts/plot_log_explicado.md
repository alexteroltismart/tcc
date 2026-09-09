# `plot_log.py` explicado linha por linha

Referência do script de análise gráfica (`plot_log.py`, 307 linhas) que está nesta mesma pasta.
Os números de linha correspondem à versão atual do arquivo. Se editar o script, reconfira.

Para o parse que alimenta este script, ver `weedit_log.md` (§8) e `parse_log_manual.py`.

---

## Linhas 1–10 — docstring do módulo

```python
"""Análise gráfica geral de um log Weedit ao longo do tempo.
...
  python3 plot_log.py [log.zip] [--out DIR] [--step 1s] [--model quadro|ag]
"""
```

Docstring com as 4 saídas e a linha de uso. Fica no topo porque é o primeiro lugar onde alguém
(ou um agente) procura o que o arquivo faz. Não é decoração: `python3 -c "import plot_log; help(plot_log)"`
lê exatamente isso.

## Linhas 11–21 — imports

| Linha | Código | Por quê |
|---|---|---|
| 11 | `import argparse, importlib.util, re` | `argparse` = CLI; `importlib.util` = carregar o parser por caminho (linha 265); `re` = fatiar hex em `hex_to_bits` |
| 12 | `from pathlib import Path` | caminhos como objeto: `Path(...).stem`, `mkdir(parents=True)`, `/` para concatenar |
| 14 | `import matplotlib` | precisa do módulo raiz **antes** de escolher o backend |
| 15 | `matplotlib.use("Agg")` | backend sem tela. **Tem que vir antes do `pyplot`** — sem isso o script quebra em servidor/SSH sem X11 |
| 16 | `import matplotlib.pyplot as plt` | API de figuras |
| 17 | `import numpy as np` | matrizes dos heatmaps e `atleast_1d`/`median` |
| 18 | `import pandas as pd` | séries temporais, `resample`, `DatetimeIndex` |
| 19 | `import matplotlib.dates` | `date2num` na linha 201. Explícito de propósito: funcionava por importação transitiva do `pyplot`, que é um acidente, não um contrato |
| 20 | `import matplotlib.ticker` | `FormatStrFormatter` nas linhas 240–241 |
| 21 | `from matplotlib.colors import LinearSegmentedColormap, ListedColormap` | as duas colormaps próprias (linhas 30 e 31) |

`sys` foi removido — estava importado e nunca usado.

## Linhas 23–24 — constantes de caminho

```python
HERE = Path(__file__).resolve().parent
DEFAULT_LOG = "/home/shared/data/Weedit/s3_bucket/WQR20230004/20260318-155931.zip"
```

- **23**: pasta do próprio script, resolvida (segue symlink). É o que permite achar o
  `parse_log_manual.py` ao lado **independente do diretório de onde você chamou o script**.
- **24**: log de exemplo, para o script rodar sem argumento. É o espelho local do S3
  (`/home/shared/data/Weedit/s3_bucket/{MachineCode}/`).

## Linhas 26–31 — tokens de cor

```python
SURFACE, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
SEQ = LinearSegmentedColormap.from_list("blue_seq", ["#86b6ef", "#3987e5", "#256abf", "#1c5cab", "#0d366b"])
BINARY = ListedColormap([SURFACE, SERIES[0]])
```

- **27**: cinco tokens, cada um com um papel fixo: fundo, tinta primária (títulos), tinta secundária
  (eixos/legenda), tinta apagada (números dos ticks) e a linha do grid. Texto **nunca** usa a cor da
  série — quem carrega identidade é o traço, não a letra.
- **28**: paleta categórica de 8 slots, **em ordem fixa**. A série 1 é sempre azul, a 2 sempre laranja.
  Nunca é ciclada nem gerada: se um painel precisasse de 9 séries, o certo seria dividir o painel.
  Foi validada (pior par adjacente: ΔE 9,1 sob protanopia; ΔE 19,6 em visão normal).
- **30**: rampa **sequencial de um só matiz** para magnitude (CDD/VAR e tempo no GPS). Começa no
  `#86b6ef` porque tudo mais claro que isso desaparece no fundo `#fcfcfb`. Arco-íris (jet, rainbow)
  está fora: distorce a percepção de magnitude.
- **31**: colormap de exatamente 2 cores para máscara binária — fundo = fechado, azul = aberto.
  `ListedColormap` (discreta) em vez de `LinearSegmentedColormap` (contínua) para não sugerir
  meio-tom onde só existe 0 ou 1.

## Linhas 33–40 — `rcParams`: o estilo aplicado uma vez

```python
plt.rcParams.update({...})
```

Em vez de repetir `color=`/`fontsize=` em cada chamada, o estilo entra uma vez no estado global:

| Chave | Efeito |
|---|---|
| `figure.facecolor`, `axes.facecolor`, `savefig.facecolor` | fundo da figura, do painel e **do arquivo salvo**. Sem o terceiro o PNG sai com fundo branco puro, diferente da tela |
| `axes.edgecolor`, `grid.color`, `grid.linewidth: 0.6` | moldura e grid recessivos: o grid orienta, não compete com o dado |
| `axes.labelcolor` (INK2), `axes.titlecolor` (INK) | hierarquia: título mais forte que rótulo de eixo |
| `xtick.color`, `ytick.color` (MUTED) | números dos eixos são o texto menos importante |
| `font.size: 8`, `axes.titlesize: 9`, `legend.fontsize: 7` | 9 painéis numa figura só cabem com tipo pequeno |
| `legend.frameon: False` | caixa de legenda sem borda nem fundo — menos tinta, nada tapado |
| `lines.linewidth: 1.2` | traço fino: com 4 séries sobrepostas, linha grossa esconde as de baixo |

## Linhas 42–73 — `PANELS`: a especificação dos painéis

```python
PANELS = [
    ("Velocidade", "bruto (mm/s ≈ × 0,0036 = km/h)", [
        ("speed", "speed_center", "WDT *SX0:98", 1),
        ...
```

Estrutura: `(título, unidade do eixo Y, [(parte, coluna, rótulo, fator), ...])`.
`parte` é a chave do dicionário devolvido por `convert()` (`speed`, `can`, `details`, `vol`, `cdd`, …);
`coluna` é o nome da coluna lá dentro; `rótulo` é o texto da legenda; `fator` multiplica o valor.

A regra que estrutura tudo: **um painel = uma unidade física**. Nada de eixo Y duplo.

| Linhas | Painel | Detalhe que importa |
|---|---|---|
| 43–46 | Velocidade | três fontes independentes (WDT `*SX0:98`, CAN da bomba, `V` dos detalhes) no mesmo eixo, porque compartilham a unidade bruta. Se as três não se sobrepõem no gráfico, o parse está errado |
| 47–49 | Pressão | `fator=0.1` converte o `P` do log (0,1 kPa) para kPa e põe no mesmo eixo do `can_pressure`. É a checagem cruzada mais barata que existe |
| 50–56 | Vazão | 6 séries em L/min: CAN, previsão da bomba, alvo, nominal, braglia e o flowmeter |
| 57–60 | Taxa | `Usage_mlHa` com `fator=0.001` (ml/ha → L/ha) ao lado do `can_rate` e do alvo `R` |
| 61–63 | Seções e bicos | contagens — `sections_open` (barra) e `current_nozzles_open` (bicos disparando) |
| 64–66 | PWM | `%` |
| 67 | Tensão | uma série só, `VOL/10` (o log guarda décimo de volt inteiro) |
| 68–70 | Delta de velocidade | `wdt_deltac` e `speed_delta` (mesma grandeza: curva) |
| 71 | Luminosidade | `Sunlight` ganhou painel próprio justamente porque **não** é a mesma unidade do delta |

## Linhas 75–82 — `COUNTERS`

```python
COUNTERS = [("details", "Area", "Área acumulada", 1), ...]
```

Mesma tupla, sem título/unidade de painel: cada contador vira **seu próprio painel** (linha 98),
porque área, distância, ml e segundos não compartilham eixo.

## Linhas 85–93 — `get_series`: o filtro único de entrada

```python
def get_series(parts, part, col, factor, step):
    df = parts.get(part)
    if df is None or col not in df.columns:
        return None
    s = pd.to_numeric(df[col], errors="coerce").dropna()
    if s.empty or (s == 0).all():
        return None
    return (s * factor).resample(step).mean().dropna()
```

- **86–88**: `parts.get(part)` em vez de `parts[part]` — parte inexistente devolve `None` em vez de
  `KeyError`. Some a coluna também: máquina sem VAR simplesmente não tem `var`.
- **89**: `to_numeric(errors="coerce")` transforma o que não é número em `NaN` (a coluna de detalhes
  é `object`: mistura número com string, como o nome do bico); o `dropna()` limpa.
- **90–91**: **a decisão de projeto mais útil do script.** Série vazia ou 100% zero devolve `None` e
  desaparece do gráfico — em vez de um traço reto em zero mentindo que "existe e está zerado".
  Quem é descartado é reportado no fim (linhas 298–302), então some do gráfico, não do relatório.
- **92**: escala e reamostra pela média em `step` (default `1s`). Reamostrar é o que mantém o PNG
  leve: um log de 100 ms virando 1 s corta 10× os pontos. `mean()` (não `first()`) porque a média é
  o resumo honesto de um intervalo.

## Linhas 96–132 — `draw_panels`: monta uma figura de painéis empilhados

### 96–110: montar as linhas antes de desenhar

```python
rows = []
for entry in spec:
    if per_panel_axis:                     # counters.png: um painel por série
        s = get_series(parts, *entry[:2], entry[3], step)
        if s is not None:
            s = s - s.iloc[0]              # Δ desde o início da janela
            rows.append((entry[2], "Δ desde o início", [(s, entry[2])]))
    else:
        name, unit, items = entry
        series = [(get_series(parts, p, c, f, step), lab) for p, c, lab, f in items]
        series = [(s, lab) for s, lab in series if s is not None]
```

- **97**: itera a especificação — os dois modos leem a mesma estrutura de tupla.
- **98–99**: modo contador. `*entry[:2]` desempacota `(parte, coluna)` e `entry[3]` é o fator;
  o `entry[2]` (rótulo) não é argumento de `get_series`, é o nome do painel.
- **101**: subtrai o primeiro valor. Um contador acumulado desde a fábrica (`Area = 15.602.975`)
  plotado cru vira uma reta com um `+1.56e7` no canto; em Δ, você lê **quanto rendeu nesta janela**.
- **102**: o título do painel é o rótulo do contador, e a unidade do eixo é "Δ desde o início".
- **104–108**: modo painel. Resolve todas as séries do painel, **descarta as `None`** e só cria o
  painel se sobrou alguma. Painel de máquina que não manda nada simplesmente não aparece.
- **109–110**: nenhuma linha ⇒ devolve `None` sem criar arquivo. Quem chama imprime `--` para essa figura.

### 112–131: desenhar

```python
fig, axes = plt.subplots(len(rows), 1, figsize=(13, 1.9 * len(rows)), sharex=True)
axes = np.atleast_1d(axes)
```

- **112**: uma coluna, N linhas. Altura **proporcional** ao número de painéis (1,9" cada), então a
  figura não fica achatada com 9 painéis nem esticada com 2. `sharex=True` é o ponto do exercício:
  todos os painéis dividem o eixo de tempo, e você lê o evento na vertical, em todas as grandezas.
- **113**: `plt.subplots` devolve um `Axes` solto quando N=1 e um array quando N>1.
  `atleast_1d` normaliza, e o `for` da linha 114 funciona nos dois casos.
- **115–116**: uma linha por série; a cor vem de `SERIES[i % len]` — **índice pela posição na
  especificação**, não pelo valor. Ou seja, a cor segue a entidade: se uma série faltar noutro log,
  as demais não trocam de cor.
- **117**: título. Com 2+ séries a legenda já nomeia tudo; com 1 série o nome dela entra no título
  (`"PWM — pwm_wdt_system"`) e nenhuma legenda é criada. O `series[0][1] == name` evita o
  `"Distância — Distância"` do modo contador, onde título e rótulo são a mesma coisa.
- **118**: `pad=14` abre espaço para a legenda que vai ficar acima do painel; `pad=3` quando não tem.
- **119–121**: rótulo do eixo Y = unidade; grid só horizontal (o eixo de tempo já é compartilhado);
  molduras de cima e da direita removidas.
- **122**: mata a notação de offset (`+1.5316e7`) que o matplotlib inventa em valor grande.
- **123–125**: legenda **fora da área de dados** (`bbox_to_anchor=(0, 1.0)` = colada no topo, à
  esquerda), em até 4 colunas. Foi assim que as colisões com a curva sumiram. `labelcolor=INK2`
  mantém o texto em tinta, não na cor da série.
- **126**: só o painel de baixo recebe "tempo" — com `sharex`, repetir em todos é ruído.
- **127**: título da figura, alinhado à esquerda (`x=0.007, ha="left"`) para casar com os títulos dos painéis.
- **128**: `tight_layout` com `rect` reservando 1,5% no topo para o suptitle.
- **129–130**: salva a 130 dpi e **fecha a figura** — sem o `close`, gerar várias figuras vaza memória.
- **131**: devolve o caminho, que é o sinal de "esta figura existe" para o `main`.

> Bug que já morava aqui: a variável do laço chamava-se `title`, igual ao parâmetro da função, e
> sobrescrevia o título da figura pelo do último painel. Hoje é `panel_title`.

## Linhas 136–145 — `hex_to_bits`: a conversão que erra em silêncio

```python
if not isinstance(hex_str, str):
    return ""
if model == "ag":
    chunks = re.findall("[0-9a-fA-F]{2}", hex_str)
    return "".join(f"{int(c, 16):05b}"[::-1] for c in chunks)
return "".join(f"{int(c, 16):04b}"[::-1] if c in "0123456789abcdefABCDEF" else "0000"
               for c in hex_str)
```

Reproduz as duas convenções de `log_converter_utils.py`:

- **138–139**: `NaN` (float) entra aqui vindo do pandas; devolve string vazia em vez de explodir.
- **141–142**: modo **AG** — agrupa de 2 em 2 (byte) e inverte os bits. Cuidado com `:05b`: é largura
  **mínima**, não corte. Byte ≥ 32 sai com 8 bits, não 5. Não é bug meu, é o comportamento do
  `weedit_ag_hex_to_bin` original — e é a razão de `matrix_bits` cortar pela mediana da largura.
- **143–144**: modo **quadro** (default) — 4 bits por nibble, invertidos. Caractere não-hex vira
  `"0000"`, espelhando o `parse_hex` do repo, que devolve 0 em `ValueError`.

Usar o modelo errado **inverte a barra sem levantar erro**: o gráfico fica bonito e espelhado.
É exatamente por isso que essa função tem `--selftest`.

## Linhas 148–161 — `matrix_bytes`: CDD/VAR (1 byte por bico)

```python
s = s.dropna()
if s.empty:
    return None, None
stride = max(1, len(s) // max_cols)
s = s.iloc[::stride]
width = int(s.str.len().median()) // 2
pairs = [(ts, v) for ts, v in s.items() if len(v) >= width * 2]
rows = [[int(v[i:i + 2], 16) for i in range(0, width * 2, 2)] for _, v in pairs]
if not rows:
    return None, None
return np.array(rows).T, pd.DatetimeIndex([ts for ts, _ in pairs])
```

- **152–153**: **decimação**. Um PNG não mostra mais de ~1500 colunas de pixel úteis; `stride` pega
  1 em cada N amostras para não gerar uma matriz gigante que o matplotlib reduziria de qualquer jeito.
- **154**: largura em bicos = mediana do comprimento hex / 2 (2 chars por bico). Mediana, não `max`,
  porque linha truncada existe.
- **157–158**: emparelha timestamp e payload **antes** de filtrar, e só então monta as linhas.
  Era aqui o desalinhamento: filtrar os payloads e depois fatiar `s.index[:len(rows)]` assume que os
  descartados são os últimos — se o payload curto está no meio, o eixo de tempo escorrega.
- **161**: `.T` transpõe — a matriz sai como (amostras × bicos) e o `imshow` quer (bicos × tempo),
  bico no eixo Y.

## Linhas 164–176 — `matrix_bits`: WDT/SEC (1 bit por bico)

Mesma estrutura, com duas diferenças: converte cada payload com `hex_to_bits` (linha 170) e a
largura vem da **mediana do comprimento em bits** (171) — necessária por causa do `:05b` de largura
variável do modo AG. O comentário da linha 172 marca que o cuidado com o emparelhamento é o mesmo.

## Linhas 179–220 — `draw_nozzles`: os heatmaps

- **180–194**: monta a lista de camadas. Cada uma é
  `(nome, matriz, índice de tempo, colormap, limites)`. CDD e VAR usam a rampa sequencial e limites
  automáticos (`None`); WDT e SEC usam a colormap binária com limites fixos `(0, 1)` — sem fixar,
  um trecho todo fechado normalizaria 0 para "aberto".
- **189–190**: as duas camadas binárias vêm de um laço porque só mudam a chave, a coluna e o rótulo.
- **195–196**: nada para desenhar ⇒ `None`.
- **198–199**: altura 2,4" por camada; `atleast_1d` como antes.
- **201**: `date2num` converte os timestamps para o float que o matplotlib usa internamente.
  `imshow` não aceita eixo de datas direto — é preciso passar por `extent`.
- **202–204**: `aspect="auto"` deixa a célula esticar (senão a matriz sai quadrada e ilegível);
  `origin="lower"` põe o bico 0 embaixo; `interpolation="nearest"` **não inventa meio-tom** entre
  bicos vizinhos; `extent` amarra a imagem ao intervalo real de tempo e à contagem de bicos.
- **205**: avisa ao eixo X que aqueles floats são datas, e aí os ticks saem como hora.
- **206**: o título já diz quantos bicos a matriz tem — é a conferência de configuração da máquina
  mais direta que existe (60+60 = 120 no log de exemplo).
- **208–211**: colorbar. Na camada binária, dois ticks rotulados `fechado`/`aberto` em vez da escala
  `0,0–1,0`, que não significa nada num booleano.
- **212–213**: contorno e ticks da colorbar nos tokens recessivos.
- **214–219**: rótulo de tempo só embaixo, suptitle lembrando que **o lado esquerdo está invertido**
  (é como o pipeline monta a barra), layout, salva, fecha.

## Linhas 223–247 — `draw_gps`: o trajeto

- **224–226**: sem CAN ou sem coluna de latitude, não há trajeto. Máquina cujo GPS chega por serial
  (NovAtel/NMEA) não cai aqui — está documentado em `weedit_log.md` §5.
- **227–228**: descarta o par (0,0) — o "null island" que aparece quando o payload é inválido. O
  limiar `0.001` cobre também quase-zero de arredondamento.
- **231**: cor = **minutos desde o início**, não índice: assim uma parada aparece como aglomerado de
  cor parada, e você lê a direção do percurso.
- **233**: `scatter` com `s=3, linewidths=0` — ponto pequeno, sem borda, para 3 mil pontos não virarem
  um borrão. A cor usa a rampa sequencial (tempo é magnitude).
- **234–236**: colorbar rotulada, nos tokens recessivos.
- **239–241**: mata a notação `-5.397e1` e força 4 casas — coordenada tem que ser legível como número.
- **243**: `aspect="equal"` — sem isso o traçado sai distorcido e uma curva parece uma reta.

## Linhas 250–262 — `selftest`

```python
assert hex_to_bits("F0", "quadro") == "11110000"
assert hex_to_bits("1", "quadro") == "1000"
assert hex_to_bits("8", "quadro") == "0001"
assert hex_to_bits("01", "ag") == "10000"
assert hex_to_bits("FF", "ag") == "11111111"
assert hex_to_bits("ZZ", "quadro") == "00000000"
assert hex_to_bits(None, "quadro") == ""
```

Sete `assert` cobrindo a única lógica do script que erra **sem sintoma visível**: a ordem dos bits.
`F0 → 11110000` (F = 1111 invertido, 0 = 0000), `1 → 1000` e `8 → 0001` provam a inversão por nibble;
os dois casos AG fixam a largura variável do `:05b`; os dois últimos fixam a tolerância a lixo
(`ZZ` → zeros, `NaN` → vazio). `python3 plot_log.py --selftest` roda em milissegundos, sem log nenhum.

## Linhas 265–269 — `load_parser`

```python
spec = importlib.util.spec_from_file_location("parse_log_manual", HERE / "parse_log_manual.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
return mod
```

Importa o parser **por caminho absoluto**, não por `import parse_log_manual`. Motivo: o `import`
normal depende de o diretório estar no `sys.path`, o que só é verdade se você chamar o script de
dentro da pasta. Com `HERE`, funciona de qualquer cwd — e é o mesmo mecanismo que a §8 usa no notebook.
Custo: 4 linhas em vez de 1. Benefício: nenhuma cópia da lógica de parse aqui dentro.

## Linhas 272–303 — `main`

```python
ap.add_argument("log", nargs="?", default=DEFAULT_LOG)
ap.add_argument("--out", default="plots")
ap.add_argument("--step", default="1s", help="reamostragem dos painéis (default 1s)")
ap.add_argument("--model", default="quadro", choices=["quadro", "ag"])
ap.add_argument("--bitola", type=int, default=6000)
ap.add_argument("--selftest", action="store_true", help="checa a ordem de bits e sai")
```

- **274**: `nargs="?"` = argumento posicional opcional, então `python3 plot_log.py` sozinho funciona.
- **275**: pasta de saída relativa por default (`./plots`).
- **276**: `--step` é string porque vai direto para o `resample` do pandas (`"200ms"`, `"1s"`, `"5s"`).
- **277**: `choices` no `--model` faz o argparse recusar valor inválido — melhor errar no CLI do que
  gerar um heatmap espelhado.
- **278**: `--bitola` só afeta `wdt_deltac` (é divisor na fórmula do parser), mas precisa estar aqui
  porque é parâmetro de máquina, não do gráfico.
- **281–282**: `--selftest` sai antes de tocar em qualquer log — dá para rodar sem dados na máquina.
- **284**: cria a pasta de saída (`parents=True, exist_ok=True`: não reclama se já existe).
- **285**: chama o parser. Só aqui o log é lido, uma vez, e os DataFrames são reaproveitados pelas 4 figuras.
- **286**: imprime a janela real do log. É a primeira coisa a conferir: os logs de exemplo têm
  **2 e 5,5 minutos**, não um dia.
- **288–294**: as quatro figuras, na ordem. O `Path(a.log).stem` põe o nome do log no título, então o
  PNG não fica anônimo depois de sair da pasta.
- **295–296**: relatório: `ok` com o caminho, ou `--  (sem dados)` quando a função devolveu `None`.
- **298–302**: recalcula quais séries pedidas não existem e lista. É a linha que já mostrou, sem
  precisar abrir o PNG, que a Horsch Leeb do `WQR20250011` não manda `can_flow`/`can_rate` —
  exatamente o cenário de "Common Issues" do `CLAUDE.md` do repo. Recomputar `get_series` aqui é
  trabalho repetido; num log de minutos é irrelevante e mantém a função pura.

## Linhas 306–307 — guarda de execução

```python
if __name__ == "__main__":
    main()
```

Só executa quando chamado como script. Assim `import plot_log` (ou o `importlib` de um notebook)
pega as funções sem gerar figura nenhuma.

---

## O que ficou deliberadamente de fora

| Não tem | Por quê | Quando adicionar |
|---|---|---|
| Modo escuro | é PNG de diagnóstico, tema único | se for para tela/apresentação: mesma rampa, tokens escuros |
| Interatividade (zoom, tooltip) | PNG resolve o diagnóstico | log longo e exploração fina → `--html` com plotly |
| Mapa com base cartográfica | precisaria de dependência e rede | análise de cobertura, aí já é `log_raster` do repo |
| Conversão de velocidade para km/h | o fator não está documentado no repo | quando alguém confirmar o fator no firmware |
| Cache do parse entre execuções | 2–5 s por log | varredura de centenas de logs → salvar `parts` em parquet |
