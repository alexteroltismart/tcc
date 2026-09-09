"""ETAPA DE CONTROLE — PARADA (a pedido, 2026-09-08).

Este arquivo guarda o que já estava pronto da etapa de controle: linearização,
PI por IMC, margens de estabilidade, malha fechada com anti-windup e feedforward,
varredura de sensibilidade e as figuras. NÃO tem `main()` — não roda como script.

Retomar só depois da validação da planta (`validate_plant_model.py`). O que falta:
`main()` amarrando calibração -> projeto -> simulação -> REPORT.md.

Achado que motivou a parada: no log a malha de pressão está FECHADA (o controlador
de fábrica regula), então o ganho u->P não é identificável a partir desses dados —
a pressão fica plana em ~400 kPa enquanto o PWM varia de 718 a 865 (r = +0,10).
"""

import argparse, json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SURFACE, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
SEQ = matplotlib.colors.LinearSegmentedColormap.from_list(
    "seq", ["#86b6ef", "#3987e5", "#256abf", "#1c5cab", "#0d366b"])
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlecolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "grid.color": GRID, "grid.linewidth": 0.6,
    "font.size": 8, "axes.titlesize": 9, "legend.fontsize": 7, "legend.frameon": False,
    "lines.linewidth": 1.2,
})

U, Y, D, SP, Q = "can_pwm_output", "can_pressure", "nozzles_on", "can_target_pressure", "can_flow"


# ===================== A. identificabilidade =====================
def identifiability(u, y, d, q):
    """Evidência, a partir dos próprios dados, de que a malha está fechada."""
    spray = d > 1
    closed = d == 0
    corr = lambda a, b: float(np.corrcoef(a, b)[0, 1]) if len(a) > 2 else np.nan
    bins = np.quantile(u[spray], np.linspace(0, 1, 7))
    table = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = spray & (u >= lo) & (u <= hi)
        if m.sum() > 3:
            table.append({"u_lo": float(lo), "u_hi": float(hi), "n": int(m.sum()),
                          "P_mean": float(y[m].mean()), "d_mean": float(d[m].mean()),
                          "q_mean": float(q[m].mean())})
    return {
        "corr_u_P_pulverizando": corr(u[spray], y[spray]),
        "corr_u_q_pulverizando": corr(u[spray], q[spray]),
        "corr_d_q_pulverizando": corr(d[spray], q[spray]),
        "P_std_pulverizando_kPa": float(y[spray].std()),
        "faixa_u_pulverizando": [float(u[spray].min()), float(u[spray].max())],
        "faixa_P_pulverizando": [float(y[spray].min()), float(y[spray].max())],
        "n_pulverizando": int(spray.sum()), "n_fechado": int(closed.sum()),
        "P_por_faixa_de_u": table,
        "conclusao": ("pressão praticamente invariante sobre toda a faixa de PWM => a malha "
                      "de pressão está fechada e o ganho u->P não é identificável neste log; "
                      "o que é identificável é o orifício dos bicos (q, d, P) e a inclinação "
                      "dq/du a pressão constante."),
    }


# ===================== B. calibração =====================
def calibrate(u, y, d, q, k_p, C, tau_a):
    """k_n pelo regime permanente de orifício; k_b e u0 pelos dois pontos de operação.

    Regime permanente do modelo:  k_p (u - u0) = (k_n N + k_b) sqrt(P)
      fechado    (N=0):  k_p (u1 - u0) = k_b sqrt(P1)
      pulverizando:      k_p (u2 - u0) = (k_n N2 + k_b) sqrt(P2)
    Subtraindo, k_b sai em função de k_p — e k_p > k_n N2 sqrt(P2)/(u2-u1) é a
    condição para k_b > 0 (bypass fisicamente possível).
    """
    spray, closed = d > 1, d == 0
    kn_samples = q[spray] / (d[spray] * np.sqrt(y[spray]))
    k_n = float(kn_samples.mean())

    P1, u1 = float(y[closed].mean()), float(u[closed].mean())
    P2, u2, d2 = float(y[spray].mean()), float(u[spray].mean()), float(d[spray].mean())
    q_noz = k_n * d2 * np.sqrt(P2)
    k_p_min = q_noz / (u2 - u1)
    k_b = (k_p * (u2 - u1) - q_noz) / (np.sqrt(P2) - np.sqrt(P1))
    u0 = u1 - k_b * np.sqrt(P1) / k_p

    theta = np.array([C, k_p, u0, k_n, k_b, tau_a])
    info = {
        "k_n": k_n, "k_n_std": float(kn_samples.std()),
        "k_n_ci95": [float(k_n - 1.96 * kn_samples.std() / np.sqrt(spray.sum())),
                     float(k_n + 1.96 * kn_samples.std() / np.sqrt(spray.sum()))],
        "k_p_assumido": float(k_p), "k_p_minimo_fisico": float(k_p_min),
        "k_b_derivado": float(k_b), "u0_derivado": float(u0),
        "C_assumido": float(C), "tau_a_assumido": float(tau_a),
        "ponto_fechado": {"P": P1, "u": u1},
        "ponto_pulverizando": {"P": P2, "u": u2, "N": d2, "q_bicos": float(q_noz)},
        "vazao_bomba_pulverizando": float(k_p * (u2 - u0)),
        "vazao_bypass_pulverizando": float(k_b * np.sqrt(P2)),
        "coerente": bool(k_b > 0 and 0 <= u0 < u.min()),
    }
    return theta, info


def steady_state_P(theta, u_val, N):
    """P de regime permanente: k_p(u-u0) = (k_n N + k_b) sqrt(P)."""
    C, k_p, u0, k_n, k_b, tau = theta
    return (np.maximum(k_p * (u_val - u0), 0.0) / (k_n * N + k_b)) ** 2


def simulate(theta, u, N, dt, P0, qp0=None):
    C, k_p, u0, k_n, k_b, tau = theta
    n = len(u)
    P = np.empty(n); P[0] = P0
    q = (k_n * N[0] + k_b) * np.sqrt(max(P0, 0.0)) if qp0 is None else qp0
    for k in range(n - 1):
        q_out = (k_n * N[k] + k_b) * np.sqrt(max(P[k], 0.0))
        P[k + 1] = max(P[k] + dt * (q - q_out) / C, 0.0)
        q = max(q + dt * (k_p * (u[k] - u0) - q) / tau, 0.0)
    return P


# ===================== C. projeto =====================
def linearize(theta, P_bar, N_bar):
    """x = [P, q_p]; saída P. Devolve ganho DC, constante de tempo dominante e polos."""
    C, k_p, u0, k_n, k_b, tau = theta
    a11 = -(k_n * N_bar + k_b) / (2 * C * np.sqrt(max(P_bar, 1e-9)))
    A = np.array([[a11, 1.0 / C], [0.0, -1.0 / tau]])
    B = np.array([[0.0], [k_p / tau]])
    Cm = np.array([[1.0, 0.0]])
    K = float((-Cm @ np.linalg.solve(A, B)).item())
    poles = np.linalg.eigvals(A)
    return K, float(-1.0 / np.max(poles.real)), poles


def pi_imc(K, tau, lam):
    return tau / (K * lam), tau


def margins(K, tau, Kc, Ti):
    w = np.logspace(-3, 3, 6000)
    L = Kc * (1 + 1 / (Ti * 1j * w)) * K / (tau * 1j * w + 1)
    mag, ph = np.abs(L), np.unwrap(np.angle(L)) * 180 / np.pi
    out = {"wc_rad_s": np.nan, "pm_deg": np.nan, "wg_rad_s": np.nan, "gm_db": np.nan}
    i = np.where(np.diff(np.sign(mag - 1)))[0]
    if len(i):
        out["wc_rad_s"], out["pm_deg"] = float(w[i[0]]), float(180 + ph[i[0]])
    j = np.where(np.diff(np.sign(ph + 180)))[0]
    if len(j):
        out["wg_rad_s"], out["gm_db"] = float(w[j[0]]), float(-20 * np.log10(mag[j[0]]))
    return out, (w, mag, ph)


# ===================== D. malha fechada =====================
def run_controller(theta, sp, N, dt, P0, kind, Kc=0.0, Ti=np.inf, u_lim=(0, 1000), u_bias=0.0):
    """kind: 'aberta' (u fixo), 'P', 'PI', 'PI+ff' (feedforward pelo nº de bicos)."""
    C, k_p, u0, k_n, k_b, tau = theta
    n = len(sp)
    P = np.empty(n); Uc = np.empty(n)
    P[0] = P0
    q = (k_n * N[0] + k_b) * np.sqrt(max(P0, 0.0))
    I = 0.0
    for k in range(n):
        e = sp[k] - P[k]
        if kind == "aberta":
            u = u_bias
        else:
            u_ff = 0.0
            if kind == "PI+ff":
                # inverte o regime permanente: PWM que já entrega a vazão exigida
                u_ff = u0 + (k_n * N[k] + k_b) * np.sqrt(max(sp[k], 0.0)) / k_p - u_bias
            u_un = u_bias + u_ff + Kc * e + (Kc / Ti) * (I + e * dt) if kind != "P" else u_bias + Kc * e
            u = float(np.clip(u_un, *u_lim))
            if kind in ("PI", "PI+ff") and u == u_un:
                I += e * dt
        Uc[k] = u
        if k < n - 1:
            q_out = (k_n * N[k] + k_b) * np.sqrt(max(P[k], 0.0))
            P[k + 1] = max(P[k] + dt * (q - q_out) / C, 0.0)
            q = max(q + dt * (k_p * (u - u0) - q) / tau, 0.0)
    return P, Uc


def perf(sp, y, u, dt, mask=None):
    m = np.ones(len(y), bool) if mask is None else mask
    e = (sp - y)[m]
    du = np.diff(u[m]) if m.sum() > 1 else np.array([0.0])
    return {"iae_kPa_s": float(np.sum(np.abs(e)) * dt), "ise": float(np.sum(e ** 2) * dt),
            "max_abs_dev_kPa": float(np.abs(e).max()), "rms_dev_kPa": float(np.sqrt(np.mean(e ** 2))),
            "du_rms": float(np.sqrt(np.mean(du ** 2)))}


# ===================== figuras =====================
def fig_identifiability(u, y, d, q, ident, out):
    spray = d > 1
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.4))
    ax[0].scatter(u[spray], y[spray], s=5, color=S[0], linewidths=0)
    ax[0].axhline(y[spray].mean(), color=S[7], lw=1, ls="--")
    ax[0].set_title(f"Pressão vs PWM (pulverizando) — r = {ident['corr_u_P_pulverizando']:+.2f}", loc="left")
    ax[0].set_xlabel("PWM [0,1 %]"); ax[0].set_ylabel("pressão [kPa]")
    ax[1].scatter(u[spray], q[spray], s=5, color=S[2], linewidths=0)
    ax[1].set_title(f"Vazão vs PWM — r = {ident['corr_u_q_pulverizando']:+.2f}", loc="left")
    ax[1].set_xlabel("PWM [0,1 %]"); ax[1].set_ylabel("vazão [L/min]")
    ax[2].scatter(d[spray] * np.sqrt(y[spray]), q[spray], s=5, color=S[1], linewidths=0)
    kn = ident.get("k_n_plot")
    if kn:
        xx = np.linspace(0, (d[spray] * np.sqrt(y[spray])).max(), 50)
        ax[2].plot(xx, kn * xx, color=INK2, lw=1.2, label=f"k_n = {kn:.4f}")
        ax[2].legend(loc="lower right", labelcolor=INK2)
    ax[2].set_title("Orifício: vazão vs N·√P (o que É identificável)", loc="left")
    ax[2].set_xlabel("N·√P [bico·√kPa]"); ax[2].set_ylabel("vazão [L/min]")
    for a in ax:
        a.grid(True); a.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A. Identificabilidade — a malha de pressão está fechada no log",
                 x=0.006, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.93)); fig.savefig(out, dpi=130); plt.close(fig)


def fig_model_check(theta, u, y, d, q, dt, out):
    """Verificação do modelo calibrado: regime permanente e vazão dos bicos."""
    C, k_p, u0, k_n, k_b, tau = theta
    spray = d > 1
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.4))

    N_grid = np.array([0, 10, 20, 40, 60, 80, 120])
    for i, uu in enumerate([720, 760, 800, 840, 865]):
        ax[0].plot(N_grid, steady_state_P(theta, uu, N_grid), color=SEQ(i / 4), label=f"u={uu}")
    ax[0].scatter([0], [y[d == 0].mean()], color=S[7], zorder=3, s=25, label="medido (fechado)")
    ax[0].scatter([d[spray].mean()], [y[spray].mean()], color=S[1], zorder=3, s=25, label="medido (pulv.)")
    ax[0].set_title("Curva estática do modelo calibrado", loc="left")
    ax[0].set_xlabel("bicos disparando N"); ax[0].set_ylabel("pressão de regime [kPa]")
    ax[0].legend(ncol=2, labelcolor=INK2, fontsize=6)

    q_hat = k_n * d * np.sqrt(np.maximum(y, 0))
    ax[1].scatter(q[spray], q_hat[spray], s=5, color=S[0], linewidths=0)
    lim = [0, max(q[spray].max(), q_hat[spray].max()) * 1.05]
    ax[1].plot(lim, lim, color=INK2, lw=1)
    r2 = 1 - np.sum((q[spray] - q_hat[spray]) ** 2) / np.sum((q[spray] - q[spray].mean()) ** 2)
    ax[1].set_title(f"Vazão dos bicos: modelo vs flowmeter (R² = {r2:.3f})", loc="left")
    ax[1].set_xlabel("medido [L/min]"); ax[1].set_ylabel("modelo [L/min]")

    # resposta do modelo a um degrau de carga, no ponto de operação
    n = int(20 / dt)
    N_step = np.concatenate([np.full(n // 2, 20.0), np.full(n - n // 2, 60.0)])
    u_fix = np.full(n, float(u[spray].mean()))
    P_step = simulate(theta, u_fix, N_step, dt, steady_state_P(theta, u_fix[0], 20.0))
    ts = np.arange(n) * dt
    ax[2].plot(ts, P_step, color=S[0])
    ax[2].set_title("Resposta a degrau de carga 20→60 bicos (u fixo)", loc="left")
    ax[2].set_xlabel("t [s]"); ax[2].set_ylabel("pressão [kPa]")
    for a in ax:
        a.grid(True); a.spines[["top", "right"]].set_visible(False)
    fig.suptitle("B. Modelo calibrado — coerência estática e dinâmica em malha aberta",
                 x=0.006, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.93)); fig.savefig(out, dpi=130); plt.close(fig)
    return {"r2_vazao_bicos": float(r2)}


def fig_bode(w, mag, ph, marg, out):
    fig, ax = plt.subplots(2, 1, figsize=(7.5, 5), sharex=True)
    ax[0].semilogx(w, 20 * np.log10(mag), color=S[0]); ax[0].axhline(0, color=GRID)
    ax[0].set_ylabel("|L| [dB]")
    ax[0].set_title(f"C. Laço L(s) = PI × planta linearizada — MF {marg['pm_deg']:.0f}°, "
                    f"ωc {marg['wc_rad_s']:.2f} rad/s", loc="left")
    ax[1].semilogx(w, ph, color=S[0]); ax[1].axhline(-180, color=S[7], lw=1, ls="--")
    ax[1].set_ylabel("fase [°]"); ax[1].set_xlabel("ω [rad/s]")
    if np.isfinite(marg["wc_rad_s"]):
        for a in ax:
            a.axvline(marg["wc_rad_s"], color=S[3], lw=1, ls=":")
    for a in ax:
        a.grid(True); a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out, dpi=130); plt.close(fig)


def fig_closed_loop(t, sp, d, runs, y_log, u_log, out):
    fig, ax = plt.subplots(3, 1, figsize=(12, 7.4), sharex=True)
    ax[0].plot(t, sp, color=S[3], ls="--", label="setpoint (log)")
    ax[0].plot(t, y_log, color=MUTED, lw=1, label="medido (controlador de fábrica)")
    for i, (name, (P, Uc)) in enumerate(runs.items()):
        ax[0].plot(t, P, color=S[i], label=name)
    ax[0].set_ylabel("pressão [kPa]")
    ax[0].set_title("D. Malha fechada no modelo, excitada pela sequência real de bicos", loc="left", pad=14)
    ax[0].legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=5, labelcolor=INK2)
    for i, (name, (P, Uc)) in enumerate(runs.items()):
        ax[1].plot(t, Uc, color=S[i], label=name)
    ax[1].plot(t, u_log, color=MUTED, lw=1, label="PWM registrado")
    ax[1].set_ylabel("PWM [0,1 %]")
    ax[1].legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=5, labelcolor=INK2)
    ax[2].plot(t, d, color=S[2])
    ax[2].set_ylabel("bicos disparando"); ax[2].set_xlabel("t [s]")
    ax[2].set_title("perturbação de carga (do log)", loc="left")
    for a in ax:
        a.grid(True, axis="y"); a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out, dpi=130); plt.close(fig)


def fig_sweep(sweep, out):
    Cs = sorted({s["C"] for s in sweep})
    taus = sorted({s["tau_a"] for s in sweep})
    M = np.full((len(taus), len(Cs)), np.nan)
    for s in sweep:
        M[taus.index(s["tau_a"]), Cs.index(s["C"])] = s["iae_kPa_s"]
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    im = ax.imshow(M, cmap=SEQ, aspect="auto", origin="lower")
    ax.set_xticks(range(len(Cs)), [f"{c:g}" for c in Cs])
    ax.set_yticks(range(len(taus)), [f"{t:g}" for t in taus])
    ax.set_xlabel("C [L/kPa]"); ax.set_ylabel("τ_a [s]")
    ax.set_title("E. Sensibilidade — IAE do PI (mesmo ganho) aos parâmetros assumidos", loc="left")
    for i in range(len(taus)):
        for j in range(len(Cs)):
            if np.isfinite(M[i, j]):
                ax.text(j, i, f"{M[i,j]:.0f}", ha="center", va="center", fontsize=7,
                        color="#ffffff" if M[i, j] > np.nanmedian(M) else INK)
    cb = fig.colorbar(im, ax=ax, pad=0.02, label="IAE [kPa·s]")
    cb.outline.set_edgecolor(GRID); cb.ax.tick_params(colors=MUTED)
    fig.tight_layout(); fig.savefig(out, dpi=130); plt.close(fig)
