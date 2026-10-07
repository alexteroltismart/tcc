"""Converte manualmente um log Weedit (.zip) em DataFrames. Só stdlib + pandas."""
import fnmatch, json, re, struct, zipfile
from pathlib import Path
import pandas as pd

# ---------- 1. abrir o zip ----------
def read_txts(path, members=None):
    """[(nome, texto)] de cada .txt: zip de log único (JD), zip com pastas e vários .txt
    (Jacto, um dia inteiro) ou um .txt solto. `members` é um glob sobre o nome."""
    if str(path).endswith(".txt"):
        with open(path, "rb") as fh:
            yield str(path), fh.read().decode("utf-8", errors="replace")
            return
    with zipfile.ZipFile(path) as z:
        names = sorted(n for n in z.namelist() if n.endswith(".txt"))
        if members:
            names = [n for n in names if fnmatch.fnmatch(n.split("/")[-1], members)]
        if not names:
            raise ValueError(f"nenhum .txt em {path}" + (f" casando {members!r}" if members else ""))
        for n in names:                     # um por vez: o dia Jacto tem ~800 MB de texto
            yield n, z.read(n).decode("utf-8", errors="replace")

# ---------- 2. cabeçalho ----------
def extract_header(text):
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

def header_bitola(text):
    m = re.search(r"# Bitola:\s*(\d+)\s*mm", text)
    return int(m.group(1)) if m else None

# ---------- 3. tokenizar ----------
def read_log(text, log_date):
    lines = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    df = pd.Series(lines).str.split(" ", n=3, expand=True)
    df.columns = ["DTime", "Sys", "ID", "MSG"][: df.shape[1]]
    if df.shape[1] < 4:
        raise ValueError("log sem coluna MSG")
    df = df[df.DTime.str.len() == 12].reset_index(drop=True)

    dtime = pd.to_timedelta(df.DTime, errors="coerce")
    base = pd.to_datetime(log_date).floor("D")
    d = dtime.diff()
    rollover = (d < pd.Timedelta(hours=-1)) & (dtime.shift() >= pd.Timedelta(hours=20)) & (dtime <= pd.Timedelta(hours=4))
    df["Time"] = base + pd.to_timedelta(rollover.cumsum(), unit="D") + dtime
    return df.dropna(subset=["Time", "Sys"]).sort_values("Time").reset_index(drop=True)

# ---------- 4. mensagens Weedit ----------
DETAIL_NAMES = {"A":"Area","B":"Bias","D":"Distance_m","H":"Herbicide_ml","K":"Sensitivity","M":"Mode",
                "N":"Nozzle","L":"Liquid_HerbSolu","P":"Pressure","Q":"Savings","I":"WDT_Serial_ID",
                "R":"Rate","T":"RunTime","U":"Usage_mlHa","V":"WDTSpeed","X":"Status","Y":"Sunlight",
                "m":"Margin","t":"WDTTime","w":"Wind","i":"Poll_Interval","f":"Flowmeter"}
MODES = {0:"Localizada Simples",1:"Localizada PWM",2:"Cobertura",3:"Dual",4:"GoG Simples",
         5:"GoG PWM",6:"Cobertura CDD",7:"GoG Dual",91:"Taxa Variável",92:"Aplicação na Linha",
         93:"Aplicação na Entrelinha"}

def median_len_filter(s):
    return s.str.len() == s.str.len().median()

def get_sections(df):
    crit = ((df.Sys == "WDT") & df.ID.str.startswith("*SX0:3,")) | \
           ((df.Sys == "SEC") & df.ID.str.startswith("*SX0:1,"))
    d = df[crit].copy()
    d = d[median_len_filter(d.ID)]
    d["SEC_HEX"] = d.ID.str[7:]
    return d[["Time", "SEC_HEX"]].set_index("Time")

def get_wdt(df):
    d = df[(df.Sys == "WDT") & df.ID.str.startswith("*PX0:h")].copy()
    # reindex: linha *PX0:h sem vírgula devolve 1 coluna e o assign de 2 quebraria
    d[["WDT_HEX", "CK"]] = d.ID.str[6:].str.split(",", n=1, expand=True).reindex(columns=[0, 1])
    d = d[median_len_filter(d.WDT_HEX)]
    return d[["Time", "WDT_HEX"]].set_index("Time")

def get_speed(df, bitola_mm):
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

def reverse_words(hex_str):
    return "".join(reversed(re.findall("[0-9a-fA-F]{8}", hex_str))) if isinstance(hex_str, str) else hex_str

def side_data(df, sys_value, prefixes, mapping, name):
    d = df[(df.Sys == sys_value) & df.ID.str.startswith(prefixes)].copy()
    if d.empty:
        return None
    d[["SIDE", name]] = d.ID.str[5:].str.split(",", n=1, expand=True)
    d["SIDE"] = d.SIDE.replace(mapping)
    if not set(mapping.values()).issubset(set(d.SIDE)):
        return None                       # falta um lado -> nada
    d = d.dropna(subset=[name]).drop_duplicates(["Time", "SIDE"])
    d = d[d[name].str.fullmatch("[A-Fa-f0-9]+")]
    d = d[d.groupby("SIDE")[name].transform(lambda s: s.str.len() == s.str.len().median())]
    piv = d.pivot(index="Time", columns="SIDE", values=name)
    piv["LEFT"] = [reverse_words(v) for v in piv.LEFT]
    idx = piv.resample("50ms").first().index
    left = piv[["LEFT"]].dropna().reindex(idx, method="nearest", tolerance="10s")
    right = piv[["RIGHT"]].dropna().reindex(idx, method="nearest", tolerance="10s")
    out = pd.concat([left, right], axis=1).dropna()
    out[name] = out.LEFT + out.RIGHT
    return out[[name, "LEFT", "RIGHT"]]

get_cdd = lambda df: side_data(df, "WDT", ("*SX0:31", "*SX0:32"), {"31": "LEFT", "32": "RIGHT"}, "CDD")
get_var = lambda df: side_data(df, "SEC", ("*SX0:23", "*SX0:24"), {"23": "LEFT", "24": "RIGHT"}, "VAR")

def get_details(df):
    d = df[(df.Sys == "WDT") & df.ID.notna()].copy()
    # nome do bico tem espaço: o split(n=3) jogou o resto em MSG -> junta de volta
    glue = d.ID.str.startswith(("*PX0:I", "*CX0:I")) & d.MSG.notna() & (d.MSG != "")
    d.loc[glue, "ID"] = d.loc[glue, "ID"] + d.loc[glue, "MSG"]
    d = d[d.ID.str.startswith(("*PX0:", "*CX0:"))].copy()
    d["ID"] = d.ID.str[5:].str.replace(",,", ",")
    fields = pd.DataFrame([{f[0]: f[1:] for f in row.split(",")[:-1] if f} for row in d.ID],
                          index=d.index)   # "if f": campo vazio faria f[0] estourar
    out = pd.concat([d[["Time"]], fields], axis=1).sort_values("Time").ffill().bfill()
    out = out.drop_duplicates("Time").set_index("Time").resample("100ms").nearest()
    for c in out.columns:                        # float() puro: pd.to_numeric segfaulta aqui
        out[c] = out[c].map(_f)
    out = out.rename(columns=DETAIL_NAMES)
    if "Nozzle" in out:
        out["Nozzle"] = out.Nozzle.astype(str).str.lstrip(":")
    if "Mode" in out:
        out["Application_Mode"] = out.Mode.replace(MODES)
    return out

def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return v

def get_voltage(df):
    d = df[(df.Sys == "VOL") & df.ID.notna()].set_index("Time")
    d["Vol"] = (10 * pd.to_numeric(d.ID.str[:-1], errors="coerce")).round()
    return d[["Vol"]].dropna().resample("50ms").first().dropna()

# ---------- 5. mensagens CAN ----------
# {IDMSG_prefix: [struct_fmt, {index_na_tupla: nome}]}
CAN_DEFS = {
    "10FFF8E111": ["<HHHH", {1: "can_flow", 2: "can_pressure"}],
    "18FFFBE10025": ["<HHHH", {2: "can_pressure", 3: "can_rate"}],
    "18FFFFE1DE": ["<BHHHB", {1: "can_flow", 2: "can_rate", 3: "can_pressure", 4: "can_pump_pwm"}],
    "18FF028102": ["3byte", {0: "can_flow"}],
    "18FE4926": ["<HHHH", {0: "can_flow", 1: "can_accumulator"}],
    "1333333300": ["<BHHHB", {1: "target_liters_flow", 2: "current_nominal_flow", 3: "predicted_flow", 4: "braglia_flow"}],
    "1333333303": ["<BBBBhh", {1: "sections_open", 2: "current_nozzles_open", 3: "pwm_wdt_system", 4: "speed_center", 5: "speed_delta"}],
    # sub-IDs 02 e 04 da bomba: a saída do controlador atual e o setpoint de pressão.
    # Definições copiadas de docs/Notebook/Update_Secrets.py (sem ratio => valor bruto).
    "1333333302": ["<BHHHB", {1: "pwm_output", 2: "pressure_pwm", 3: "flow_pwm"}],
    "1333333304": ["<BHHBBB", {1: "nominal_pressure", 2: "target_pressure"}],
    "FEF3": ["<II", {0: "latitude", 1: "longitude"}],      # < 8 chars -> casa por PGN
    # Jacto 3030/4530 (machineModel 6/7/18/22), de Update_Secrets.py.
    # can_pressure repete o nome do JD de propósito: as duas nunca vêm no mesmo log.
    "1AFFFFF9": ["<HHHH", {0: "can_speed", 2: "can_pressure"}],
    "1AFFFFED": ["<BHHHB", {2: "pump_rpm"}],
    "1AFFFFFC": ["<HHHH", {0: "pump_flow"}],
    "1AFFFFFF": ["<HHHH", {0: "engine_rpm"}],
    "1888888ADE": ["<BBBBHH", {4: "sent_machine_flow", 5: "stm_flow"}],
    "1888888A77": ["<BBBBHH", {4: "machine_pwm", 5: "pump_pwm"}],
    "18888888AA": ["<BHBBBBB", {1: "flow_lmin", 3: "braglia_mode"}],
}
CAN_RATIOS = {  # {prefix: {nome: (offset, ratio)}}
    "10FFF8E111": {"can_flow": (0, 0.1), "can_pressure": (0, 0.1)},
    "18FFFBE10025": {"can_rate": (0, 0.1), "can_pressure": (0, 0.5)},
    "18FFFFE1DE": {"can_flow": (0, 0.01), "can_rate": (0, 0.0935396), "can_pressure": (0, 0.2), "can_pump_pwm": (0, 3.90625)},
    "18FF028102": {"can_flow": (0, 6e-05)},
    "18FE4926": {"can_flow": (0, 0.01), "can_accumulator": (0, 0.1)},
    "FEF3": {"latitude": (-210, 1e-07), "longitude": (-210, 1e-07)},
    "1AFFFFF9": {"can_pressure": (0, 6.89476), "can_speed": (0, 2.7777777777777777)},
    "1AFFFFFC": {"pump_flow": (0, 0.1)},
    "1888888ADE": {"sent_machine_flow": (0, 0.1), "stm_flow": (0, 0.1)},
    "18888888AA": {"flow_lmin": (0, 0.1)},
}

def build_idmsg(df):
    d = df[df.Sys.str.startswith("CAN")].copy()
    d["ID"] = d.ID.str[2:].str.zfill(8)
    d["IDMSG"] = d.ID + d.MSG
    return d[d.IDMSG.str.len() == 24].set_index("Time")

def unpack(idmsgs, fmt):
    if fmt == "3byte":
        return pd.DataFrame([[int.from_bytes(bytes.fromhex(x[10:16]), "little")] for x in idmsgs])
    return pd.DataFrame([struct.unpack(fmt, bytes.fromhex(x[8:])) for x in idmsgs])

def parse_can(df_can, time_interval="100ms"):
    out = []
    for prefix, (fmt, sig) in CAN_DEFS.items():
        if len(prefix) >= 8:
            sel = df_can[df_can.IDMSG.str[: len(prefix)] == prefix]
        else:
            sel = df_can[df_can.IDMSG.str[2:6] == prefix]
        if sel.empty:
            continue
        raw = unpack(sel.IDMSG, fmt)
        parsed = pd.DataFrame(index=sel.index)
        for ix, name in sig.items():
            off, ratio = CAN_RATIOS.get(prefix, {}).get(name, (0, 1))
            parsed[name] = raw[ix].to_numpy() * ratio + off
        out.append(parsed)
    if not out:
        raise ValueError("nenhuma mensagem CAN conhecida no log")
    df = pd.concat(out).sort_index().resample(time_interval).first()
    limit = max(1, int(pd.Timedelta("60s") / pd.Timedelta(time_interval)))
    return df.ffill(limit=limit).bfill(limit=limit)

def selftest():
    """Um log de cada família de máquina; falha se a decodificação regredir."""
    cfg, df, p = convert("/home/shared/data/Weedit/s3_bucket/WQR20230004/20260318-155931.zip")
    assert df.attrs["bitola_mm"] == 6000 and "can_flow" in p["can"]
    assert (len(p["cdd"].LEFT.iloc[0]) // 2, len(p["cdd"].RIGHT.iloc[0]) // 2) == (60, 60)
    jacto = Path("/home/jupyter-alex/rep/claude_working/context_files/20260908/data_jacto/20260903.zip")
    cfg, df, p = convert(jacto, members="20260831-040413*")
    assert df.attrs["machine_model"] == 7 and df.attrs["bitola_mm"] == 3900
    assert (len(p["cdd"].LEFT.iloc[0]) // 2, len(p["cdd"].RIGHT.iloc[0]) // 2) == (72, 72)
    assert 100 < p["can"].can_pressure[p["can"].current_nozzles_open > 1].median() < 700
    assert {"flow_lmin", "pump_flow", "engine_rpm"} <= set(p["can"].columns)
    print("selftest ok (JD WQR20230004 + Jacto WQR20250023)")

# ---------- 6. juntar ----------
def convert(path, log_date=None, bitola_mm=None, members=None):
    """bitola_mm=None -> cabeçalho do log (fallback 6000). Contexto em df.attrs."""
    cfg, dfs, files = None, [], []
    for name, text in read_txts(path, members):
        files.append(name)
        cfg = cfg or extract_header(text)
        bitola_mm = bitola_mm or header_bitola(text)
        # ponytail: tudo em memória; um dia Jacto inteiro (~800 MB) pede --members
        dfs.append(read_log(text, log_date or name.split("/")[-1].split(".")[0].split("-")[0]))
    df = pd.concat(dfs).sort_values("Time").reset_index(drop=True)
    bitola_mm = bitola_mm or 6000
    df_can = build_idmsg(df)
    parts = {
        "sections": get_sections(df),
        "wdt": get_wdt(df),
        "speed": get_speed(df, bitola_mm),
        "cdd": get_cdd(df),
        "var": get_var(df),
        "details": get_details(df),
        "vol": get_voltage(df),
        "can": parse_can(df_can),
    }
    mc = (cfg or {}).get("machineConfig", {})
    df.attrs.update(files=files, bitola_mm=bitola_mm,
                    machine_code=mc.get("machineCode"), machine_model=mc.get("machineModel"))
    return cfg, df, parts

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("log", nargs="?", default="/home/shared/data/Weedit/s3_bucket/WQR20230004/20260318-155931.zip")
    ap.add_argument("--members", help="glob dos .txt dentro do zip, ex.: '20260831-04*'")
    ap.add_argument("--selftest", action="store_true", help="checa um log JD e um Jacto e sai")
    a = ap.parse_args()
    if a.selftest:
        raise SystemExit(selftest())
    cfg, df, parts = convert(a.log, members=a.members)
    print("header keys:", list(cfg)[:8] if cfg else None)
    print("arquivos:", len(df.attrs["files"]), "| máquina:", df.attrs["machine_code"],
          "modelo", df.attrs["machine_model"], "| bitola:", df.attrs["bitola_mm"], "mm")
    print("linhas de dados:", len(df), "| Sys:", df.Sys.value_counts().to_dict())
    for k, v in parts.items():
        print(f"{k:9} {'None' if v is None else str(v.shape)}", end="  ")
        if v is not None and len(v):
            print("cols:", list(v.columns)[:6])
        else:
            print()
    print()
    print(parts["can"].head(3))
    print()
    print("CDD amostra:", parts["cdd"].CDD.iloc[0][:40] if parts["cdd"] is not None else None)
    print("bicos por lado:", (len(parts['cdd'].LEFT.iloc[0])//2, len(parts['cdd'].RIGHT.iloc[0])//2) if parts["cdd"] is not None else None)
