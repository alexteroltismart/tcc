"""Teste à parte (v22): feedforward com antecipação da troca de bicos.
O sistema que comanda os bicos sabe com antecedência qual bico vai abrir ou fechar. Aqui o
feedforward usa o número de bicos de daqui a T_ant segundos, α_ff(n(t + T_ant)), e a válvula
começa a se mover antes da troca. O PI continua lendo a pressão real.
T_ant = 0,24 s é o tempo para a válvula compensar um bico na velocidade máxima (0,121/0,5);
0,12 s é metade disso (metade da rampa antes da troca, metade depois).
Não entra nos números do script principal. Só gera figuras (e imprime % fora e IAE).
Rodar: py -3 simulacao/teste_antecipacao.py"""
import sys, inspect
from pathlib import Path
sys.path.insert(0, r"D:\tech\tcc\simulacao")
sys.stdout.reconfigure(encoding="utf-8")
import numpy as np
import modelo_barra as m
import matplotlib.pyplot as plt

SAIDA = Path(__file__).resolve().parent / "figuras_teste"
SAIDA.mkdir(exist_ok=True)
T_UM_BICO = (m.K / m.KV_MAX) / m.BASE["w_max"]          # ≈ 0,24 s


def n_em(eventos, t):
    """Número de bicos abertos no instante t, pela lista de eventos (t_inicio, n)."""
    n = eventos[0][1]
    for te, ne in eventos:
        if te <= t + 1e-12:
            n = ne
    return n


src = inspect.getsource(m.simular)
alvo = 'ff = alpha_ff(n) if modo == "PI+FF" else bias'
assert alvo in src
ns = dict(vars(m))
ns["n_em"] = n_em
exec(src.replace(alvo, 'ff = alpha_ff(n_em(eventos, t + t_ant)) if modo == "PI+FF" else bias')
        .replace("def simular(eventos, t_fim, modo, par, kc, ti, dt=DT):",
                 "def simular_ant(eventos, t_fim, modo, par, kc, ti, dt=DT, t_ant=0.0):"), ns)
simular_ant = ns["simular_ant"]

kg = m.ganho_kg(7)["Kg"]
tun, _ = m.sintonia_polos(kg, m.BASE)
cen = m.cenarios()
config = [("PI", "PI", 0.0, m.COR["PI"], "-"),
          ("PI+FF", "PI+FF sem antecipação", 0.0, m.COR["PI+FF"], "-"),
          ("PI+FF", f"PI+FF antecipado {T_UM_BICO / 2:.2f} s".replace(".", ","), T_UM_BICO / 2, "#7B3FA0", "-"),
          ("PI+FF", f"PI+FF antecipado {T_UM_BICO:.2f} s".replace(".", ","), T_UM_BICO, "#C0392B", "--")]

for c in ("C1", "C3"):
    ev, tf = cen[c]
    fig, ax = plt.subplots(3, 1, figsize=(9, 7.5), sharex=True, gridspec_kw={"height_ratios": [3, 2, 1]})
    ax[0].axhspan(m.FAIXA[0] * m.P_REF, m.FAIXA[1] * m.P_REF, color="green", alpha=0.12,
                  label="Faixa ±10% (ISO 16122-2)")
    for modo, rot, t_ant, cor, ls in config:
        s = simular_ant(ev, tf, modo, m.BASE, *tun["PI"], t_ant=t_ant)
        r = m.metricas(s)
        print(f"{c} {rot:28s} fora={r['fora_pct']:5.1f}%  IAE={r['IAE']:.3f}")
        ax[0].plot(s["t"], s["P"], color=cor, ls=ls, lw=1.2,
                   label=f"{rot} ({r['fora_pct']:.1f}% fora)".replace(".", ","))
        ax[1].plot(s["t"], s["alpha"], color=cor, ls=ls, lw=1.2)
    ax[0].axhline(m.P_REF, color="k", ls=":", lw=1)
    ax[2].step([e[0] for e in ev] + [tf], [e[1] for e in ev] + [ev[-1][1]], "k", where="post")
    ax[0].set_ylabel("P [kgf/cm²]")
    ax[1].set_ylabel("Abertura α")
    ax[2].set_ylabel("n")
    ax[2].set_xlabel("t [s]")
    ax[0].set_title(f"Cenário {c}: feedforward com antecipação da troca de bicos (teste)")
    ax[0].legend(loc="upper left", fontsize=7.5, ncol=2)
    for a in ax:
        a.grid(alpha=0.3)
        m.virgula(a)
    fig.tight_layout()
    fig.savefig(SAIDA / f"antecipacao_{c}.png", dpi=150)
    plt.close(fig)
print("figuras em", SAIDA)
