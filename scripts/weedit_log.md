# Weedit — Parse do arquivo de log (mensagens Weedit + CAN)

Contexto extraído de `/home/jupyter-alex/rep/weedit` (`CLAUDE.md` §"CANBUS Log Format & Processing" + código) e
**conferido contra um log real**: `/home/shared/data/Weedit/s3_bucket/WQR20230004/20260318-155931.zip`
(56.832 linhas). Escopo: **só o parse do arquivo de log** — como as linhas viram DataFrame, e como cada
tipo de mensagem (Weedit ASCII e CAN hex) é decodificado. Nada de raster, GPKG, relatório ou nuvem.

Arquivos que importam:

| Arquivo | Papel |
|---|---|
| `services/src/utils/log_processing_utils.py` | `extract_header_log()` — cabeçalho `#` → JSON de config |
| `services/src/libs/log_converter.py` | `read_log()` (tokenização) + todo o parse das mensagens Weedit |
| `services/src/libs/log_converter_utils.py` | `process_side_data()` / `get_cdd()` / `get_var()` |
| `services/src/libs/can_utils.py` | `CANUtils` — matching e unpack das mensagens CAN |
| `services/src/libs/gps_utils.py` | GPS: NovAtel serial, NMEA e PGN de CAN |
| `docs/Notebook/Update_Secrets.py` | fonte das definições CAN (vão para o AWS Secrets) |

---

## 1. Estrutura física do arquivo

`.zip` → um único `.txt` (`upload_files.py:decompress_file` pega `namelist()[0]`).
O `.txt` tem duas partes:

```
# Current section controller settings          ← cabeçalho: TODA linha começa com '#'
# Software Version: 4.300100
# Bitola: 6000mm, Power Saving: 0, Off Delay: 1
# Current config profile: 410_KPa
# Configurations:
#{ ... JSON de configuração, uma linha por '#' ... #}
15:59:28.163 CANTX0 0x0CFEF31C FD1057763145FF5C   ← dados: {DTime} {Sys} {ID} [{MSG}]
15:59:31.811 WDT *PX0:h000000000000000000000000000623,P1946,V4491,,C111
```

### Cabeçalho (`extract_header_log`)
- Regex `r"# Configurations:\r?\n(#\{.*?#\})"`, remove todos os `#` e `\r`, `json.loads`.
- Se existir `profiles`, os overrides do perfil são mesclados dentro de `default`; retorna `default`.
- Dali saem `miscConfig.toggleNozzles`/`evenOddNozzles` → `toggle_nozzles`, `weeditConfig.rowWidth` → `row_width`,
  e `header_operation_mode` (`process_machine_config_from_header`).
- Sem esse bloco: retorna `None` e o pipeline segue só com o config da máquina.

---

## 2. `read_log()` — de texto para DataFrame (`log_converter.py:931`)

```python
df = pd.read_table(buffer, dtype="object", sep="/", on_bad_lines="skip",
                   encoding_errors="replace", header=None, comment=None)
df = df[~df[0].astype(str).str.lstrip().str.startswith("#")]   # descarta cabeçalho
df = df[0].str.split(" ", n=3, expand=True)                    # → DTime, Sys, ID, MSG
df = df[df.DTime.str.len() == 12]                              # "15:59:28.163"
```

Pontos que mordem:

- **`sep="/"`** não é separador de campo, é um truque para *não* quebrar a linha (nenhum log tem `/`
  nos dados). O split real é o `str.split(" ", n=3)`.
- **`n=3` significa 4 colunas no máximo** → tudo que sobrar depois do 3º espaço vai inteiro para `MSG`.
- Se a linha tiver menos de 4 colunas em *todo* o arquivo, `read_log` retorna `None`.
- **Filtro `len(DTime)==12`** joga fora linha corrompida/parcial sem precisar de try/except.
- **Data**: `DateLog = floor(log_timestamp, "D")`; vira `Time = DateLog + DTime`.
- **Virada de meia-noite**: só conta como rollover se o salto for `< -1h` **e** vindo de `>= 20h`
  **e** caindo em `<= 4h` (`cumsum` soma um dia). Isso evita que log fora de ordem crie dias fantasmas.
- **O log NÃO vem ordenado** — no arquivo real aparece `15:59:30.963` e logo depois `15:59:25.163`.
  `read_log` faz `sort_values("Time")` no fim. Nunca assuma ordem lendo o `.txt` na mão.
- `align_timestamp()` (opcional) corrige offset usando a cadência das mensagens `FEF3` (GPS).

### Tipos de `Sys` no log real

| Sys | Contagem | O que é | Quem consome |
|---|---|---|---|
| `CANI` | 28.524 | CAN Input (recebido de terceiros: JD, Case…) | `can_utils` |
| `WDT` | 13.469 | mensagens ASCII do Weedit (detecção, velocidade, CDD, detalhes) | `log_converter` |
| `SEC` | 10.187 | seções / VAR / eco de comando | `log_converter` |
| `CANT` / `CANP` / `CANTX0` | 1.145 / 1.120 / 597 | CAN Transmit / Passthrough / TX do section controller | `can_utils` |
| `ROW` | 1.119 | máscara de linhas em ASCII binário (`1011001…`) | **não é parseado** |
| `CTR`, `TIMECTR`, `PUMP` | 114 / 114 / 56 | contadores e debug da bomba (`PUMP:72, WDT:100, DUTY:0`) | **não é parseado** |
| `VOL` | 114 | tensão: `13.26V` | `get_voltage()` |

Regra geral: **`Sys.startswith("CAN")` → caminho CAN; `WDT`/`SEC` → caminho Weedit ASCII.**

---

## 3. Mensagens Weedit (ASCII, `Sys` = `WDT`/`SEC`)

O campo `ID` carrega o payload, no formato `*{canal}X0:{código}[,campos…]`.
Os prefixos, com exemplos reais:

### 3.1 Seções — `*SX0:3,` (WDT) e `*SX0:1,` (SEC) → coluna `SEC`
```
15:59:31.791 WDT *SX0:3,000000000000000000000000000000
```
`get_app()` (linha ~414): filtra os dois prefixos, mantém só as linhas cujo `len(ID)` é **a mediana**
(descarta truncadas), e converte `ID[7:]` hex→bin com `hex_to_bin()`.

### 3.2 Detecção de erva — `*PX0:h` (WDT) → coluna `WDT`
```
15:59:31.811 WDT *PX0:h000000000000000000000000000623,P1946,V4491,,C111
```
`ID[6:]` é dividido em `WDT,CK` (checksum) no primeiro `,`; `WDT` vira binário por bico
(`hex_to_bin`), filtrado pela mediana de comprimento, e reamostrado a `time_interval` (50 ms)
por `resample_df_to_specific_frequency_nearest`.

- Máquinas **WEEDIT-AG** (não custom) não têm `SEC`: `df_section = df_wdt` e `SEC = "1" * n_nozzles`.
- `hex_to_bin` é **dependente do modelo**: `weedit_ag_hex_to_bin` vs `weedit_quadro_hex_to_bin`
  (a ordem dos bits do bico difere). Usar o errado inverte a barra inteira, sem erro nenhum.
- `SEC` e `WDT` vazios juntos ⇒ erro `DATA` e log descartado.

### 3.3 Velocidade — `*SX0:98,` (WDT)
```
15:59:31.828 WDT *SX0:98,25341620,4458,-69,9831
                  cmd  clock   wdt_speed wdt_delta cdd_seq
```
`get_speed()` (~530):
```
speed_center = wdt_speed + wdt_delta / 2
wdt_deltac   = 1000 * wdt_delta / bitola     # bitola em mm, do cabeçalho
```
Reamostra por `mean()`, arredonda, `astype(int)`.

### 3.4 CDD e VAR — pares esquerda/direita (`process_side_data`)
```
15:59:31.814 WDT *SX0:31,94BDFFFFD6CAFFFF…   ← CDD LEFT
15:59:31.846 WDT *SX0:32,…                    ← CDD RIGHT
15:59:31.8xx SEC *SX0:23,0000C766FD0000C7FF…  ← VAR LEFT
15:59:31.8xx SEC *SX0:24,…                    ← VAR RIGHT
```
| Coluna | `Sys` | Prefixos | Função |
|---|---|---|---|
| `CDD` | **WDT** | `*SX0:31` / `*SX0:32` | `get_cdd()` |
| `VAR` | **SEC** | `*SX0:23` / `*SX0:24` | `get_var()` |

O `Sys` importa: no log real existe também `SEC *SX0:31` **sem vírgula** — é eco de comando, não dado,
e é justamente o `Sys` que separa um do outro.

Pipeline de `process_side_data()`:
1. `ID[5:]` → `SIDE` + payload; `31/23`→LEFT, `32/24`→RIGHT.
2. Se algum dos lados não aparece no log → **retorna `None`** (não devolve meia barra).
3. Dedup por `(Time, SIDE)`, filtro por mediana de comprimento **por lado**, e `fullmatch("[A-Fa-f0-9]+")`.
4. Pivot por `Time`; o lado esquerdo passa por `reverse_side_data()`, que inverte a ordem das
   **palavras de 4 bytes** (`re.findall("[0-9a-fA-F]{8}")` + `reversed`), não os bicos um a um.
   Esse `findall` **descarta a sobra** se o payload não for múltiplo de 8 hex — nos logs reais o
   payload tem 120 chars (múltiplo de 8, nada perdido), mas outra largura de barra pode perder
   até 3 bicos em silêncio.
5. Reamostra 50 ms com `nearest` e tolerância de 10 s por lado; `CDD = LEFT + RIGHT` (concatenação de strings).
6. Cada bico ocupa **2 caracteres hex** → `n_nozzles = len(LEFT)//2 + len(RIGHT)//2`, e é assim que
   `check_nozzles_side_bar()` corrige a config da máquina pela realidade do log.

### 3.5 Detalhes da aplicação — `*PX0:I` / `*CX0:I` (e `*?X0:n` / `*?X0:N`)
```
15:59:31.818 WDT *PX0:I33001203,X3,E0,F00022010,L580580,H15316470,U0,A15602975,T42,V4491,D9831,P1946,Y1,Q0,C36
15:59:31.822 WDT *CX0:I33001203,W3000,S18,M1,R98.8,B100,N:Magnojet APS 30-02,G2,m300,w2,u5184,v5184,C92
```
`get_app_details()` (~612) corta `ID[5:]` e monta um dict `{primeira letra: resto}` por campo separado por `,`.
Mapa (`detail_names`, ~260):

`A`=Area · `B`=Bias · `D`=Distance_m · `H`=Herbicide_ml · `K`=Sensitivity · `M`=Mode · `N`=Nozzle ·
`L`=Liquid_HerbSolu · `P`=Pressure · `Q`=Savings · `I`=WDT_Serial_ID · `R`=Rate · `T`=RunTime ·
`U`=Usage_mlHa · `V`=WDTSpeed · `X`=Status · `Y`=Sunlight · `m`=Margin · `t`=WDTTime · `w`=Wind ·
`i`=Poll_Interval · `f`=Flowmeter

`Mode` → `Application_Mode` via `operation_modes`:
`0` Localizada Simples · `1` Localizada PWM · `2` Cobertura · `3` Dual · `4` GoG Simples ·
`5` GoG PWM · `6` Cobertura CDD · `7` GoG Dual · `91` Taxa Variável · `92` Aplicação na Linha ·
`93` Aplicação na Entrelinha

**A pegadinha do nome do bico:** `N:Magnojet APS 30-02` tem espaços, então o `split(" ", n=3)` do
`read_log` quebra a linha no meio do campo e o resto cai em `MSG`. Por isso `get_app_details` faz
`ID = ID + MSG` quando o `ID` começa com `*PX0:I`/`*CX0:I` e `MSG` não está vazio (~626). Quem parsear
essas linhas fora do pipeline **precisa refazer essa junção**.

Outros detalhes:
- `*?X0:n` → `{rate_spot, rate_cover}`, `*?X0:N` → `{pwm_spot, pwm_cover}` (`get_pwm_rate`, campos 4 e 5) — só
  quando não é WEEDIT-AG.
- Reamostragem `100ms` + `nearest`, `ffill().bfill()`.
- Conversão numérica é feita com `float()` puro em `map`, **não** com `pd.to_numeric`: a combinação
  pandas 2.3.3 + pyarrow 22 dá **segfault** em frame reamostrado (ver `_try_float`).
- `_drop_stray_non_numeric()` limpa o valor não-numérico solto (um `*SX0:99` que vaza no `Margin`
  derrubava o log inteiro depois, no `np.clip`).

### 3.6 Tensão — `VOL`
```
15:59:32.001 VOL 13.26V     →  Vol = round(10 * float("13.26")) = 133
```
`get_voltage()` (~981) tira o `V` final e multiplica por 10 (décimo de volt inteiro).

---

## 4. Mensagens CAN (`Sys` começa com `CAN`)

### 4.1 A chave `IDMSG`
```
15:59:28.163 CANTX0 0x0CFEF31C FD1057763145FF5C
                    └─ ID ──┘  └──── MSG ────┘
IDMSG = ID[2:].zfill(8) + MSG      # tira o "0x", 8 hex de ID + 16 hex de dados = 24 chars
```
No pipeline principal (`log_converter.py:1155`):
```python
df_new["ID"]    = df_new.ID.str[2:].str.zfill(8)
df_new["IDMSG"] = df_new.ID + df_new.MSG
df_new = df_new[df_new.IDMSG.str.len() == 24]     # descarta qualquer coisa fora do formato
```
`can_utils` faz `ID.str[2:] + MSG` **sem `zfill`** quando monta o `IDMSG` por conta própria
(`get_boom_height_case/m4030`, linhas 390 e 429) — ID de 7 dígitos não bate nessas funções. Se for
comparar prefixos na mão, use sempre a versão com `zfill(8)`.

### 4.2 As definições (AWS Secrets, geradas por `docs/Notebook/Update_Secrets.py`)

Dois dicionários por ID, unidos em `can_msg_parse_definitions_df` (`can_utils.py:33`):
```python
can_msg_parse_definitions   = {'10FFF8E111': ['<HHHH', {'2':'can_pressure', '1':'can_flow'}]}
can_msg_offset_and_ratios   = {'10FFF8E111': {'can_pressure': [0, 0.1], 'can_flow': [0, 0.1]}}
                                                           # [offset, ratio]
```
Vira uma tabela `MSGID | fmt | ix | col_name | offset | ratio`, com `offset=0`/`ratio=1` para o que
não tiver override.

### 4.3 Matching (`get_parsed_df`, ~201)
- `len(msg_id) >= 8` → **prefixo do IDMSG** (`IDMSG[:len] == msg_id`), o que permite filtrar por sub-ID
  (o byte de multiplexação logo depois do ID, ex.: `10FFF8E1` + `11`).
- `len(msg_id) < 8` → **PGN**: `IDMSG[2:6] == msg_id` (ex.: `FEF3`, `FEE8`), casando qualquer
  prioridade/endereço.
- Uma linha pode casar com mais de uma definição — é intencional.
- Se nada casar: **exceção** ("No known CAN messages found in this log").

### 4.4 Unpack (`parse_can_info`, ~162)
```python
if fmt == "3byte":
    x_int = [[int.from_bytes(bytes.fromhex(x[10:16]), "little")] for x in msgs]
else:
    x_int = [struct.unpack(fmt, bytes.fromhex(x[8:])) for x in msgs]   # x[8:] = só os 8 bytes de dados
...
valor = campo_bruto[ix] * ratio + offset
```
- `fmt` é um formato `struct` little-endian (`<HHHH`, `<BHHHB`, `<BbbbbbbB`, `<qq`, …).
- `ix` é o índice **na tupla desempacotada**, não byte offset.
- `3byte` é o caso especial: 3 bytes little-endian tirados de `IDMSG[10:16]`.
- Depois: `resample(time_interval).first()` → filtro de mediana móvel na altura de barra →
  `ffill/bfill` **com limite de 60 s** (sem o limite, uma parada entre duas operações propagava
  valor velho pelo log todo e estourava memória adiante).

### 4.5 IDs principais

| IDMSG (prefixo) | Origem | Sinais (fmt) |
|---|---|---|
| `10FFF8E111` | JD Rate Controller | `can_flow` ×0.1 L/min, `can_pressure` ×0.1 kPa (`<HHHH`) |
| `18FFFBE10025` | JD Rate Controller | `can_rate` ×0.1 L/ha, `can_pressure` ×0.5 (`<HHHH`) |
| `18FFFBE10026` | JD | `pump_rpm` ×0.1 |
| `18FFFFE1DE` | JD antigo | `can_flow` ×0.01, `can_rate` ×0.0935396, `can_pressure` ×0.2, `can_pump_pwm` ×3.90625 (`<BHHHB`) |
| `18FF028102` / `18FF028302` | JD 3 bytes | `can_flow` ×6e-05 (`3byte`) |
| `18FF028103` / `18FF028303` | JD 3 bytes | `can_pressure` ×0.001 (`3byte`) |
| `18FE4926` | Horsch Leeb / Raven | `can_flow` ×0.01, `can_accumulator` ×0.1 (`<HHHH`) |
| `1AFFFFF9` | máquina | `can_speed` ×2.7778, `can_pressure` ×6.89476 |
| `1AFFFFFC` | máquina | `pump_flow` ×0.1 |
| `1333333300` | bomba Weedit | `target_liters_flow`, `current_nominal_flow`, `predicted_flow`, `braglia_flow` (`<BHHHB`) |
| `1333333302` | bomba Weedit | `pwm_output`, `pressure_pwm`, `flow_pwm` (`<BHHHB`) |
| `1333333303` | bomba Weedit | `sections_open`, `current_nozzles_open`, `pwm_wdt_system`, `speed_center`, `speed_delta` (`<BBBBhh`) |

> Divergência: o `CLAUDE.md` do repo lista `1333333303` como `<BBBBHh` e sem `pwm_wdt_system`;
> a fonte real (`Update_Secrets.py`) usa `<BBBBhh`. Vale o código.
| `1333333304` | bomba Weedit | `nominal_pressure`, `target_pressure` (`<BHHBBB`) |
| `08FFF4CD9B0{0,1,2,9,A}` | sensores de altura | `Ground_*`, `Canopy_*` (`<HHHH`) |
| `18EF9080..18EF9086 +10` | altura XRT | `Ground_*`, `Canopy_*` (`<BBHHBB`) |
| `0CF00400` / `0CF004F0` / `0CF00482` | motor | `engine_rpm` ×0.125 |
| `FEF3` (PGN) | posição J1939 | `latitude`, `longitude` ×1e-7 −210 (`<II`) |
| `FEE8` (PGN) | atitude/velocidade | `heading` ×0.0078125, `speed` ×0.00390625, `pitch`, `elevation` |
| `F805FEF3` | GPS de alta resolução | `latitude`, `longitude` ×1e-16 (`<qq`) |
| `18FF408F01FFF8FF` | seções por CAN | `Can_Sections` (`<II`) |

Altura de barra tem parser dedicado (`parse_bh_message`, `can_utils.py:254`), não a tabela genérica:
`M4030` → `<HHHH` → `{Ground: [1], Canopy: [2]}`; `case` → `<BHHHB` → `{Ground_L2, Ground_C0, Ground_R2}`;
`f` → `<H`. A ordem de tentativa é **XRT → `18FF049002` (case) → `08FFF4CD9B0*` (M4030)**.

---

## 5. GPS — três caminhos, nessa ordem (`gps_utils.py`)

1. **NovAtel serial** (`Sys == "GPS"`): `ID` com exatamente **48 hex** → `struct.unpack("<ddd")` →
   `(lat, lon, alt)` em double (`parse_gps_novatel`).
2. **NMEA texto** (fallback): linha cujo `ID` começa com `$GPGGA`/`$GNGGA` — **em qualquer `Sys`**
   (chega como `SAUX` no firmware Stara RS-485 e como `GPS` nas WEEDIT-AG). É a sentença que
   seleciona a linha, não o canal. Conversão DDMM.MMMMM → graus decimais em `parse_gpgga_nmea`.
3. **CAN** (`get_data_CAN`): PGN `FEF3` via `msgid="0CFEF31C"`, comparando `IDMSG[2:][:4]`, e
   ignorando `MSG == "FFFFFFFFFFFFFFFF"` (payload inválido).
   `parse_65267`: `struct.unpack("<II")` × `1e-7` **− 210**.

No log de exemplo, o GPS vem justamente como `CANTX0 0x0CFEF31C` — o section controller já converte o
NMEA para PGN padrão antes de gravar (`prep_nmea_2000_gps` está desativado no `get_parsed_df` por isso).

---

## 6. Resumo do parse, ponta a ponta

```
.zip
 └─ .txt
     ├─ linhas "#"          → extract_header_log()  → cfg (toggle_nozzles, row_width, modo)
     └─ linhas de dados     → read_log()            → DataFrame [DTime, Sys, ID, MSG, Time]
                                                        │
              ┌─────────────────────────────────────────┴──────────────────────────────┐
        Sys ∈ {WDT, SEC, VOL}                                        Sys.startswith("CAN")
              │                                                                        │
    get_app()        → SEC, WDT (bin por bico)              IDMSG = ID[2:].zfill(8)+MSG, len==24
    get_cdd()/get_var() → CDD, VAR (LEFT+RIGHT)                        │
    get_speed()      → speed_center, wdt_deltac              get_parsed_df() → match prefixo/PGN
    get_app_details()→ Area, Rate, Pressure, Mode…                     → parse_can_info() (struct)
    get_voltage()    → Vol                                             → valor*ratio + offset
                                                             get_boom_height() → Ground/Canopy
                                                             GpsUtils          → lat/lon/elev
```

## 7. Checklist de pegadinhas (todas verificadas no código/log real)

1. O log **não vem ordenado no tempo**; `read_log` ordena. Ler o `.txt` cru engana.
2. `split(" ", n=3)`: campo com espaço (`N:Magnojet APS 30-02`) vaza para `MSG` — refaça `ID+MSG`
   para `*PX0:I`/`*CX0:I`.
3. Filtros por **mediana de comprimento** descartam silenciosamente linhas truncadas em `SEC`, `WDT`,
   `CDD` e `VAR`. Contagem menor que o esperado costuma ser isso, não perda de dados na origem.
4. `process_side_data` devolve `None` se **um** dos lados faltar — sem CDD/VAR nenhum, não meia barra.
5. `hex_to_bin` depende do modelo (AG vs Quadro): errar inverte a barra sem levantar erro.
6. `CDD`/`VAR`: 2 chars hex por bico; o lado esquerdo é invertido em blocos de **4 bytes**, e o
    `re.findall("…{8}")` corta a sobra se o payload não for múltiplo de 8 hex (120 nos logs reais).
7. `IDMSG` com `zfill(8)` no pipeline principal, **sem** `zfill` dentro de `can_utils` — ID de 7 dígitos
   se comporta diferente nas duas rotas.
8. Definição CAN com `len < 8` casa por **PGN** (`IDMSG[2:6]`), ou seja, ignora prioridade e endereço.
9. `ix` das definições é índice da tupla do `struct`, não offset de byte.
10. `ffill/bfill` do CAN tem limite de 60 s; a máquina parada não propaga valor antigo.
11. `pd.to_numeric` em frame reamostrado dá **segfault** (pandas 2.3.3 + pyarrow 22): use `float()` em `map`.
12. `Sys` `ROW`, `PUMP`, `CTR`, `TIMECTR` existem no log e **não são parseados** por nada do pipeline —
    se precisar deles, é código novo.

---

# 8. Passo a passo: converter um log em DataFrame na mão

Roteiro para reproduzir o parse fora do pipeline (notebook, script de análise, debug de log de campo).
Não precisa de AWS, nem de Lambda, nem das libs do repo — só `pandas` + stdlib. As libs do repo
(`libs.log_converter`) puxam `geohash2`, `aws_lambda_powertools`, `geopandas` etc., então em máquina
enxuta o caminho manual é o único que roda.

**Script pronto e executável: `parse_log_manual.py`, ao lado deste arquivo.**
Explicação linha por linha dele: **`parse_log_manual_explicado.md`**.

```bash
python3 parse_log_manual.py                                   # usa um log de exemplo
python3 parse_log_manual.py /caminho/para/AAAAMMDD-HHMMSS.zip # qualquer log
```

Validado em dois logs reais de máquinas diferentes:
`WQR20230004/20260318-155931.zip` (56.727 linhas) e `WQR20250011/20260317-152229.zip` (70.217 linhas).

## Passo 1 — abrir o zip

Um zip, um `.txt` dentro. O nome do arquivo carrega a data (`20260318-155931.txt`), que é o
`log_timestamp` usado para datar as linhas.

```python
with zipfile.ZipFile(zip_path) as z:
    name = z.namelist()[0]                 # o pipeline também usa só o primeiro
    text = z.read(name).decode("utf-8", errors="replace")   # errors="replace": log de campo vem com lixo
```

## Passo 2 — extrair o cabeçalho (config da máquina)

```python
m = re.search(r"# Configurations:\r?\n(#\{.*?#\})", text, re.DOTALL)
cleaned = re.sub(r"#", "", m.group(1)).strip().replace("\r", "")
cfg = json.loads(cleaned)
if "profiles" in cfg:                      # perfil ativo sobrescreve o default
    for _, pdata in cfg.pop("profiles").items():
        for k, ov in pdata.items():
            if isinstance(cfg["default"].get(k), dict):
                cfg["default"][k].update(ov)
cfg = cfg.get("default", cfg)
```
Saída real: `['machineConfig', 'wifiConfig', 'weeditConfig', 'miscConfig']`.
Daqui saem `bitola` (para a velocidade), `miscConfig.toggleNozzles`, `weeditConfig.rowWidth`.
Log antigo pode não ter esse bloco → `None`, e você precisa da config da máquina por outra via.

## Passo 3 — tokenizar em `DTime | Sys | ID | MSG | Time`

```python
lines = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith("#")]
df = pd.Series(lines).str.split(" ", n=3, expand=True)
df.columns = ["DTime", "Sys", "ID", "MSG"]
df = df[df.DTime.str.len() == 12].reset_index(drop=True)     # descarta linha corrompida

dtime = pd.to_timedelta(df.DTime, errors="coerce")
base  = pd.to_datetime(log_date).floor("D")
d = dtime.diff()
rollover = (d < pd.Timedelta(hours=-1)) & (dtime.shift() >= pd.Timedelta(hours=20)) & (dtime <= pd.Timedelta(hours=4))
df["Time"] = base + pd.to_timedelta(rollover.cumsum(), unit="D") + dtime
df = df.dropna(subset=["Time", "Sys"]).sort_values("Time").reset_index(drop=True)
```

Confira aqui antes de seguir: `df.Sys.value_counts()`. No log de exemplo dá
`CANI 28524 · WDT 13469 · SEC 10187 · CANT 1145 · CANP 1120 · ROW 1119 · CANTX0 597 · '' 168 · CTR/TIMECTR/VOL 114 · PUMP 56`.
Se `CANI`/`CANTX0` estiverem zerados, o log é de máquina sem CAN (ou o `Sys` mudou de nome no firmware)
e o passo 5 vai levantar exceção.

## Passo 4 — mensagens Weedit (uma função por prefixo)

Todas seguem o mesmo padrão: filtra `Sys` + prefixo do `ID`, corta o payload, aplica o **filtro de
mediana de comprimento**, reamostra.

```python
# 4.1 seções -> hex por bico
crit = ((df.Sys == "WDT") & df.ID.str.startswith("*SX0:3,")) | \
       ((df.Sys == "SEC") & df.ID.str.startswith("*SX0:1,"))
d = df[crit]; d = d[d.ID.str.len() == d.ID.str.len().median()]
sections = d.assign(SEC_HEX=d.ID.str[7:]).set_index("Time")[["SEC_HEX"]]

# 4.2 detecção de erva: ID[6:] = "<hex>,<checksum>"
d = df[(df.Sys == "WDT") & df.ID.str.startswith("*PX0:h")]
d[["WDT_HEX", "CK"]] = d.ID.str[6:].str.split(",", n=1, expand=True)

# 4.3 velocidade
d = df[(df.Sys == "WDT") & df.ID.str.startswith("*SX0:98,")]
cols = ["cmd", "clock", "wdt_speed", "wdt_delta", "cdd_seq"]
d[cols] = d.ID.str.split(",", expand=True).iloc[:, :5].apply(pd.to_numeric, errors="coerce")
d["speed_center"] = d.wdt_speed + d.wdt_delta / 2
d["wdt_deltac"]   = 1000 * d.wdt_delta / bitola_mm      # bitola do cabeçalho!

# 4.4 CDD (WDT, 31/32) e VAR (SEC, 23/24) — ver side_data() no script
# 4.5 detalhes: junta ID+MSG nos *PX0:I / *CX0:I antes de dividir por ','
# 4.6 tensão: Vol = round(10 * float(ID[:-1]))
```

Para virar bit por bico, o payload hex precisa do `hex_to_bin` **do modelo certo**
(`weedit_ag_hex_to_bin` vs `weedit_quadro_hex_to_bin`, em `log_converter_utils.py`). O script manual
deixa o hex cru de propósito: converter com a função errada inverte a barra sem dar erro.

## Passo 5 — mensagens CAN

```python
# 5.1 monta a chave
d = df[df.Sys.str.startswith("CAN")].copy()
d["ID"]    = d.ID.str[2:].str.zfill(8)          # "0x0CFEF31C" -> "0CFEF31C"
d["IDMSG"] = d.ID + d.MSG
df_can = d[d.IDMSG.str.len() == 24].set_index("Time")

# 5.2 casa cada definição
if len(prefix) >= 8: sel = df_can[df_can.IDMSG.str[:len(prefix)] == prefix]   # prefixo/sub-ID
else:                sel = df_can[df_can.IDMSG.str[2:6] == prefix]           # PGN

# 5.3 desempacota os 8 bytes de dados e escala
raw = pd.DataFrame([struct.unpack(fmt, bytes.fromhex(x[8:])) for x in sel.IDMSG])
parsed[name] = raw[ix].to_numpy() * ratio + offset

# 5.4 reamostra com limite de preenchimento
df = pd.concat(out).sort_index().resample("100ms").first()
limit = max(1, int(pd.Timedelta("60s") / pd.Timedelta("100ms")))     # 600
df = df.ffill(limit=limit).bfill(limit=limit)
```

O script traz um `CAN_DEFS`/`CAN_RATIOS` reduzido (8 IDs: JD, Horsch, bomba Weedit e GPS `FEF3`).
Para a tabela completa, copie os dois dicionários de `docs/Notebook/Update_Secrets.py` — o formato é o
mesmo, só troque a chave `'1'` string por `1` int (ou faça `int(k)` ao carregar, como o
`get_can_msg_parse_definitions_df` faz).

## Passo 6 — conferir o resultado

Saída real de `parse_log_manual.py` no log de exemplo:

```
header keys: ['machineConfig', 'wifiConfig', 'weeditConfig', 'miscConfig']
linhas de dados: 56727
sections  (1122, 1)   wdt (2234, 1)   speed (2188, 2)
cdd       (2277, 3)   var (2277, 3)   details (1139, 30)   vol (114, 1)
can       (1206, 14)  cols: can_flow, can_pressure, can_rate, target_liters_flow, …

                         can_flow  can_pressure   latitude  longitude
2026-03-18 15:59:25.100       8.5         270.3 -11.458347 -53.976593

CDD amostra: FFFF34FFFFC3A5FFFF82FFFFFF2A4BA8B234FFE1
bicos por lado: (60, 60)
```

Checagens que valem antes de confiar no DataFrame:

| Checagem | O que esperar | Se falhar |
|---|---|---|
| `len(LEFT)//2 + len(RIGHT)//2` | = número de bicos da máquina (aqui 60+60) | config de bicos errada, ou payload truncado |
| `can_pressure`, `can_flow` | kPa e L/min plausíveis (270 kPa, 8,5 L/min) | `ratio`/`offset` ou sub-ID errado |
| `latitude`/`longitude` | dentro do talhão (aqui −11,46 / −53,98) | esqueceu o `−210` do `parse_65267` |
| `var is None` | normal em máquina sem taxa variável | no `WQR20250011` dá `None` mesmo: a máquina não manda `*SX0:23/24` |
| `speed_center` | km/h × 100 conforme firmware, sem negativo estranho | `bitola` errada afeta só `wdt_deltac` |

## Passo 7 — daí para frente (fora deste escopo)

Com os DataFrames em mão, o pipeline real ainda faz: GPS → geometria da barra
(`split_calc_boom_coords`), merge de tudo em 50 ms, cálculo de `ha_min`/`can_rate_lha`, raster e GPKG.
Nada disso é parse, e está fora deste documento.

---

# 9. Análise gráfica: `plot_log.py`

Consome o `parse_log_manual.convert()` e plota tudo ao longo do tempo. Só `matplotlib` + `pandas`.

```bash
python3 plot_log.py                                  # log de exemplo, PNGs em ./plots
python3 plot_log.py LOG.zip --out /tmp/analise        # outro log, outra pasta
python3 plot_log.py LOG.zip --step 200ms              # mais resolução (default 1s)
python3 plot_log.py LOG.zip --model ag --bitola 3000  # máquina WEEDIT-AG
python3 plot_log.py --selftest                        # checa a ordem de bits do hex_to_bits
```

| Figura | Conteúdo |
|---|---|
| `overview.png` | 9 painéis: velocidade, pressão, vazão, taxa, seções/bicos abertos, PWM, tensão, delta de velocidade, luminosidade |
| `counters.png` | contadores acumulados como **Δ desde o início da janela** (área, distância, herbicida, solução, economia, runtime) |
| `nozzles.png` | heatmaps bico × tempo: CDD, VAR, detecção (WDT) e seções (SEC) |
| `gps.png` | trajeto lat/lon colorido pelo tempo |

Explicação linha por linha do script: **`plot_log_explicado.md`**, nesta mesma pasta.

Regras de leitura embutidas no script:

- **Um eixo Y por painel.** Medidas de unidade diferente nunca compartilham painel (sem eixo duplo).
  Por isso `Pressure` entra como `P/10` (o log traz 0,1 kPa) e cai no mesmo painel do `can_pressure`,
  enquanto `Sunlight` ganhou painel próprio.
- **Paleta categórica em ordem fixa**, 8 slots, validada (pior par adjacente ΔE 9,1 sob protanopia;
  todos os checks PASS). Legenda sempre que há ≥2 séries, acima da área de dados; painel de série
  única nomeia a série no título.
- **Heatmap com rampa sequencial de um matiz** (azul, começando no step 250 para não sumir no fundo
  claro); máscara binária usa duas cores com colorbar rotulada `fechado`/`aberto`.
- **Série 100% NaN ou 100% zero é descartada** e listada no fim da execução — é assim que se vê num
  relance o que a máquina não manda. Exemplos reais:
  - `WQR20230004`: ausentes `braglia_flow`, `Flowmeter`, `can_pump_pwm`.
  - `WQR20250011` (Horsch Leeb): ausentes também `can_flow`, `can_pressure`, `can_rate`,
    `sections_open`, `current_nozzles_open` — máquina sem rate controller no CAN, exatamente o caso
    descrito em "Common Issues" do `CLAUDE.md`.

Pegadinhas que valem lembrar:

- **A janela de um log é curta.** Nos dois exemplos: 2 min (`WQR20230004`) e 5,5 min (`WQR20250011`),
  com 56k–70k linhas. `--step 1s` já dá 120–330 pontos; não espere um dia inteiro num arquivo.
- `hex_to_bits` reproduz as duas convenções do pipeline: `quadro` = 4 bits por nibble **invertidos**;
  `ag` = bits por byte invertidos com `{i:05b}`, que é largura **mínima** — byte ≥ 32 rende 8 bits, não 5.
  Por isso `matrix_bits` corta pela mediana da largura. O `--selftest` trava nisso.
- Velocidade fica em unidade bruta (≈ mm/s; × 0,0036 ≈ km/h). Não converti porque o fator não está
  documentado no repo — melhor eixo honesto que número errado.
- Modo escuro não foi feito: é PNG de diagnóstico, tema único. Se for para tela, vale gerar a variante
  com os tokens escuros da mesma rampa.

---

# 10. Exportar para simulação / identificação de sistemas: `export_dataset.py`

Explicação linha por linha: **`export_dataset_explicado.md`**.

O `parse_log_manual.py` entrega famílias em cadências diferentes (50 ms, 100 ms, evento) e colunas de
texto (hex por bico). Nada disso serve direto para simulação ou identificação. Este exportador
transforma tudo em **uma matriz numérica de Δt constante**, com `t` em segundos e metadados ao lado.

```bash
python3 export_dataset.py                                   # ./dataset, csv+parquet, Δt=100ms, ZOH
python3 export_dataset.py LOG.zip --dt 50ms --trim          # cadência nativa das mensagens
python3 export_dataset.py LOG.zip --format npz,mat          # numpy / MATLAB-Octave
python3 export_dataset.py LOG.zip --fill interp             # interpolação no tempo em vez de ZOH
python3 export_dataset.py LOG.zip --out /tmp/id --trim --format parquet
```

## Formatos

| Formato | Arquivo | Quando usar |
|---|---|---|
| `parquet` | `dataset.parquet` | **default para Python.** Preserva dtype e o índice temporal; leitura rápida |
| `csv` | `dataset.csv` | universal (Excel, R, gnuplot, qualquer coisa). Perde dtype |
| `npz` | `dataset.npz` | `t`, `data` (matriz), `columns`, `timestamp` — numpy puro, sem pandas |
| `mat` | `dataset.mat` | MATLAB/Octave: `t`, `y` (amostras × sinais), `names`, `Ts` |
| sempre | `dataset_meta.json` | Δt, fs, unidade e fonte de cada sinal, `n_unique`, sugestão de E/S, cabeçalho do log |

## As duas decisões que importam para controle

**1. `--fill zoh` (default) vs `--fill interp`.**
`zoh` mantém o último valor até chegar a próxima mensagem — é o que um registrador amostrado
realmente faz, e é a hipótese padrão para **entrada** em identificação de tempo discreto.
`interp` interpola no tempo (só no interior, sem extrapolar) e é mais adequado para **saída** de
sensor contínuo lido em cadência irregular. Não existe escolha certa para todos os sinais: exporte
duas vezes se precisar de tratamento diferente para `u` e `y`.

**2. `--trim`.** Recorta as bordas até a janela onde **todos** os sinais têm valor. Sem ele, o
começo da série tem NaN nos sinais cuja família começa depois (no log de exemplo, 69 amostras: o CAN
começa antes das mensagens WDT). Com `--trim`, o log de exemplo sai **1138 × 50 sem um único NaN** —
que é o que a maioria das rotinas de identificação exige.

## Sinais derivados das máscaras hex

O que era texto vira número, com nome explícito:

| Sinal | De onde | O que é |
|---|---|---|
| `nozzles_on` | `wdt.WDT_HEX` | contagem de bits 1 = bicos disparando naquele instante |
| `sections_on` | `sections.SEC_HEX` | contagem de bicos habilitados pela seção |
| `cdd_mean`, `cdd_max` | `cdd.CDD` | média e máximo do byte por bico na barra |
| `var_mean` | `var.VAR` | média do byte de taxa variável |

A contagem usa o `hex_to_bits` do `plot_log.py`, então respeita `--model quadro|ag`.

## Consumindo

```python
import pandas as pd, numpy as np, json
df = pd.read_parquet("dataset/dataset.parquet")
meta = json.load(open("dataset/dataset_meta.json"))
Ts = meta["dt_s"]                                  # 0.1 s
u = df[meta["io_hint"]["inputs"]].to_numpy()       # entradas sugeridas
y = df[["can_pressure"]].to_numpy()                # saída escolhida por você
```

```python
# numpy puro, sem pandas
z = np.load("dataset/dataset.npz", allow_pickle=True)
t, data, cols = z["t"], z["data"], list(z["columns"])
pwm = data[:, cols.index("can_pwm_wdt_system")]
```

```matlab
% MATLAB / Octave
S = load('dataset/dataset.mat');
i = find(strcmp(S.names, 'can_pwm_wdt_system'));
j = find(strcmp(S.names, 'can_pressure'));
d = iddata(S.y(:,j), S.y(:,i), S.Ts);   % planta PWM -> pressão
```

O `io_hint` do metadata é **sugestão**: entradas `pwm_wdt_system`, `can_pump_pwm`,
`target_liters_flow`, `sections_open`, `nozzles_on`, `speed_center`; saídas `can_flow`,
`can_pressure`, `details_pressure`, `predicted_flow`. Confirme a causalidade antes de identificar —
`sections_open` e `nozzles_on` são mais perturbação de carga que entrada manipulada.

## Sanidade verificada no log de exemplo

| Checagem | Resultado | O que prova |
|---|---|---|
| `Δt` entre amostras | constante 0,1 s | a grade é regular de fato |
| `parquet` = `npz` = `mat` = `csv` | mesmas dimensões (1138 × 50) | os quatro formatos carregam o mesmo dado |
| `corr(details_pressure/10, can_pressure)` | **0,985** | o `P` do log realmente está em 0,1 kPa |
| `corr(nozzles_on, can_flow)` | **0,853** | a contagem de bits decodificada bate com a vazão medida |
| `max(sections_on)` vs `max(can_sections_open)` | 120 = 120 | a decodificação do bitmask concorda com o contador que vem no CAN |
| NaN após `--trim` | 0 | matriz densa, pronta para regressão |

## Pegadinhas

- **`--dt 100ms` é uma escolha, não o dado.** As mensagens nativas são de 50 ms; para dinâmica rápida
  (transitório de pressão), exporte com `--dt 50ms`. Reamostrar para mais lento é filtro implícito.
- **16 colunas são constantes** no log de exemplo (`details_rate`, `details_mode`, `can_braglia_flow`…).
  O metadata traz `n_unique` por coluna justamente para você descartá-las antes de uma regressão —
  coluna constante deixa a matriz de regressores deficiente de rank.
- **`nozzles_on > sections_on` em 2 de 1138 amostras** (0,17%): artefato do realinhamento ZOH, a
  máscara de detecção chegando um instante antes da atualização da seção. Não é erro de decodificação,
  mas se o seu modelo usa a diferença dos dois, saturе em zero.
- A velocidade continua em unidade bruta (≈ mm/s). O metadata diz isso em `unit`; converter é decisão
  de quem modela.
- `details_h` (a máscara hex de detecção) é **excluída** de propósito: parte dos valores parseia como
  número e geraria uma coluna sem significado físico. A informação útil dela está em `nozzles_on`.

---

# 11. Validação do modelo da planta: `validate_plant_model.py`

Etapa 1 de 2. **Só validação do modelo hidráulico** — controle ficou para depois
(o que já estava escrito está parado em `wip_control_stage.py`, com o motivo no cabeçalho).

Explicação linha por linha: **`validate_plant_model_explicado.md`**.

Pergunta: alimentando o modelo apenas com o que a máquina conhece — **bicos disparando,
seções abertas, pressão alvo e vazão alvo** — a pressão e a vazão previstas ficam
próximas das medidas?

```bash
python3 validate_plant_model.py                        # ./validation
python3 validate_plant_model.py --data outro/dataset.parquet --out val2
python3 validate_plant_model.py --split-mode tempo     # divide o log inteiro (default divide as amostras pulverizando)
```

## Hipóteses testadas

| # | Hipótese | Resultado |
|---|---|---|
| **H1** | `P ≈ P_alvo` (o regulador mantém a pressão) | **válida pulverizando** (−1,8 %, RMSE 14,9 kPa); **inválida** com seções fechadas (−141 kPa) |
| **H2** | `q = k · A(N,S) · √P` (orifício / Torricelli) | **válida**: R² 0,92 em janela de 1 s, RMSE 3,0 L/min |
| **H3** | `q_alvo ≈ q_medida` | R² 0,66 — mas `target_liters_flow` é **setpoint**, não previsão |

Variantes de H2 (coeficiente calibrado só na estimação, métricas na validação):

| Variante | k | RMSE val. | R² val. |
|---|---|---|---|
| (a) `k·N·√P_alvo` — só entradas | 0,0288 | 3,72 | 0,879 |
| (b) `k·N·√P_medida` | 0,0291 | 3,69 | 0,881 |
| (c) `k·S·√P_alvo` — área pelas seções | 0,0126 | 4,08 | 0,854 |
| (d) `(a·N + b·S)·√P_alvo` | — | 4,08 | 0,854 |
| (e) (a) + atraso de 1ª ordem | — | 5,60 | 0,726 |

Três leituras que saem dessa tabela:

- **(a) ≈ (b)**: usar a pressão **alvo** em vez da medida praticamente não custa nada —
  consequência direta da H1 valer. O modelo funciona como simulador, sem realimentação.
- **(a) melhor que (c)/(d)**: a área efetiva é melhor descrita pelos **bicos disparando**
  que pelas seções abertas. (c) ganha na estimação e perde na validação — sobreajuste.
- **(e) piora**: o τ ajustado (1,6 s) não generaliza, e o perfil de RMSE × τ é achatado
  na estimação (painel direito de `model_compare.png`). **O atraso não é identificável**
  com estes dados; o modelo estático é o que o dado sustenta.

## O detalhe que muda a interpretação

Durante a pulverização, `nozzles_on` **cai a zero em 16 % das amostras**, em 30 trechos
de ~257 ms (é pulverização localizada: o bico dispara só sobre a erva). Nesses instantes o
modelo prevê vazão zero e o flowmeter ainda lê 24,5 L/min — ele e a capacitância da linha
filtram buracos dessa duração. Comparar amostra a amostra a 100 ms mede a **banda do
sensor**, não o modelo. Daí a validação multiescala:

| Janela | RMSE val. [L/min] | R² val. |
|---|---|---|
| 0,1 s | 3,72 | 0,879 |
| 0,5 s | 3,13 | 0,914 |
| 1,0 s | 3,01 | 0,920 |

Janelas com menos de 8 blocos são descartadas — com 2 ou 3 blocos o R² não significa nada.

**Hipótese testada e descartada:** achei que parte do resíduo fosse *aliasing* dos 100 ms.
Reexportei na cadência nativa (`--dt 50ms`) e o resultado é o mesmo (RMSE 3,79 vs 3,72;
R² 0,873 vs 0,879) — os buracos de 250 ms estão muito acima das duas taxas. A ressalva no
relatório foi corrigida para registrar o teste em vez da suposição.

## Saídas

```
validation/
  REPORT.md               relatório com equações, parâmetros, tabelas e ressalvas
  metrics.json            todas as métricas + parâmetros + estatística dos buracos
  pressure_check.png      H1: pressão medida vs alvo, e histograma do erro por regime
  flow_timeseries.png     H2: vazão medida vs modelos, resíduo e um zoom de 12 s
  flow_scatter.png        dispersão medido × modelo na validação
  model_compare.png       RMSE por variante + perfil do atraso τ
  multiscale.png          RMSE e R² por janela de agregação
  residual_structure.png  resíduo vs N, vs P e vs vazão (procura de padrão)
```

## Detalhes metodológicos

- **Divisão temporal, contada sobre as amostras pulverizando** (`--split-mode pulverizando`,
  default): dividir o log inteiro em 70/30 deixaria a estimação quase toda com as seções
  fechadas, onde não há informação de vazão. Nada de embaralhar amostras — é série temporal.
- `k` é ajustado por mínimos quadrados **sem intercepto** (o modelo físico passa pela origem:
  sem bico aberto, sem vazão).
- `k_n ≈ 0,029 L/min por bico·√kPa` é um **coeficiente efetivo**: absorve o coeficiente de
  descarga do bico e a perda de carga até a ponta, porque a pressão é medida num ponto da
  linha. Não é o Cd do bico.
- O log tem um único perfil de pressão (406 kPa, coerente com o perfil `410_KPa` do
  cabeçalho). O modelo **não** foi testado sob mudança de alvo — isso exige outro log.

---

# 12. Máquinas Jacto 3030/4530 (2026-10-07)

Os 4 scripts processam JD e Jacto sem flag de máquina. Validado com
`data_jacto/20260903.zip` (WQR20250023, `machineModel` 7, 104 `.txt`, 821 MB).
A JD continua **idêntica** ao baseline (CSV com o mesmo md5 e `metrics.json` igual).

```bash
python3 parse_log_manual.py --selftest                                   # JD + Jacto
python3 export_dataset.py data_jacto/20260903.zip --members '20260831-040413*' --trim
python3 plot_log.py       data_jacto/20260903.zip --members '20260903-03[234]*'
```

`machineModel` 6, 7, 18 e 22 = "Jacto 3030/4530" (`section-controller/src/canMap.cpp`).
No bucket: WQR20240009 e WQB20200001 (7), WQR20250010 (18).

| Diferença | JD | Jacto | Tratamento |
|---|---|---|---|
| zip | 1 `.txt` na raiz | pasta com 1 `.txt` por trecho do dia | `read_txts` lê todos; `--members GLOB` recorta |
| cabeçalho | `profiles` é dicionário | `"profiles": "{}"` (texto) | só mescla quando é dicionário |
| bitola | 6000 | 3900 (4380 na WQR20240009) | lida de `# Bitola:`; `--bitola` sobrescreve |
| pressão | `10FFF8E111` | `1AFFFFF9` ×6,89476 | as duas viram `can_pressure` |
| vazão na barra | `can_flow` (flowmeter) | **nenhuma medida** | `flow_measured: null` no metadata |

IDs Jacto adicionados (de `Update_Secrets.py`): `1AFFFFF9`, `1AFFFFED`, `1AFFFFFC`, `1AFFFFFF`,
`1888888ADE`, `1888888A77`, `18888888AA`. Contexto do log (arquivos, máquina, modelo, bitola)
fica em `df.attrs` e vai para o `dataset_meta.json`.

## Achados

- **`flow_lmin` (`18888888AA`) é o `predicted_flow`**, não um flowmeter: correlação 0,999 sem
  atraso, e cai para cerca de 1,4 L/min quando os bicos fecham (o flowmeter JD mantinha 24,5).
  `pump_flow`/`sent_machine_flow` são a vazão total da bomba, com o retorno incluído (correlação
  0,07 com N·√P). Por isso o `validate_plant_model.py` **recusa a H2 na Jacto**; `--flow can_flow_lmin`
  força a execução, e o REPORT avisa que o resultado é circular.
- `Flowmeter` (campo `f` dos detalhes) existe no log Jacto, mas vem zerado.
- **H1 (pressão):** `can_pressure` bate com o sensor Weedit (correlação 0,985). Em
  `20260831-040413`, pulverizando, a pressão fica +6 % acima do alvo de 460 kPa, com RMSE de 74,5 kPa e
  picos de até 1089 kPa (acima do limite de 1000 que o firmware aplica: são espúrios).
- **Troca de alvo** (490→450→410 kPa) só aparece em `20260903-0322…0349`. Nos alvos 410/450 a
  máquina estava quase sem bicos disparando e devagar; a pressão sobe para cerca de 600 kPa sem consumo.
  Alvo e carga estão confundidos, então **o teste de troca de alvo continua em aberto**.
- Unidades de `can_speed` e `pump_rpm` não estão documentadas.

Os `*_explicado.md` foram atualizados para esta versão (2026-10-07).
