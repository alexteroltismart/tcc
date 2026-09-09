# `validate_plant_model.py` explicado linha por linha

Referência do validador do modelo da planta (`validate_plant_model.py`, 667 linhas), nesta
mesma pasta. Números de linha da versão atual. Resultados e leitura: `weedit_log.md` §11.

Pergunta que o script responde: alimentando o modelo **só com o que a máquina conhece**
(bicos disparando, seções abertas, pressão alvo, vazão alvo), a pressão e a vazão previstas
ficam próximas das medidas?

Três hipóteses, testadas separadamente:

| # | Hipótese |
|---|---|
| H1 | `P ≈ P_alvo` — o regulador mantém a pressão |
| H2 | `q = k · A(N,S) · √P` — bicos como orifício (Torricelli) |
| H3 | `q_alvo ≈ q_medida` — a conta interna da máquina |

---

## Linhas 1–20 — docstring

Enumera as hipóteses e as cinco variantes de H2 — (a) só entradas, (b) com pressão medida,
(c) área pelas seções, (d) mistura, (e) com atraso. Deixar isso no topo é o que permite ler
o resto do arquivo sabendo o que cada variante existe para responder.

## Linhas 22–44 — imports e estilo

- **22–30**: `argparse`, `json`, `Path`, `matplotlib` (com `use("Agg")` **antes** do
  `pyplot`, linha 26), `numpy`, `pandas` e `minimize_scalar` do scipy — o único otimizador
  usado, e só para o τ da variante (e).
- **32–41**: os mesmos tokens de cor e `rcParams` dos outros scripts da pasta (paleta
  categórica validada, grid recessivo, traço fino). Mantidos idênticos de propósito: as
  figuras das três etapas ficam visualmente coerentes.

## Linhas 42–44 — `COLS`: o contrato com o dataset

```python
COLS = {"N": "nozzles_on", "S": "sections_on", "P": "can_pressure", "Q": "can_flow",
        "P_sp": "can_target_pressure", "Q_sp": "can_target_liters_flow"}
```

Um único lugar mapeia papel → nome de coluna. É o que permite o `main` (linha 505) checar
tudo de uma vez e falhar com mensagem útil se o dataset foi exportado sem as mensagens
`1333333302/04` da bomba.

## Linhas 47–64 — `score`: as métricas

```python
y, yhat = y[mask], yhat[mask]
ok = np.isfinite(y) & np.isfinite(yhat)
...
big = np.abs(y) > 1.0                      # MAPE só onde o valor não é ~zero
```

- **48–50**: aplica a máscara (regime × conjunto) e depois descarta não-finitos — nesta
  ordem, senão a máscara e o array ficam com tamanhos diferentes.
- **51–52**: menos de 3 amostras ⇒ tudo NaN. Métrica com n=2 é ruído, e é melhor propagar
  NaN do que um número que alguém vai citar.
- **58–60**: `rmse`, `mae`, `bias`. O **viés** separado do RMSE é essencial aqui: um modelo
  pode ter RMSE alto por ruído (viés ~0) ou por erro sistemático (viés grande) — e o
  tratamento é diferente.
- **61**: `r2` = 1 − SSE/SST.
- **62**: `fit_pct` = 100·(1 − ‖e‖/‖y−ȳ‖), a mesma definição do `compare` do System
  Identification Toolbox — está aqui para quem vem do MATLAB comparar direto.
- **63**: `mape_pct` **só onde |y| > 1**. Sem esse filtro, uma amostra de vazão 0,05 L/min
  gera erro percentual de milhares e domina a média. É o cuidado que torna o MAPE citável.

## Linhas 67–71 — `block_mean`

```python
xs = x[mask]
nb = len(xs) // n
return xs[:nb * n].reshape(nb, n).mean(1) if nb else np.array([])
```

Média em blocos de `n` amostras. O `[:nb * n]` descarta a sobra que não completa um bloco —
sem isso o `reshape` levanta erro. Aplica a máscara **antes** de agrupar: os blocos são
formados só com amostras do regime de interesse.

## Linhas 74–94 — `multiscale`: a métrica que salva a análise

```python
for B in blocks:
    n = max(1, int(round(B / dt)))
    a, b = block_mean(q, mask, n), block_mean(yhat, mask, n)
    if len(a) < min_blocks:               # poucos blocos => métrica sem sentido
        ...
        continue
```

Por que existe: o flowmeter e a capacitância da linha filtram os buracos de ~250 ms entre
disparos, então **comparar amostra a amostra mede a banda do sensor, não o modelo**. A
validação honesta agrega os **dois** sinais na mesma janela e compara por banda.

- **83**: converte a janela em segundos para número de amostras usando o Δt do dataset.
- **85–88**: janela com menos de `min_blocks` (8) blocos é marcada `descartado` em vez de
  reportada. Foi uma correção necessária: com 2 blocos o R² dava −0,04 e não significava nada.
- **90–93**: RMSE e R² **por bloco**, guardando `n_blocos` para o leitor julgar.

## Linhas 97–121 — `dropout_stats`: quantificar os buracos de disparo

```python
idx = np.flatnonzero(spray)
win = np.zeros(len(N), bool)
win[idx[0]:idx[-1] + 1] = True
z = ((N == 0) & win).astype(int)
d = np.diff(np.concatenate([[0], z, [0]]))
starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
dur = (ends - starts) * dt
```

- **103–108**: a **janela** de pulverização é o intervalo entre o primeiro e o último
  disparo — não a máscara por amostra. O docstring registra o bug que isso corrige:
  `spray` é `N > 1`, então `(N == 0) & spray` é **vazio por construção**, e a primeira
  versão reportava "0 % de buracos".
- **110–112**: truque padrão para achar corridas de `True`: acolchoa com zeros nas duas
  pontas, deriva, e os `+1`/`−1` são início e fim de cada corrida. `(ends - starts) * dt`
  dá a duração de cada uma.
- **113–121**: além da contagem e duração, devolve **o que o flowmeter lê durante os
  buracos** — é o número que prova que o sensor não acompanha (24,5 L/min em média, contra
  0 do modelo).

## Linhas 124–133 — `lag1`

```python
a = dt / (tau + dt)
y[0] = x[0]
for k in range(1, len(x)):
    y[k] = y[k - 1] + a * (x[k] - y[k - 1])
```

Filtro de 1ª ordem discretizado por Euler, usado só pela variante (e). `tau <= 0` devolve
cópia (linha 126–127), o que faz τ = 0 significar exatamente "sem dinâmica" e mantém o
perfil contínuo na origem.

## Linhas 137–143 — `fit_gain`

```python
ok = np.isfinite(x) & np.isfinite(y) & (x > 0)
return float(np.dot(x[ok], y[ok]) / np.dot(x[ok], x[ok]))
```

Mínimos quadrados **sem intercepto** — solução fechada `k = ⟨x,y⟩/⟨x,x⟩`. Sem intercepto
porque o modelo físico passa pela origem: sem bico aberto, sem vazão. Um intercepto
ajustável melhoraria o RMSE e destruiria o significado físico de `k`.
O `x > 0` exclui as amostras em que o "drive" é zero, que não informam nada sobre `k`.

## Linhas 146–155 — `fit_two_gains`

```python
A = np.column_stack([N * rt, Sv * rt])[mask]
sol, *_ = np.linalg.lstsq(A[ok], y[ok], rcond=None)
```

A variante (d): dois coeficientes de área (bicos e seções) por LS multivariado. O resultado
no log de exemplo é revelador — `a_N ≈ −0,0002`, isto é, dado `sections_on` o termo dos
bicos vira ~zero: as duas entradas são quase colineares e o LS distribui como quiser. É por
isso que (d) empata com (c) e ambas perdem para (a) na validação.

## Linhas 158–214 — `build_models`: as cinco variantes

### 160–168: sinais e as duas raízes

```python
rt_sp, rt_m = np.sqrt(np.maximum(P_sp, 0)), np.sqrt(np.maximum(P, 0))
```

`√P` com a pressão **alvo** e com a **medida**, calculadas uma vez. O `maximum(·, 0)`
protege a raiz — pressão negativa não existe, mas um sensor com offset pode reportar.

### 170–184: (a) a (d)

Cada variante é três linhas: ajusta o ganho na janela de estimação, gera a série prevista
para **todo** o log, guarda o parâmetro. Prever fora da estimação é o que permite medir
validação de verdade.

- **(a)** `k·N·√P_alvo` — a variante que interessa: usa **só entradas**.
- **(b)** `k·N·√P_medida` — serve de contraste: a diferença (a)−(b) isola quanto custa usar
  o alvo em vez da pressão medida. Deu quase nada (3,72 vs 3,69), o que é a confirmação
  independente de que a H1 vale.
- **(c)/(d)** — respondem "a área efetiva é melhor descrita pelos bicos disparando ou pelas
  seções abertas?".

### 186–208: (e) e o perfil do atraso

```python
sp_ = N > 1                    # mesma máscara do perfil e das métricas
def rmse_tau(tau):
    dr = lag1(drive, tau, dt)
    k = fit_gain(dr, q, est)
    m = est & sp_
    return float(np.sqrt(np.mean((k * dr[m] - q[m]) ** 2)))
r = minimize_scalar(rmse_tau, bounds=(0.0, 5.0), method="bounded")
```

- **Perfil (profile likelihood):** para **cada** τ o ganho ótimo é recalculado antes de
  comparar o RMSE. Sem isso — e a primeira versão errava assim — o τ é usado para corrigir
  **amplitude**, não atraso, e o resultado não tem sentido.
- **`m = est & sp_`**: o τ é escolhido no mesmo conjunto em que as métricas são reportadas.
  Também foi correção: antes o mínimo era buscado sobre todas as amostras de estimação
  (incluindo as seções fechadas, onde modelo e medida são ~0 e o τ não muda nada).
- **196–206**: além do τ ótimo, varre 31 valores e guarda `rmse_est`/`rmse_val` de cada um.
  É esse perfil que revela o achado: **o objetivo é achatado em estimação e cresce em
  validação**, ou seja, o atraso não é identificável com estes dados. Guardar o perfil é o
  que transforma "o ajuste ficou ruim" em "a grandeza não é identificável".

### 210–214: (H3)

```python
models["(H3) vazão alvo da máquina"] = q_sp
```

Entra como "modelo" sem nenhum ajuste — é a própria conta da máquina, medida com a mesma
régua das demais.

## Linhas 220–227 — `shade_regimes`

```python
edges = np.flatnonzero(np.diff(spray.astype(int)))
bounds = np.concatenate([[0], edges + 1, [len(t)]])
for a, b in zip(bounds[:-1], bounds[1:]):
    if spray[a]:
        ax.axvspan(t[a], t[b - 1], ...)
```

Sombreia os trechos pulverizando. Detecta as transições pela derivada da máscara e desenha
um `axvspan` por corrida — em vez de um span por amostra, que geraria centenas de retângulos.

## Linhas 229–264 — `fig_flow`

Três painéis: série, resíduo e um **zoom de 12 s** no meio do trecho pulverizando
(linhas 250–262). O zoom foi o que revelou a causa dos resíduos de −30 L/min: o modelo cai a
zero nos buracos de disparo e a medida não. Sem ele, a figura de 113 s esconde o mecanismo.

Detalhes que importam: a medida é plotada **por último, com `zorder=5` e traço mais grosso**
(linha 236) — o dado tem que ficar acima dos modelos; e a legenda fica **fora** da área de
dados (`bbox_to_anchor=(0, 1.0)`, linha 240), depois de uma versão em que ela cobria a curva.

## Linhas 267–284 — `fig_scatter`

Dispersão medido × modelo, **só na validação e só pulverizando** (`m = spray & val`,
linha 271), com a reta 1:1 e R²/RMSE no título de cada painel. A reta 1:1 (não uma regressão)
é o que expõe viés: pontos sistematicamente de um lado da diagonal.

## Linhas 286–304 — `fig_pressure` (H1)

Série (medida vs alvo) e histograma do erro **separado por regime**. É a figura que mostra
os dois patamares: 250 kPa com seções fechadas e 406 kPa travado enquanto pulveriza. Os dois
histogramas sobrepostos (`alpha=0.7`, linha 298) tornam óbvio que são duas populações, não
uma distribuição com cauda.

## Linhas 306–334 — `fig_compare`

Barras de RMSE estimação vs validação por variante, com o número escrito em cima
(linhas 315–318) — é o que permite ler a tabela sem abrir o JSON. O painel da direita
(linhas 325–332) é o **perfil do τ**, e o título diz o que ele significa: objetivo achatado
= τ não identificável.

## Linhas 336–359 — `fig_multiscale`

```python
e_by = {m["bloco_s"]: m for m in ms_est if not m["descartado"]}
v_by = {m["bloco_s"]: m for m in ms_val if not m["descartado"]}
xs = sorted(set(e_by) & set(v_by))
```

Só as janelas válidas **nos dois** conjuntos. Foi correção de um erro real: estimação e
validação descartam janelas diferentes (a validação tem menos amostras), e plotar as duas
listas direto quebrava com "x and y must have same first dimension". Cada ponto é anotado
com o `n` de blocos (linhas 348–350) — sem isso, um R² alto com 12 blocos passaria por
robusto.

## Linhas 361–379 — `fig_residual_structure`

Resíduo do melhor modelo contra `N`, contra a pressão e contra a própria vazão. O objetivo
é diagnóstico, e está no título: **resíduo sem padrão = modelo adequado**. Padrão em algum
dos três painéis apontaria termo faltante (por exemplo curvatura vs `N` indicaria que a
área efetiva não é linear na contagem).

## Linhas 381–487 — `REPORT`: o relatório como template

Uma f-string gigante com marcadores, preenchida no fim do `main`. Duas razões para ser
template e não `print`: o relatório fica **versionável** ao lado das figuras, e a estrutura
(hipótese → parâmetros → métricas → veredito → ressalvas) é fixa, então dois logs geram
relatórios comparáveis linha a linha.

A seção "Ressalvas" é parte do produto, não decoração. A ressalva 1, em particular, foi
**reescrita depois de testada**: a suspeita era que o resíduo instantâneo fosse aliasing dos
100 ms; reexportando a 50 ms o resultado não mudou (3,79 vs 3,72 L/min), então o texto
registra o teste e a conclusão em vez da suposição.

## Linhas 489–664 — `main`

### 490–508: CLI e checagem de contrato

```python
falta = [c for c in COLS.values() if c not in df.columns]
if falta:
    raise SystemExit("colunas ausentes no dataset: " + ", ".join(falta)
                     + "\nreexporte com export_dataset.py")
```

- **503**: o Δt vem do `dataset_meta.json`, com a mediana das diferenças de `t` como
  reserva. Ler o metadata em vez de inferir evita erro silencioso de escala nas janelas.
- **505–508**: falha **antes** de qualquer conta, dizendo qual coluna falta e o que fazer.

### 510–521: a divisão estimação/validação

```python
if a.split_mode == "pulverizando" and spray.any():
    alvo = a.split * spray.sum()
    i = int(np.searchsorted(np.cumsum(spray), alvo) + 1)
else:
    i = int(len(t) * a.split)
```

O ponto metodológico mais importante do script. Dividir o **log inteiro** em 70/30 deixaria
a estimação quase toda com as seções fechadas (onde não há informação de vazão) e a
validação com quase toda a pulverização — foi o que aconteceu na primeira versão: 112
amostras pulverizando na estimação contra 290 na validação. A soma cumulativa da máscara
com `searchsorted` acha o instante que divide as **amostras pulverizando** na proporção
pedida. Continua sendo divisão **temporal** (nada de embaralhar) — é série temporal.

### 525–533: H1

```python
sc = score(sig["P_sp"], sig["P"], mask)      # "modelo" = alvo; medido = real
rel = (sig["P"] - sig["P_sp"])[mask]
sc["erro_pct"] = float(100 * np.mean(rel / np.where(base == 0, np.nan, base)))
```

Trata o **alvo como previsão** e a pressão medida como verdade — é literalmente a hipótese
"o regulador entrega o alvo". O erro percentual usa `np.where(base == 0, np.nan, base)`
para não dividir por zero quando o alvo não está publicado.

### 535–547: H2/H3 e as métricas auxiliares

Três recortes por variante: pulverizando-estimação, pulverizando-validação e todo-o-log-
validação. O terceiro existe para quem quiser a métrica sem recorte de regime, mas o
relatório usa os dois primeiros — fora da pulverização a vazão é ~0 e a métrica relativa
perde sentido.

### 549–562: metadata e figuras

Tudo o que foi calculado vai para `metrics.json` (inclusive o perfil de τ e a estatística
dos buracos) **antes** de desenhar. Assim, figura quebrada não custa as métricas.

### 564–606: montagem do veredito

```python
validas = [m for e, m in zip(ms_est, ms_val) if not (m["descartado"] or e["descartado"])]
ms_ref = validas[-1] if validas else {...}
best = min(res, key=lambda k: res[k]["pulverizando_validacao"]["rmse"])
```

- **571–573**: a referência do veredito é a **maior janela válida nos dois conjuntos** —
  escolhida por regra, não escrita à mão, para o texto acompanhar o dado quando o log muda.
- **575**: o "melhor" modelo é decidido pelo RMSE de **validação**, nunca de estimação.
- **578–606**: o veredito é gerado com os números, não redigido: se outro log mudar as
  conclusões, o texto muda também. Inclui a leitura da não-identificabilidade do τ e a
  ressalva de que (a) vs (b) isola o custo de usar o alvo.

### 608–664: impressão e escrita

Ecoa H1, a tabela de variantes, a validação multiescala (marcando as janelas descartadas com
o `n` dos dois lados) e a estatística dos buracos; depois escreve `REPORT.md` e lista os
arquivos gerados.

## Linhas 666–667 — guarda de execução

`if __name__ == "__main__": main()` — permite `import validate_plant_model` num notebook
para reusar `score`, `multiscale` ou `build_models` sem gerar nada.

---

## Correções que a revisão linha a linha produziu

| Onde | Problema | Correção |
|---|---|---|
| `dropout_stats` | `(N==0) & spray` é vazio por construção → "0 % de buracos" | passou a usar a **janela** entre o primeiro e o último disparo |
| ajuste do τ | RMSE mínimo buscado sobre todas as amostras de estimação, mas o perfil usava só as pulverizando | mesma máscara nos dois (`est & (N>1)`) |
| ajuste do τ | τ corrigia amplitude porque o ganho era fixo | ganho recalculado por LS para cada τ (perfil) |
| `fig_multiscale` | estimação e validação descartam janelas diferentes → erro de dimensão | só janelas válidas nos dois conjuntos |
| divisão dos dados | 70/30 do log inteiro deixava a estimação sem pulverização | divisão contada sobre as amostras pulverizando |
| relatório H1 | viés impresso com sinal invertido em relação ao erro percentual | ambos como *medido − alvo* |
| relatório | "o flowmeter nunca zera (mínimo 0,0 L/min)" — contradição | passou a reportar o que o sensor lê **durante os buracos** |
| ressalva 1 | suposição de aliasing dos 100 ms | testada a 50 ms e reescrita com o resultado |

## O que este script deliberadamente não faz

| Não faz | Por quê |
|---|---|
| Identificar a dinâmica (C, τ) | o log é de malha fechada e o τ não é identificável — ver `wip_control_stage.py` |
| Projetar ou simular controle | etapa 2, parada a pedido |
| Estimar intervalo de confiança dos coeficientes | `metrics.json` traz `n` e viés; IC exigiria hipótese de ruído que os dados não sustentam |
| Corrigir a área efetiva pelo ciclo de trabalho | testado (média móvel e atraso), não melhora — o resíduo é do sensor |
| Validar sob mudança de pressão alvo | o log tem um único perfil (406 kPa); exige outro log |
