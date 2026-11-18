"""Modelo e simulação do controle de pressão de uma barra de pulverização bico a bico.

Implementa as equações do Capítulo 3 do TCC (contexto/07.md):
  1. identificação estática a partir da Tabela 1 de Rosa, Terra e Drews Jr (2019),
     com validação cruzada "deixa um de fora";
  2. modelo dinâmico (nó de pressão com capacitância + atuador da válvula com saturação);
  3. PI discreto com feedforward em n e anti-windup;
  4. cenários C1-C3 e C5 (erro de modelo), métricas e figuras.

Unidades: P em kgf/cm², Q em L/min, t em s.
Rodar:  py -3 simulacao/modelo_barra.py
Saída:  simulacao/resultados.json e simulacao/figuras/*.png
"""

import json
import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = Path(__file__).resolve().parent
FIG = AQUI / "figuras"

# ---------------------------------------------------------------------------
# 1. Dados (Rosa; Terra; Drews Jr, 2019, Tabela 1) e identificação estática
# ---------------------------------------------------------------------------
TABELA1 = [  # n bicos abertos, P [kgf/cm²], Q [L/min]  (válvula de recirculação fechada)
    (7, 3.57, 5.60), (6, 3.88, 5.07), (5, 4.24, 4.40), (4, 4.64, 3.60),
    (3, 4.96, 2.80), (2, 5.27, 2.00), (1, 5.58, 1.00),
]
N_T = np.array([r[0] for r in TABELA1])
P_T = np.array([r[1] for r in TABELA1])
Q_T = np.array([r[2] for r in TABELA1])

K = float(np.mean(Q_T / (N_T * np.sqrt(P_T))))         # constante do bico, eq. (3.2)
FONTE = tuple(np.polyfit(Q_T, P_T, 2))                 # curva da fonte (a2, a1, a0), eq. (3.5)
A2, A1, A0 = FONTE


def eq27(n):
    """Expressão empírica de Rosa et al. (2019), eq. (2.7) do texto."""
    return 42.59 * math.exp(-2.335 * n) + 2.307 * math.exp(-0.4591 * n)


def q_fonte(p, fonte=FONTE):
    """Vazão da fonte para a pressão p: raiz positiva de a2 Q² + a1 Q + (a0 - p) = 0."""
    a2, a1, a0 = fonte
    if p >= a0:
        return 0.0
    return (-a1 - math.sqrt(a1 * a1 - 4 * a2 * (a0 - p))) / (2 * a2)


def dq_fonte(p):
    """dQs/dP, usado na linearização."""
    return 1.0 / (2 * A2 * q_fonte(p) + A1)


def p_regime(k_total, fonte=FONTE):
    """Pressão de regime: Qs(P) = k_total·√P, resolvida por bissecção em [0, a0]."""
    lo, hi = 0.0, fonte[2]
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if q_fonte(mid, fonte) - k_total * math.sqrt(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def identificacao():
    r1 = P_T[-1] / Q_T[-1] ** 2
    r_med = P_T / Q_T ** 2
    tab_r = []
    for n, rm in zip(N_T, r_med):
        tab_r.append({"n": int(n), "medida": rm, "R1_n2": r1 / n ** 2, "eq27": eq27(n)})
    tab_op = []
    for n, p, q in TABELA1:
        pp = p_regime(n * K)
        tab_op.append({"n": n, "P_prev": pp, "P_med": p, "Q_prev": n * K * math.sqrt(pp), "Q_med": q})
    res = lambda f: math.sqrt(np.mean([(f(t["n"]) - t["medida"]) ** 2 for t in tab_r]))
    pfit = np.polyval(FONTE, Q_T)
    lin = np.polyval(np.polyfit(Q_T, P_T, 1), Q_T)
    sst = float(((P_T - P_T.mean()) ** 2).sum())
    out = {
        "K": K, "K_min": float(np.min(Q_T / (N_T * np.sqrt(P_T)))),
        "K_max": float(np.max(Q_T / (N_T * np.sqrt(P_T)))),
        "fonte": {"a2": A2, "a1": A1, "a0": A0,
                  "rmse": float(np.sqrt(np.mean((P_T - pfit) ** 2))),
                  "r2": 1 - float(((P_T - pfit) ** 2).sum()) / sst,
                  "rmse_linear": float(np.sqrt(np.mean((P_T - lin) ** 2))),
                  "q_fonte_p0": q_fonte(0.0)},
        "rmse_R1_n2": res(lambda n: r1 / n ** 2), "rmse_eq27": res(eq27),
        "tabela_resistencia": tab_r, "tabela_operacao": tab_op,
        "erro_max_P_pct": max(abs(t["P_prev"] - t["P_med"]) / t["P_med"] * 100 for t in tab_op),
        "erro_max_Q_pct": max(abs(t["Q_prev"] - t["Q_med"]) / t["Q_med"] * 100 for t in tab_op),
    }
    # regressão: números publicados no texto (o 05.md trazia 0,6%/2,5%, calculados com P arredondado)
    assert abs(out["K"] - 0.425) < 1e-3, out["K"]
    assert out["erro_max_P_pct"] < 0.75 and out["erro_max_Q_pct"] < 2.3, out
    return out


def validacao_cruzada():
    """Deixa um de fora: ajusta K e a fonte com 6 pontos e prevê o 7º."""
    linhas = []
    for i, (n, p, q) in enumerate(TABELA1):
        m = np.arange(len(TABELA1)) != i
        k_i = float(np.mean(Q_T[m] / (N_T[m] * np.sqrt(P_T[m]))))
        fonte_i = tuple(np.polyfit(Q_T[m], P_T[m], 2))
        pp = p_regime(n * k_i, fonte_i)
        qq = n * k_i * math.sqrt(pp)
        linhas.append({"n": n, "K": k_i, "P_prev": pp, "P_med": p, "Q_prev": qq, "Q_med": q,
                       "erro_P_pct": (pp - p) / p * 100, "erro_Q_pct": (qq - q) / q * 100})
    return {"linhas": linhas,
            "erro_max_P_pct": max(abs(l["erro_P_pct"]) for l in linhas),
            "erro_max_Q_pct": max(abs(l["erro_Q_pct"]) for l in linhas)}


# ---------------------------------------------------------------------------
# 2. Parâmetros de projeto e hipóteses dinâmicas (H5, H6)
# ---------------------------------------------------------------------------
P_REF = 3.5          # kgf/cm², abaixo da P máxima com 7 bicos e válvula fechada
KV_MAX = 3.5         # (L/min)/√(kgf/cm²), válvula toda aberta; K_v(α) = KV_MAX·α (linear)
BASE = {"C_h_mL": 0.5, "tau_a": 0.2, "w_max": 0.5}   # mL/(kgf/cm²), s, 1/s
TS = 0.05            # período do controlador [s]
DT = 1e-3            # passo de integração [s]
FAIXA = (0.95 ** 2, 1.05 ** 2)   # ±5% na vazão do bico → faixa de pressão
LAMBDAS = [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0]   # candidatos para a sintonia [s]
MF_MIN = 60.0        # margem de fase mínima aceita [°]
PLANTA = {"K": K, "fonte": FONTE, "valvula": "linear"}     # planta nominal (igual ao modelo)


def estimativa_ch():
    """C_h = V/β: volume da mangueira da barra dividido pelo módulo volumétrico efetivo."""
    kgf_mpa = 0.0980665                      # 1 kgf/cm² em MPa
    v_ml = {d: math.pi * (d / 1000) ** 2 / 4 * 5.0 * 1e6 for d in (10, 13)}   # 5 m de mangueira
    c = {f"d{d}_b{b}": v * kgf_mpa / b for d, v in v_ml.items() for b in (100, 1000)}
    return {"V_mL": v_ml, "C_mL": c, "C_min": min(c.values()), "C_max": max(c.values())}


def alpha_ff(n, p_ref=P_REF):
    """Feedforward: abertura que mantém P = P_ref em regime com n bicos (modelo nominal)."""
    kv = q_fonte(p_ref) / math.sqrt(p_ref) - n * K
    return min(max(kv / KV_MAX, 0.0), 1.0)


def linearizar(n, c_h_ml):
    """Ganho α→P e constante de tempo da pressão em torno de (P_REF, α_ff(n))."""
    c = c_h_ml / 1000.0
    a = alpha_ff(n)
    k_tot = n * K + KV_MAX * a
    dfdp = (dq_fonte(P_REF) - k_tot / (2 * math.sqrt(P_REF))) / (60 * c)
    dfda = -KV_MAX * math.sqrt(P_REF) / (60 * c)
    tau_p = -1.0 / dfdp
    return {"n": n, "alpha_ff": a, "Kg": dfda * tau_p, "tau_p": tau_p}


def sintonia(par, lam):
    """PI pela regra SIMC: a constante de tempo mais lenta (válvula ou linha) é a dominante,
    a mais rápida e meio período de amostragem entram como atraso."""
    lin = linearizar(4, par["C_h_mL"])
    tau1 = max(lin["tau_p"], par["tau_a"])
    theta = min(lin["tau_p"], par["tau_a"]) + TS / 2
    kc = tau1 / (abs(lin["Kg"]) * (lam + theta))
    ti = min(tau1, 4 * (lam + theta))
    return kc, ti, tau1, theta


def margens(n, par, kc, ti):
    """Margens de fase e de ganho de L(s) = PI·atuador·planta·e^(-s·Ts/2), por varredura."""
    lin = linearizar(n, par["C_h_mL"])
    w = np.logspace(-2, 3, 50000)
    mag = (kc * np.sqrt(1 + 1 / (ti * w) ** 2) / np.sqrt(1 + (par["tau_a"] * w) ** 2)
           * abs(lin["Kg"]) / np.sqrt(1 + (lin["tau_p"] * w) ** 2))
    fase = (-np.arctan(1 / (ti * w)) - np.arctan(par["tau_a"] * w)
            - np.arctan(lin["tau_p"] * w) - w * TS / 2)
    ic = np.argmin(np.abs(mag - 1))
    ip = np.argmin(np.abs(fase + math.pi))
    return {**lin, "MF_graus": math.degrees(fase[ic] + math.pi), "wc": float(w[ic]),
            "MG_dB": float(-20 * math.log10(mag[ip]))}


def escolhe_lambda(par):
    """Menor λ da lista que deixa margem de fase ≥ MF_MIN (resposta rápida, mas segura)."""
    tabela = []
    for lam in LAMBDAS:
        kc, ti, _, _ = sintonia(par, lam)
        tabela.append({"lambda": lam, "Kc": kc, "Ti": ti, **margens(4, par, kc, ti)})
    escolhido = next(t for t in tabela if t["MF_graus"] >= MF_MIN)
    return escolhido["lambda"], tabela


# ---------------------------------------------------------------------------
# 3. Simulação
# ---------------------------------------------------------------------------
def n_degraus(seq, dur):
    """Converte lista de n em degraus de duração 'dur' → lista de (t_inicio, n)."""
    return [(i * dur, n) for i, n in enumerate(seq)]


def simular(eventos, t_fim, modo, par, kc, ti, planta=PLANTA, dt=DT):
    """modo: 'aberta' (α fixo para n=7), 'PI' (bias fixo) ou 'PI+FF'.
    'planta' pode diferir do modelo usado pelo controlador (cenário C5)."""
    c = par["C_h_mL"] / 1000.0
    k_b, fonte = planta["K"], planta["fonte"]
    expoente = 2 if planta["valvula"] == "quadratica" else 1
    n = eventos[0][1]
    alpha = alpha_ff(7) if modo == "aberta" else alpha_ff(n)
    bias = alpha
    p, integ, alpha_c = P_REF, 0.0, alpha
    passos = int(round(t_fim / dt))
    cada = int(round(TS / dt))
    ev = list(eventos)
    t_out, p_out, a_out, n_out = (np.empty(passos) for _ in range(4))
    for k in range(passos):
        t = k * dt
        while ev and ev[0][0] <= t + 1e-12:              # comutação dos bicos
            n = ev.pop(0)[1]
        if k % cada == 0 and modo != "aberta":          # controlador amostrado a cada TS
            e = p - P_REF                                # abrir a válvula reduz P
            ff = alpha_ff(n) if modo == "PI+FF" else bias
            u = ff + kc * (e + integ / ti)
            sat_pos = (u >= 1 and e > 0) or (u <= 0 and e < 0)
            sat_vel = abs(alpha_c - alpha) / par["tau_a"] >= par["w_max"]   # válvula na vel. máxima
            if not (sat_pos or sat_vel):                 # anti-windup: integração condicional
                integ += e * TS
            alpha_c = min(max(ff + kc * (e + integ / ti), 0.0), 1.0)
        v = min(max((alpha_c - alpha) / par["tau_a"], -par["w_max"]), par["w_max"])
        alpha = min(max(alpha + v * dt, 0.0), 1.0)       # atuador: 1ª ordem com limite de velocidade
        k_tot = n * k_b + KV_MAX * alpha ** expoente
        dp = (q_fonte(p, fonte) - k_tot * math.sqrt(max(p, 0.0))) / (60 * c)
        p = max(p + dp * dt, 0.0)                        # Euler: P(k+1) = P(k) + dt·dP/dt
        t_out[k], p_out[k], a_out[k], n_out[k] = t, p, alpha, n
    return {"t": t_out, "P": p_out, "alpha": a_out, "n": n_out}


def metricas(sim, eventos):
    t, p = sim["t"], sim["P"]
    dt = t[1] - t[0]
    e = p - P_REF
    fora = (p < FAIXA[0] * P_REF) | (p > FAIXA[1] * P_REF)
    acom = []
    tempos = [ev[0] for ev in eventos[1:]] + [t[-1] + dt]
    for t0, t1 in zip(tempos[:-1], tempos[1:]):
        seg = (t >= t0) & (t < t1)
        ruins = np.where(np.abs(e[seg]) > 0.02 * P_REF)[0]
        if len(ruins) == 0:
            acom.append(0.0)
        elif ruins[-1] == seg.sum() - 1:
            acom.append(None)                         # não acomodou dentro do intervalo
        else:
            acom.append(float(t[seg][ruins[-1] + 1] - t0))
    ok = [a for a in acom if a is not None]
    return {"fora_pct": float(fora.mean() * 100), "IAE": float(np.sum(np.abs(e)) * dt),
            "desvio_max_pct": float(np.max(np.abs(e)) / P_REF * 100),
            "t_acom_medio": float(np.mean(ok)) if ok else None,
            "degraus_sem_acomodar": sum(a is None for a in acom), "degraus": len(acom)}


def cenarios():
    rng = np.random.default_rng(42)
    t, ev, estado = 0.0, [(0.0, 7)], np.ones(7, bool)
    while t < 20:
        t += float(rng.uniform(0.1, 0.5))
        estado[rng.integers(7)] ^= True
        if not estado.any():
            estado[rng.integers(7)] = True
        ev.append((round(t, 3), int(estado.sum())))
    return {
        "C1": (n_degraus([7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7], 2.0), 26.0),
        "C2": ([(0.0, 7), (2.0, 4), (8.0, 1)], 14.0),
        "C3": ([e for e in ev if e[0] < 20], 20.0),
    }


def casos_c5():
    """Plantas diferentes do modelo nominal; o controlador continua usando o modelo nominal."""
    a2, a1, a0 = FONTE
    return {
        "Nominal": PLANTA,
        "Bicos K −10%": {**PLANTA, "K": 0.9 * K},
        "Fonte a0 +5%": {**PLANTA, "fonte": (a2, a1, 1.05 * a0)},
        "Válvula quadrática": {**PLANTA, "valvula": "quadratica"},
        "Bicos K +10%": {**PLANTA, "K": 1.1 * K},
    }


# ---------------------------------------------------------------------------
# 4. Figuras
# ---------------------------------------------------------------------------
COR = {"aberta": "#888888", "PI": "#E07B39", "PI+FF": "#2C6FBB"}


def fig_estatica(ident):
    n = np.arange(1, 8)
    nn = np.linspace(1, 7, 200)
    r1 = P_T[-1] / Q_T[-1] ** 2
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.semilogy(N_T, P_T / Q_T ** 2, "ko", label="Medida (Rosa et al., 2019)")
    ax.semilogy(nn, r1 / nn ** 2, "-", color=COR["PI+FF"], label=r"$R_1/n^2$ (modelo deste trabalho)")
    ax.semilogy(nn, [eq27(x) for x in nn], "--", color=COR["PI"], label="Eq. (2.7) de Rosa et al.")
    ax.set_xlabel("Bicos abertos $n$")
    ax.set_ylabel(r"$R_F$ equivalente [(kgf/cm²)/(L/min)²]")
    ax.set_xticks(n)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG / "a_resistencia_n.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 4.5))
    q = np.linspace(0, ident["fonte"]["q_fonte_p0"], 200)
    ax.plot(q, np.polyval(FONTE, q), "k-", lw=2, label="Curva da fonte (ajustada)")
    for ni in range(1, 8):
        qq = np.linspace(0, 6.2, 200)
        ax.plot(qq, (qq / (ni * K)) ** 2, "-", color=COR["PI+FF"], alpha=0.5, lw=1)
        qa = min(6.0, ni * K * math.sqrt(6.3))
        ax.text(qa, (qa / (ni * K)) ** 2, f" n={ni}", fontsize=8, va="bottom")
    ax.plot(Q_T, P_T, "o", color=COR["PI"], label="Pontos medidos (Tabela 1)")
    ax.axhline(P_REF, color="green", ls=":", label=f"$P_{{ref}}$ = {P_REF}")
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 6.5)
    ax.set_xlabel("Q [L/min]")
    ax.set_ylabel("P [kgf/cm²]")
    ax.grid(alpha=0.3)
    ax.legend(loc="lower left")
    fig.tight_layout()
    fig.savefig(FIG / "b_fonte_carga.png", dpi=150)
    plt.close(fig)


def fig_tempo(sims, nome, arquivo):
    fig, ax = plt.subplots(3, 1, figsize=(8, 7), sharex=True,
                           gridspec_kw={"height_ratios": [3, 2, 1]})
    ax[0].axhspan(FAIXA[0] * P_REF, FAIXA[1] * P_REF, color="green", alpha=0.12,
                  label="Faixa ±5% na vazão")
    for modo, s in sims.items():
        ax[0].plot(s["t"], s["P"], color=COR[modo], label="malha aberta" if modo == "aberta" else modo)
        ax[1].plot(s["t"], s["alpha"], color=COR[modo])
    ax[0].axhline(P_REF, color="k", ls=":", lw=1)
    ax[2].step(next(iter(sims.values()))["t"], next(iter(sims.values()))["n"], "k", where="post")
    ax[0].set_ylabel("P [kgf/cm²]")
    ax[1].set_ylabel("Abertura α")
    ax[2].set_ylabel("n")
    ax[2].set_xlabel("t [s]")
    ax[0].set_title(nome)
    ax[0].legend(loc="upper left", fontsize=8, ncol=2)
    for a in ax:
        a.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG / arquivo, dpi=150)
    plt.close(fig)


def fig_c5(c5):
    casos = [c for c in c5 if c5[c].get("atingivel", True)]
    x = np.arange(len(casos))
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    for j, modo in enumerate(["PI", "PI+FF"]):
        v = [c5[c][modo]["fora_pct"] for c in casos]
        b = ax.bar(x + (j - 0.5) * 0.38, v, 0.38, color=COR[modo], label=modo)
        ax.bar_label(b, fmt="%.1f", fontsize=8)
    ax.set_xticks(x, casos)
    ax.set_ylabel("Tempo fora da faixa [%]")
    ax.set_title("Cenário C3 com erro de modelo (C5)")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG / "e_C5_erro_modelo.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 5. Execução
# ---------------------------------------------------------------------------
def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # console do Windows (cp1252) não tem α, τ
    FIG.mkdir(exist_ok=True)
    for velho in ("e_sensibilidade.png", "f_margens.png"):   # figuras de versões anteriores
        (FIG / velho).unlink(missing_ok=True)
    ident = identificacao()
    loo = validacao_cruzada()
    p_max = {n: p_regime(n * K) for n in range(1, 8)}
    assert P_REF < p_max[7], "P_ref inatingível com 7 bicos e válvula fechada"
    lam, tabela_lambda = escolhe_lambda(BASE)
    kc, ti, tau1, theta = sintonia(BASE, lam)
    assert ti >= TS, "Ti menor que o período de amostragem"
    marg = [margens(n, BASE, kc, ti) for n in range(1, 8)]

    resultados = {"identificacao": ident, "validacao_cruzada": loo, "estimativa_C_h": estimativa_ch(),
                  "P_max_valvula_fechada": p_max,
                  "projeto": {"P_ref": P_REF, "KV_max": KV_MAX, "Ts": TS, "lambda": lam, **BASE,
                              "tau1": tau1, "theta": theta, "Kc": kc, "Ti": ti,
                              "alpha_ff": {n: alpha_ff(n) for n in range(0, 8)}},
                  "escolha_lambda": tabela_lambda, "margens": marg, "cenarios": {}, "C5": {}}

    cen = cenarios()
    for nome, (ev, tf) in cen.items():
        sims = {m: simular(ev, tf, m, BASE, kc, ti) for m in ["aberta", "PI", "PI+FF"]}
        resultados["cenarios"][nome] = {m: metricas(s, ev) for m, s in sims.items()}
        resultados["cenarios"][nome]["eventos"] = len(ev)
        fig_tempo(sims, f"Cenário {nome}", f"{'c' if nome != 'C3' else 'd'}_{nome}.png")

    ev, tf = cen["C3"]
    for nome, pl in casos_c5().items():
        pmax7 = p_regime(7 * pl["K"], pl["fonte"])
        r = {"P_max_7": float(pmax7), "atingivel": bool(pmax7 > P_REF)}
        if r["atingivel"]:
            for modo in ["PI", "PI+FF"]:
                r[modo] = metricas(simular(ev, tf, modo, BASE, kc, ti, planta=pl), ev)
        resultados["C5"][nome] = r

    fig_estatica(ident)
    fig_c5(resultados["C5"])
    (AQUI / "resultados.json").write_text(json.dumps(resultados, indent=2, ensure_ascii=False),
                                          encoding="utf-8")

    print(f"K = {ident['K']:.4f}  fonte: a2={A2:.4f} a1={A1:.4f} a0={A0:.3f}  "
          f"erro max P={ident['erro_max_P_pct']:.2f}% Q={ident['erro_max_Q_pct']:.2f}%")
    print(f"LOO: erro max P={loo['erro_max_P_pct']:.2f}% Q={loo['erro_max_Q_pct']:.2f}%")
    print("C_h estimado [mL/(kgf/cm²)]:", {k: round(v, 3) for k, v in resultados["estimativa_C_h"]["C_mL"].items()})
    print("P max (válvula fechada):", {n: round(p, 3) for n, p in p_max.items()})
    for t in tabela_lambda:
        print(f"  λ={t['lambda']:.2f}  Kc={t['Kc']:.3f}  Ti={t['Ti']:.3f}  MF={t['MF_graus']:.1f}°  MG={t['MG_dB']:.1f} dB")
    print(f"PI: λ={lam}  Kc={kc:.4f} /(kgf/cm²)  Ti={ti:.3f} s  τ1={tau1:.3f}  θ={theta:.3f}")
    for m in marg:
        print(f"  n={m['n']}  α_ff={m['alpha_ff']:.3f}  Kg={m['Kg']:.3f}  τp={m['tau_p']:.4f}s"
              f"  MF={m['MF_graus']:.1f}°  MG={m['MG_dB']:.1f} dB")
    for nome, r in resultados["cenarios"].items():
        for modo in ["aberta", "PI", "PI+FF"]:
            x = r[modo]
            ta = "—" if x["t_acom_medio"] is None else f"{x['t_acom_medio']:.2f}s"
            print(f"{nome:3s} {modo:6s} fora={x['fora_pct']:5.1f}%  IAE={x['IAE']:.3f}  "
                  f"desv.max={x['desvio_max_pct']:5.1f}%  t_acom={ta}  "
                  f"sem acomodar={x['degraus_sem_acomodar']}/{x['degraus']}")
    for nome, r in resultados["C5"].items():
        if r["atingivel"]:
            print(f"C5 {nome:20s} Pmax7={r['P_max_7']:.2f}  PI fora={r['PI']['fora_pct']:.1f}%  "
                  f"PI+FF fora={r['PI+FF']['fora_pct']:.1f}%  IAE PI+FF={r['PI+FF']['IAE']:.2f}")
        else:
            print(f"C5 {nome:20s} Pmax7={r['P_max_7']:.2f}  inatingível")


if __name__ == "__main__":
    main()
