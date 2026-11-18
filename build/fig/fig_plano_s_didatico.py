"""Figura conceitual do plano s (seção 2.6.2): seis posições de polo e a resposta de cada uma,
y(t) = e^(σt)·cos(ωt). Não usa dados do modelo. Rodar: py -3 build/fig/fig_plano_s_didatico.py"""
from pathlib import Path
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
vir = lambda ax: (ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v,_: f"{v:g}".replace(".",","))),
                  ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v,_: f"{v:g}".replace(".",","))))
# ---------- Figura A: o que a posição do polo diz ----------
fig, ax = plt.subplots(figsize=(9, 6.2))
ax.axhline(0, color="k", lw=0.8); ax.axvline(0, color="k", lw=0.8)
ax.axvspan(-11, 0, color="#2a9d8f", alpha=0.07); ax.axvspan(0, 4, color="#e63946", alpha=0.07)
ax.text(-10.7, -5.0, "ESTÁVEL (semiplano esquerdo)", fontsize=10, color="#2a9d8f", weight="bold")
ax.text(0.3, -5.0, "INSTÁVEL", fontsize=10, color="#e63946", weight="bold")
casos = [(-8, 0, "real, longe do eixo:\nsome rápido", -8), (-2.5, 0, "real, perto do eixo:\nsome devagar", -2.5),
         (-8, 6, "complexo, longe:\noscila pouco e some rápido", -8), (-1.5, 6, "complexo, perto:\noscila muito", -3.6),
         (0, 6, "no eixo:\noscila para sempre", 0.6), (2, 0, "à direita:\ncresce sem parar", 2)]
t = np.linspace(0, 3, 400)
for s, w, txt, xc in casos:
    pts = [(s, w), (s, -w)] if w else [(s, 0)]
    for p in pts: ax.plot(*p, "x", color="k", ms=10, mew=2)
    y = np.exp(s*t)*np.cos(w*t)
    ins = ax.inset_axes([xc-1.3, w+0.9 if w else 1.2, 2.6, 2.2], transform=ax.transData)
    ins.plot(t, np.clip(y, -1.5, 3), color="#264653", lw=1.3); ins.axhline(0, color="gray", lw=0.5)
    ins.set_xticks([]); ins.set_yticks([]); ins.set_ylim(-1.3, 1.6 if s <= 0 else 3)
    ins.set_title(txt, fontsize=7, pad=2)
ax.annotate("", (-10.5, -7.2), (-0.5, -7.2), arrowprops=dict(arrowstyle="->"))
ax.text(-5.5, -7.0, "mais à esquerda = some mais rápido (parte real)", ha="center", fontsize=8, va="bottom")
ax.annotate("", (3.5, -1.5), (3.5, -7.5), arrowprops=dict(arrowstyle="->"))
ax.text(3.3, -4.5, "mais alto =\noscila mais\nrápido\n(parte imag.)", ha="right", fontsize=8, va="center")
ax.set_xlim(-11, 4); ax.set_ylim(-8, 10); vir(ax)
ax.set_xlabel("parte real, σ [1/s]"); ax.set_ylabel("parte imaginária, ω [rad/s]")
ax.set_title("Plano s: onde está o polo e como a resposta se comporta")
fig.tight_layout(); fig.savefig(Path(__file__).with_name("fig_plano_s_didatico.png"), dpi=150); plt.close(fig)

