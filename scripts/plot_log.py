"""Análise gráfica geral de um log Weedit ao longo do tempo.

Consome parse_log_manual.convert() e gera 4 PNGs:
  overview.png  painéis operacionais (unidade por painel, eixo X compartilhado)
  counters.png  contadores acumulados
  nozzles.png   CDD / detecção / seções por bico x tempo
  gps.png       trajeto

  python3 plot_log.py [log.zip] [--out DIR] [--step 1s] [--model quadro|ag]
"""
import argparse, importlib.util, re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates
import matplotlib.ticker
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

HERE = Path(__file__).resolve().parent
DEFAULT_LOG = "/home/shared/data/Weedit/s3_bucket/WQR20230004/20260318-155931.zip"

# ---- tokens de estilo (paleta validada; ordem fixa, nunca ciclada) ----
SURFACE, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
# piso de contraste no claro: nada mais claro que o step 250 (#86b6ef, 2,06:1)
SEQ = LinearSegmentedColormap.from_list("blue_seq", ["#86b6ef", "#3987e5", "#256abf", "#1c5cab", "#0d366b"])
BINARY = ListedColormap([SURFACE, SERIES[0]])

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlecolor": INK,
    "text.color": INK, "xtick.color": MUTED, "ytick.color": MUTED,
    "grid.color": GRID, "grid.linewidth": 0.6, "font.size": 8,
    "axes.titlesize": 9, "legend.fontsize": 7, "legend.frameon": False,
    "lines.linewidth": 1.2, "savefig.facecolor": SURFACE,
})

# ---- painéis: (título, unidade, [(parte, coluna, rótulo, fator)]) ----
PANELS = [
    ("Velocidade", "bruto (mm/s ≈ × 0,0036 = km/h)", [
        ("speed", "speed_center", "WDT *SX0:98", 1),
        ("can", "speed_center", "CAN bomba 1333333303", 1),
        ("details", "WDTSpeed", "details V", 1)]),
    ("Pressão", "kPa", [
        ("details", "Pressure", "sensor Weedit (P/10)", 0.1),
        ("can", "can_pressure", "CAN", 1)]),
    ("Vazão", "L/min", [
        ("can", "can_flow", "CAN can_flow", 1),
        ("can", "predicted_flow", "predicted_flow (bomba)", 1),
        ("can", "target_liters_flow", "target_liters_flow", 1),
        ("can", "current_nominal_flow", "current_nominal_flow", 1),
        ("can", "braglia_flow", "braglia_flow", 1),
        ("details", "Flowmeter", "flowmeter (f)", 1)]),
    ("Taxa aplicada", "L/ha", [
        ("can", "can_rate", "CAN can_rate", 1),
        ("details", "Usage_mlHa", "Usage_mlHa / 1000", 0.001),
        ("details", "Rate", "alvo (R)", 1)]),
    ("Seções e bicos abertos", "contagem", [
        ("can", "sections_open", "sections_open", 1),
        ("can", "current_nozzles_open", "current_nozzles_open", 1)]),
    ("PWM", "%", [
        ("can", "pwm_wdt_system", "pwm_wdt_system", 1),
        ("can", "can_pump_pwm", "can_pump_pwm", 1)]),
    ("Tensão de alimentação", "V", [("vol", "Vol", "VOL / 10", 0.1)]),
    ("Delta de velocidade (curva)", "bruto", [
        ("speed", "wdt_deltac", "wdt_deltac", 1),
        ("can", "speed_delta", "speed_delta (CAN)", 1)]),
    ("Luminosidade", "Sunlight (nível)", [("details", "Sunlight", "Sunlight", 1)]),
]

COUNTERS = [
    ("details", "Area", "Área acumulada", 1),
    ("details", "Distance_m", "Distância", 1),
    ("details", "Herbicide_ml", "Herbicida (ml)", 1),
    ("details", "Liquid_HerbSolu", "Solução (L)", 1),
    ("details", "Savings", "Economia", 1),
    ("details", "RunTime", "RunTime", 1),
]


def get_series(parts, part, col, factor, step):
    """Série pronta para plotar, ou None se não existe / é vazia / é constante-zero."""
    df = parts.get(part)
    if df is None or col not in df.columns:
        return None
    s = pd.to_numeric(df[col], errors="coerce").dropna()
    if s.empty or (s == 0).all():
        return None
    return (s * factor).resample(step).mean().dropna()


def draw_panels(parts, spec, step, title, out, per_panel_axis=False):
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
            if series:
                rows.append((name, unit, series))
    if not rows:
        return None

    fig, axes = plt.subplots(len(rows), 1, figsize=(13, 1.9 * len(rows)), sharex=True)
    axes = np.atleast_1d(axes)
    for ax, (name, unit, series) in zip(axes, rows):
        for i, (s, lab) in enumerate(series):
            ax.plot(s.index, s.values, color=SERIES[i % len(SERIES)], label=lab)
        panel_title = name if (len(series) > 1 or series[0][1] == name) else f"{name} — {series[0][1]}"
        ax.set_title(panel_title, loc="left", pad=14 if len(series) > 1 else 3)
        ax.set_ylabel(unit)
        ax.grid(True, axis="y")
        ax.spines[["top", "right"]].set_visible(False)
        ax.ticklabel_format(axis="y", style="plain", useOffset=False)
        if len(series) > 1:                     # legenda fora da área de dados
            ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=min(len(series), 4),
                      labelcolor=INK2, handlelength=1.4, columnspacing=1.4, borderpad=0)
    axes[-1].set_xlabel("tempo")
    fig.suptitle(title, x=0.007, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.985))
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


# ---- heatmaps por bico ----
def hex_to_bits(hex_str, model):
    """Mesma convenção de log_converter_utils: quadro = 4 bits/nibble invertidos,
    ag = 5 bits/byte invertidos."""
    if not isinstance(hex_str, str):
        return ""
    if model == "ag":
        chunks = re.findall("[0-9a-fA-F]{2}", hex_str)
        return "".join(f"{int(c, 16):05b}"[::-1] for c in chunks)
    return "".join(f"{int(c, 16):04b}"[::-1] if c in "0123456789abcdefABCDEF" else "0000"
                   for c in hex_str)


def matrix_bytes(s, max_cols=1500):
    s = s.dropna()
    if s.empty:
        return None, None
    stride = max(1, len(s) // max_cols)
    s = s.iloc[::stride]
    width = int(s.str.len().median()) // 2
    # emparelha tempo+payload antes de filtrar: a linha curta descartada não é
    # necessariamente a última, então fatiar s.index depois desalinha o eixo X
    pairs = [(ts, v) for ts, v in s.items() if len(v) >= width * 2]
    rows = [[int(v[i:i + 2], 16) for i in range(0, width * 2, 2)] for _, v in pairs]
    if not rows:
        return None, None
    return np.array(rows).T, pd.DatetimeIndex([ts for ts, _ in pairs])


def matrix_bits(s, model, max_cols=1500):
    s = s.dropna()
    if s.empty:
        return None, None
    stride = max(1, len(s) // max_cols)
    s = s.iloc[::stride]
    bits = [(ts, hex_to_bits(v, model)) for ts, v in s.items()]
    width = int(np.median([len(b) for _, b in bits]))
    pairs = [(ts, b) for ts, b in bits if len(b) >= width]      # mesmo cuidado de matrix_bytes
    rows = [[int(c) for c in b[:width]] for _, b in pairs]
    if not rows:
        return None, None
    return np.array(rows).T, pd.DatetimeIndex([ts for ts, _ in pairs])


def draw_nozzles(parts, model, out):
    layers = []
    if parts.get("cdd") is not None:
        m, idx = matrix_bytes(parts["cdd"].CDD)
        if m is not None:
            layers.append(("CDD por bico (0–255)", m, idx, SEQ, None))
    if parts.get("var") is not None:
        m, idx = matrix_bytes(parts["var"].VAR)
        if m is not None:
            layers.append(("VAR por bico (0–255)", m, idx, SEQ, None))
    for key, col, label in (("wdt", "WDT_HEX", "Detecção de erva (WDT)"),
                            ("sections", "SEC_HEX", "Seções abertas (SEC)")):
        if parts.get(key) is not None:
            m, idx = matrix_bits(parts[key][col], model)
            if m is not None:
                layers.append((label, m, idx, BINARY, (0, 1)))
    if not layers:
        return None

    fig, axes = plt.subplots(len(layers), 1, figsize=(13, 2.4 * len(layers)))
    axes = np.atleast_1d(axes)
    for ax, (name, m, idx, cmap, lim) in zip(axes, layers):
        x = matplotlib.dates.date2num(idx)
        im = ax.imshow(m, aspect="auto", origin="lower", cmap=cmap, interpolation="nearest",
                       extent=(x[0], x[-1], 0, m.shape[0]),
                       vmin=None if lim is None else lim[0], vmax=None if lim is None else lim[1])
        ax.xaxis_date()
        ax.set_title(f"{name} — {m.shape[0]} bicos", loc="left", pad=3)
        ax.set_ylabel("bico")
        cb = fig.colorbar(im, ax=ax, pad=0.01, fraction=0.02,
                          ticks=[0, 1] if lim else None)
        if lim:
            cb.ax.set_yticklabels(["fechado", "aberto"])
        cb.outline.set_edgecolor(GRID)
        cb.ax.tick_params(colors=MUTED)
    axes[-1].set_xlabel("tempo")
    fig.suptitle("Barra ao longo do tempo (esquerda invertida + direita, como no pipeline)",
                 x=0.007, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.985))
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


def draw_gps(parts, out):
    can = parts.get("can")
    if can is None or "latitude" not in can.columns:
        return None
    g = can[["latitude", "longitude"]].dropna()
    g = g[(g.latitude.abs() > 0.001) & (g.longitude.abs() > 0.001)]
    if g.empty:
        return None
    t = (g.index - g.index[0]).total_seconds() / 60
    fig, ax = plt.subplots(figsize=(7.5, 7))
    sc = ax.scatter(g.longitude, g.latitude, c=t, cmap=SEQ, s=3, linewidths=0)
    cb = fig.colorbar(sc, ax=ax, pad=0.01, fraction=0.04, label="minutos desde o início")
    cb.outline.set_edgecolor(GRID)
    cb.ax.tick_params(colors=MUTED)
    ax.set_title("Trajeto (cor = tempo)", loc="left")
    ax.set_xlabel("longitude"); ax.set_ylabel("latitude")
    ax.ticklabel_format(style="plain", useOffset=False)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%.4f"))
    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%.4f"))
    ax.grid(True); ax.spines[["top", "right"]].set_visible(False)
    ax.set_aspect("equal", adjustable="datalim")
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)
    return out


def selftest():
    """Ordem de bits do hex_to_bits — a lógica mais fácil de errar em silêncio."""
    assert hex_to_bits("F0", "quadro") == "11110000"      # F -> 1111 invertido; 0 -> 0000
    assert hex_to_bits("1", "quadro") == "1000"           # 0001 invertido
    assert hex_to_bits("8", "quadro") == "0001"
    assert hex_to_bits("01", "ag") == "10000"             # 5 bits por byte, invertidos
    # {i:05b} é largura MÍNIMA: byte >= 32 rende 8 bits, não 5. Quirk herdado de
    # weedit_ag_hex_to_bin — a largura por byte varia, e é por isso que matrix_bits
    # corta pela mediana.
    assert hex_to_bits("FF", "ag") == "11111111"
    assert hex_to_bits("ZZ", "quadro") == "00000000"      # hex inválido -> zeros, como parse_hex
    assert hex_to_bits(None, "quadro") == ""
    print("selftest ok")


def load_parser():
    spec = importlib.util.spec_from_file_location("parse_log_manual", HERE / "parse_log_manual.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log", nargs="?", default=DEFAULT_LOG)
    ap.add_argument("--out", default="plots")
    ap.add_argument("--step", default="1s", help="reamostragem dos painéis (default 1s)")
    ap.add_argument("--model", default="quadro", choices=["quadro", "ag"])
    ap.add_argument("--bitola", type=int, default=6000)
    ap.add_argument("--selftest", action="store_true", help="checa a ordem de bits e sai")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    outdir = Path(a.out); outdir.mkdir(parents=True, exist_ok=True)
    cfg, df, parts = load_parser().convert(a.log, bitola_mm=a.bitola)
    print(f"log: {a.log}\nlinhas: {len(df)}  janela: {df.Time.min()} → {df.Time.max()}")

    made = [
        draw_panels(parts, PANELS, a.step, f"Log {Path(a.log).stem} — visão operacional", outdir / "overview.png"),
        draw_panels(parts, COUNTERS, a.step, f"Log {Path(a.log).stem} — contadores acumulados",
                    outdir / "counters.png", per_panel_axis=True),
        draw_nozzles(parts, a.model, outdir / "nozzles.png"),
        draw_gps(parts, outdir / "gps.png"),
    ]
    for m in made:
        print("ok " if m else "-- ", m or "(sem dados)")

    # séries pedidas que o log não tem — some do gráfico, não do relatório
    faltando = [f"{p}.{c}" for _, _, items in PANELS for p, c, _, f in items
                if get_series(parts, p, c, f, a.step) is None]
    if faltando:
        print("séries ausentes/zeradas neste log:", ", ".join(faltando))


if __name__ == "__main__":
    main()
