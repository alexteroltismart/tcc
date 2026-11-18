"""Diagrama de blocos da malha linearizada no domínio de Laplace (seção 3.5.4).
Referência fixa (ΔP_ref = 0): só o número de bicos entra como distúrbio.
Controlador contínuo e sensor em tempo real (realimentação direta), sem limite de velocidade."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
plt.rcParams.update({"font.family": "Arial", "font.size": 9.5, "mathtext.fontset": "custom",
                     "mathtext.rm": "Arial", "mathtext.it": "Arial:italic"})
fig, ax = plt.subplots(figsize=(10.5, 4.15)); ax.set_xlim(0, 105); ax.set_ylim(3, 44); ax.axis("off")


def box(x, y, w, h, titulo, eq, ref=None):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0", fc="white", ec="black", lw=1.1))
    ax.text(x, y + h/2 - 1.0, titulo, ha="center", va="top", fontsize=9)
    ax.text(x, y - 0.9 if ref else y - 1.2, eq, ha="center", va="center", fontsize=12)
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


y = 18
# linha principal
box(28, y, 17, 11, r"Controlador $G_c(s)$", r"$K_c\,(1 + \frac{1}{T_i\,s})$", "Eq. (3.22)")
summ(44, y)
box(57, y, 13, 11, "Válvula", r"$\frac{1}{\tau_a\,s + 1}$", "Eq. (3.18)")
box(73, y, 10, 11, "Planta", r"$K_g$", "Eq. (3.17)")
summ(86, y)
# feedforward e distúrbio
ax.text(16, 36, r"$\Delta N(s)$" + "\nnúmero de bicos", ha="center", va="center")
box(44, 36, 15, 9, "Feedforward", r"$-\,K_n / K_g$", "Eq. (3.14), linearizada")
box(86, 36, 12, 9, "Distúrbio", r"$K_n$", "Eq. (3.17)")
# sensor em tempo real: a pressão medida é a própria ΔP (realimentação unitária)

arrow([(10, y), (19.5, y)], r"$E(s)$", (15, y + 0.6))
arrow([(36.5, y), (42.2, y)])
arrow([(45.8, y), (50.5, y)], r"$\Delta A_c(s)$", (48.1, y + 0.6), fs=8.5)
arrow([(63.5, y), (68, y)], r"$\Delta A(s)$", (65.8, y + 0.6), fs=8.5)
arrow([(78, y), (84.2, y)])
arrow([(87.8, y), (104, y)], r"$\Delta P(s)$", (97.5, y + 0.6))
ax.plot([10, 10], [5, y], color="black", lw=1.1)
ax.plot([94, 94, 10], [y, 5, 5], color="black", lw=1.1)
ax.text(53, 5.4, r"$\Delta P$ medida (tempo real); $E = \Delta P$, pois $P_{ref}$ é fixa", ha="center", va="bottom", fontsize=9.5)
arrow([(23, 36), (36.5, 36)])
arrow([(44, 31.5), (44, y + 1.8)])
arrow([(16, 38.6), (16, 42.5), (66, 42.5), (66, 36), (80, 36)])
arrow([(86, 31.5), (86, y + 1.8)])
ax.text(66.5, 42.9, "perturbação", ha="center", va="bottom", fontsize=9.5)
fig.savefig("fig/fig12_freq.png", dpi=250, bbox_inches="tight", facecolor="white")
