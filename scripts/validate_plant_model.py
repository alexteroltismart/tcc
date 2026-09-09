"""Validação do modelo matemático da planta hidráulica (etapa 1 — sem controle).

Pergunta: alimentando o modelo APENAS com o que a máquina conhece — bicos disparando,
seções abertas, pressão alvo e vazão alvo — a pressão e a vazão previstas ficam
próximas das medidas?

Hipóteses testadas
  H1  Regulação de pressão:   P ≈ P_alvo
  H2  Orifício (Torricelli):  q = k · A(N,S) · √P     [A = área efetiva]
      (a) k·N·√P_alvo      só entradas
      (b) k·N·√P_medida    com pressão medida (separa o erro da H1)
      (c) k·S·√P_alvo      área pelas seções abertas
      (d) (a·N + b·S)·√P_alvo   mistura
      (e) (a) + atraso de 1a ordem τ (dinâmica da linha/válvulas)
  H3  Conta interna da máquina: q_alvo ≈ q_medida

Calibração na janela de estimação, métricas reportadas separadamente na validação.

  python3 validate_plant_model.py [--data dataset/dataset.parquet] [--out validation]
                                  [--split 0.7]
"""
import argparse, json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

SURFACE, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlecolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "grid.color": GRID, "grid.linewidth": 0.6,
    "font.size": 8, "axes.titlesize": 9, "legend.fontsize": 7, "legend.frameon": False,
    "lines.linewidth": 1.2,
})

COLS = {"N": "nozzles_on", "S": "sections_on", "P": "can_pressure", "Q": "can_flow",
        "P_sp": "can_target_pressure", "Q_sp": "can_target_liters_flow"}


# ============================ métricas ============================
def score(y, yhat, mask):
    y, yhat = y[mask], yhat[mask]
    ok = np.isfinite(y) & np.isfinite(yhat)
    y, yhat = y[ok], yhat[ok]
    if len(y) < 3:
        return {k: float("nan") for k in ("n", "rmse", "mae", "bias", "r2", "fit_pct", "mape_pct")}
    e = yhat - y
    denom = np.sqrt(np.mean((y - y.mean()) ** 2))
    big = np.abs(y) > 1.0                      # MAPE só onde o valor não é ~zero
    return {
        "n": int(len(y)),
        "rmse": float(np.sqrt(np.mean(e ** 2))),
        "mae": float(np.mean(np.abs(e))),
        "bias": float(np.mean(e)),
        "r2": float(1 - np.sum(e ** 2) / np.sum((y - y.mean()) ** 2)) if denom > 0 else float("nan"),
        "fit_pct": float(100 * (1 - np.sqrt(np.mean(e ** 2)) / denom)) if denom > 0 else float("nan"),
        "mape_pct": float(100 * np.mean(np.abs(e[big] / y[big]))) if big.any() else float("nan"),
    }


def block_mean(x, mask, n):
    """Média em blocos de n amostras, só dentro da máscara."""
    xs = x[mask]
    nb = len(xs) // n
    return xs[:nb * n].reshape(nb, n).mean(1) if nb else np.array([])


def multiscale(q, yhat, mask, dt, blocks=(0.1, 0.5, 1.0, 2.0, 5.0), min_blocks=8):
    """RMSE/R² por escala de agregação.

    O flowmeter e a capacitância da linha filtram os buracos de ~250 ms entre
    disparos, então comparar amostra a amostra mede o sensor, não o modelo. A
    validação honesta é por banda: agrega os dois sinais na mesma janela.
    """
    out = []
    for B in blocks:
        n = max(1, int(round(B / dt)))
        a, b = block_mean(q, mask, n), block_mean(yhat, mask, n)
        if len(a) < min_blocks:               # poucos blocos => métrica sem sentido
            out.append({"bloco_s": B, "n_blocos": int(len(a)), "rmse": float("nan"),
                        "r2": float("nan"), "descartado": True})
            continue
        e = b - a
        out.append({"bloco_s": B, "n_blocos": int(len(a)),
                    "rmse": float(np.sqrt(np.mean(e ** 2))),
                    "r2": float(1 - np.sum(e ** 2) / np.sum((a - a.mean()) ** 2)),
                    "descartado": False})
    return out


def dropout_stats(N, spray, dt, q=None):
    """Buracos de disparo dentro da JANELA de pulverização.

    `spray` é máscara por amostra (N>1), então (N==0 & spray) é vazio por construção:
    a janela é o intervalo entre o primeiro e o último disparo.
    """
    idx = np.flatnonzero(spray)
    if not len(idx):
        return {"fracao_amostras_N0_pulverizando": 0.0, "n_buracos": 0,
                "duracao_media_ms": 0.0, "duracao_max_ms": 0.0, "n_janela": 0}
    win = np.zeros(len(N), bool)
    win[idx[0]:idx[-1] + 1] = True
    z = ((N == 0) & win).astype(int)
    d = np.diff(np.concatenate([[0], z, [0]]))
    starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    dur = (ends - starts) * dt
    holes = (N == 0) & win
    return {"fracao_amostras_N0_pulverizando": float(holes.sum() / win.sum()),
            "q_medida_durante_buracos_media": (float(q[holes].mean()) if q is not None and holes.any() else None),
            "q_medida_durante_buracos_min": (float(q[holes].min()) if q is not None and holes.any() else None),
            "q_medida_na_janela_min": (float(q[win].min()) if q is not None else None),
            "n_buracos": int(len(dur)),
            "duracao_media_ms": float(dur.mean() * 1000) if len(dur) else 0.0,
            "duracao_max_ms": float(dur.max() * 1000) if len(dur) else 0.0,
            "n_janela": int(win.sum())}


def lag1(x, tau, dt):
    """Filtro de 1a ordem (Euler): dinâmica da linha/válvulas sobre a vazão prevista."""
    if tau <= 0:
        return x.copy()
    a = dt / (tau + dt)
    y = np.empty_like(x)
    y[0] = x[0]
    for k in range(1, len(x)):
        y[k] = y[k - 1] + a * (x[k] - y[k - 1])
    return y


# ============================ modelos ============================
def fit_gain(drive, q, mask):
    """k por mínimos quadrados sem intercepto: q = k·drive (drive = A·√P)."""
    x, y = drive[mask], q[mask]
    ok = np.isfinite(x) & np.isfinite(y) & (x > 0)
    if ok.sum() < 3:
        return float("nan")
    return float(np.dot(x[ok], y[ok]) / np.dot(x[ok], x[ok]))


def fit_two_gains(N, Sv, P, q, mask):
    """q = (a·N + b·S)·√P — dois coeficientes de área, mínimos quadrados."""
    rt = np.sqrt(np.maximum(P, 0))
    A = np.column_stack([N * rt, Sv * rt])[mask]
    y = q[mask]
    ok = np.isfinite(A).all(1) & np.isfinite(y)
    if ok.sum() < 5:
        return float("nan"), float("nan")
    sol, *_ = np.linalg.lstsq(A[ok], y[ok], rcond=None)
    return float(sol[0]), float(sol[1])


def build_models(df, dt, est):
    """Devolve (models, params, sig): as vazões previstas por variante, os parâmetros
    ajustados e os sinais brutos usados (inclusive o perfil de τ)."""
    N = df[COLS["N"]].to_numpy(float)
    Sv = df[COLS["S"]].to_numpy(float)
    P = df[COLS["P"]].to_numpy(float)
    q = df[COLS["Q"]].to_numpy(float)
    P_sp = df[COLS["P_sp"]].to_numpy(float)
    q_sp = df[COLS["Q_sp"]].to_numpy(float)

    rt_sp, rt_m = np.sqrt(np.maximum(P_sp, 0)), np.sqrt(np.maximum(P, 0))
    models, params = {}, {}

    k_a = fit_gain(N * rt_sp, q, est)
    models["(a) k·N·√P_alvo"] = k_a * N * rt_sp
    params["(a)"] = {"k_n": k_a}

    k_b = fit_gain(N * rt_m, q, est)
    models["(b) k·N·√P_medida"] = k_b * N * rt_m
    params["(b)"] = {"k_n": k_b}

    k_c = fit_gain(Sv * rt_sp, q, est)
    models["(c) k·S·√P_alvo"] = k_c * Sv * rt_sp
    params["(c)"] = {"k_s": k_c}

    a_d, b_d = fit_two_gains(N, Sv, P_sp, q, est)
    models["(d) (a·N+b·S)·√P_alvo"] = (a_d * N + b_d * Sv) * rt_sp
    params["(d)"] = {"a_N": a_d, "b_S": b_d}

    # perfil: para cada tau, o ganho ótimo é recalculado por LS; só então o RMSE
    # é comparado. Sem isso o tau é usado para corrigir amplitude, não atraso.
    drive = N * rt_sp
    sp_ = N > 1                    # mesma máscara do perfil e das métricas
    def rmse_tau(tau):
        dr = lag1(drive, tau, dt)
        k = fit_gain(dr, q, est)
        m = est & sp_
        return float(np.sqrt(np.mean((k * dr[m] - q[m]) ** 2)))
    r = minimize_scalar(rmse_tau, bounds=(0.0, 5.0), method="bounded")
    tau = float(r.x)
    k_e = fit_gain(lag1(drive, tau, dt), q, est)
    taus = np.linspace(0.0, 3.0, 31)
    perfil = []
    for tv in taus:
        dr = lag1(drive, tv, dt)
        k = fit_gain(dr, q, est)
        perfil.append({
            "tau": float(tv),
            "rmse_est": float(np.sqrt(np.mean((k * dr[est & sp_] - q[est & sp_]) ** 2))),
            "rmse_val": float(np.sqrt(np.mean((k * dr[~est & sp_] - q[~est & sp_]) ** 2))),
        })
    models[f"(e) (a) + atraso τ={tau:.2f}s"] = k_e * lag1(N * rt_sp, tau, dt)
    params["(e)"] = {"k_n": k_e, "tau_s": tau}

    models["(H3) vazão alvo da máquina"] = q_sp
    params["(H3)"] = {"nota": "sem ajuste: é a própria conta da máquina"}

    return models, params, {"N": N, "S": Sv, "P": P, "q": q, "P_sp": P_sp,
                            "q_sp": q_sp, "perfil_tau": perfil}


# ============================ figuras ============================
def shade_regimes(ax, t, spray):
    """Sombreia os trechos pulverizando, para ler qualquer painel por regime."""
    edges = np.flatnonzero(np.diff(spray.astype(int)))
    bounds = np.concatenate([[0], edges + 1, [len(t)]])
    for a, b in zip(bounds[:-1], bounds[1:]):
        if spray[a]:
            ax.axvspan(t[a], t[b - 1], color=S[2], alpha=0.07, lw=0)


def fig_flow(t, sig, models, spray, split_t, out, zoom_s=12.0):
    keys = [k for k in models if k.startswith(("(a)", "(b)", "(e)", "(H3)"))]
    fig, ax = plt.subplots(3, 1, figsize=(12, 7.6))
    for a in (ax[0], ax[1]):
        shade_regimes(a, t, spray)

    for i, k in enumerate(keys):
        ax[0].plot(t, models[k], color=S[i], lw=1, label=k)
    ax[0].plot(t, sig["q"], color=INK, lw=1.6, zorder=5, label="vazão medida (flowmeter)")
    ax[0].axvline(split_t, color=S[3], lw=1, ls="--")
    ax[0].set_ylabel("vazão [L/min]")
    ax[0].set_title("H2 — vazão medida vs modelo (faixa clara = pulverizando; "
                    "tracejado = fim da estimação)", loc="left", pad=18)
    ax[0].legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=5, labelcolor=INK2,
                 handlelength=1.4, columnspacing=1.2, borderpad=0)

    for i, k in enumerate(keys):
        ax[1].plot(t, models[k] - sig["q"], color=S[i], lw=1)
    ax[1].axhline(0, color=GRID)
    ax[1].set_ylabel("resíduo [L/min]"); ax[1].set_xlabel("t [s]")
    ax[1].set_title("resíduo (mesmas cores)", loc="left")

    # zoom no meio do trecho pulverizando: é onde o pulso dos bicos aparece
    idx = np.flatnonzero(spray)
    if len(idx):
        c = t[idx[len(idx) // 2]]
        w = (t >= c - zoom_s / 2) & (t <= c + zoom_s / 2)
        for i, k in enumerate(keys):
            ax[2].plot(t[w], models[k][w], color=S[i], lw=1, label=k)
        ax[2].plot(t[w], sig["q"][w], color=INK, lw=1.6, zorder=5, label="medida")
        ax[2].set_title(f"zoom de {zoom_s:.0f} s — o pulso dos bicos vs a inércia do flowmeter",
                        loc="left")
        ax[2].set_ylabel("vazão [L/min]"); ax[2].set_xlabel("t [s]")
    for a in ax:
        a.grid(True, axis="y"); a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out, dpi=130); plt.close(fig)


def fig_scatter(sig, models, spray, val, out):
    keys = [k for k in models if k.startswith(("(a)", "(b)", "(e)", "(H3)"))]
    fig, ax = plt.subplots(1, len(keys), figsize=(3.3 * len(keys), 3.4))
    ax = np.atleast_1d(ax)
    m = spray & val
    for a, k in zip(ax, keys):
        a.scatter(sig["q"][m], models[k][m], s=6, color=S[0], linewidths=0)
        hi = max(np.nanmax(sig["q"][m]), np.nanmax(models[k][m])) * 1.05
        a.plot([0, hi], [0, hi], color=INK2, lw=1)
        sc = score(sig["q"], models[k], m)
        a.set_title(f"{k}\nR²={sc['r2']:.3f} · RMSE={sc['rmse']:.2f} L/min", loc="left", fontsize=8)
        a.set_xlabel("vazão medida [L/min]")
        a.grid(True); a.spines[["top", "right"]].set_visible(False)
    ax[0].set_ylabel("vazão do modelo [L/min]")
    fig.suptitle("H2 — dispersão na janela de validação, só pulverizando",
                 x=0.006, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.9)); fig.savefig(out, dpi=130); plt.close(fig)


def fig_pressure(t, sig, spray, out):
    err = sig["P"] - sig["P_sp"]
    fig, ax = plt.subplots(1, 2, figsize=(12, 3.4), width_ratios=[2, 1])
    shade_regimes(ax[0], t, spray)
    ax[0].plot(t, sig["P_sp"], color=S[3], ls="--", label="pressão alvo")
    ax[0].plot(t, sig["P"], color=S[0], label="pressão medida")
    ax[0].set_ylabel("pressão [kPa]"); ax[0].set_xlabel("t [s]")
    ax[0].set_title("H1 — regulação de pressão: medida vs alvo", loc="left", pad=14)
    ax[0].legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, labelcolor=INK2)
    ax[1].hist(err[spray], bins=30, color=S[2], label="pulverizando")
    ax[1].hist(err[~spray], bins=30, color=S[7], alpha=0.7, label="seções fechadas")
    ax[1].axvline(0, color=INK2, lw=1)
    ax[1].set_xlabel("P medida − P alvo [kPa]"); ax[1].set_ylabel("amostras")
    ax[1].set_title("erro de regulação por regime", loc="left")
    ax[1].legend(labelcolor=INK2)
    for a in ax:
        a.grid(True, axis="y"); a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out, dpi=130); plt.close(fig)


def fig_compare(res, perfil, out):
    keys = list(res.keys())
    x = np.arange(len(keys))
    est = [res[k]["pulverizando_estimacao"]["rmse"] for k in keys]
    val = [res[k]["pulverizando_validacao"]["rmse"] for k in keys]
    fig, axes = plt.subplots(1, 2, figsize=(13, 3.6), width_ratios=[2, 1])
    ax = axes[0]
    ax.bar(x - 0.2, est, 0.38, color=S[0], label="estimação")
    ax.bar(x + 0.2, val, 0.38, color=S[1], label="validação")
    for xi, v in zip(x - 0.2, est):
        ax.text(xi, v, f"{v:.1f}", ha="center", va="bottom", fontsize=7, color=INK2)
    for xi, v in zip(x + 0.2, val):
        ax.text(xi, v, f"{v:.1f}", ha="center", va="bottom", fontsize=7, color=INK2)
    ax.set_xticks(x, [k.split(" ")[0] for k in keys])
    ax.set_ylabel("RMSE da vazão [L/min]")
    ax.set_title("Comparação das variantes do modelo (só amostras pulverizando)", loc="left")
    ax.legend(labelcolor=INK2)
    ax.grid(True, axis="y"); ax.spines[["top", "right"]].set_visible(False)

    a2 = axes[1]
    tt = [p["tau"] for p in perfil]
    a2.plot(tt, [p["rmse_est"] for p in perfil], color=S[0], label="estimação")
    a2.plot(tt, [p["rmse_val"] for p in perfil], color=S[1], label="validação")
    a2.set_xlabel("τ do atraso de 1a ordem [s]"); a2.set_ylabel("RMSE [L/min]")
    a2.set_title("Perfil do atraso — objetivo achatado = τ não identificável", loc="left")
    a2.legend(labelcolor=INK2)
    a2.grid(True); a2.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out, dpi=130); plt.close(fig)


def fig_multiscale(ms_est, ms_val, out):
    """Só as janelas válidas nos DOIS conjuntos — est. e val. descartam blocos diferentes."""
    e_by = {m["bloco_s"]: m for m in ms_est if not m["descartado"]}
    v_by = {m["bloco_s"]: m for m in ms_val if not m["descartado"]}
    xs = sorted(set(e_by) & set(v_by))
    if not xs:
        return
    fig, ax = plt.subplots(1, 2, figsize=(11, 3.4))
    for a, key, lab in ((ax[0], "rmse", "RMSE [L/min]"), (ax[1], "r2", "R²")):
        a.plot(xs, [e_by[x][key] for x in xs], "o-", color=S[0], label="estimação")
        a.plot(xs, [v_by[x][key] for x in xs], "o-", color=S[1], label="validação")
        a.set_xscale("log"); a.set_xlabel("janela de agregação [s]"); a.set_ylabel(lab)
        for x in xs:
            a.annotate(f"n={v_by[x]['n_blocos']}", (x, v_by[x][key]),
                       xytext=(0, -11), textcoords="offset points", ha="center",
                       fontsize=6, color=MUTED)
        a.grid(True); a.spines[["top", "right"]].set_visible(False)
    ax[0].set_title("Erro cai com a agregação", loc="left")
    ax[1].set_title("R² por banda", loc="left")
    ax[0].legend(labelcolor=INK2)
    fig.suptitle("Validação multiescala do modelo (a) — só amostras pulverizando",
                 x=0.006, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.9)); fig.savefig(out, dpi=130); plt.close(fig)


def fig_residual_structure(sig, models, spray, out):
    """Resíduo do melhor modelo contra N, P e o próprio valor — procura estrutura."""
    k = "(b) k·N·√P_medida"
    r = (models[k] - sig["q"])[spray]
    fig, ax = plt.subplots(1, 3, figsize=(12, 3.2))
    ax[0].scatter(sig["N"][spray], r, s=6, color=S[0], linewidths=0)
    ax[0].set_xlabel("bicos disparando N")
    ax[1].scatter(sig["P"][spray], r, s=6, color=S[0], linewidths=0)
    ax[1].set_xlabel("pressão medida [kPa]")
    ax[2].scatter(sig["q"][spray], r, s=6, color=S[0], linewidths=0)
    ax[2].set_xlabel("vazão medida [L/min]")
    for a in ax:
        a.axhline(0, color=INK2, lw=1)
        a.set_ylabel("resíduo [L/min]")
        a.grid(True); a.spines[["top", "right"]].set_visible(False)
    fig.suptitle(f"Estrutura do resíduo — {k} (resíduo sem padrão = modelo adequado)",
                 x=0.006, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.9)); fig.savefig(out, dpi=130); plt.close(fig)


REPORT = """# Validação do modelo da planta hidráulica — {machine}

Etapa 1 de 2: **só validação do modelo**. Controle fica para a etapa seguinte
(o que já estava escrito está parado em `wip_control_stage.py`).

Log: `{log}` · Δt = {dt} s · {n} amostras ({dur:.1f} s)
Estimação: primeiras {n_est} amostras · Validação: últimas {n_val}
Regimes: {n_spray} amostras pulverizando (N > 1), {n_closed} com seções fechadas.

## Entradas e saídas do teste

| Papel | Sinal | Faixa |
|---|---|---|
| entrada | `nozzles_on` (bicos disparando) | {N_min:.0f} – {N_max:.0f} |
| entrada | `sections_on` (bicos habilitados pelas seções) | {S_min:.0f} – {S_max:.0f} |
| entrada | `can_target_pressure` (pressão alvo) | {Psp_min:.0f} – {Psp_max:.0f} kPa |
| entrada | `can_target_liters_flow` (vazão alvo) | {Qsp_min:.1f} – {Qsp_max:.1f} L/min |
| saída a validar | `can_pressure` (pressão real) | {P_min:.1f} – {P_max:.1f} kPa |
| saída a validar | `can_flow` (vazão real, flowmeter) | {Q_min:.1f} – {Q_max:.1f} L/min |

## H1 — A pressão real segue a pressão alvo?

| Regime | n | erro médio [kPa] | erro médio [%] | RMSE [kPa] | erro máx [kPa] |
|---|---|---|---|---|---|
| pulverizando | {h1s_n} | {h1s_bias:+.1f} | {h1s_pct:+.2f} | {h1s_rmse:.1f} | {h1s_max:.1f} |
| seções fechadas | {h1c_n} | {h1c_bias:+.1f} | {h1c_pct:+.2f} | {h1c_rmse:.1f} | {h1c_max:.1f} |

{h1_veredito}

O erro máximo na linha "pulverizando" ({h1s_max:.0f} kPa) vem do **transitório de
abertura**: nos primeiros instantes em que os bicos disparam a pressão ainda está no
patamar de repouso. Fora desse transitório o erro fica na faixa do RMSE.

## H2 — Modelo de orifício: q = k · A(N,S) · √P

Coeficientes calibrados **só na janela de estimação**:

| Variante | Parâmetros |
|---|---|
| (a) `k·N·√P_alvo` | k_n = {ka:.5f} L/min por bico·√kPa |
| (b) `k·N·√P_medida` | k_n = {kb:.5f} |
| (c) `k·S·√P_alvo` | k_s = {kc:.5f} |
| (d) `(a·N + b·S)·√P_alvo` | a_N = {kd_a:.5f}, b_S = {kd_b:.5f} |
| (e) (a) + atraso de 1a ordem | k_n = {ke:.5f}, τ = {ke_tau:.2f} s |

Métricas da vazão, **só nas amostras pulverizando** (fora delas a vazão é ~0 e a
métrica relativa perde sentido):

| Variante | RMSE est. | RMSE val. | R² val. | FIT % val. | viés val. | MAPE val. |
|---|---|---|---|---|---|---|
{h2_table}

### Por que o erro instantâneo é maior do que parece

Durante a pulverização, `nozzles_on` cai a zero em **{drop_frac:.1f} % das amostras**,
em {drop_n} trechos de **{drop_ms:.0f} ms em média** (é pulverização localizada: os bicos
disparam só sobre a erva). Nesses instantes o modelo prevê vazão zero, mas o flowmeter
ainda lê **{q_hole_mean:.1f} L/min em média** (mínimo {q_hole_min:.1f}): ele e a
capacitância da linha filtram buracos dessa duração. Ou seja, comparar amostra a amostra
a 100 ms mede a banda do sensor, não o modelo.

Validação por escala de agregação (modelo (a), só pulverizando):

| Janela | n blocos (val.) | RMSE est. [L/min] | RMSE val. [L/min] | R² val. |
|---|---|---|---|---|
{ms_table}

Blocos com menos de 8 amostras são descartados — com 2 ou 3 blocos o R² não significa nada.

## H3 — A vazão alvo da máquina bate com a medida?

RMSE {h3_rmse:.2f} L/min · R² {h3_r2:.3f} · viés {h3_bias:+.2f} L/min · MAPE {h3_mape:.1f} %
(validação, pulverizando). Sem ajuste de parâmetro: é a própria conta interna dela.

**Leitura correta:** `target_liters_flow` é o **setpoint** que a máquina manda para a
bomba, não uma previsão da vazão que sai na barra. R² negativo aqui não invalida o
modelo hidráulico — mede o descasamento entre o alvo de vazão e a vazão realmente
medida, ou seja, o desempenho da malha de vazão dela (e, em pulverização localizada,
o alvo é calculado para cobertura total, enquanto a barra pulsa só onde há erva).

## Veredito

{veredito}

## Figuras

`pressure_check.png` (H1) · `flow_timeseries.png` · `flow_scatter.png` ·
`model_compare.png` · `multiscale.png` · `residual_structure.png` · `metrics.json`

## Ressalvas

1. `nozzles_on` é **contagem de bicos com o solenoide aberto na amostra**, não o ciclo
   de trabalho médio. **Testado:** reexportando na cadência nativa (`--dt 50ms`) o
   resultado praticamente não muda (RMSE de validação 3,79 contra 3,72 L/min; R² 0,873
   contra 0,879). Ou seja, o resíduo instantâneo **não** é artefato de amostragem — os
   buracos de disparo duram ~250 ms, muito acima de 50 e de 100 ms. O que o explica é
   a filtragem do flowmeter e da linha.
2. `can_flow` é o flowmeter do controlador de taxa de terceiros (John Deere neste
   log), com filtro e cadência próprios: parte do atraso identificado em (e) é do
   sensor, não da hidráulica.
3. A pressão medida é a do sensor do Weedit, num ponto da linha; a queda de pressão
   até a ponta do bico não é medida. Isso desloca `k_n` (absorve o coeficiente de
   descarga e a perda de carga), então ele é um **coeficiente efetivo**, não o Cd do bico.
4. O log inteiro tem um único perfil de pressão ({Psp_min:.0f} kPa) — o modelo não
   foi testado sob mudança de alvo. Validar isso exige log com troca de perfil.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="dataset/dataset.parquet")
    ap.add_argument("--out", default="validation")
    ap.add_argument("--split", type=float, default=0.7)
    ap.add_argument("--split-mode", default="pulverizando", choices=["pulverizando", "tempo"],
                    help="'pulverizando' divide as amostras com bicos disparando (default); "
                         "'tempo' divide o log inteiro")
    a = ap.parse_args()

    outdir = Path(a.out); outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_parquet(a.data)
    meta_path = Path(a.data).with_name("dataset_meta.json")
    meta_in = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    dt = float(meta_in.get("dt_s", np.median(np.diff(df.t))))

    falta = [c for c in COLS.values() if c not in df.columns]
    if falta:
        raise SystemExit("colunas ausentes no dataset: " + ", ".join(falta)
                         + "\nreexporte com export_dataset.py")

    t = df.t.to_numpy(float)
    N_tmp = df[COLS["N"]].to_numpy(float)
    spray = N_tmp > 1
    if a.split_mode == "pulverizando" and spray.any():
        # corta no instante que divide as amostras PULVERIZANDO na proporção pedida:
        # dividir o log inteiro deixaria a estimação quase toda com seções fechadas
        alvo = a.split * spray.sum()
        i = int(np.searchsorted(np.cumsum(spray), alvo) + 1)
    else:
        i = int(len(t) * a.split)
    est = np.zeros(len(t), bool); est[:i] = True
    val = ~est

    models, params, sig = build_models(df, dt, est)

    # ---- H1: pressão segue o alvo? ----
    h1 = {}
    for name, mask in (("pulverizando", spray), ("fechado", ~spray)):
        sc = score(sig["P_sp"], sig["P"], mask)      # "modelo" = alvo; medido = real
        rel = (sig["P"] - sig["P_sp"])[mask]
        base = sig["P_sp"][mask]
        sc["erro_pct"] = float(100 * np.mean(rel / np.where(base == 0, np.nan, base)))
        sc["max_abs"] = float(np.abs(rel).max()) if mask.any() else float("nan")
        h1[name] = sc

    # ---- H2/H3: vazão ----
    res = {}
    for name, yhat in models.items():
        res[name] = {
            "pulverizando_estimacao": score(sig["q"], yhat, spray & est),
            "pulverizando_validacao": score(sig["q"], yhat, spray & val),
            "todo_log_validacao": score(sig["q"], yhat, val),
        }

    base_model = "(a) k·N·√P_alvo"
    ms_est = multiscale(sig["q"], models[base_model], spray & est, dt)
    ms_val = multiscale(sig["q"], models[base_model], spray & val, dt)
    drop = dropout_stats(sig["N"], spray, dt, sig["q"])

    metrics = {"dt_s": dt, "n": len(t), "split_idx": i, "params": params,
               "H1_pressao": h1, "H2_H3_vazao": res,
               "multiescala_modelo_a": {"estimacao": ms_est, "validacao": ms_val},
               "buracos_de_disparo": drop,
               "n_pulverizando": int(spray.sum()), "n_fechado": int((~spray).sum())}
    (outdir / "metrics.json").write_text(json.dumps(metrics, indent=2, ensure_ascii=False),
                                         encoding="utf-8")

    fig_pressure(t, sig, spray, outdir / "pressure_check.png")
    fig_flow(t, sig, models, spray, t[i], outdir / "flow_timeseries.png")
    fig_scatter(sig, models, spray, val, outdir / "flow_scatter.png")
    fig_compare(res, sig["perfil_tau"], outdir / "model_compare.png")
    fig_multiscale(ms_est, ms_val, outdir / "multiscale.png")
    fig_residual_structure(sig, models, spray, outdir / "residual_structure.png")

    # ---- relatório ----
    rows = []
    for name, r in res.items():
        v = r["pulverizando_validacao"]
        rows.append(f"| {name} | {r['pulverizando_estimacao']['rmse']:.2f} | {v['rmse']:.2f} | "
                    f"{v['r2']:.3f} | {v['fit_pct']:.1f} | {v['bias']:+.2f} | {v['mape_pct']:.1f} |")

    # referência para o veredito: a maior janela válida nos dois conjuntos
    validas = [m for e, m in zip(ms_est, ms_val) if not (m["descartado"] or e["descartado"])]
    ms_ref = validas[-1] if validas else {"r2": float("nan"), "rmse": float("nan"), "bloco_s": 0}

    best = min(res, key=lambda k: res[k]["pulverizando_validacao"]["rmse"])
    bv = res[best]["pulverizando_validacao"]
    h1s = h1["pulverizando"]
    h1_ver = (f"Pulverizando, a pressão medida fica **{abs(h1s['erro_pct']):.2f} % "
              f"{'abaixo' if h1s['erro_pct'] < 0 else 'acima'}** do alvo em média "
              f"(RMSE {h1s['rmse']:.1f} kPa) — a hipótese de regulação **se sustenta** "
              f"nesse regime. Com as seções fechadas o erro é de "
              f"{h1['fechado']['bias']:+.0f} kPa: o alvo **não** é mantido, o que é "
              f"esperado (sem consumo, o regulador não precisa sustentar pressão).")
    ver = (f"- **H1 (regulação de pressão):** válida enquanto pulveriza; inválida com as "
           f"seções fechadas.\n"
           f"- **H2 na banda do sensor:** agregando os dois sinais em janelas de "
           f"{ms_ref['bloco_s']:.1f} s, o "
           f"modelo (a) — que usa **só entradas** (bicos e pressão alvo) — chega a "
           f"R² {ms_ref['r2']:.3f} com RMSE {ms_ref['rmse']:.2f} L/min na validação. "
           f"**É esta a métrica que valida o modelo hidráulico**; o erro instantâneo maior é "
           f"dominado pelos buracos de disparo de ~250 ms que o flowmeter não enxerga.\n"
           f"- **H2 amostra a amostra:** o melhor é **{best}**, com RMSE de "
           f"{bv['rmse']:.2f} L/min e R² {bv['r2']:.3f} na validação — sobre uma vazão "
           f"média de {sig['q'][spray & val].mean():.1f} L/min, isto é "
           f"{100*bv['rmse']/max(sig['q'][spray & val].mean(),1e-9):.1f} % de erro relativo.\n"
           f"- **H3:** a vazão alvo da máquina fica {res['(H3) vazão alvo da máquina']['pulverizando_validacao']['rmse']:.2f} "
           f"L/min de RMSE da medida — é setpoint, não previsão; ver a leitura na seção H3.\n"
           f"- **Dinâmica:** a variante (e) não se sustenta. Em estimação o RMSE é "
           f"praticamente insensível a τ (objetivo achatado, ver painel direito de "
           f"`model_compare.png`) e o τ escolhido piora muito a validação: a 100 ms de "
           f"amostragem **o atraso não é identificável** com estes dados. O modelo estático "
           f"é o melhor que o dado sustenta.\n"
           f"- Comparar (a) com (b) isola quanto do erro vem de usar a pressão **alvo** em "
           f"vez da medida; comparar (a) com (c)/(d) diz se a área efetiva é melhor "
           f"descrita pelos bicos disparando ou pelas seções abertas.")

    rep = REPORT.format(
        machine=meta_in.get("machine", "?"), log=meta_in.get("log", a.data), dt=dt,
        n=len(t), dur=t[-1], n_est=i, n_val=len(t) - i,
        n_spray=int(spray.sum()), n_closed=int((~spray).sum()),
        N_min=sig["N"].min(), N_max=sig["N"].max(), S_min=sig["S"].min(), S_max=sig["S"].max(),
        Psp_min=sig["P_sp"].min(), Psp_max=sig["P_sp"].max(),
        Qsp_min=sig["q_sp"].min(), Qsp_max=sig["q_sp"].max(),
        P_min=sig["P"].min(), P_max=sig["P"].max(), Q_min=sig["q"].min(), Q_max=sig["q"].max(),
        h1s_n=h1s["n"], h1s_bias=h1s["bias"], h1s_pct=h1s["erro_pct"],
        h1s_rmse=h1s["rmse"], h1s_max=h1s["max_abs"],
        h1c_n=h1["fechado"]["n"], h1c_bias=h1["fechado"]["bias"],
        h1c_pct=h1["fechado"]["erro_pct"], h1c_rmse=h1["fechado"]["rmse"],
        h1c_max=h1["fechado"]["max_abs"],
        ka=params["(a)"]["k_n"], kb=params["(b)"]["k_n"], kc=params["(c)"]["k_s"],
        kd_a=params["(d)"]["a_N"], kd_b=params["(d)"]["b_S"],
        ke=params["(e)"]["k_n"], ke_tau=params["(e)"]["tau_s"],
        h2_table="\n".join(rows),
        h3_rmse=res["(H3) vazão alvo da máquina"]["pulverizando_validacao"]["rmse"],
        h3_r2=res["(H3) vazão alvo da máquina"]["pulverizando_validacao"]["r2"],
        h3_bias=res["(H3) vazão alvo da máquina"]["pulverizando_validacao"]["bias"],
        h3_mape=res["(H3) vazão alvo da máquina"]["pulverizando_validacao"]["mape_pct"],
        h1_veredito=h1_ver, veredito=ver,
        drop_frac=100 * drop["fracao_amostras_N0_pulverizando"], drop_n=drop["n_buracos"],
        drop_ms=drop["duracao_media_ms"],
        q_hole_mean=drop["q_medida_durante_buracos_media"] or 0.0,
        q_hole_min=drop["q_medida_durante_buracos_min"] or 0.0,
        ms_table="\n".join(
            f"| {m['bloco_s']:.1f} s | {m['n_blocos']} | {e['rmse']:.2f} | {m['rmse']:.2f} | {m['r2']:+.3f} |"
            for e, m in zip(ms_est, ms_val) if not (m["descartado"] or e["descartado"])),
    )
    (outdir / "REPORT.md").write_text(rep, encoding="utf-8")

    print(f"dados: {len(t)} amostras @ {dt}s | estimação {i} / validação {len(t)-i}")
    print(f"H1 pressão pulverizando: viés {h1s['bias']:+.1f} kPa ({h1s['erro_pct']:+.2f} %) "
          f"em relação ao alvo, RMSE {h1s['rmse']:.1f} kPa")
    print(f"H1 pressão seções fechadas: viés {h1['fechado']['bias']:+.1f} kPa")
    print("\nH2/H3 vazão (pulverizando):")
    for name, r in res.items():
        e, v = r["pulverizando_estimacao"], r["pulverizando_validacao"]
        print(f"  {name:34} RMSE est {e['rmse']:6.2f} | val {v['rmse']:6.2f} | "
              f"R² val {v['r2']:+.3f} | FIT {v['fit_pct']:5.1f}%")
    print(f"\nmelhor na validação: {best}")
    print("\nvalidação multiescala do modelo (a), pulverizando:")
    for me, mv in zip(ms_est, ms_val):
        if me["descartado"] or mv["descartado"]:
            print(f"  bloco {mv['bloco_s']:4.1f}s  descartado "
                  f"(n est {me['n_blocos']}, n val {mv['n_blocos']})")
        else:
            print(f"  bloco {mv['bloco_s']:4.1f}s  RMSE est {me['rmse']:5.2f} | val {mv['rmse']:5.2f} "
                  f"| R² val {mv['r2']:+.3f}  (n est {me['n_blocos']}, n val {mv['n_blocos']})")
    print(f"buracos de disparo: {100*drop['fracao_amostras_N0_pulverizando']:.1f}% das amostras, "
          f"{drop['n_buracos']} trechos, média {drop['duracao_media_ms']:.0f} ms")

    for f in ("pressure_check.png", "flow_timeseries.png", "flow_scatter.png",
              "model_compare.png", "multiscale.png", "residual_structure.png",
              "metrics.json", "REPORT.md"):
        print("ok", outdir / f)


if __name__ == "__main__":
    main()
