"""Diagrama de blocos da malha com as equações no domínio do tempo (versão em tempo da Figura 12)."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
plt.rcParams.update({"font.family": "Arial", "font.size": 9.5, "mathtext.fontset": "custom",
                     "mathtext.rm": "Arial", "mathtext.it": "Arial:italic"})
fig, ax = plt.subplots(figsize=(12, 5.2)); ax.set_xlim(0, 120); ax.set_ylim(-2, 46); ax.axis("off")


def box(x, y, w, h, titulo, eq, ref=None, fs=11):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0", fc="white", ec="black", lw=1.1))
    ax.text(x, y + h/2 - 1.0, titulo, ha="center", va="top", fontsize=9)
    ax.text(x, y - 0.6, eq, ha="center", va="center", fontsize=fs, linespacing=1.6)
    if ref:
        ax.text(x, y - h/2 + 0.5, ref, ha="center", va="bottom", fontsize=7.5, color="0.35")


def summ(x, y, r=1.8):
    ax.add_patch(Circle((x, y), r, fc="white", ec="black", lw=1.1)); ax.text(x, y, "Σ", ha="center", va="center")


def arrow(pts, label=None, lpos=None, ls="-", va="bottom", fs=9.5):
    for (x0, y0), (x1, y1) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x0, x1], [y0, y1], color="black", lw=1.1, ls=ls)
    ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="-|>", lw=1.1, ls=ls, color="black",
                                                                  shrinkA=0, shrinkB=0, mutation_scale=12))
    if label:
        ax.text(*lpos, label, ha="center", va=va, fontsize=fs)


y = 19
# linha principal
ax.text(-1.5, y, r"$P_{ref}$", ha="left", va="center", fontsize=11)
summ(8, y); ax.text(5.2, y + 1.2, "−", fontsize=12); ax.text(8.6, y - 4.2, "+", fontsize=10)
box(25, y, 23, 12, "Controlador P ou PI",
    r"$K_c\,[\,e(t) + \frac{1}{T_i}\int_0^t e(\tau)\,d\tau\,]$", "Eqs. (3.16) e (2.13)")
summ(42, y)
box(53.5, y, 12, 12, "Limite", r"$0 \leq \alpha_c \leq 1$", fs=10.5)
box(72, y, 19, 12, "Válvula",
    r"$\frac{d\alpha}{dt} = \frac{\alpha_c - \alpha}{\tau_a}$" + "\n" + r"$|d\alpha/dt| \leq \omega_{max}$",
    "Eq. (3.12)", fs=11)
box(97, y, 22, 12, "Planta (pressão instantânea)",
    r"$Q_s(P) = [\,n\,K + K_v(\alpha)\,]\,\sqrt{P}$", "Eqs. (3.10) e (3.11)", fs=10.5)
# feedforward e bicos
ax.text(14, 38, r"$n(t)$" + "\nnúmero de bicos", ha="center", va="center")
box(44, 38, 36, 10, "Feedforward",
    r"$\alpha_{ff}(n) = [\,Q_s(P_{ref})\,/\,\sqrt{P_{ref}} - n\,K\,]\,/\,K_{v,max}$", "Eq. (3.14)", fs=10)
# sensor amostrado
box(72, 2.5, 34, 8.5, "Sensor amostrado",
    r"$P_m(t) = P(k\,T_s)$,  $k\,T_s \leq t < (k+1)\,T_s$", r"$T_s$ = 50 ms", fs=9.5)

arrow([(3, y), (6.2, y)])
arrow([(9.8, y), (13.5, y)], r"$e(t)$", (11.7, y + 0.6))
arrow([(36.5, y), (40.2, y)])
arrow([(43.8, y), (47.5, y)], r"$\alpha_c$", (45.7, y + 0.6))
arrow([(59.5, y), (62.5, y)])
arrow([(81.5, y), (86, y)], r"$\alpha(t)$", (83.8, y + 0.6), fs=9)
arrow([(108, y), (119, y)], r"$P(t)$", (115, y + 0.6))
arrow([(111.5, y), (111.5, 2.5), (89, 2.5)])
arrow([(55, 2.5), (8, 2.5), (8, y - 1.8)], r"$P$ medida", (30, 2.9))
arrow([(21, 38), (26, 38)])
arrow([(42, 33), (42, y + 1.8)])
arrow([(14, 40.6), (14, 44.5), (97, 44.5), (97, y + 6)], "perturbação", (75, 44.9))
arrow([(53.5, y - 6), (53.5, 10), (25, 10), (25, y - 6)], ls="--")
ax.text(39.2, 9.6, "limite de posição (anti-windup)", ha="center", va="top", fontsize=8.5)
fig.savefig("fig/fig12_tempo.png", dpi=250, bbox_inches="tight", facecolor="white")
