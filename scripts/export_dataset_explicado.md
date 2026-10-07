# `export_dataset.py` explicado linha por linha

Referência do exportador de dataset (`export_dataset.py`, 277 linhas), nesta mesma pasta.
Números de linha da versão atual (2026-10-07, com suporte a JD e Jacto).

O que ele faz: pega as famílias que o `parse_log_manual.py` devolve — em cadências
diferentes (50 ms, 100 ms, evento) e com colunas de texto (hex por bico) — e produz **uma
matriz numérica de Δt constante**, com `t` em segundos e metadados ao lado.
Contexto e uso: `weedit_log.md` §10.

---

## Linhas 1–10 — docstring

Diz a intenção e a linha de comando. A frase que importa é "**tudo vira UMA matriz
numérica amostrada a Δt constante**": é a diferença entre um log e um dataset. Simulação e
identificação de sistemas exigem grade regular; o log não tem.

## Linhas 11–15 — imports

| Linha | Código | Por quê |
|---|---|---|
| 11 | `import argparse, importlib.util, json, re` | CLI; carregar os dois módulos vizinhos por caminho; escrever o metadata; `re` para colapsar prefixo duplicado no nome da coluna |
| 12 | `from pathlib import Path` | caminhos e `mkdir(parents=True)` |
| 14–15 | `numpy`, `pandas` | matriz e séries temporais |

`scipy` **não** é importado aqui no topo: só entra dentro do `write_outputs` (linha 176),
quando o formato `mat` é pedido. Assim quem não tem scipy ainda exporta csv/parquet/npz.

## Linhas 17–18 — constantes

```python
HERE = Path(__file__).resolve().parent
DEFAULT_LOG = "/home/shared/data/Weedit/s3_bucket/WQR20230004/20260318-155931.zip"
```

`HERE` é o que permite achar `parse_log_manual.py` e `plot_log.py` ao lado, de qualquer cwd.

## Linhas 20–45 — `UNITS`: a unidade de cada sinal

```python
UNITS = {
    "can_flow": "L/min", "can_pressure": "kPa", ...
    "pressure": "0,1 kPa (bruto: /10 = kPa)", ...
    "vol": "0,1 V (bruto: /10 = V)", ...
    # Jacto
    "flow_lmin": "L/min", "pump_flow": "L/min", "sent_machine_flow": "L/min",
    "stm_flow": "L/min", "engine_rpm": "rpm",
}
```

Duas decisões:

- **Indexado pelo nome ORIGINAL da coluna** (minúsculo), não pelo nome exportado. Assim
  `pwm_wdt_system` é reconhecido venha ele como `can_pwm_wdt_system` ou não — e não é
  preciso repetir a entrada para cada prefixo possível. Foi um bug real: na primeira
  versão as chaves eram os nomes exportados e 33 colunas saíam como "desconhecida".
- **O que não está no dicionário sai como `"desconhecida"`**, de propósito. Unidade
  ausente é honesta; unidade errada estraga a modelagem de quem consome.
- Onde o log guarda valor escalado (`pressure` em 0,1 kPa, `vol` em 0,1 V), a unidade **diz
  o fator**. O exportador não converte: converter aqui esconderia o dado bruto.
- Os sinais da Jacto (linhas 42–44) entram só com a unidade que o `Update_Secrets.py`
  garante. `pump_rpm`, `can_speed`, `machine_pwm` e `pump_pwm` ficam de fora de propósito:
  a escala deles não está documentada, então saem como `"desconhecida"`.

## Linhas 47–50 — `FLOW_MEASURED`: qual coluna é vazão medida na barra

```python
FLOW_MEASURED = ["can_flow"]
```

Lista de preferência da coluna que o `validate_plant_model.py` usa como **saída medida** da
H2 (vai para o metadata como `flow_measured`, linha 243). Só a JD entra:

- **JD**: `can_flow` é o flowmeter do controlador de taxa, no CAN.
- **Jacto**: não há vazão medida na barra. O `flow_lmin` (`18888888AA`) é o `predicted_flow`
  da placa STM da bomba — correlação 0,999, sem atraso, e zera junto com os bicos, sem a
  inércia de um flowmeter. O `pump_flow` (`1AFFFFFC`) é a vazão total da bomba, que **inclui
  o retorno** (correlação 0,07 com N·√P). Validar contra qualquer um seria circular ou
  errado, então na Jacto `flow_measured` sai `null` e o validador recusa a H2.

Chegou a ser `["can_flow", "can_flow_lmin"]` e foi retirado quando a comparação mostrou que
o `flow_lmin` é estimativa.

## Linhas 52–58 — `IO_HINT_COLS`

```python
IO_HINT_COLS = {
    "inputs": ["pwm_wdt_system", "can_pump_pwm", "target_liters_flow",
               "sections_open", "nozzles_on", "speed_center"],
    "outputs": ["can_flow", "flow_lmin", "can_pressure", "pressure", "predicted_flow"],
}
```

Sugestão de partição entrada/saída, para quem for identificar a malha bomba → pressão/vazão.
Também em nomes **originais**; o `main` traduz para os nomes exportados (função `io_hint`,
linha 191). É rótulo de conveniência, e o metadata carrega a ressalva de que é sugestão —
`sections_open` e `nozzles_on`, por exemplo, são mais perturbação de carga que entrada manipulada.
`flow_lmin` está nas saídas por ser o único sinal de vazão de barra da Jacto, mas é
**estimativa** (ver `FLOW_MEASURED`); `io_hint` só lista, não valida.

## Linhas 60–64 — `load_parser`

```python
spec = importlib.util.spec_from_file_location("parse_log_manual", HERE / "parse_log_manual.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
```

Importa o parser **por caminho**, não por `import` no `sys.path`. Mesmo motivo do
`plot_log.py`: funciona de qualquer diretório, e não há cópia da lógica de parse aqui.

## Linhas 67–71 — `clean_name`: o nome da coluna exportada

```python
name = f"{part}_{col}".lower()
name = re.sub(r"^(\w+?)_\1(_|$)", r"\1\2", name)
return name.rstrip("_")
```

Prefixar com a família (`can`, `speed`, `details`, `vol`) evita colisão — `speed_center`
existe **em duas** famílias (na mensagem `*SX0:98` do WDT e na mensagem CAN da bomba), e sem
prefixo uma sobrescreveria a outra em silêncio.

O `re.sub` colapsa o prefixo duplicado: `can`+`can_flow` daria `can_can_flow`, e o regex
`^(\w+?)_\1(_|$)` reconhece "primeiro token repetido" e remove uma cópia →
`can_flow`. Idem `speed`+`speed_center` → `speed_center`, `vol`+`Vol` → `vol`.
O `rstrip("_")` cobre o caso em que a coluna original é exatamente o nome da família.

## Linhas 74–76 — `popcount_series`

```python
return s.dropna().map(lambda v: sum(c == "1" for c in hex_to_bits(v, model)))
```

Máscara hex por bico → **contagem de bicos ativos**. É a conversão que transforma texto em
sinal usável: `nozzles_on` e `sections_on` nascem daqui. Usa o `hex_to_bits` do
`plot_log.py` (passado como argumento), então respeita `--model quadro|ag`.

## Linhas 79–86 — `byte_stats`

```python
vals = [int(v[i:i + 2], 16) for i in range(0, len(v) - len(v) % 2, 2)]
return float(np.mean(vals)) if how == "mean" else float(np.max(vals))
```

CDD/VAR têm **1 byte por bico**; isto reduz a barra inteira a um número por amostra (média
ou máximo). O `len(v) - len(v) % 2` protege contra payload de tamanho ímpar (pararia no
meio de um byte). Nada de `int(v, 16)` no payload todo: 240 caracteres hex viram um inteiro
gigante sem sentido físico.

## Linhas 89–104 — `DROP_COLS` e `numeric_columns`

```python
DROP_COLS = {"h"}

for c in df.columns:
    if str(c).lower() in DROP_COLS:
        continue
    s = pd.to_numeric(df[c], errors="coerce")
    if s.notna().any():
        out[c] = s
```

- **`h` é excluída** e o comentário diz por quê: é a máscara hex de detecção que vem junto
  nos detalhes, e parte dos valores é só dígito, então **parseia como número** e produziria
  uma coluna com NaN intercalado e nenhum significado físico. Era o único NaN que sobrava
  depois do `--trim`. A informação útil dela está em `nozzles_on`.
- `to_numeric(errors="coerce")` + `notna().any()`: coluna 100 % texto (nome de bico, modo
  como string) fica fora da matriz. Coluna mista entra com NaN onde não era número.

## Linhas 107–156 — `build_dataset`: a função central

### 111–118: famílias numéricas

```python
for part in ("speed", "can", "vol", "details"):
    ...
    sources[name] = (f"{part}.{col}", col.lower())
```

Ordem fixa das quatro famílias já numéricas. O `sources` guarda **uma tupla**: a origem
legível (`can.can_flow`) para o metadata, e o nome original em minúsculo — que é a chave
usada depois para achar a unidade e traduzir o `io_hint`.

### 120–133: sinais derivados das máscaras

```python
derived = [
    ("nozzles_on", "wdt", "WDT_HEX", lambda s: popcount_series(s, hex_to_bits, model)),
    ("sections_on", "sections", "SEC_HEX", ...),
    ("cdd_mean", "cdd", "CDD", lambda s: byte_stats(s, "mean")),
    ("cdd_max", "cdd", "CDD", ...),
    ("var_mean", "var", "VAR", ...),
]
```

Tabela em vez de cinco blocos repetidos. Família ausente (máquina sem VAR) é simplesmente
saltada nas linhas 130–131 — sem erro, e a coluna não aparece no dataset.

### 138–140: a grade

```python
t0 = min(s.index.min() for s in cols.values())
t1 = max(s.index.max() for s in cols.values())
grid = pd.date_range(t0.floor(dt), t1.ceil(dt), freq=dt)
```

A grade cobre a **união** das famílias (do primeiro ao último instante de qualquer sinal),
alinhada ao passo (`floor`/`ceil`). Consequência importante: sinais cuja família começa
depois têm NaN no começo — é exatamente o que o `--trim` recorta depois.

### 142–152: o preenchimento — a decisão que mais afeta controle

```python
if fill == "interp":
    merged = s.reindex(s.index.union(grid)).interpolate(method="time", limit_area="inside")
    out[name] = merged.reindex(grid)
else:
    out[name] = s.reindex(grid, method="ffill" if fill == "zoh" else None)
```

- **`interp`**: une o índice original com a grade, interpola **no tempo** (não por posição)
  e só então desce para a grade. `limit_area="inside"` proíbe extrapolação — fora do
  intervalo com dado real, fica NaN em vez de inventar valor.
- **`zoh`** (default): `reindex(..., method="ffill")` — zero-order hold. É o que um
  registrador amostrado realmente faz entre duas mensagens, e é a hipótese padrão para
  **entrada** em identificação de tempo discreto.
- **`none`**: `method=None` faz casamento **exato** de timestamp. Só sobrevive a amostra que
  cai precisamente na grade — a matriz sai quase toda NaN. Existe para inspeção, não para uso.
- Linha 144, `s[~s.index.duplicated(keep="first")].sort_index()`: `reindex` exige índice
  único e monotônico; sem isso o pandas levanta erro em cima de retransmissão.

### 154–156: eixo de tempo

```python
out.index.name = "timestamp"
out.insert(0, "t", (out.index - out.index[0]).total_seconds())
```

Duas representações do tempo, de propósito: o `timestamp` (índice, para juntar com outros
dados) e `t` em **segundos desde o início** como primeira coluna — que é o que toolbox de
controle e MATLAB esperam.

## Linhas 159–188 — `write_outputs`: os quatro formatos

| Linhas | Formato | Detalhe |
|---|---|---|
| 162–164 | `csv` | universal, perde dtype; `index=True` mantém o timestamp |
| 165–167 | `parquet` | **preserva dtype e o índice temporal**; é o default de leitura |
| 168–174 | `npz` | `t`, `data` (matriz), `columns` (object array), `timestamp` em int64 ns — numpy puro, sem pandas do outro lado |
| 175–184 | `mat` | `savemat` com `t` (coluna), `y` (amostras × sinais), `names`, `Ts`. `import` local do scipy e `oned_as="column"` para o MATLAB receber vetor-coluna |

Em todos os casos a coluna `t` é retirada da matriz de sinais (`df.drop(columns=["t"])`) e
entra separada: `y` fica só com sinais, o que é o formato que `iddata`/`lsim` esperam.
Linhas 185–187: o `dataset_meta.json` é escrito **sempre**, independentemente dos formatos.

## Linhas 191–198 — `io_hint`

```python
def match(wanted):
    return [c for c in df.columns
            if c != "t" and sources.get(c, ("", c))[1] in wanted and df[c].notna().any()]
```

Traduz a lista de nomes originais para os nomes realmente exportados, e **descarta o que
não tem nenhuma amostra válida** neste log. Por isso a sugestão de E/S de uma máquina sem
rate controller sai menor — sem prometer sinal que não existe.

## Linhas 201–273 — `main`

### 202–216: CLI

| Flag | Papel |
|---|---|
| `log` (posicional, opcional) | default no log de exemplo, então roda sem argumento. Aceita zip de log único (JD), zip com vários `.txt` em pastas (Jacto) ou `.txt` solto |
| `--out` | pasta de saída (`dataset`) |
| `--dt` | passo da grade, string passada direto ao pandas (`100ms`, `50ms`, `1s`) |
| `--format` | lista por vírgula; parseada na linha 218 |
| `--fill` | `zoh` (default) / `interp` / `none` |
| `--model` | convenção de bits do bico, repassada ao `hex_to_bits` |
| `--bitola` | default `None` = lê do cabeçalho do log (`# Bitola: 3900mm`), fallback 6000. Só afeta `wdt_deltac`; passe o valor só para sobrescrever |
| `--members` | glob sobre o nome dos `.txt` dentro do zip (ex.: `'20260831-04*'`). Necessário no zip Jacto, que traz o dia inteiro (~800 MB) e é carregado todo na memória |
| `--trim` | recorta as bordas até o suporte comum |

### 221–226: carregar e converter

```python
parser = load_parser()
plot = importlib.util.spec_from_file_location("plot_log", HERE / "plot_log.py")
plot_mod = importlib.util.module_from_spec(plot); plot.loader.exec_module(plot_mod)
cfg, raw, parts = parser.convert(a.log, bitola_mm=a.bitola, members=a.members)
df, sources = build_dataset(parts, a.dt, a.fill, plot_mod.hex_to_bits, a.model)
```

O `plot_log.py` é carregado **só** para reusar `hex_to_bits` — evitar uma terceira cópia da
convenção de bits vale o acoplamento, mas é um acoplamento real: mexer naquela função muda
o `nozzles_on` deste dataset. O `--selftest` do `plot_log.py` é o que protege isso.

`raw.attrs` traz o contexto que o `convert` resolveu (arquivos lidos, máquina, modelo,
bitola efetiva) e alimenta o metadata abaixo.

### 228–235: `--trim`

```python
ok = df.drop(columns=["t"]).notna().all(axis=1)
first, last = ok.idxmax(), ok[::-1].idxmax()
df = df.loc[first:last].copy()
df["t"] = (df.index - df.index[0]).total_seconds()
```

`ok` marca a amostra em que **todos** os sinais têm valor. `idxmax()` numa série booleana dá
o índice do primeiro `True`; `ok[::-1].idxmax()` dá o **último** (a série invertida). Recorta
esse intervalo e **recalcula `t`** — sem isso a série começaria em t = 6,9 s.
Só as bordas são cortadas: NaN no meio (se houver) permanece, e é reportado.

### 237–261: metadados

```python
meta = {"log": ..., "machine": ..., "machine_model": ..., "files": ..., "flow_measured": ...,
        "dt_s": dt_s, "fs_hz": round(1.0 / dt_s, 6), "fill": a.fill,
        "trim": ..., "rows_trimmed": ...,
        "columns": {c: {"source": ..., "unit": ..., "n_valid": ..., "n_unique": ...}},
        "io_hint": io_hint(df, sources), "header_config": cfg}
```

O que cada campo resolve:

- `machine` (linha 240): `machineCode` do cabeçalho; sem cabeçalho, cai no nome da pasta do
  log. Antes era sempre a pasta, o que no zip Jacto dava `data_jacto`.
- `machine_model` (linha 241): o `machineModel` do cabeçalho — 6/7/18/22 = Jacto 3030/4530.
- `files` (linha 242): quais `.txt` do zip entraram (procedência do `--members`).
- `flow_measured` (linha 243): primeira coluna de `FLOW_MEASURED` presente e com dado;
  `null` na Jacto. É o que o `validate_plant_model.py --flow auto` lê.
- `bitola_mm` (linha 253): a bitola **efetiva** (`raw.attrs`), não o argumento — com
  `--bitola` omitido, é a do cabeçalho.
- `dt_s`/`fs_hz`: o consumidor não precisa inferir a taxa dos timestamps.
- `fill`, `trim`, `rows_trimmed`: **procedência** — a matriz não conta como foi preenchida.
- `n_valid` e **`n_unique`**: `n_unique <= 1` é coluna constante, que deixa a matriz de
  regressores deficiente de rank. O exportador **não** remove: só informa, e quem modela decide.
- `unit` por coluna, buscada pelo nome original (linha 255).
- `header_config`: o JSON de configuração da máquina vai junto, então o dataset é
  autoexplicativo mesmo longe do log.
- `t0_local`: hora do log, **sem fuso**. Era `t0_utc` — nome errado, porque o log só tem
  hora local; corrigido para não induzir alguém a aplicar um deslocamento de fuso.

### 263–273: relatório de execução

Imprime linhas cruas, tamanho da grade, quantas amostras o `--trim` cortou, número de
sinais e — linha 269 — a lista de colunas **sem nenhuma amostra válida**. É a linha que
mostra num relance o que aquela máquina não emite.

---

## Pontos de atenção

| Ponto | Consequência |
|---|---|
| `--fill none` casa timestamp exato | matriz quase toda NaN; use `zoh` ou `interp` |
| `hex_to_bits` vem do `plot_log.py` | editar lá muda o `nozzles_on` daqui |
| `--dt` mais lento que a cadência nativa (50 ms) | filtro implícito; para transitório rápido use `--dt 50ms` |
| `--trim` só corta bordas | NaN no meio sobrevive (hoje não há nenhum) |
| Coluna constante não é removida | veja `n_unique` no metadata antes de uma regressão |
| Unidade "desconhecida" | é intencional: preferir vazio a errado |
| `flow_measured: null` (Jacto) | não há vazão medida na barra; `flow_lmin` é estimativa |
| zip Jacto sem `--members` | o dia inteiro (~800 MB de texto) vai para a memória |
