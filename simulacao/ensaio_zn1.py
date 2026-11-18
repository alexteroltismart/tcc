"""Ensaio do 1º método de Ziegler-Nichols (curva de reação) no simulador.

OGATA (2010, p. 523-524, Tabela 8.1): aplica-se um degrau na entrada da planta em malha aberta,
traça-se a tangente no ponto de inflexão da resposta e lêem-se o atraso L e a constante de tempo T.
O método só se aplica se a curva tiver forma de S.

Aqui a "planta" é tudo o que fica entre o comando α_c e a pressão P: válvula (Eq. 3.12, 1ª ordem com
limite de velocidade) + parte hidráulica estática (Eq. 3.11). Com 7 bicos, partindo de α_ff(7).

Rodar:  py -3 simulacao/ensaio_zn1.py   → imprime L, T, K e ganhos; salva figuras/f_zn1_curva_reacao.png
Não altera modelo_barra.py nem resultados.json.
"""
import math

import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

from modelo_barra import BASE, DT, FIG, K, KV_MAX, TS, alpha_ff, p_regime

N = 7
T_DEG = 0.5          # instante do degrau [s] (múltiplo de TS: o degrau cai numa amostra)
T_FIM = 2.5


def degrau_aberto(dalfa, par=BASE, n=N):
    """Malha aberta: α_c salta de α_ff(n) para α_ff(n)+dalfa em T_DEG. Retorna t, P(t) e α(t)."""
    a0 = alpha_ff(n)
    alpha = a0
    passos = int(round(T_FIM / DT))
    t = np.arange(passos) * DT
    p = np.empty(passos); a = np.empty(passos)
    for k in range(passos):
        alpha_c = a0 + dalfa if t[k] >= T_DEG - 1e-12 else a0
        v = min(max((alpha_c - alpha) / par["tau_a"], -par["w_max"]), par["w_max"])
        alpha = min(max(alpha + v * DT, 0.0), 1.0)
        p[k] = p_regime(n * K + KV_MAX * alpha)
        a[k] = alpha
    return t, p, a


def tangente(t, y, t0):
    """Tangente no ponto de maior inclinação (inflexão) da curva normalizada y (0 → 1).
    Retorna L (corte com y = 0, medido a partir de t0), T (de L até o corte com y = 1) e o ponto."""
    dy = np.gradient(y, t)
    i = int(np.argmax(dy))
    m = dy[i]
    t_corte0 = t[i] - y[i] / m
    t_corte1 = t[i] + (1 - y[i]) / m
    return t_corte0 - t0, t_corte1 - t_corte0, (t[i], y[i], m)


def ensaio(dalfa):
    t, p, a = degrau_aberto(dalfa)
    p0, pf = p[t < T_DEG][-1], p[-1]
    kg = (pf - p0) / dalfa                         # ganho estático da planta (negativo)
    y = (p - p0) / (pf - p0)                       # resposta normalizada, sobe de 0 a 1
    # (a) curva contínua (passo de 1 ms)
    L, T, pt = tangente(t, y, T_DEG)
    # (b) curva vista pelo sensor amostrado: só os pontos t = k·TS, ligados por retas
    cada = int(round(TS / DT))
    ts, ys = t[::cada], y[::cada]
    Ls, Tsmp, pts = tangente(ts, ys, T_DEG)
    # inflexão de verdade: d²y/dt² muda de sinal depois do degrau?
    d2 = np.gradient(np.gradient(y, t), t)[t > T_DEG + 2 * DT]
    inflexao = bool(np.any(d2[:-1] * d2[1:] < 0) and np.max(d2) > 1e-6 * np.max(np.abs(d2)))
    return {"dalfa": dalfa, "t": t, "y": y, "alpha": a, "Kg": kg, "L": L, "T": T, "pt": pt,
            "ts": ts, "ys": ys, "L_s": Ls, "T_s": Tsmp, "pt_s": pts, "inflexao": inflexao,
            "vel_max": bool(np.max(np.abs(np.diff(a))) / DT >= 0.999 * BASE["w_max"])}


def tabela_81(L, T, kg):
    """OGATA (2010, Tabela 8.1), com o ganho da planta: K_c = (T/L)/|K_g|."""
    if L <= 1e-9:
        return {"P": (math.inf, math.inf), "PI": (math.inf, 0.0)}
    base = T / (L * abs(kg))
    return {"P": (base, math.inf), "PI": (0.9 * base, L / 0.3)}


def fig(r_peq, r_gde):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    for a, r, tit in [(ax[0], r_peq, "degrau pequeno"), (ax[1], r_gde, "degrau grande (limite de velocidade)")]:
        a.plot(r["t"] - T_DEG, r["y"], color="#2C6FBB", label="pressão (simulador, 1 ms)")
        a.plot(r["ts"] - T_DEG, r["ys"], "o", color="#E07B39", ms=3.5, label=f"leituras a cada $T_s$")
        ti, yi, m = r["pt"]
        tt = np.array([r["L"], r["L"] + r["T"]])
        a.plot(tt, [0, 1], "k--", lw=1, label="tangente na maior inclinação")
        a.axhline(1, color="k", ls=":", lw=0.8)
        a.set_xlim(-0.1, 1.5); a.set_ylim(-0.05, 1.1)
        a.set_xlabel("t − t_degrau [s]")
        a.set_title(f"{tit}: Δα_c = {r['dalfa']:.2f}".replace(".", ","), fontsize=10)
        a.grid(alpha=0.3)
        a.text(0.6, 0.35, f"L = {r['L']*1000:.1f} ms\nT = {r['T']:.3f} s".replace(".", ","), fontsize=9)
    ax[0].set_ylabel("resposta normalizada  (P − P₀)/(P_f − P₀)")
    ax[0].legend(loc="lower right", fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "f_zn1_curva_reacao.png", dpi=150)
    plt.close(fig)


def main():
    r_peq = ensaio(0.02)     # 0,02/0,2 = 0,1 s⁻¹ < ω_max: válvula linear
    r_gde = ensaio(0.20)     # 0,2/0,2 = 1,0 s⁻¹ > ω_max: começa em rampa
    for r in (r_peq, r_gde):
        print(f"\nDegrau Δα_c = {r['dalfa']:.2f}  (bateu no limite de velocidade: {r['vel_max']})")
        print(f"  K_g = {r['Kg']:.3f} kgf/cm²   curva em S (inflexão depois do degrau): {r['inflexao']}")
        print(f"  contínua : L = {r['L']*1000:7.2f} ms   T = {r['T']:.3f} s")
        print(f"  amostrada: L = {r['L_s']*1000:7.2f} ms   T = {r['T_s']:.3f} s")
        for nome, (L, T) in {"contínua": (r["L"], r["T"]), "amostrada": (r["L_s"], r["T_s"])}.items():
            g = tabela_81(L, T, r["Kg"])
            print(f"  Tabela 8.1 ({nome}): P Kc = {g['P'][0]:.3g}   PI Kc = {g['PI'][0]:.3g}, Ti = {g['PI'][1]:.3g} s")
    # referência: o atraso que costuma ser atribuído ao amostrador (não aparece na curva)
    g = tabela_81(TS / 2, BASE["tau_a"], r_peq["Kg"])
    print(f"\nSe L = Ts/2 = {TS/2*1000:.0f} ms e T = τa: P Kc = {g['P'][0]:.3f}   PI Kc = {g['PI'][0]:.3f}, Ti = {g['PI'][1]:.3f} s")
    a = math.exp(-TS / BASE["tau_a"])
    print(f"Ganho crítico do laço amostrado (1+a)/((1-a)|Kg|) = {(1 + a) / ((1 - a) * abs(r_peq['Kg'])):.3f}")
    fig(r_peq, r_gde)


if __name__ == "__main__":
    main()
