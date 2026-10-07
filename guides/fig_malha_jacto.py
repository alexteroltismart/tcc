"""Figura e números da malha de bomba Weedit na Jacto (guia controle_bomba_jacto3030.md).

Decodifica do log SD do section controller só o que a malha usa: comando do ESP (0x18888888),
resposta da placa STM (0x1888888A), debug do controlador (CANP 0x13333333) e a pressão da
máquina (0x1AFFFFF9). Uso:
    python3 fig_malha_jacto.py ZIP --members '20260831-040413*' [--out fig.png]
"""
import argparse, re, sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from parse_log_manual import read_txts

LINE = re.compile(r"^(\d\d:\d\d:\d\d\.\d+) (CANP|CANTX0|CANRX0) 0x([0-9A-F]{8}) ([0-9A-F]{16})")
SENS = re.compile(r"^(\d\d:\d\d:\d\d\.\d+)\s+SENSORS : Press:([\d.]+)")
OUTS = re.compile(r"^(\d\d:\d\d:\d\d\.\d+)\s+OUTPUTS : .*POF:(-?[\d.]+), PSL:(-?[\d.]+)")
HOLD = 5  # s: segura o último valor no máximo isso (não atravessa buraco de log)
u16 = lambda b, i: b[i] | b[i + 1] << 8


def decode(text):
    rows = []
    for ln in text.splitlines():
        m = LINE.match(ln)
        if m:
            t, kind, cid, d = m.groups()
            b = bytes.fromhex(d)
            if cid == "13333333" and b[0] == 2:
                rows.append((t, "esp_pwm_calc", u16(b, 1)))
            elif cid == "13333333" and b[0] == 4:
                rows.append((t, "p_alvo", u16(b, 3)))
            elif cid == "13333333" and b[0] == 0:
                rows.append((t, "q_nominal", u16(b, 3)))
            elif cid == "18888888" and b[0] == 0x88:
                rows.append((t, "esp_cmd", u16(b, 6)))
            elif cid == "18888888" and b[0] == 0xAA:
                rows.append((t, "braglia_cmd", b[4]))
            elif cid == "1888888A" and b[0] == 0x77:
                rows += [(t, "stm_modo", b[3]), (t, "duty_maquina", u16(b, 4)), (t, "duty_aplicado", u16(b, 6))]
            elif cid == "1AFFFFF9":
                rows.append((t, "p_maquina", u16(b, 4) * 6.89476))
            elif cid == "1AFFFFED":
                rows.append((t, "rpm_bomba", u16(b, 3)))
            continue
        m = SENS.match(ln)
        if m:
            rows.append((m.group(1), "p_weedit", float(m.group(2))))
        m = OUTS.match(ln)
        if m:
            rows += [(m.group(1), "POF", float(m.group(2))), (m.group(1), "PSL", float(m.group(3)))]
    d = pd.DataFrame(rows, columns=["t", "k", "v"])
    d["t"] = pd.to_timedelta(d.t)
    return d.pivot_table(index="t", columns="k", values="v", aggfunc="last").sort_index()


def stats(w):
    s = w.resample("1s").last()
    out = {"duração com dado (min)": round(s.notna().any(axis=1).sum() / 60, 1)}
    s = s.ffill(limit=HOLD)
    if "duty_aplicado" in s:
        v = s[s.stm_modo.notna() & s.esp_cmd.notna()]
        stm = v.stm_modo == 1
        out["STM no controle (% do tempo)"] = round(100 * stm.mean(), 1)
        diff = (v.duty_aplicado - v.esp_cmd).abs()[stm]
        out["|aplicado − comando| ≤ 10 com STM no controle (%)"] = round(100 * (diff <= 10).mean(), 1)
        out["duty da máquina p10/p50/p90"] = v.duty_maquina.quantile([.1, .5, .9]).round().tolist()
    else:
        out["resposta da STM (0x1888888A)"] = "nenhuma"
    on = s[(s.rpm_bomba > 0) & (s.get("duty_maquina", 0) > 0)] if "duty_maquina" in s else s.iloc[:0]
    if len(on) > 30:
        a, b = np.polyfit(on.duty_maquina, on.rpm_bomba, 1)
        out["rpm Jacto = a·duty_máquina + b: a, b, zero em, r"] = [round(float(a), 3), round(float(b), 1), round(float(-b / a), 1),
                                                                round(float(on[["duty_maquina", "rpm_bomba"]].corr().iloc[0, 1]), 2)]
        out["corr(rpm Jacto, duty aplicado pela STM)"] = round(on[["duty_aplicado", "rpm_bomba"]].corr().iloc[0, 1], 2)
    out["corr(PWM calculado, vazão nominal dos bicos) 1 s"] = round(s[["esp_pwm_calc", "q_nominal"]].corr().iloc[0, 1], 2)
    sp = s[(s.q_nominal > 5) & (s.p_alvo > 0)]
    if len(sp):
        e = sp.p_weedit - sp.p_alvo
        out["pulverizando: alvo, erro médio, RMSE (kPa)"] = [float(sp.p_alvo.median()), round(float(e.mean()), 1), round(float(np.sqrt((e ** 2).mean())), 1)]
        out["pulverizando: POF, PSL medianos"] = [round(sp.POF.median()), round(sp.PSL.median())]
        out["pulverizando: % do tempo com integrador saturado (|POF| ou |PSL| ≥ 99)"] = round(100 * ((sp.POF.abs() >= 99) | (sp.PSL.abs() >= 99)).mean())
        out["pulverizando: % do tempo com PWM no máximo (700)"] = round(100 * (sp.esp_pwm_calc >= 700).mean())
    out["PWM calculado min/max"] = [int(w.esp_pwm_calc.min()), int(w.esp_pwm_calc.max())]
    return out


def plot(w, title, out):
    s = w.resample("1s").last().ffill(limit=HOLD)
    x = (s.index - s.index[0]).total_seconds() / 60
    fig, ax = plt.subplots(3, 1, figsize=(10, 7), sharex=True, layout="constrained")
    ax[0].plot(x, s.p_weedit, label="pressão Weedit (entrada do PI)")
    if "p_maquina" in s:
        ax[0].plot(x, s.p_maquina, lw=.8, alpha=.7, label="pressão da máquina (CAN)")
    ax[0].plot(x, s.p_alvo, "k--", lw=1, label="alvo")
    ax[0].set_ylabel("kPa")
    ax[1].plot(x, s.esp_cmd, label="comando do ESP (0x88)")
    if "duty_aplicado" in s:
        ax[1].plot(x, s.duty_aplicado, lw=.8, label="duty aplicado pela STM (0x77)")
        ax[1].plot(x, s.duty_maquina, lw=.8, label="duty pedido pela máquina (PUMP_VIN)")
    ax[1].set_ylabel("duty (0–1000)")
    ax[2].step(x, s.q_nominal, where="post", label="vazão nominal dos bicos abertos (L/min)")
    ax[2].step(x, 20 * s.braglia_cmd, where="post", label="Braglia ×20 (1 aberta, 2 fechada)")
    if "stm_modo" in s:
        ax[2].step(x, 20 * s.stm_modo, where="post", label="modo STM ×20 (1 STM, 0 bypass)")
    ax[2].set_xlabel("min")
    for a in ax:
        a.grid(alpha=.3)
        a.legend(loc="upper left", fontsize=7, ncol=3, frameon=False)
    fig.suptitle(title, fontsize=10)
    fig.savefig(out, dpi=130)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--members", default="20260831-040413*")
    ap.add_argument("--out")
    a = ap.parse_args()
    # vários arquivos casando o glob = um trecho contínuo (concatena antes das estatísticas)
    parts = [decode(text) for _, text in read_txts(a.log, a.members)]
    w = pd.concat(parts).sort_index()
    w = w[~w.index.duplicated()]
    print(a.members, f"({len(parts)} arquivo(s))")
    for k, v in stats(w).items():
        print(f"  {k}: {v}")
    if a.out:
        plot(w, f"Malha de bomba Weedit — Jacto WQR20250023 — {a.members.rstrip('*')}", a.out)
        print("  figura:", a.out)
