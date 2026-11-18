"""Modelo e simulação do controle de pressão de uma barra de pulverização bico a bico.

Implementa as equações do Capítulo 3 do TCC (contexto/20.md):
  1. identificação estática a partir da Tabela 1 de Rosa, Terra e Drews Jr (2019),
     com validação cruzada "deixa um de fora";
  2. modelo dinâmico simplificado: a pressão segue o modelo estático a cada instante
     e só o atuador da válvula tem dinâmica (atraso + limite de velocidade);
  3. sintonia por alocação de polos (ζ e tempo de acomodação escolhidos);
  4. controladores P, PI e PI + feedforward em n, com anti-windup; o sensor e o controlador
     leem a pressão em tempo real (a cada passo de integração, sem amostragem);
  5. cenários C1-C3, métricas e figuras;
  6. modelo linear com o número de bicos como distúrbio (referência fixa).
Versões anteriores: simulacao/v07/ (com capacitância na linha), simulacao/v09/ (sintonia lambda),
simulacao/v16/ (sintonia pelo ganho crítico), simulacao/v17/ (só ΔP/ΔN no modelo linear)
simulacao/v18/ (controlador amostrado a 50 ms) e simulacao/v19/ (referência como 2ª entrada).

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
    """Expressão empírica de Rosa et al. (2019), eq. (2.5) do texto."""
    return 42.59 * math.exp(-2.335 * n) + 2.307 * math.exp(-0.4591 * n)


def q_fonte(p, fonte=FONTE):
    """Vazão da fonte para a pressão p: raiz positiva de a2 Q² + a1 Q + (a0 - p) = 0."""
    a2, a1, a0 = fonte
    if p >= a0:
        return 0.0
    return (-a1 - math.sqrt(a1 * a1 - 4 * a2 * (a0 - p))) / (2 * a2)


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
BASE = {"tau_a": 0.2, "w_max": 0.5}   # s, 1/s
DT = 1e-3            # passo de integração [s]; 10 ms já distorce o horário das trocas no C3
DALFA = 0.01         # degrau de abertura usado para medir o ganho K_g
FAIXA = (0.90, 1.10)             # ±10% na pressão (ISO 16122-2:2015, 4.5.4)


def alpha_ff(n, p_ref=P_REF):
    """Feedforward: abertura que mantém P = P_ref em regime com n bicos (modelo nominal)."""
    kv = q_fonte(p_ref) / math.sqrt(p_ref) - n * K
    return min(max(kv / KV_MAX, 0.0), 1.0)


def ganho_kg(n):
    """Conferência de K_g: ΔP/Δα medido no modelo estático, abrindo e fechando a válvula
    DALFA/2 em torno de α_ff (diferença centrada). O valor usado vem de derivada_dp_dc."""
    a = alpha_ff(n)
    p_mais = p_regime(n * K + KV_MAX * (a + DALFA / 2))
    p_menos = p_regime(n * K + KV_MAX * (a - DALFA / 2))
    return {"n": n, "alpha_ff": a, "P_mais": p_mais, "P_menos": p_menos,
            "Kg": (p_mais - p_menos) / DALFA}


def derivada_dp_dc(p=P_REF):
    """Linearização do equilíbrio do nó (Tabela 3): cada vazão vira a reta tangente no ponto de
    operação e a soma das retas dá ΔP = K_g·Δα + K_n·ΔN.
    Denominador D = C/(2√P) − dQs/dP (saídas + fonte), com dQs/dP = 1/(2·a2·Qs + a1).
    K_g = −K_v,max·√P / D (3.15) e K_n = −K·√P / D (3.16); dP/dC = −√P / D."""
    q = q_fonte(p)
    c = q / math.sqrt(p)
    dqs_dp = 1 / (2 * A2 * q + A1)
    return {"Qs": q, "C": c, "dQs_dP": dqs_dp, "saidas": c / (2 * math.sqrt(p)),
            "dP_dC": -math.sqrt(p) / (c / (2 * math.sqrt(p)) - dqs_dp)}


ZETA = 0.7           # amortecimento desejado da malha fechada do PI
TS_ESPEC = 0.5       # tempo de acomodação desejado [s], critério de 2% (OGATA, 2010, Eq. 5.22)


def sintonia_polos(kg, par, zeta=ZETA, ts=TS_ESPEC):
    """Alocação de polos: iguala o denominador da malha PI (Eq. 3.27) a s² + 2ζωn·s + ωn².
    ωn = 4/(ζ·ts) (3.29); Kc·|Kg| = 2ζωn·τa − 1 (3.30); Ti = Kc·|Kg|/(τa·ωn²) (3.31).
    O P usa o mesmo Kc do PI."""
    wn = 4 / (zeta * ts)
    g, ta = abs(kg), par["tau_a"]
    kc = (2 * zeta * wn * ta - 1) / g
    ti = kc * g / (ta * wn ** 2)
    return {"P": (kc, math.inf), "PI": (kc, ti)}, wn


# ---------------------------------------------------------------------------
# 3. Simulação
# ---------------------------------------------------------------------------
def n_degraus(seq, dur):
    """Converte lista de n em degraus de duração 'dur' → lista de (t_inicio, n)."""
    return [(i * dur, n) for i, n in enumerate(seq)]


def simular(eventos, t_fim, modo, par, kc, ti, dt=DT):
    """modo: 'aberta' (α fixo para n=7), 'P' e 'PI' (bias fixo) ou 'PI+FF'.
    No 'P', ti = math.inf e a integral fica sempre zero."""
    n = eventos[0][1]
    alpha = alpha_ff(7) if modo == "aberta" else alpha_ff(n)
    bias = alpha
    p, integ, alpha_c = P_REF, 0.0, alpha
    passos = int(round(t_fim / dt))
    ev = list(eventos)
    t_out, p_out, a_out, n_out = (np.empty(passos) for _ in range(4))
    for k in range(passos):
        t = k * dt
        while ev and ev[0][0] <= t + 1e-12:              # comutação dos bicos
            n = ev.pop(0)[1]
        if modo != "aberta":                            # controlador em tempo real: lê P a cada passo
            e = p - P_REF                                # abrir a válvula reduz P
            ff = alpha_ff(n) if modo == "PI+FF" else bias
            u = ff + kc * (e + integ / ti)
            sat_pos = (u >= 1 and e > 0) or (u <= 0 and e < 0)
            if modo != "P" and not sat_pos:              # anti-windup: integração condicional no limite de posição
                integ += e * dt
            alpha_c = min(max(ff + kc * (e + integ / ti), 0.0), 1.0)
        v = min(max((alpha_c - alpha) / par["tau_a"], -par["w_max"]), par["w_max"])
        alpha = min(max(alpha + v * dt, 0.0), 1.0)       # atuador: 1ª ordem com limite de velocidade
        p = p_regime(n * K + KV_MAX * alpha)   # pressão segue o modelo estático
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


# ---------------------------------------------------------------------------
# 4. Figuras
# ---------------------------------------------------------------------------
COR = {"aberta": "#888888", "P": "#3A9E5C", "PI": "#E07B39", "PI+FF": "#2C6FBB"}


def fig_estatica(ident):
    n = np.arange(1, 8)
    nn = np.linspace(1, 7, 200)
    r1 = P_T[-1] / Q_T[-1] ** 2
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.semilogy(N_T, P_T / Q_T ** 2, "ko", label="Medida (Rosa et al., 2019)")
    ax.semilogy(nn, r1 / nn ** 2, "-", color=COR["PI+FF"], label=r"$R_1/n^2$ (modelo deste trabalho)")
    ax.semilogy(nn, [eq27(x) for x in nn], "--", color=COR["PI"], label="Eq. (2.5) de Rosa et al.")
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
                  label="Faixa ±10% (ISO 16122-2)")
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


def frac_vel_max(sim, par):
    """Fração do tempo em que a válvula se move na velocidade máxima ω_max."""
    v = np.abs(np.diff(sim["alpha"])) / DT
    return float(np.mean(v >= 0.999 * par["w_max"]) * 100)


# ---------------------------------------------------------------------------
# 4b. Modelo linear: funções de transferência ΔP(s)/ΔN(s) em torno de n = 7, P = P_ref
#     (válvula de 1ª ordem sem limite de velocidade; controlador contínuo, como no simulador)
# ---------------------------------------------------------------------------
def modelo_linear(kg, kn, ganho, par):
    """Funções de transferência da pressão ao número de bicos (referência fixa, ΔP_ref = 0),
    montadas bloco a bloco: G_c = num_c/den_c, válvula 1/(τa·s + 1), L = G_c·|Kg|/(τa·s + 1).
    Denominador: den_c·(τa·s + 1) + |Kg|·num_c   (1 + L com as frações tiradas)
      T_n   = Kn·den_c·(τa·s + 1) / den              (sem FF)
      T_nFF = Kn·den_c·τa·s / den                    (com FF)
    Coeficientes em potências decrescentes de s."""
    ta, g = par["tau_a"], abs(kg)
    valv = np.array([ta, 1.0])
    tf = {}
    for modo in ("P", "PI", "PI+FF"):
        kc, ti = ganho[modo]
        num_c, den_c = (np.array([kc]), np.array([1.0])) if ti == math.inf else \
            (np.array([kc * ti, kc]), np.array([ti, 0.0]))
        den = np.polyadd(np.polymul(den_c, valv), g * num_c)
        num_n = np.polymul(den_c, [ta, 0.0] if modo == "PI+FF" else valv) * kn
        tf[modo] = (num_n.tolist(), den.tolist())
    kc_p = ganho["P"][0]
    kc, ti = ganho["PI"]
    den_pi = [ta * ti, ti * (1 + kc * g), kc * g]          # forma fechada (Eq. do texto)
    assert np.allclose(tf["PI"][1], den_pi), \
        "denominador montado bloco a bloco difere da forma fechada"
    assert np.allclose(tf["P"][1], [ta, 1 + kc_p * g])
    wn = math.sqrt(den_pi[2] / den_pi[0])
    zeta = den_pi[1] / den_pi[0] / (2 * wn)
    return {"Kn": kn, "tf": tf, "polos_PI": [complex(r) for r in np.roots(den_pi)],
            "polo_P": -(1 + kc_p * g) / ta, "wn": wn, "zeta": zeta, "ts_2pct": 4 / (zeta * wn),
            "erro_P_regime": kn * -1 / (1 + kc_p * g)}


def resposta_linear(lin, kg, ganho, par, modo, t_fim=3.0, t_ev=0.5, dt=DT, d_n=-1.0):
    """Resposta no tempo do modelo linear, por Euler, a um degrau de d_n bicos em t_ev
    (referência fixa). O padrão (d_n = −1) é um bico fechando."""
    kc, ti = ganho[modo]
    t = np.arange(0, t_fim, dt)
    da, integ = 0.0, 0.0                                   # desvios de α e soma do integrador
    p = np.empty_like(t)
    for k, tk in enumerate(t):
        dn = d_n if tk >= t_ev else 0.0
        dp = kg * da + lin["Kn"] * dn                      # pressão instantânea, linearizada (H6)
        dff = -lin["Kn"] / kg * dn if modo == "PI+FF" else 0.0
        e = dp                                             # referência fixa: ΔP_ref = 0
        dac = dff + kc * (e + (integ / ti if ti != math.inf else 0.0))
        integ += e * dt
        da += dt * (dac - da) / par["tau_a"]
        p[k] = P_REF + dp
    return t, p


def virgula(ax):
    """Números dos eixos com vírgula decimal."""
    fmt = matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}".replace(".", ","))
    ax.xaxis.set_major_formatter(fmt)
    ax.yaxis.set_major_formatter(fmt)


def fmt_v(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


def metricas_degrau(sim, t_ev=0.5):
    """Resposta a um bico fechando: salto no instante da troca, quanto a pressão passa abaixo
    da referência depois dele e tempo de acomodação na faixa de ±2% do salto em torno do
    valor final."""
    t, p = sim["t"], sim["P"]
    d = t >= t_ev - 1e-12
    tt, pp = t[d], p[d]
    fim = float(pp[-1])
    salto = float(pp.max() - P_REF)
    banda = 0.02 * abs(salto)
    ts = float(tt[np.where(np.abs(pp - fim) > banda)[0][-1]] - t_ev)
    j = int(np.argmin(pp))
    abaixo = float(max(P_REF - pp[j], 0.0))
    return {"salto": salto, "ts": ts, "abaixo": abaixo, "abaixo_pct_salto": 100 * abaixo / salto,
            "t_min": float(tt[j] - t_ev), "erro_final": fim - P_REF, "banda": banda, "P_final": fim}


def resposta_1_bico(lin, kg, ganho, par):
    """Um bico fecha em t = 0,5 s (7 → 6): simulador com e sem limite de velocidade da válvula
    e modelo linear (função de transferência)."""
    ev, tf = [(0.0, 7), (0.5, 6)], 3.0
    sem_lim = {**par, "w_max": 1e3}                       # válvula sem limite de velocidade
    res = {}
    for modo in ("P", "PI", "PI+FF"):
        s_lim = simular(ev, tf, modo, par, *ganho[modo])
        s_sem = simular(ev, tf, modo, sem_lim, *ganho[modo])
        t, p = resposta_linear(lin, kg, ganho, par, modo, tf)
        res[modo] = {"sims": (s_sem, s_lim), "linear": (t, p),
                     "sem_limite": metricas_degrau(s_sem), "com_limite": metricas_degrau(s_lim),
                     "dif_max_linear": float(np.max(np.abs(p - s_sem["P"])))}
    return res


def fig_linear(resp):
    fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
    for ax, modo in zip(axs, ("P", "PI", "PI+FF")):
        r = resp[modo]
        s_sem, s_lim = r["sims"]
        m0, m1 = r["sem_limite"], r["com_limite"]
        ax.axhspan(m0["P_final"] - m0["banda"], m0["P_final"] + m0["banda"], color="gray", alpha=0.15,
                   label="±2% do salto")
        ax.axhline(P_REF, color="k", ls=":", lw=0.8)
        ax.plot(s_sem["t"], s_sem["P"], color="k", ls="--", lw=1.3,
                label="sem limite de velocidade (≈ função de transferência)")
        ax.plot(s_lim["t"], s_lim["P"], color=COR[modo], lw=1.8,
                label=r"com limite ($\omega_{max}$ = 0,5 s$^{-1}$)")
        ax.axvline(0.5 + m0["ts"], color="k", ls="--", lw=0.7)
        ax.axvline(0.5 + m1["ts"], color=COR[modo], ls="--", lw=0.7)
        ax.text(0.5 + m0["ts"] + 0.02, 3.80, f"$t_s$ = {fmt_v(m0['ts'], 2)} s", fontsize=8)
        ax.text(0.5 + m1["ts"] + 0.02, 3.72, f"$t_s$ = {fmt_v(m1['ts'], 2)} s", fontsize=8, color=COR[modo])
        ax.text(0.53, 3.835, f"salto +{fmt_v(m0['salto'])}", fontsize=8)
        if modo == "P":
            ax.text(1.5, m0["P_final"] + 0.02, f"erro final +{fmt_v(m0['erro_final'])}", fontsize=8)
        else:
            for m, c, dx in ((m0, "k", -0.02), (m1, COR[modo], 0.10)):
                tq, pq = 0.5 + m["t_min"], P_REF - m["abaixo"]
                ax.annotate(f"−{fmt_v(m['abaixo'])} ({m['abaixo_pct_salto']:.0f}% do salto)", (tq, pq),
                            (tq + dx, pq - 0.05), fontsize=8, color=c,
                            arrowprops=dict(arrowstyle="->", lw=0.6, color=c))
        ax.set_ylabel(f"{modo}\nP [kgf/cm²]")
        ax.set_ylim(3.22, 3.90)
        ax.grid(alpha=0.3)
        ax.legend(fontsize=7.5, loc="lower right" if modo == "P" else "center right")
        virgula(ax)
    axs[0].set_title("Um bico fecha em t = 0,5 s (7 → 6): válvula com e sem limite de velocidade")
    axs[-1].set_xlabel("t [s]")
    axs[-1].set_xlim(0.3, 2.0)
    fig.tight_layout()
    fig.savefig(FIG / "g_funcao_transferencia.png", dpi=150)
    plt.close(fig)


def fig_linearizacao():
    """Vazão dos sete bicos, Q = 7·K·√P, e a reta tangente no ponto de operação (P_ref)."""
    n, p0 = 7, P_REF
    q = lambda p: n * K * np.sqrt(p)
    incl = n * K / (2 * math.sqrt(p0))                     # derivada no ponto de operação
    reta = lambda p: q(p0) + incl * (p - p0)
    pp = np.linspace(0.3, 6.5, 300)
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    ax.plot(pp, q(pp), color=COR["PI+FF"], lw=2, label=r"curva real, $Q_{barra} = 7K\sqrt{P}$")
    ax.plot(pp, reta(pp), "--", color=COR["PI"], lw=1.5, label="reta tangente no ponto de operação")
    ax.plot(p0, q(p0), "ko", ms=7, label=f"ponto de operação ($P$ = {fmt_v(p0, 1)})")
    res = {"inclinacao": incl}
    for pt, rot in ((3.8, "perto"), (1.0, "longe")):
        erro = 100 * (reta(pt) - q(pt)) / q(pt)
        res[rot] = {"P": pt, "erro_pct": float(erro)}
        ax.plot([pt, pt], [q(pt), reta(pt)], color="k", lw=1)
        ax.annotate(f"{rot} (P = {fmt_v(pt, 1)}): erro {fmt_v(erro, 1)}%", (pt, (q(pt) + reta(pt)) / 2),
                    (pt + 0.4 if pt < P_REF else pt - 3.0, reta(pt) + (1.6 if pt < P_REF else 0.6)), fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.6))
    ax.set_xlabel("Pressão $P$ [kgf/cm²]")
    ax.set_ylabel("Vazão dos bicos $Q_{barra}$ [L/min]")
    ax.set_xlim(0, 6.6)
    ax.set_ylim(0, 9)
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right", fontsize=8)
    virgula(ax)
    fig.tight_layout()
    fig.savefig(FIG / "h_linearizacao.png", dpi=150)
    plt.close(fig)
    return res


def fig_plano_s(lin, par):
    """Polos e zeros da malha no plano s, com a região que atende ζ ≥ ZETA e t_s ≤ TS_ESPEC."""
    from matplotlib.patches import Polygon
    ta = par["tau_a"]
    polo = lin["polos_PI"][0]
    sig, wd = -polo.real, abs(polo.imag)
    ang = math.acos(ZETA)
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    h, H = sig * math.tan(ang), 20 * math.tan(ang)
    ax.add_patch(Polygon([(-sig, h), (-20, H), (-20, -H), (-sig, -h)], closed=True, color="#2a9d8f",
                         alpha=0.15,
                         label=f"região que atende ζ ≥ {fmt_v(ZETA, 1)} e $t_s$ ≤ {fmt_v(TS_ESPEC, 1)} s"))
    r = np.linspace(0, 20, 10)
    for sgn in (1, -1):
        ax.plot(-r * math.cos(ang), sgn * r * math.sin(ang), "--", color="#2a9d8f", lw=1)
    ax.axvline(-sig, color="#2a9d8f", ls=":", lw=1.2)
    ax.text(-sig + 0.2, 12.8, f"σ = 4/$t_s$ = {fmt_v(4 / TS_ESPEC, 0)}", fontsize=8, color="#2a9d8f")
    ax.text(-19.5, 11.0, f"linha ζ = {fmt_v(ZETA, 1)}\n(ângulo de {fmt_v(math.degrees(ang), 1)}°)",
            fontsize=8, color="#2a9d8f")
    th = np.linspace(math.pi - ang, math.pi, 30)
    ax.plot(3 * np.cos(th), 3 * np.sin(th), color="#2a9d8f", lw=0.8)
    ax.plot(-1 / ta, 0, "x", color="gray", ms=10, mew=2, label=f"polo da válvula sozinha ({fmt_v(-1 / ta, 0)})")
    ax.plot(lin["polo_P"], 0, "x", color=COR["P"], ms=10, mew=2,
            label=f"polo da malha com P ({fmt_v(lin['polo_P'], 0)})")
    ax.plot([-sig, -sig], [wd, -wd], "x", color=COR["PI"], ms=12, mew=2.5,
            label=f"polos da malha com PI ({fmt_v(-sig, 1)} ± j{fmt_v(wd, 1)})")
    ax.plot([0, -1 / ta], [0, 0], "o", mfc="none", color="#264653", ms=10, mew=1.5,
            label=f"zeros da resposta aos bicos (0 e {fmt_v(-1 / ta, 0)})")
    ax.plot([0, -sig], [0, wd], "--", color=COR["PI"], lw=0.8)
    ax.text(-4.5, 5.3, f"ωn = {fmt_v(lin['wn'], 2)}", fontsize=8, color=COR["PI"], rotation=-45)
    ax.text(-1 / ta, -1.3, f"polo da válvula\ne zero ({fmt_v(-1 / ta, 0)})", fontsize=7, ha="center",
            va="top", color="#555555")
    ax.set_xlim(-20, 3)
    ax.set_ylim(-14, 14)
    ax.set_aspect("equal")
    ax.set_xlabel("parte real, σ [1/s]")
    ax.set_ylabel("parte imaginária, ω [rad/s]")
    ax.legend(fontsize=7.5, loc="lower left")
    ax.grid(alpha=0.25)
    virgula(ax)
    fig.tight_layout()
    fig.savefig(FIG / "i_plano_s.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 5. Execução
# ---------------------------------------------------------------------------
def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # console do Windows (cp1252) não tem α, τ
    FIG.mkdir(exist_ok=True)
    for velho in ("e_sensibilidade.png", "f_margens.png", "e_C5_erro_modelo.png", "f_ganho_critico.png",
                  "h_superposicao.png"):   # versões anteriores
        (FIG / velho).unlink(missing_ok=True)
    ident = identificacao()
    loo = validacao_cruzada()
    p_max = {n: p_regime(n * K) for n in range(1, 8)}
    assert P_REF < p_max[7], "P_ref inatingível com 7 bicos e válvula fechada"
    dpc = derivada_dp_dc()                                 # soma das retas da Tabela 3, Eqs. (3.15)–(3.16)
    kg, kn = KV_MAX * dpc["dP_dC"], K * dpc["dP_dC"]
    ganhos = [ganho_kg(n) for n in range(1, 8)]            # conferência por diferença centrada
    assert max(abs(g["Kg"] - kg) for g in ganhos) < 1e-3 * abs(kg), ("K_g analítico ≠ numérico", kg)
    a0 = alpha_ff(7)
    kn_num = (p_regime(7.005 * K + KV_MAX * a0) - p_regime(6.995 * K + KV_MAX * a0)) / 0.01
    assert abs(kn_num - kn) < 1e-3 * abs(kn), ("K_n analítico ≠ numérico", kn, kn_num)

    tun, wn_espec = sintonia_polos(kg, BASE)
    ganho = {"P": tun["P"], "PI": tun["PI"], "PI+FF": tun["PI"]}
    kc, ti = tun["PI"]
    assert kc > 0 and ti > 0, ("ganhos inválidos", kc, ti)

    resultados = {"identificacao": ident, "validacao_cruzada": loo,
                  "P_max_valvula_fechada": p_max, "ganho_Kg": ganhos,
                  "projeto": {"P_ref": P_REF, "KV_max": KV_MAX, "dt": DT, "faixa": FAIXA,
                              **BASE, "Kg": kg, "zeta": ZETA, "ts_espec": TS_ESPEC, "wn": wn_espec,
                              "P_Kc": kc, "PI_Kc": kc, "PI_Ti": ti,
                              "alpha_ff": {n: alpha_ff(n) for n in range(0, 8)}},
                  "cenarios": {}, "varredura_w_max": {}}

    cen = cenarios()
    modos = ["aberta", "P", "PI", "PI+FF"]
    for nome, (ev, tf) in cen.items():
        sims = {m: simular(ev, tf, m, BASE, *ganho.get(m, (0.0, math.inf))) for m in modos}
        resultados["cenarios"][nome] = {m: {**metricas(s, ev), "vel_max_pct": frac_vel_max(s, BASE),
                                            "P_final": float(s["P"][-1])} for m, s in sims.items()}
        resultados["cenarios"][nome]["eventos"] = len(ev)
        fig_tempo(sims, f"Cenário {nome}", f"{'c' if nome != 'C3' else 'd'}_{nome}.png")

    for w in (0.5, 1.0, 2.0):                              # velocidade da válvula e o feedforward
        par = {**BASE, "w_max": w}
        resultados["varredura_w_max"][w] = {
            c: {m: metricas(simular(cen[c][0], cen[c][1], m, par, *ganho[m]), cen[c][0])["fora_pct"]
                for m in ("PI", "PI+FF")} for c in ("C2", "C3")}

    lin = modelo_linear(kg, kn, ganho, BASE)
    assert abs(lin["Kn"] - kg * K / KV_MAX) < 0.01 * abs(lin["Kn"]), lin["Kn"]   # válvula linear (H5)
    assert all(r.real < 0 for r in lin["polos_PI"]), "malha linear instável"
    assert abs(lin["zeta"] - ZETA) < 0.01 * ZETA and abs(lin["wn"] - wn_espec) < 0.01 * wn_espec, \
        ("polos diferentes dos especificados", lin["zeta"], lin["wn"])
    resp = resposta_1_bico(lin, kg, ganho, BASE)
    fig_linear(resp)
    fig_plano_s(lin, BASE)
    lin_fig = fig_linearizacao()
    resultados["resposta_1_bico"] = {m: {k: v for k, v in r.items() if k not in ("sims", "linear")}
                                     for m, r in resp.items()}
    resultados["linearizacao_fig"] = lin_fig
    resultados["modelo_linear"] = {**{k: v for k, v in lin.items() if k not in ("polos_PI", "tf")},
                                   "polos_PI": [[r.real, r.imag] for r in lin["polos_PI"]],
                                   "tf": {m: {"num": n, "den": d} for m, (n, d) in lin["tf"].items()},
                                   "linearizacao_no": dpc,
                                   "Kn_numerico": kn_num}

    fig_estatica(ident)
    (AQUI / "resultados.json").write_text(json.dumps(resultados, indent=2, ensure_ascii=False),
                                          encoding="utf-8")

    print(f"K = {ident['K']:.4f}  fonte: a2={A2:.4f} a1={A1:.4f} a0={A0:.3f}  "
          f"erro max P={ident['erro_max_P_pct']:.2f}% Q={ident['erro_max_Q_pct']:.2f}%")
    print(f"LOO: erro max P={loo['erro_max_P_pct']:.2f}% Q={loo['erro_max_Q_pct']:.2f}%")
    print("P max (válvula fechada):", {n: round(p, 3) for n, p in p_max.items()})
    for g in ganhos:
        print(f"  n={g['n']}  α_ff={g['alpha_ff']:.3f}  P(α+)={g['P_mais']:.4f}  "
              f"P(α−)={g['P_menos']:.4f}  Kg={g['Kg']:.3f}")
    print(f"Polos: ζ={ZETA}  ts={TS_ESPEC} s  ωn={wn_espec:.3f} rad/s  "
          f"Kc={kc:.4f}  Ti={ti:.4f} s")
    for nome, r in resultados["cenarios"].items():
        for modo in modos:
            x = r[modo]
            ta = "—" if x["t_acom_medio"] is None else f"{x['t_acom_medio']:.2f}s"
            print(f"{nome:3s} {modo:6s} fora={x['fora_pct']:5.1f}%  IAE={x['IAE']:.3f}  "
                  f"desv.max={x['desvio_max_pct']:5.1f}%  t_acom={ta}  "
                  f"sem acomodar={x['degraus_sem_acomodar']}/{x['degraus']}  "
                  f"vel.max={x['vel_max_pct']:4.1f}%  P_final={x['P_final']:.3f}")
    print(f"Linear: Kn={lin['Kn']:.4f}  polo P={lin['polo_P']:.2f}  polos PI={lin['polos_PI']}  "
          f"ωn={lin['wn']:.2f} rad/s  ζ={lin['zeta']:.3f}  ts(2%)={lin['ts_2pct']:.3f} s  "
          f"erro P={lin['erro_P_regime']:.4f}")
    for m, (n, d) in lin["tf"].items():
        print(f"  T_n {m}(s): num={np.round(n, 5).tolist()}  den={np.round(d, 5).tolist()}")
    print(f"Linearização do nó: Qs={dpc['Qs']:.3f} C={dpc['C']:.4f} C/(2√P)={dpc['saidas']:.4f} "
          f"dQs/dP={dpc['dQs_dP']:.4f} dP/dC={dpc['dP_dC']:.4f} → Kg={KV_MAX * dpc['dP_dC']:.4f} "
          f"Kn={K * dpc['dP_dC']:.4f}")
    for w, r in resultados["varredura_w_max"].items():
        print(f"ω_max={w:.2f}/s  " + "  ".join(
            f"{c}: PI {x['PI']:.1f}% PI+FF {x['PI+FF']:.1f}%" for c, x in r.items()))


if __name__ == "__main__":
    main()
