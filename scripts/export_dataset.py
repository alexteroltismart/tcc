"""Exporta um log Weedit como dataset de grade regular, para simulação / identificação
de sistemas / teoria de controle.

O parse original entrega famílias em cadências diferentes (50 ms, 100 ms, evento) e
colunas de texto (hex por bico). Aqui tudo vira UMA matriz numérica amostrada a Δt
constante, com t em segundos e metadados ao lado.

  python3 export_dataset.py [log.zip] [--dt 100ms] [--format csv,parquet,npz,mat]
                            [--fill zoh|interp|none] [--out DIR] [--model quadro|ag]
"""
import argparse, importlib.util, json, re
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DEFAULT_LOG = "/home/shared/data/Weedit/s3_bucket/WQR20230004/20260318-155931.zip"

# unidade por sinal, indexada pelo nome ORIGINAL da coluna (minúsculo), não pelo
# nome exportado: assim `pwm_wdt_system` é reconhecido venha ele como `can_pwm_wdt_system`
# ou não. O que não estiver aqui sai como "desconhecida" — melhor do que unidade errada.
UNITS = {
    "can_flow": "L/min", "can_pressure": "kPa", "can_rate": "L/ha",
    "can_accumulator": "L", "can_pump_pwm": "%", "pwm_wdt_system": "%",
    "target_liters_flow": "L/min", "current_nominal_flow": "L/min",
    "predicted_flow": "L/min", "braglia_flow": "L/min",
    "sections_open": "contagem", "current_nozzles_open": "contagem",
    "speed_center": "mm/s (bruto; x0,0036 ~ km/h)", "speed_delta": "mm/s (bruto)",
    "wdt_deltac": "adimensional (1000*delta/bitola)",
    "latitude": "grau", "longitude": "grau",
    "pressure": "0,1 kPa (bruto: /10 = kPa)", "wdtspeed": "mm/s (bruto)",
    "usage_mlha": "ml/ha", "rate": "L/ha", "area": "m2 acumulado",
    "distance_m": "m acumulado", "herbicide_ml": "ml acumulado",
    "liquid_herbsolu": "ml acumulado", "savings": "ml acumulado",
    "runtime": "h", "wdttime": "s", "sunlight": "nivel", "margin": "mm",
    "bias": "%", "sensitivity": "nivel", "wind": "nivel", "mode": "codigo",
    "vol": "0,1 V (bruto: /10 = V)",
    "nozzles_on": "contagem de bicos disparando",
    "sections_on": "contagem de bicos habilitados",
    "cdd_mean": "0-255 (media na barra)", "cdd_max": "0-255", "var_mean": "0-255",
}

# sugestão de partição entrada/saída para identificar a malha bomba -> pressão/vazão.
# Nomes ORIGINAIS de coluna; o `main` traduz para os nomes exportados.
IO_HINT_COLS = {
    "inputs": ["pwm_wdt_system", "can_pump_pwm", "target_liters_flow",
               "sections_open", "nozzles_on", "speed_center"],
    "outputs": ["can_flow", "can_pressure", "pressure", "predicted_flow"],
}

def load_parser():
    spec = importlib.util.spec_from_file_location("parse_log_manual", HERE / "parse_log_manual.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def clean_name(part, col):
    """`can`+`can_flow` -> can_flow; `speed`+`speed_center` -> speed_center; `vol`+`Vol` -> vol."""
    name = f"{part}_{col}".lower()
    name = re.sub(r"^(\w+?)_\1(_|$)", r"\1\2", name)
    return name.rstrip("_")


def popcount_series(s, hex_to_bits, model):
    """Máscara hex por bico -> contagem de bicos ativos (numérico, serve de entrada)."""
    return s.dropna().map(lambda v: sum(c == "1" for c in hex_to_bits(v, model)))


def byte_stats(s, how):
    """CDD/VAR hex -> estatística por amostra na barra (média ou máximo do byte)."""
    def f(v):
        if not isinstance(v, str) or len(v) < 2:
            return np.nan
        vals = [int(v[i:i + 2], 16) for i in range(0, len(v) - len(v) % 2, 2)]
        return float(np.mean(vals)) if how == "mean" else float(np.max(vals))
    return s.dropna().map(f)


# `h` é a máscara hex de detecção que vem junto nos detalhes: parte dos valores
# parseia como número (são só dígitos) e viraria uma coluna de NaN intercalado sem
# significado físico. A contagem de bicos já está em `nozzles_on`.
DROP_COLS = {"h"}


def numeric_columns(df):
    """Só o que é numérico de fato — texto (nome de bico, modo) fica fora da matriz."""
    out = {}
    for c in df.columns:
        if str(c).lower() in DROP_COLS:
            continue
        s = pd.to_numeric(df[c], errors="coerce")
        if s.notna().any():
            out[c] = s
    return out


def build_dataset(parts, dt, fill, hex_to_bits, model):
    """Todas as famílias numa grade regular de Δt. Devolve (DataFrame, lista de fontes)."""
    cols, sources = {}, {}

    for part in ("speed", "can", "vol", "details"):
        df = parts.get(part)
        if df is None or df.empty:
            continue
        for col, s in numeric_columns(df).items():
            name = clean_name(part, col)
            cols[name] = s
            sources[name] = (f"{part}.{col}", col.lower())

    # máscaras hex -> sinais numéricos derivados
    derived = [
        ("nozzles_on", "wdt", "WDT_HEX", lambda s: popcount_series(s, hex_to_bits, model)),
        ("sections_on", "sections", "SEC_HEX", lambda s: popcount_series(s, hex_to_bits, model)),
        ("cdd_mean", "cdd", "CDD", lambda s: byte_stats(s, "mean")),
        ("cdd_max", "cdd", "CDD", lambda s: byte_stats(s, "max")),
        ("var_mean", "var", "VAR", lambda s: byte_stats(s, "mean")),
    ]
    for name, part, col, fn in derived:
        df = parts.get(part)
        if df is None or df.empty or col not in df.columns:
            continue
        cols[name] = fn(df[col])
        sources[name] = (f"{part}.{col} (derivado)", name)

    if not cols:
        raise ValueError("nada numérico para exportar")

    t0 = min(s.index.min() for s in cols.values())
    t1 = max(s.index.max() for s in cols.values())
    grid = pd.date_range(t0.floor(dt), t1.ceil(dt), freq=dt)

    out = pd.DataFrame(index=grid)
    for name, s in cols.items():
        s = s[~s.index.duplicated(keep="first")].sort_index()
        if fill == "interp":
            # união dos índices, interpola no tempo, depois desce para a grade
            merged = s.reindex(s.index.union(grid)).interpolate(method="time", limit_area="inside")
            out[name] = merged.reindex(grid)
        else:
            # zero-order hold: o valor vale até chegar o próximo — é o que um
            # registrador amostrado realmente faz entre duas mensagens
            out[name] = s.reindex(grid, method="ffill" if fill == "zoh" else None)

    out.index.name = "timestamp"
    out.insert(0, "t", (out.index - out.index[0]).total_seconds())
    return out, sources


def write_outputs(df, meta, outdir, formats):
    written = []
    stem = outdir / "dataset"
    if "csv" in formats:
        df.to_csv(f"{stem}.csv", index=True)
        written.append(f"{stem}.csv")
    if "parquet" in formats:
        df.to_parquet(f"{stem}.parquet")          # preserva dtype e índice temporal
        written.append(f"{stem}.parquet")
    if "npz" in formats:
        sig = df.drop(columns=["t"])
        np.savez_compressed(f"{stem}.npz", t=df.t.to_numpy(float),
                            data=sig.to_numpy(float),
                            columns=np.array(sig.columns, dtype=object),
                            timestamp=df.index.astype("int64").to_numpy())
        written.append(f"{stem}.npz")
    if "mat" in formats:
        from scipy.io import savemat
        sig = df.drop(columns=["t"])
        savemat(f"{stem}.mat", {
            "t": df.t.to_numpy(float).reshape(-1, 1),
            "y": sig.to_numpy(float),
            "names": np.array(sig.columns.tolist(), dtype=object),
            "Ts": meta["dt_s"],
        }, oned_as="column")
        written.append(f"{stem}.mat")
    (outdir / "dataset_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False),
                                              encoding="utf-8")
    written.append(str(outdir / "dataset_meta.json"))
    return written


def io_hint(df, sources):
    """Traduz a sugestão de E/S para os nomes de coluna realmente exportados."""
    def match(wanted):
        return [c for c in df.columns
                if c != "t" and sources.get(c, ("", c))[1] in wanted and df[c].notna().any()]
    return {"inputs": match(set(IO_HINT_COLS["inputs"])),
            "outputs": match(set(IO_HINT_COLS["outputs"])),
            "nota": "sugestão, não verdade: confirme causalidade antes de identificar."}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log", nargs="?", default=DEFAULT_LOG)
    ap.add_argument("--out", default="dataset")
    ap.add_argument("--dt", default="100ms", help="passo da grade (default 100ms)")
    ap.add_argument("--format", default="csv,parquet",
                    help="csv,parquet,npz,mat (vírgula, default csv,parquet)")
    ap.add_argument("--fill", default="zoh", choices=["zoh", "interp", "none"],
                    help="zoh = mantém o último valor (default); interp = interpola no tempo; none = sem preenchimento, só amostras que caem exatamente na grade")
    ap.add_argument("--model", default="quadro", choices=["quadro", "ag"])
    ap.add_argument("--bitola", type=int, default=6000)
    ap.add_argument("--trim", action="store_true",
                    help="corta as bordas até a janela onde todo sinal tem valor "
                         "(suporte comum, o que identificação normalmente exige)")
    a = ap.parse_args()

    formats = [f.strip() for f in a.format.split(",") if f.strip()]
    outdir = Path(a.out); outdir.mkdir(parents=True, exist_ok=True)

    parser = load_parser()
    plot = importlib.util.spec_from_file_location("plot_log", HERE / "plot_log.py")
    plot_mod = importlib.util.module_from_spec(plot); plot.loader.exec_module(plot_mod)

    cfg, raw, parts = parser.convert(a.log, bitola_mm=a.bitola)
    df, sources = build_dataset(parts, a.dt, a.fill, plot_mod.hex_to_bits, a.model)

    cortadas = 0
    if a.trim:
        ok = df.drop(columns=["t"]).notna().all(axis=1)
        if ok.any():
            first, last = ok.idxmax(), ok[::-1].idxmax()
            cortadas = len(df) - len(df.loc[first:last])
            df = df.loc[first:last].copy()
            df["t"] = (df.index - df.index[0]).total_seconds()

    dt_s = pd.Timedelta(a.dt).total_seconds()
    meta = {
        "log": str(a.log),
        "machine": Path(a.log).parent.name,
        "t0_local": str(df.index[0]),  # hora do log, sem fuso — não é UTC
        "n_samples": int(len(df)),
        "dt_s": dt_s,
        "fs_hz": round(1.0 / dt_s, 6),
        "fill": a.fill,
        "trim": bool(a.trim),
        "rows_trimmed": int(cortadas),
        "duration_s": float(df.t.iloc[-1]),
        "nozzle_model": a.model,
        "bitola_mm": a.bitola,
        "columns": {c: {"source": sources.get(c, ("", c))[0],
                        "unit": UNITS.get(sources.get(c, ("", c))[1], "desconhecida"),
                        "n_valid": int(df[c].notna().sum()),
                        "n_unique": int(df[c].nunique(dropna=True))}
                    for c in df.columns if c != "t"},
        "io_hint": io_hint(df, sources),
        "header_config": cfg,
    }

    written = write_outputs(df, meta, outdir, formats)
    print(f"log: {a.log}  ({len(raw)} linhas cruas)")
    print(f"grade: {len(df)} amostras @ {a.dt} ({meta['fs_hz']} Hz), {meta['duration_s']:.1f} s, fill={a.fill}")
    if a.trim:
        print(f"trim: {cortadas} amostras cortadas nas bordas (suporte comum)")
    print(f"colunas: {len(df.columns) - 1} sinais")
    vazias = [c for c in df.columns if c != "t" and df[c].notna().sum() == 0]
    if vazias:
        print("sem amostra válida:", ", ".join(vazias))
    for w in written:
        print("ok", w)


if __name__ == "__main__":
    main()
