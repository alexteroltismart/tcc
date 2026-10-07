# `parse_log_manual.py` explicado linha por linha

Referência do parser manual (`parse_log_manual.py`, 290 linhas) que está nesta mesma pasta.
Os números de linha correspondem à versão atual do arquivo (com suporte a Jacto, 2026-10-07).

Contexto do formato do log: `weedit_log.md` (§1–§7). Passo a passo de uso: `weedit_log.md` §8.
Máquinas Jacto: `weedit_log.md` §12. Análise gráfica em cima da saída: `plot_log.py` + `plot_log_explicado.md`.

Contrato do módulo: `convert(path, log_date=None, bitola_mm=None, members=None) -> (cfg, df, parts)`,
onde `cfg` é o JSON do cabeçalho, `df` é o log tokenizado (com o contexto em `df.attrs`) e `parts`
é um dicionário de DataFrames por família de mensagem. Serve igual para JD e Jacto: não há flag de máquina.

---

## Linhas 1–4 — docstring e imports

```python
"""Converte manualmente um log Weedit (.zip) em DataFrames. Só stdlib + pandas."""
import fnmatch, json, re, struct, zipfile
from pathlib import Path
import pandas as pd
```

- **1**: a promessa do arquivo. "Só stdlib + pandas" é uma restrição de projeto, não modéstia: as libs
  do repo (`libs.log_converter`) puxam `geohash2`, `geopandas` e `aws_lambda_powertools`, então em
  máquina enxuta elas não importam — e este parser tem que rodar em qualquer notebook.
- **2**: `fnmatch` (filtro `--members`), `json` (cabeçalho), `re` (regex do cabeçalho e agrupamento
  de hex), `struct` (unpack CAN), `zipfile` (abrir o log). Nenhum precisa de instalação.
- **3**: `Path` só para o caminho do zip Jacto no `selftest` (absoluto: o script também roda copiado em `tcc/scripts`).
- **4**: pandas faz todo o trabalho vetorizado — filtro, split, pivot, reamostragem.

## Linhas 6–21 — `read_txts`: abrir o zip (ou o `.txt`)

```python
def read_txts(path, members=None):
    if str(path).endswith(".txt"):
        with open(path, "rb") as fh:
            yield str(path), fh.read().decode("utf-8", errors="replace")
            return
    with zipfile.ZipFile(path) as z:
        names = sorted(n for n in z.namelist() if n.endswith(".txt"))
        if members:
            names = [n for n in names if fnmatch.fnmatch(n.split("/")[-1], members)]
        if not names:
            raise ValueError(...)
        for n in names:
            yield n, z.read(n).decode("utf-8", errors="replace")
```

Três formatos de entrada, uma função:

| Entrada | Exemplo | O que sai |
|---|---|---|
| zip com um `.txt` na raiz | JD `WQR20230004/20260318-155931.zip` | 1 par `(nome, texto)` |
| zip com pastas e vários `.txt` | Jacto `data_jacto/20260903.zip` (104 `.txt`, 821 MB) | 1 par por `.txt`, em ordem de nome |
| `.txt` solto | log extraído à mão | 1 par |

- **10–13**: `.txt` solto vira um único par. O `return` dentro do `with` encerra o gerador.
- **15**: **filtra por `.txt` em vez de pegar `namelist()[0]`**. A versão anterior copiava o
  `upload_files.py:decompress_file` e pegava o primeiro nome — no zip Jacto, o primeiro nome é a
  **pasta** `20260903/`, que lê como zero bytes. `sorted` dá ordem cronológica, porque o nome é
  `AAAAMMDD-HHMMSS.txt`.
- **16–17**: `members` é um glob aplicado **só ao nome do arquivo** (sem a pasta), então
  `--members '20260831-04*'` funciona sem saber o caminho interno.
- **18–19**: glob que não casa nada falha com mensagem clara, em vez de um `concat` vazio adiante.
- **20–21**: **gerador**, um arquivo por vez: quem consome pode descartar o texto antes de ler o
  próximo. `errors="replace"` é obrigatório: log de campo tem byte corrompido, e sem isso um único
  caractere inválido derruba a leitura do arquivo inteiro. Devolve **o nome também**, porque a data
  do log vem do nome (linha 247).

## Linhas 23–37 — `extract_header`: o JSON escondido nos comentários

```python
m = re.search(r"# Configurations:\r?\n(#\{.*?#\})", text, re.DOTALL)
if not m:
    return None
cleaned = re.sub(r"#", "", m.group(1)).strip().replace("\r", "")
cfg = json.loads(cleaned)
profiles = cfg.pop("profiles", None)
if isinstance(profiles, dict):          # Jacto grava "profiles": "{}" (string)
    default = cfg.get("default", {})
    for _, pdata in profiles.items():
        for k, ov in pdata.items():
            if isinstance(default.get(k), dict):
                default[k].update(ov)
return cfg.get("default", cfg)
```

- **25**: a mesma regex de `log_processing_utils.py:extract_header_log`. `\r?\n` cobre log gravado
  com CRLF; `re.DOTALL` deixa o `.` casar quebra de linha, que é o que permite pegar o JSON inteiro
  espalhado em várias linhas `#`; `.*?` é preguiçoso para parar no **primeiro** `#}`.
- **26–27**: log sem bloco de configuração devolve `None`. Não é erro — firmware antigo não grava
  cabeçalho, e o `convert` segue em frente.
- **28**: remove **todo** `#` (o do começo de cada linha) e os `\r`. Cuidado herdado do pipeline:
  isso apagaria um `#` que estivesse dentro de um valor de string do JSON. Nunca aconteceu, mas é
  a razão pela qual o cabeçalho não pode conter `#` nos valores.
- **29**: agora sim, JSON válido.
- **30–31**: `profiles` sai do dicionário **sempre** (o retorno não carrega a duplicata), mas só é
  mesclado se for dicionário. Firmware Jacto (WQR20240009, WQR20250023) grava `"profiles": "{}"` —
  uma **string** — e o `.items()` levantava `AttributeError`. O repo tem o mesmo código, mas dentro
  de um `try` que devolve `None`: lá a máquina é processada **sem cabeçalho** (bitola padrão, sem
  `toggleNozzles`), em silêncio.
- **32–36**: mescla de perfil. O log guarda `default` + `profiles`; o perfil ativo sobrescreve
  chave por chave. O `isinstance(..., dict)` protege contra sobrescrever um escalar com um dicionário.
- **37**: devolve a seção `default` (o que o Lambda espera), ou o dicionário inteiro se não houver.

## Linhas 39–41 — `header_bitola`

```python
def header_bitola(text):
    m = re.search(r"# Bitola:\s*(\d+)\s*mm", text)
    return int(m.group(1)) if m else None
```

A bitola não está no JSON: vem numa linha própria do cabeçalho (`# Bitola: 3900mm, Power Saving: 0, …`).
Antes ela era um argumento com padrão 6000 — certo para a JD de exemplo, errado para a Jacto (3900)
e para a WQR20240009 (4380). Só afeta `wdt_deltac` (linha 95), mas afetava em silêncio. `None` quando
a linha não existe; o fallback para 6000 fica no `convert` (linha 249).

## Linhas 43–57 — `read_log`: texto → DataFrame

```python
lines = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith("#")]
df = pd.Series(lines).str.split(" ", n=3, expand=True)
df.columns = ["DTime", "Sys", "ID", "MSG"][: df.shape[1]]
if df.shape[1] < 4:
    raise ValueError("log sem coluna MSG")
df = df[df.DTime.str.len() == 12].reset_index(drop=True)
```

- **45**: descarta linha vazia e cabeçalho numa passada. `lstrip()` antes do `startswith` porque
  algumas linhas de cabeçalho vêm indentadas. (O pipeline faz isso com `pd.read_table(sep="/")`,
  um truque para *não* quebrar a linha; aqui `splitlines()` é mais direto e não depende de o
  caractere `/` estar ausente dos dados.)
- **46**: **o split que define o formato**: no máximo 4 campos, então tudo depois do 3º espaço vai
  inteiro para `MSG`. É o que preserva o nome de bico com espaço (`N:Magnojet APS 30-02`) em vez de
  espalhá-lo em colunas fantasmas.
- **47**: nomeia só as colunas que existem — log sem nenhuma linha de 4 campos gera 3 colunas.
- **48–49**: e aí falha explicitamente. Melhor erro claro do que `KeyError: 'MSG'` trinta linhas depois.
- **50**: `len(DTime) == 12` é o filtro de sanidade barato: `"15:59:28.163"` tem 12 caracteres.
  Linha truncada, byte corrompido ou linha de continuação simplesmente não passa — inclusive as
  linhas de boot que o firmware Jacto grava (`Core`, `resuming`, `Creating`…).

```python
dtime = pd.to_timedelta(df.DTime, errors="coerce")
base = pd.to_datetime(log_date).floor("D")
d = dtime.diff()
rollover = (d < pd.Timedelta(hours=-1)) & (dtime.shift() >= pd.Timedelta(hours=20)) & (dtime <= pd.Timedelta(hours=4))
df["Time"] = base + pd.to_timedelta(rollover.cumsum(), unit="D") + dtime
return df.dropna(subset=["Time", "Sys"]).sort_values("Time").reset_index(drop=True)
```

- **52**: hora do dia como duração desde a meia-noite. `errors="coerce"` vira `NaT` no que não parsear.
- **53**: a data vem de fora (do nome do arquivo), porque **a linha do log não tem data**, só hora.
  `floor("D")` zera a hora do timestamp do log.
- **54–55**: detecção de virada de meia-noite com **três** condições ao mesmo tempo: salto para trás
  de mais de 1 h, vindo de depois das 20 h, caindo antes das 4 h. As três juntas porque o log vem
  fora de ordem: um salto para trás isolado é reordenação, não meia-noite. Com só a primeira
  condição, todo log embaralhado ganharia dias fantasmas.
- **56**: `cumsum()` transforma os eventos de virada em "quantos dias somar" para cada linha.
- **57**: descarta linha sem tempo ou sem `Sys`, **ordena por tempo** (o arquivo não vem ordenado —
  no log de exemplo aparece `15:59:30.963` seguido de `15:59:25.163`) e refaz o índice.

## Linhas 59–66 — os dois dicionários de tradução

```python
DETAIL_NAMES = {"A":"Area","B":"Bias","D":"Distance_m", ...}
MODES = {0:"Localizada Simples", 1:"Localizada PWM", ..., 93:"Aplicação na Entrelinha"}
```

Cópias fiéis de `log_converter.py:get_detail_names()` e `get_operation_modes()`. Cada campo dos
detalhes é `letra + valor` (`P1946` = Pressure 1946); as letras minúsculas (`m`, `t`, `w`, `i`, `f`)
são campos distintos das maiúsculas — `M` é Mode e `m` é Margin. Copiar em vez de importar é o preço
de não depender do repo; se o firmware ganhar um campo novo, é aqui que se acrescenta.

## Linhas 68–69 — `median_len_filter`

```python
def median_len_filter(s):
    return s.str.len() == s.str.len().median()
```

Uma linha que aparece em quase toda função de parse do pipeline: **mantém só as linhas com o
comprimento mais comum**. É o descarte de payload truncado sem `try/except` e sem hipótese sobre o
tamanho certo — a maioria define a norma. Mediana, não média nem máximo: imune a outlier.

## Linhas 71–77 — `get_sections`

```python
crit = ((df.Sys == "WDT") & df.ID.str.startswith("*SX0:3,")) | \
       ((df.Sys == "SEC") & df.ID.str.startswith("*SX0:1,"))
d = df[crit].copy()
d = d[median_len_filter(d.ID)]
d["SEC_HEX"] = d.ID.str[7:]
return d[["Time", "SEC_HEX"]].set_index("Time")
```

- **72–73**: as duas origens possíveis de seção, cada uma com **seu** `Sys`. A vírgula no prefixo
  (`*SX0:3,`) é o que separa dado de eco de comando (existe `*SX0:31` sem vírgula, que é outra coisa).
- **74**: `.copy()` para o pandas não reclamar de `SettingWithCopy` na atribuição da linha 76.
- **76**: `ID[7:]` pula `*SX0:3,` e deixa só o hex da máscara de seções.
- **77**: indexado por tempo — é o formato que todo consumidor (merge, gráfico) espera.

O hex fica **cru** de propósito: virar bit por bico exige a função certa do modelo
(`weedit_quadro_hex_to_bin` vs `weedit_ag_hex_to_bin`), e usar a errada espelha a barra sem erro.
Na Jacto de 144 bicos são 36 chars hex (= 144 bits, convenção `quadro`).

## Linhas 79–84 — `get_wdt` (detecção de erva)

```python
d = df[(df.Sys == "WDT") & df.ID.str.startswith("*PX0:h")].copy()
# reindex: linha *PX0:h sem vírgula devolve 1 coluna e o assign de 2 quebraria
d[["WDT_HEX", "CK"]] = d.ID.str[6:].str.split(",", n=1, expand=True).reindex(columns=[0, 1])
d = d[median_len_filter(d.WDT_HEX)]
return d[["Time", "WDT_HEX"]].set_index("Time")
```

- **80**: `*PX0:h` é a máscara de detecção por bico.
- **82**: `ID[6:]` pula o prefixo e divide **uma vez** na vírgula: hex à esquerda, checksum à direita.
  O `reindex(columns=[0, 1])` é blindagem: se nenhuma linha tiver vírgula, o `split` devolve 1 coluna
  e atribuir a 2 nomes levanta `ValueError` — com o reindex, `CK` vira `NaN` e a vida segue.
- **83**: filtro de mediana aplicado ao **hex**, não ao `ID` inteiro (o checksum tem tamanho variável).

## Linhas 86–96 — `get_speed`

```python
d = df[(df.Sys == "WDT") & df.ID.str.startswith("*SX0:98,")].copy()
if d.empty:
    return None
cols = ["cmd", "clock", "wdt_speed", "wdt_delta", "cdd_seq"]
parts = d.ID.str.split(",", expand=True).iloc[:, : len(cols)]
parts.columns = cols
d[cols] = parts.apply(pd.to_numeric, errors="coerce")
d["speed_center"] = d.wdt_speed + d.wdt_delta / 2
d["wdt_deltac"] = 1000 * d.wdt_delta / bitola_mm
return d.set_index("Time")[["speed_center", "wdt_deltac"]].resample("50ms").mean().dropna()
```

- **87–89**: sem mensagem de velocidade, devolve `None` (não um DataFrame vazio) — o consumidor
  distingue "não existe" de "existe e está vazio". Acontece de verdade: a WQB20200001 (Jacto,
  firmware antigo) não manda `*SX0:98`.
- **90–92**: nomeia os 5 campos posicionais e **corta o excesso** com `iloc[:, :5]`: firmware que
  passe a mandar um sexto campo não quebra o parse.
- **93**: converte tudo de uma vez; o que não for número vira `NaN`.
- **94**: `speed_center = wdt_speed + wdt_delta/2` — a velocidade no **centro** da barra, dado que o
  log traz a de uma ponta e o diferencial. Mesma fórmula do pipeline.
- **95**: `wdt_deltac = 1000 * wdt_delta / bitola_mm` — o diferencial normalizado pela bitola (em mm),
  e é o único lugar onde `bitola_mm` entra. Bitola errada afeta só esta coluna.
- **96**: reamostra a 50 ms pela média (a cadência nativa das mensagens) e descarta buraco.

## Linhas 98–99 — `reverse_words`

```python
def reverse_words(hex_str):
    return "".join(reversed(re.findall("[0-9a-fA-F]{8}", hex_str))) if isinstance(hex_str, str) else hex_str
```

Réplica de `reverse_side_data`: inverte a ordem das **palavras de 4 bytes** (8 chars hex), não dos
bicos um a um. Dois detalhes herdados: o `findall` **descarta a sobra** se o payload não for múltiplo
de 8 hex (JD: 120 chars; Jacto: 144 chars — ambos múltiplos, nada perdido), e o `isinstance` deixa
`NaN` passar intacto em vez de estourar.

## Linhas 101–119 — `side_data`: CDD e VAR (a função mais densa do arquivo)

```python
d = df[(df.Sys == sys_value) & df.ID.str.startswith(prefixes)].copy()
if d.empty:
    return None
d[["SIDE", name]] = d.ID.str[5:].str.split(",", n=1, expand=True)
d["SIDE"] = d.SIDE.replace(mapping)
if not set(mapping.values()).issubset(set(d.SIDE)):
    return None                       # falta um lado -> nada
```

- **102–104**: `startswith` aceita **tupla** de prefixos, então os dois lados entram num filtro só.
- **105**: `ID[5:]` pula `*SX0:` e sobra `31,<hex>`; o split separa o código do lado do payload.
- **106**: `31`→`LEFT`, `32`→`RIGHT` (ou `23`/`24` no VAR) — o mapa vem do chamador.
- **107–108**: **regra dura**: se um dos lados não aparece no log, devolve `None`. Meia barra é pior
  que nada — geraria um mapa de aplicação com metade da largura, silenciosamente.

```python
d = d.dropna(subset=[name]).drop_duplicates(["Time", "SIDE"])
d = d[d[name].str.fullmatch("[A-Fa-f0-9]+")]
d = d[d.groupby("SIDE")[name].transform(lambda s: s.str.len() == s.str.len().median())]
piv = d.pivot(index="Time", columns="SIDE", values=name)
piv["LEFT"] = [reverse_words(v) for v in piv.LEFT]
```

- **109**: mesmo timestamp e mesmo lado duas vezes = retransmissão; fica a primeira.
- **110**: `fullmatch` garante hex puro — descarta linha com lixo no meio do payload.
- **111**: filtro de mediana **por lado** (`groupby("SIDE")`), porque esquerda e direita podem ter
  contagens de bico diferentes em barra assimétrica. Filtrar pela mediana global cortaria o lado menor.
- **112**: pivot: uma linha por tempo, colunas `LEFT` e `RIGHT`.
- **113**: só a esquerda é invertida, para a barra ficar contígua da ponta esquerda à direita.

```python
idx = piv.resample("50ms").first().index
left = piv[["LEFT"]].dropna().reindex(idx, method="nearest", tolerance="10s")
right = piv[["RIGHT"]].dropna().reindex(idx, method="nearest", tolerance="10s")
out = pd.concat([left, right], axis=1).dropna()
out[name] = out.LEFT + out.RIGHT
return out[[name, "LEFT", "RIGHT"]]
```

- **114**: cria a grade regular de 50 ms.
- **115–116**: cada lado é realinhado **separadamente** na grade, pelo vizinho mais próximo, com
  tolerância de 10 s. Separado porque os dois lados chegam em instantes diferentes; sem isso um
  `dropna` conjunto derrubaria metade das amostras.
- **117**: junta e mantém só os instantes com os dois lados presentes.
- **118**: `LEFT + RIGHT` é **concatenação de string**, não soma: o resultado é a barra inteira em hex.
- **119**: devolve a barra e os dois lados, que é o que permite contar bicos por lado depois.

## Linhas 121–122 — os dois usos concretos

```python
get_cdd = lambda df: side_data(df, "WDT", ("*SX0:31", "*SX0:32"), {"31": "LEFT", "32": "RIGHT"}, "CDD")
get_var = lambda df: side_data(df, "SEC", ("*SX0:23", "*SX0:24"), {"23": "LEFT", "24": "RIGHT"}, "VAR")
```

Toda a diferença entre CDD e VAR: **o `Sys`** (`WDT` vs `SEC`) e os prefixos. Vale reler: no log real
existe `SEC *SX0:31` (eco, sem vírgula) e `WDT *SX0:31,<hex>` (dado) — trocar o `Sys` aqui devolve
lixo, não erro.

## Linhas 124–142 — `get_details`

```python
d = df[(df.Sys == "WDT") & df.ID.notna()].copy()
# nome do bico tem espaço: o split(n=3) jogou o resto em MSG -> junta de volta
glue = d.ID.str.startswith(("*PX0:I", "*CX0:I")) & d.MSG.notna() & (d.MSG != "")
d.loc[glue, "ID"] = d.loc[glue, "ID"] + d.loc[glue, "MSG"]
```

- **127–128**: **a pegadinha central do formato.** `N:Magnojet APS 30-02` tem espaço, então o
  `split(" ", n=3)` da linha 46 cortou o campo no meio e o resto foi para `MSG`. Aqui o `ID` é
  remontado — só nas linhas `*PX0:I`/`*CX0:I`, que são as que têm nome de bico. Quem parseia essas
  linhas fora deste fluxo **precisa** repetir isso, ou perde metade dos campos.

```python
d = d[d.ID.str.startswith(("*PX0:", "*CX0:"))].copy()
d["ID"] = d.ID.str[5:].str.replace(",,", ",")
fields = pd.DataFrame([{f[0]: f[1:] for f in row.split(",")[:-1] if f} for row in d.ID],
                      index=d.index)   # "if f": campo vazio faria f[0] estourar
```

- **129**: o prefixo aqui é **amplo** (`*PX0:` sem a letra), então entra também a linha `*PX0:h…` de
  detecção — é por isso que o DataFrame de detalhes tem uma coluna `h` com o hex da máscara.
  É o mesmo comportamento do pipeline; a coluna `h` é ruído útil, não bug.
- **130**: `,,` (campo vazio, comum em `…,V4491,,C111`) colapsa para uma vírgula.
- **131**: o coração: cada campo vira `{primeira letra: resto}`. O `[:-1]` descarta o último campo,
  que é o checksum (`C36`). O `if f` é blindagem: `,,,` sobrevive ao replace da 130 e um campo vazio
  faria `f[0]` levantar `IndexError`.

```python
out = pd.concat([d[["Time"]], fields], axis=1).sort_values("Time").ffill().bfill()
out = out.drop_duplicates("Time").set_index("Time").resample("100ms").nearest()
for c in out.columns:                        # float() puro: pd.to_numeric segfaulta aqui
    out[c] = out[c].map(_f)
out = out.rename(columns=DETAIL_NAMES)
if "Nozzle" in out:
    out["Nozzle"] = out.Nozzle.astype(str).str.lstrip(":")
if "Mode" in out:
    out["Application_Mode"] = out.Mode.replace(MODES)
```

- **133**: cola o tempo, ordena e preenche para frente e para trás — cada linha do log traz só um
  subconjunto dos campos, e o `ffill/bfill` é o que dá uma tabela densa.
- **134**: dedup por tempo e reamostragem a 100 ms pelo vizinho (`nearest`), a cadência que o
  pipeline usa para os detalhes.
- **135–136**: conversão numérica **com `float()` puro**, não `pd.to_numeric`. Não é preferência:
  a combinação pandas 2.3.3 + pyarrow 22 **segfaulta** em DataFrame reamostrado. O comentário fica na
  linha para ninguém "melhorar" isso de volta.
- **137**: traduz as letras para nomes legíveis. Letra não mapeada **permanece como letra**
  (`E`, `F`, `W`, `S`, `G`, `u`, `v`) — visível e não inventada. Na Jacto aparece `Flowmeter`
  (campo `f`), mas zerado: não é vazão medida.
- **138–139**: `Nozzle` vem como `:Magnojet…`; tira o `:` da frente.
- **140–141**: cria a coluna com o nome do modo, **mantendo** o `Mode` numérico ao lado.

## Linhas 144–148 — `_f`

```python
def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return v
```

Converte se der, devolve o original se não der. Captura `TypeError` **e** `ValueError` porque a
coluna mistura `None` com string. É o que mantém `Nozzle` como texto enquanto `Pressure` vira número,
sem lista de exceções por coluna.

## Linhas 150–153 — `get_voltage`

```python
d = df[(df.Sys == "VOL") & df.ID.notna()].set_index("Time")
d["Vol"] = (10 * pd.to_numeric(d.ID.str[:-1], errors="coerce")).round()
return d[["Vol"]].dropna().resample("50ms").first().dropna()
```

- **151**: a linha é `VOL 13.26V`.
- **152**: `ID[:-1]` corta o `V` final e o ×10 replica o pipeline: o valor guardado é **décimo de
  volt inteiro** (13,26 V → 133). Se quiser volt, divida por 10 na leitura (é o que o `plot_log.py` faz).
- **153**: `first()` em vez de `mean()` — tensão é amostra pontual, não média de intervalo.

## Linhas 155–191 — as definições CAN

```python
CAN_DEFS = {
    "10FFF8E111": ["<HHHH", {1: "can_flow", 2: "can_pressure"}],
    ...
    "FEF3": ["<II", {0: "latitude", 1: "longitude"}],      # < 8 chars -> casa por PGN
    # Jacto 3030/4530 ...
    "1AFFFFF9": ["<HHHH", {0: "can_speed", 2: "can_pressure"}],
    ...
}
CAN_RATIOS = {
    "10FFF8E111": {"can_flow": (0, 0.1), "can_pressure": (0, 0.1)},
    ...
}
```

- **156**: o comentário do formato: `{prefixo: [fmt_struct, {índice_na_tupla: nome}]}`.
- **158–169**: JD, Horsch, bomba Weedit (`13333333` sub-IDs 00/02/03/04) e GPS — um subconjunto do
  que vive no AWS Secrets. O **índice é posição na tupla desempacotada**, não offset de byte: em
  `<BHHHB`, o índice 1 é o primeiro `H`, que começa no byte 1. Errar isso é o jeito mais comum de
  ler o campo vizinho e não notar.
- **169**: `FEF3` tem menos de 8 caracteres, e é isso que faz o casamento virar **PGN** na linha 210.
- **170–178**: Jacto 3030/4530 (`machineModel` 6/7/18/22), copiados de `Update_Secrets.py` e
  conferidos contra `section-controller/src/parseCAN.cpp`:

  | Prefixo | Sinais | Leitura |
  |---|---|---|
  | `1AFFFFF9` | `can_speed`, `can_pressure` (psi ×6,89476 → kPa) | pressão confere com o sensor Weedit (corr 0,985) |
  | `1AFFFFED` | `pump_rpm` | unidade não documentada |
  | `1AFFFFFC` | `pump_flow` ×0,1 | vazão **total** da bomba, com retorno — não acompanha os bicos |
  | `1AFFFFFF` | `engine_rpm` | ~1600 rpm |
  | `1888888ADE` / `1888888A77` | `sent_machine_flow`, `stm_flow` / `machine_pwm`, `pump_pwm` | hydrosync / placa STM |
  | `18888888AA` | `flow_lmin` ×0,1, `braglia_mode` | **é o `predicted_flow`** (corr 0,999, sem atraso) — estimativa, não flowmeter |

  **`can_pressure` repete o nome do JD de propósito** (comentário da linha 171): JD e Jacto nunca
  mandam os dois IDs no mesmo log, e assim todo consumidor (`plot_log`, `export_dataset`,
  `validate_plant_model`) lê a pressão pelo mesmo nome, sem flag de máquina. Se algum dia um log
  trouxer os dois, o `first()` da linha 221 fica com o que chegar primeiro em cada intervalo — aí é
  hora de renomear.
- **180–191**: `(offset, ratio)` por sinal, separado das definições para espelhar os dois
  dicionários do repo (`can_msg_parse_definitions` e `can_msg_offset_and_ratios`). Quem não aparece
  aqui usa `(0, 1)` (linha 216) — valor bruto (`pump_rpm`, `engine_rpm`, os PWMs).
- Para a tabela completa, copiar de `docs/Notebook/Update_Secrets.py`, trocando a chave string
  (`'1'`) por int, como o `get_can_msg_parse_definitions_df` faz com `int(k)`.

## Linhas 193–197 — `build_idmsg`

```python
d = df[df.Sys.str.startswith("CAN")].copy()
d["ID"] = d.ID.str[2:].str.zfill(8)
d["IDMSG"] = d.ID + d.MSG
return d[d.IDMSG.str.len() == 24].set_index("Time")
```

- **194**: pega `CANI`, `CANT`, `CANP`, `CANTX0` e o `CANRX0` do firmware Jacto de uma vez — qualquer
  canal CAN.
- **195**: `[2:]` remove o `0x` e `zfill(8)` completa ID curto. **Este `zfill` é o detalhe que
  diverge dentro do próprio repo**: `can_utils` monta o `IDMSG` sem ele em duas funções, então ID de
  7 dígitos se comporta diferente lá. Aqui segue a versão do pipeline principal.
- **196**: 8 chars de ID + 16 de dados.
- **197**: `len == 24` descarta o que não tem o formato completo (inclusive `MSG` nulo, que produz
  `NaN` e não passa no teste). Índice = tempo, que é o que o `resample` da linha 221 exige.

## Linhas 199–202 — `unpack`

```python
if fmt == "3byte":
    return pd.DataFrame([[int.from_bytes(bytes.fromhex(x[10:16]), "little")] for x in idmsgs])
return pd.DataFrame([struct.unpack(fmt, bytes.fromhex(x[8:])) for x in idmsgs])
```

- **200–201**: o caso especial: 3 bytes little-endian tirados de `IDMSG[10:16]` (ou seja, pulando o
  ID e o primeiro byte de dados). Um único sinal, por isso a lista de um elemento.
- **202**: o caso geral: `x[8:]` são exatamente os 8 bytes de dados; o `fmt` tem que somar 8 bytes,
  senão `struct.unpack` levanta `struct.error` — o que é bom: definição errada falha alto.

## Linhas 204–223 — `parse_can`

```python
for prefix, (fmt, sig) in CAN_DEFS.items():
    if len(prefix) >= 8:
        sel = df_can[df_can.IDMSG.str[: len(prefix)] == prefix]
    else:
        sel = df_can[df_can.IDMSG.str[2:6] == prefix]
    if sel.empty:
        continue
```

- **207–210**: **as duas regras de casamento**, e a única coisa que decide entre elas é o
  comprimento da chave. `>= 8`: prefixo do `IDMSG`, o que permite filtrar por sub-ID (o byte de
  multiplexação depois do ID, como `10FFF8E1` + `11`, ou `1888888A` + `DE`). `< 8`: PGN em
  `IDMSG[2:6]`, ignorando prioridade e endereço de origem. Comparar fatia com `==` (em vez de
  `startswith` por linha) é o que mantém isso em velocidade de C.
- **211–212**: definição que não aparece no log é ignorada em silêncio — é o normal, cada máquina
  fala um subconjunto. É isso que deixa JD e Jacto conviverem na mesma tabela sem flag de máquina.

```python
raw = unpack(sel.IDMSG, fmt)
parsed = pd.DataFrame(index=sel.index)
for ix, name in sig.items():
    off, ratio = CAN_RATIOS.get(prefix, {}).get(name, (0, 1))
    parsed[name] = raw[ix].to_numpy() * ratio + off
out.append(parsed)
```

- **213–214**: `parsed` nasce com o índice **de tempo** de `sel`; `raw` tem índice 0..n.
- **217**: `to_numpy()` é obrigatório: sem ele o pandas alinharia pelo índice, que é justamente o
  que os dois não compartilham, e o resultado viria todo `NaN`. A escala é
  `valor = bruto * ratio + offset` — a mesma ordem do pipeline (offset **depois** da razão).

```python
if not out:
    raise ValueError("nenhuma mensagem CAN conhecida no log")
df = pd.concat(out).sort_index().resample(time_interval).first()
limit = max(1, int(pd.Timedelta("60s") / pd.Timedelta(time_interval)))
return df.ffill(limit=limit).bfill(limit=limit)
```

- **219–220**: nenhuma definição casou ⇒ **erro**, igual ao pipeline. Silenciar aqui produziria um
  DataFrame vazio que só dá problema muito depois.
- **221**: `concat` de frames com colunas diferentes gera a união (com `NaN` onde a mensagem não
  existe); `sort_index` reordena no tempo; `first()` resume cada intervalo.
- **222–223**: `ffill`/`bfill` **com limite de 60 s** convertido em número de amostras. Sem o limite,
  uma parada entre duas operações propaga o último valor por todo o intervalo — no pipeline isso
  estourava memória nos resamplers seguintes.

## Linhas 225–236 — `selftest`

```python
cfg, df, p = convert("/home/shared/.../WQR20230004/20260318-155931.zip")
assert df.attrs["bitola_mm"] == 6000 and "can_flow" in p["can"]
assert (len(p["cdd"].LEFT.iloc[0]) // 2, len(p["cdd"].RIGHT.iloc[0]) // 2) == (60, 60)
jacto = Path("/home/jupyter-alex/rep/claude_working/context_files/20260908/data_jacto/20260903.zip")
cfg, df, p = convert(jacto, members="20260831-040413*")
assert df.attrs["machine_model"] == 7 and df.attrs["bitola_mm"] == 3900
assert (len(p["cdd"].LEFT.iloc[0]) // 2, len(p["cdd"].RIGHT.iloc[0]) // 2) == (72, 72)
assert 100 < p["can"].can_pressure[p["can"].current_nozzles_open > 1].median() < 700
assert {"flow_lmin", "pump_flow", "engine_rpm"} <= set(p["can"].columns)
```

Um log de cada família, só `assert`, sem framework (`python3 parse_log_manual.py --selftest`).
Cada linha trava uma coisa que já quebrou ou que quebraria em silêncio:

- **228–230 (JD)**: bitola do cabeçalho, flowmeter JD decodificado, barra 60+60.
- **231**: o zip Jacto com pastas + filtro `members` — exercita o `read_txts` inteiro. O caminho é
  relativo ao script (`here`, linha 227), não ao diretório de onde se roda.
- **232**: cabeçalho com `profiles` em string ainda abre (senão `machine_model` seria `None`) e a
  bitola veio da linha `# Bitola:` (3900, não o padrão 6000).
- **233**: barra Jacto 72+72.
- **234**: escala do `1AFFFFF9` — com o ratio de psi esquecido, a mediana pulverizando cairia para ~70.
- **235**: os IDs Jacto casaram.

## Linhas 238–264 — `convert`: a única função que você precisa chamar

```python
cfg, dfs, files = None, [], []
for name, text in read_txts(path, members):
    files.append(name)
    cfg = cfg or extract_header(text)
    bitola_mm = bitola_mm or header_bitola(text)
    dfs.append(read_log(text, log_date or name.split("/")[-1].split(".")[0].split("-")[0]))
df = pd.concat(dfs).sort_values("Time").reset_index(drop=True)
bitola_mm = bitola_mm or 6000
...
df.attrs.update(files=files, bitola_mm=bitola_mm,
                machine_code=mc.get("machineCode"), machine_model=mc.get("machineModel"))
return cfg, df, parts
```

- **242–247**: um `read_log` **por arquivo**, cada um com a sua data. Necessário porque um zip Jacto
  atravessa dias (`20260829` a `20260903`) e a linha do log só tem hora.
- **244**: o cabeçalho vem do **primeiro** arquivo que tiver um (os do mesmo zip são da mesma máquina).
- **245**: bitola passada à mão vence; senão, a primeira encontrada no cabeçalho.
- **246**: comentário `ponytail:` marca o limite conhecido: tudo vai para memória. O dia Jacto inteiro
  (~800 MB de texto, ~13 milhões de linhas) pede `members` para recortar. Processar em blocos só se
  isso virar gargalo de verdade.
- **247**: a data sai do nome **sem a pasta**: `20260903/logs-1020BA4E21A4/20260831-040413.txt` →
  `20260831`. `log_date` à mão sobrescreve para todos os arquivos.
- **248**: junta e **reordena no tempo** — os arquivos já vêm em ordem, mas cada `read_log` ordena só
  o seu pedaço.
- **249**: fallback 6000 só depois de olhar todos os arquivos.
- **250–260**: cada família num DataFrame próprio, com **a chave que o `plot_log.py` usa**
  (`parts["can"]`, `parts["cdd"]`…). Chaves com valor `None` são normais (máquina sem VAR).
- **261–263**: o contexto do log vai em `df.attrs` — arquivos lidos, bitola efetiva, código e modelo
  da máquina. Sem mudar a assinatura do retorno (os três chamadores continuam com `cfg, df, parts`),
  o `export_dataset.py` grava isso no `dataset_meta.json` e o `plot_log.py` põe no título. `cfg or {}`
  porque log sem cabeçalho devolve `None`.
- **264**: devolve os três níveis: config, log cru tokenizado e as partes parseadas. O `df` cru volta
  de propósito — é onde se investiga `Sys` que ninguém parseia (`ROW`, `PUMP`, `CTR`, `TIMECTR`).

## Linhas 266–290 — execução direta

```python
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("log", nargs="?", default="/home/shared/.../20260318-155931.zip")
    ap.add_argument("--members", help="glob dos .txt dentro do zip, ex.: '20260831-04*'")
    ap.add_argument("--selftest", action="store_true", help="checa um log JD e um Jacto e sai")
    a = ap.parse_args()
    if a.selftest:
        raise SystemExit(selftest())
    cfg, df, parts = convert(a.log, members=a.members)
```

- **267–272**: `argparse` local, porque só o modo script precisa dele. O log é posicional e opcional:
  `python3 parse_log_manual.py` puro roda no log de exemplo, e `python3 parse_log_manual.py LOG.zip`
  continua funcionando como antes.
- **273–274**: `--selftest` roda as checagens e sai. `SystemExit(None)` = código 0; um `assert`
  falhando sai com erro.
- **276–279**: as primeiras conferências: o cabeçalho abriu, quantos arquivos foram lidos, máquina,
  modelo e bitola (de `df.attrs`), e a distribuição de `Sys`.
- **280–285**: para cada parte, `shape` e as 6 primeiras colunas — `None` aparece como `None`, o que
  torna óbvio o que a máquina não manda.
- **287**: as 3 primeiras linhas do CAN parseado: é onde se vê se pressão e vazão têm ordem de
  grandeza plausível e se a coordenada caiu no talhão.
- **289–290**: amostra do CDD e **bicos por lado** (`len(LEFT)//2`, 2 chars hex por bico) — a
  checagem de configuração de barra mais direta que existe: `(60, 60)` na JD, `(72, 72)` na Jacto.

---

## Correções feitas durante esta revisão

| Linha | Era | Virou | Por quê |
|---|---|---|---|
| 2 | `import io` | removido | nunca usado |
| 15 | `z.namelist()[0]` | todos os `.txt`, ordenados | no zip Jacto o primeiro nome é uma pasta (lia zero bytes) e há 104 logs |
| 30–31 | `if "profiles" in cfg: ... profiles.items()` | `isinstance(profiles, dict)` | firmware Jacto grava `"profiles": "{}"` (string) → `AttributeError` |
| 39–41, 245 | `bitola_mm=6000` fixo | lida de `# Bitola:` | Jacto tem 3900 mm, WQR20240009 4380 mm |
| 82 | `split(",", n=1, expand=True)` | `+ .reindex(columns=[0, 1])` | log sem vírgula na linha `*PX0:h` levantava `ValueError` no assign de 2 colunas |
| 131 | `{f[0]: f[1:] for f in ...}` | `... if f}` | campo vazio sobrevivente ao `replace(",,", ",")` levantava `IndexError` |
| 136 | `.map(lambda v: _f(v))` | `.map(_f)` | o lambda não fazia nada |

Revalidado nos logs JD (`WQR20230004`: 56.727 linhas, CSV exportado com md5 idêntico ao de antes
da mudança Jacto; `WQR20250011`: 70.217 linhas) e Jacto (`WQR20250023` `20260831-040413`: 324.061
linhas; `WQR20240009`, `WQB20200001`, `WQR20250010`), com o `plot_log.py` gerando as 4 figuras.

## O que este parser deliberadamente não faz

| Não faz | Por quê | Onde está no repo |
|---|---|---|
| Converter hex em bit por bico | depende do modelo (quadro/AG) e errar espelha a barra em silêncio | `log_converter_utils.hex_to_bin` |
| Geometria da barra / GPS → polígono | precisa de `geopandas` | `log_converter.split_calc_boom_coords` |
| `ha_min`, `can_rate_lha`, raster | não é parse | `log_converter` linhas ~1289–1640 |
| Cache/manifest incremental | é script de análise, não pipeline | `graphify`/`detect` do pipeline real |
| Transcrever `ROW`, `PUMP`, `CTR`, `TIMECTR` | nada no pipeline consome | ninguém — é código novo se precisar |
| Decodificar o mapa de bicos Jacto `1AFFFFD8…DF` | o pipeline também não decodifica | ninguém — 8 mensagens a 10 Hz no log |
| Processar o dia Jacto inteiro em blocos | tudo em memória basta com `--members` | — |
