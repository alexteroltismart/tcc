# `validate_plant_model.py` explicado linha por linha

Referência do validador do modelo da planta (`validate_plant_model.py`, 689 linhas), nesta
mesma pasta. Números de linha da versão atual. Resultados e leitura: `weedit_log.md` §11
(JD) e §12 (Jacto).

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

## Linhas 1–21 — docstring

Enumera as hipóteses e as cinco variantes de H2 — (a) só entradas, (b) com pressão medida,
(c) área pelas seções, (d) mistura, (e) com atraso. Deixar isso no topo é o que permite ler
o resto do arquivo sabendo o que cada variante existe para responder.

## Linhas 22–40 — imports e estilo

- **22–30**: `argparse`, `json`, `Path`, `matplotlib` (com `use("Agg")` **antes** do
  `pyplot`, linha 26), `numpy`, `pandas` e `minimize_scalar` do scipy — o único otimizador
  usado, e só para o τ da variante (e).
- **32–40**: os mesmos tokens de cor e `rcParams` dos outros scripts da pasta (paleta
  categórica validada, grid recessivo, traço fino). Mantidos idênticos de propósito: as
  figuras das três etapas ficam visualmente coerentes.

## Linhas 42–51 — `FLOW_DESC`: o que é a vazão "medida" em cada máquina

```python
FLOW_DESC = {  # coluna -> (descrição curta, ressalva)
    "can_flow": ("vazão real, flowmeter", "...John Deere..."),
    "can_flow_lmin": ("ESTIMATIVA da placa STM da bomba, Jacto", "...A H2 aqui é circular..."),
}
```

Para cada coluna que pode ocupar o papel `Q`, uma descrição curta (vai para a tabela de
entradas/saídas do REPORT) e o texto da ressalva 2. Existe porque a vazão não significa a
mesma coisa nas duas máquinas: na JD é o flowmeter do controlador de taxa; na Jacto o único
candidato, `can_flow_lmin`, é o `predicted_flow` da placa STM (correlação 0,999, sem atraso)
— validar contra ele é comparar o modelo com outra estimativa. Coluna fora do dicionário cai
num texto genérico ("origem do sinal não documentada") no `main` (linhas 631–632).

## Linhas 53–54 — `COLS`: o contrato com o dataset

```python
COLS = {"N": "nozzles_on", "S": "sections_on", "P": "can_pressure", "Q": "can_flow",
        "P_sp": "can_target_pressure", "Q_sp": "can_target_liters_flow"}
```

Um único lugar mapeia papel → nome de coluna. É o que permite o `main` (linha 521) checar
tudo de uma vez e falhar com mensagem útil se o dataset foi exportado sem as mensagens
`1333333302/04` da bomba. `N`, `S`, `P`, `P_sp` e `Q_sp` têm o mesmo nome em JD e Jacto
(`can_pressure` vem de IDs diferentes, mas o parser dá o mesmo nome). Só `Q` muda: o
`"can_flow"` daqui é o default, e o `main` o **sobrescreve em runtime** (linha 515) a partir
do `--flow`.

## Linhas 58–75 — `score`: as métricas

```python
y, yhat = y[mask], yhat[mask]
ok = np.isfinite(y) & np.isfinite(yhat)
...
big = np.abs(y) > 1.0                      # MAPE só onde o valor não é ~zero
```

- **59–61**: aplica a máscara (regime × conjunto) e depois descarta não-finitos — nesta
  ordem, senão a máscara e o array ficam com tamanhos diferentes.
- **62–63**: menos de 3 amostras ⇒ tudo NaN. Métrica com n=2 é ruído, e é melhor propagar
  NaN do que um número que alguém vai citar.
- **69–71**: `rmse`, `mae`, `bias`. O **viés** separado do RMSE é essencial aqui: um modelo
  pode ter RMSE alto por ruído (viés ~0) ou por erro sistemático (viés grande) — e o
  tratamento é diferente.
- **72**: `r2` = 1 − SSE/SST.
- **73**: `fit_pct` = 100·(1 − ‖e‖/‖y−ȳ‖), a mesma definição do `compare` do System
  Identification Toolbox — está aqui para quem vem do MATLAB comparar direto.
- **74**: `mape_pct` **só onde |y| > 1**. Sem esse filtro, uma amostra de vazão 0,05 L/min
  gera erro percentual de milhares e domina a média. É o cuidado que torna o MAPE citável.

## Linhas 78–82 — `block_mean`

```python
xs = x[mask]
nb = len(xs) // n
return xs[:nb * n].reshape(nb, n).mean(1) if nb else np.array([])
```

Média em blocos de `n` amostras. O `[:nb * n]` descarta a sobra que não completa um bloco —
sem isso o `reshape` levanta erro. Aplica a máscara **antes** de agrupar: os blocos são
formados só com amostras do regime de interesse.

## Linhas 85–105 — `multiscale`: a métrica que salva a análise

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

- **94**: converte a janela em segundos para número de amostras usando o Δt do dataset.
- **96–99**: janela com menos de `min_blocks` (8) blocos é marcada `descartado` em vez de
  reportada. Foi uma correção necessária: com 2 blocos o R² dava −0,04 e não significava nada.
- **100–104**: RMSE e R² **por bloco**, guardando `n_blocos` para o leitor julgar.

## Linhas 108–132 — `dropout_stats`: quantificar os buracos de disparo

```python
idx = np.flatnonzero(spray)
win = np.zeros(len(N), bool)
win[idx[0]:idx[-1] + 1] = True
z = ((N == 0) & win).astype(int)
d = np.diff(np.concatenate([[0], z, [0]]))
starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
dur = (ends - starts) * dt
```

- **114–120**: a **janela** de pulverização é o intervalo entre o primeiro e o último
  disparo — não a máscara por amostra. O docstring registra o bug que isso corrige:
  `spray` é `N > 1`, então `(N == 0) & spray` é **vazio por construção**, e a primeira
  versão reportava "0 % de buracos".
- **121–123**: truque padrão para achar corridas de `True`: acolchoa com zeros nas duas
  pontas, deriva, e os `+1`/`−1` são início e fim de cada corrida. `(ends - starts) * dt`
  dá a duração de cada uma.
- **124–132**: além da contagem e duração, devolve **o que o flowmeter lê durante os
  buracos** — é o número que prova que o sensor não acompanha (24,5 L/min em média na JD,
  contra 0 do modelo). Foi também o que denunciou o `flow_lmin` da Jacto: durante os buracos
  ele lê ~1,4 L/min — zera junto com os bicos, sem a inércia de um sensor real.

## Linhas 135–144 — `lag1`

```python
a = dt / (tau + dt)
y[0] = x[0]
for k in range(1, len(x)):
    y[k] = y[k - 1] + a * (x[k] - y[k - 1])
```

Filtro de 1ª ordem discretizado por Euler, usado só pela variante (e). `tau <= 0` devolve
cópia (linhas 137–138), o que faz τ = 0 significar exatamente "sem dinâmica" e mantém o
perfil contínuo na origem.

## Linhas 148–154 — `fit_gain`

```python
ok = np.isfinite(x) & np.isfinite(y) & (x > 0)
return float(np.dot(x[ok], y[ok]) / np.dot(x[ok], x[ok]))
```

Mínimos quadrados **sem intercepto** — solução fechada `k = ⟨x,y⟩/⟨x,x⟩`. Sem intercepto
porque o modelo físico passa pela origem: sem bico aberto, sem vazão. Um intercepto
ajustável melhoraria o RMSE e destruiria o significado físico de `k`.
O `x > 0` exclui as amostras em que o "drive" é zero, que não informam nada sobre `k`.

## Linhas 157–166 — `fit_two_gains`

```python
A = np.column_stack([N * rt, Sv * rt])[mask]
sol, *_ = np.linalg.lstsq(A[ok], y[ok], rcond=None)
```

A variante (d): dois coeficientes de área (bicos e seções) por LS multivariado. O resultado
no log de exemplo é revelador — `a_N ≈ −0,0002`, isto é, dado `sections_on` o termo dos
bicos vira ~zero: as duas entradas são quase colineares e o LS distribui como quiser. É por
isso que (d) empata com (c) e ambas perdem para (a) na validação.

## Linhas 169–227 — `build_models`: as cinco variantes

### 172–179: sinais e as duas raízes

```python
rt_sp, rt_m = np.sqrt(np.maximum(P_sp, 0)), np.sqrt(np.maximum(P, 0))
```

`√P` com a pressão **alvo** e com a **medida**, calculadas uma vez. O `maximum(·, 0)`
protege a raiz — pressão negativa não existe, mas um sensor com offset pode reportar.

### 182–196: (a) a (d)

Cada variante é três linhas: ajusta o ganho na janela de estimação, gera a série prevista
para **todo** o log, guarda o parâmetro. Prever fora da estimação é o que permite medir
validação de verdade.

- **(a)** `k·N·√P_alvo` — a variante que interessa: usa **só entradas**.
- **(b)** `k·N·√P_medida` — serve de contraste: a diferença (a)−(b) isola quanto custa usar
  o alvo em vez da pressão medida. Deu quase nada (3,72 vs 3,69), o que é a confirmação
  independente de que a H1 vale.
- **(c)/(d)** — respondem "a área efetiva é melhor descrita pelos bicos disparando ou pelas
  seções abertas?".

### 198–221: (e) e o perfil do atraso

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
- **210–219**: além do τ ótimo, varre 31 valores e guarda `rmse_est`/`rmse_val` de cada um.
  É esse perfil que revela o achado: **o objetivo é achatado em estimação e cresce em
  validação**, ou seja, o atraso não é identificável com estes dados. Guardar o perfil é o
  que transforma "o ajuste ficou ruim" em "a grandeza não é identificável".

### 223–224: (H3)

```python
models["(H3) vazão alvo da máquina"] = q_sp
```

Entra como "modelo" sem nenhum ajuste — é a própria conta da máquina, medida com a mesma
régua das demais.

## Linhas 231–237 — `shade_regimes`

```python
edges = np.flatnonzero(np.diff(spray.astype(int)))
bounds = np.concatenate([[0], edges + 1, [len(t)]])
for a, b in zip(bounds[:-1], bounds[1:]):
    if spray[a]:
        ax.axvspan(t[a], t[b - 1], ...)
```

Sombreia os trechos pulverizando. Detecta as transições pela derivada da máscara e desenha
um `axvspan` por corrida — em vez de um span por amostra, que geraria centenas de retângulos.

## Linhas 240–275 — `fig_flow`

Três painéis: série, resíduo e um **zoom de 12 s** no meio do trecho pulverizando
(linhas 262–273). O zoom foi o que revelou a causa dos resíduos de −30 L/min: o modelo cai a
zero nos buracos de disparo e a medida não. Sem ele, a figura de 113 s esconde o mecanismo.

Detalhes que importam: a medida é plotada **por último, com `zorder=5` e traço mais grosso**
(linha 248) — o dado tem que ficar acima dos modelos; e a legenda fica **fora** da área de
dados (`bbox_to_anchor=(0, 1.0)`, linha 253), depois de uma versão em que ela cobria a curva.

## Linhas 278–294 — `fig_scatter`

Dispersão medido × modelo, **só na validação e só pulverizando** (`m = spray & val`,
linha 282), com a reta 1:1 e R²/RMSE no título de cada painel. A reta 1:1 (não uma regressão)
é o que expõe viés: pontos sistematicamente de um lado da diagonal.

## Linhas 297–314 — `fig_pressure` (H1)

Série (medida vs alvo) e histograma do erro **separado por regime**. É a figura que mostra
os dois patamares: 250 kPa com seções fechadas e 406 kPa travado enquanto pulveriza. Os dois
histogramas sobrepostos (`alpha=0.7`, linha 307) tornam óbvio que são duas populações, não
uma distribuição com cauda.

## Linhas 317–344 — `fig_compare`

Barras de RMSE estimação vs validação por variante, com o número escrito em cima
(linhas 326–329) — é o que permite ler a tabela sem abrir o JSON. O painel da direita
(linhas 336–343) é o **perfil do τ**, e o título diz o que ele significa: objetivo achatado
= τ não identificável.

## Linhas 347–369 — `fig_multiscale`

```python
e_by = {m["bloco_s"]: m for m in ms_est if not m["descartado"]}
v_by = {m["bloco_s"]: m for m in ms_val if not m["descartado"]}
xs = sorted(set(e_by) & set(v_by))
```

Só as janelas válidas **nos dois** conjuntos. Foi correção de um erro real: estimação e
validação descartam janelas diferentes (a validação tem menos amostras), e plotar as duas
listas direto quebrava com "x and y must have same first dimension". Cada ponto é anotado
com o `n` de blocos (linhas 359–361) — sem isso, um R² alto com 12 blocos passaria por
robusto.

## Linhas 372–389 — `fig_residual_structure`

Resíduo do melhor modelo contra `N`, contra a pressão e contra a própria vazão. O objetivo
é diagnóstico, e está no título: **resíduo sem padrão = modelo adequado**. Padrão em algum
dos três painéis apontaria termo faltante (por exemplo curvatura vs `N` indicaria que a
área efetiva não é linear na contagem).

## Linhas 392–494 — `REPORT`: o relatório como template

Uma f-string gigante com marcadores, preenchida no fim do `main`. Duas razões para ser
template e não `print`: o relatório fica **versionável** ao lado das figuras, e a estrutura
(hipótese → parâmetros → métricas → veredito → ressalvas) é fixa, então dois logs geram
relatórios comparáveis linha a linha.

A seção "Ressalvas" é parte do produto, não decoração. A ressalva 1, em particular, foi
**reescrita depois de testada**: a suspeita era que o resíduo instantâneo fosse aliasing dos
100 ms; reexportando a 50 ms o resultado não mudou (3,79 vs 3,72 L/min), então o texto
registra o teste e a conclusão em vez da suposição. Como esse teste foi feito só no log
JD, o texto agora diz isso ("Testado no log JD WQR20230004", linha 484).

Quatro marcadores tiram do template o que era específico da JD:

| Marcador | Linha | Preenchido com |
|---|---|---|
| `{qcol}`, `{qdesc}` | 410 | a coluna usada como vazão e a descrição curta do `FLOW_DESC` |
| `{flow_note}` | 489 | a ressalva 2 do `FLOW_DESC` (flowmeter JD, ou o aviso de validação circular na Jacto) |
| `{psp_note}` | 493 | "um único perfil de pressão" quando o alvo é constante; senão a faixa do alvo |

O resto do texto (o flowmeter que "não enxerga" os buracos, o transitório de abertura na H1)
continua escrito para a JD — num REPORT Jacto, leia os números, não essas frases.

## Linhas 497–685 — `main`

### 498–524: CLI, escolha da vazão e checagem de contrato

```python
COLS["Q"] = (meta_in.get("flow_measured", "can_flow") if a.flow == "auto" else a.flow)
if not COLS["Q"]:
    raise SystemExit("o dataset não tem vazão medida na barra (Jacto: flow_lmin é estimativa).\n"
                     "H2 seria circular; para rodar assim mesmo: --flow can_flow_lmin")
...
falta = [c for c in COLS.values() if c not in df.columns]
```

- **505–507**: `--flow auto|<coluna>`. Default `auto`.
- **514**: o Δt vem do `dataset_meta.json`, com a mediana das diferenças de `t` como
  reserva. Ler o metadata em vez de inferir evita erro silencioso de escala nas janelas.
- **515**: com `auto`, a vazão é o `flow_measured` que o `export_dataset.py` gravou. Três
  casos: dataset JD → `"can_flow"`; dataset Jacto → `null` (não há vazão medida na barra);
  dataset antigo, sem a chave → o default `"can_flow"`, que é o comportamento de antes.
- **516–518**: `null` encerra **antes** de qualquer conta, explicando que a H2 seria
  circular e como forçar (`--flow can_flow_lmin`). Forçado, o REPORT carrega a ressalva.
  No log Jacto `20260831-040413`, forçado, a H1 dá pressão +6,3 % acima do alvo de 460 kPa
  (RMSE 74,5 kPa); os números de H2 existem, mas medem estimativa contra estimativa.
- **519**: imprime a coluna escolhida — quem lê o terminal sabe o que foi validado.
- **521–524**: falha **antes** de qualquer conta, dizendo qual coluna falta e o que fazer.

### 526–537: a divisão estimação/validação

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

### 541–549: H1

```python
sc = score(sig["P_sp"], sig["P"], mask)      # "modelo" = alvo; medido = real
rel = (sig["P"] - sig["P_sp"])[mask]
sc["erro_pct"] = float(100 * np.mean(rel / np.where(base == 0, np.nan, base)))
```

Trata o **alvo como previsão** e a pressão medida como verdade — é literalmente a hipótese
"o regulador entrega o alvo". O erro percentual usa `np.where(base == 0, np.nan, base)`
para não dividir por zero quando o alvo não está publicado.

### 551–563: H2/H3 e as métricas auxiliares

Três recortes por variante: pulverizando-estimação, pulverizando-validação e todo-o-log-
validação. O terceiro existe para quem quiser a métrica sem recorte de regime, mas o
relatório usa os dois primeiros — fora da pulverização a vazão é ~0 e a métrica relativa
perde sentido.

### 565–578: metadata e figuras

Tudo o que foi calculado vai para `metrics.json` (inclusive o perfil de τ e a estatística
dos buracos) **antes** de desenhar. Assim, figura quebrada não custa as métricas.

### 580–621: montagem do veredito

```python
validas = [m for e, m in zip(ms_est, ms_val) if not (m["descartado"] or e["descartado"])]
ms_ref = validas[-1] if validas else {...}
best = min(res, key=lambda k: res[k]["pulverizando_validacao"]["rmse"])
```

- **588–589**: a referência do veredito é a **maior janela válida nos dois conjuntos** —
  escolhida por regra, não escrita à mão, para o texto acompanhar o dado quando o log muda.
- **591**: o "melhor" modelo é decidido pelo RMSE de **validação**, nunca de estimação.
- **594–621**: o veredito é gerado com os números, não redigido: se outro log mudar as
  conclusões, o texto muda também. Inclui a leitura da não-identificabilidade do τ e a
  ressalva de que (a) vs (b) isola o custo de usar o alvo.

### 623–685: relatório e impressão

O `REPORT.format` (623–658) preenche o template; as linhas 631–636 calculam `qcol`, `qdesc`,
`flow_note` e `psp_note` a partir do `COLS["Q"]` e da faixa do alvo. Depois ecoa H1, a tabela de variantes, a validação multiescala (marcando as janelas descartadas com
o `n` dos dois lados) e a estatística dos buracos; depois escreve `REPORT.md` e lista os
arquivos gerados.

## Linhas 688–689 — guarda de execução

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
| vazão fixa em `can_flow` | dataset Jacto não tem `can_flow`; o único candidato é estimativa | `--flow`/`flow_measured`; Jacto recusada por padrão (validação circular) |

## O que este script deliberadamente não faz

| Não faz | Por quê |
|---|---|
| Identificar a dinâmica (C, τ) | o log é de malha fechada e o τ não é identificável — ver `wip_control_stage.py` |
| Projetar ou simular controle | etapa 2, parada a pedido |
| Estimar intervalo de confiança dos coeficientes | `metrics.json` traz `n` e viés; IC exigiria hipótese de ruído que os dados não sustentam |
| Corrigir a área efetiva pelo ciclo de trabalho | testado (média móvel e atraso), não melhora — o resíduo é do sensor |
| Validar sob mudança de pressão alvo | o log JD tem um único perfil (406 kPa); no dia Jacto a troca de alvo coincide com a máquina quase sem bicos abertos — alvo e carga confundidos |
| Validar a H2 na Jacto | não há vazão medida na barra; `flow_lmin` é o `predicted_flow` |
