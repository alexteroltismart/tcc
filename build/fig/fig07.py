import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
plt.rcParams.update({"font.family": "Arial", "font.size": 9.5, "mathtext.fontset": "custom",
                     "mathtext.rm": "Arial", "mathtext.it": "Arial:italic"})
fig, ax = plt.subplots(figsize=(10, 4.2)); ax.set_xlim(0, 101); ax.set_ylim(0, 42); ax.axis("off")


def box(x, y, w, h, txt):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0", fc="white", ec="black", lw=1.1))
    ax.text(x, y, txt, ha="center", va="center", linespacing=1.3)


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
ax.text(1, y, r"$P_{ref}$", ha="left", va="center", fontsize=11)
summ(12, y); ax.text(9.2, y + 0.6, "+", fontsize=10); ax.text(12.6, y - 4.2, "−", fontsize=12)
box(26, y, 13, 8, "P ou PI\n" + r"$K_c$, $T_i$" + "\nanti-windup")
summ(41, y)
box(53, y, 13, 7.5, "Limite\n" + r"$0 \leq \alpha_c \leq 1$")
box(70, y, 17, 7.5, "Atuador da válvula\n" + r"$\tau_a$, $\omega_{max}$ (Eq. 3.12)")
box(88.5, y, 14, 7.5, "Planta hidráulica\n(Eq. 3.10)")
box(41, 34, 14, 6.5, "Feedforward\n" + r"$\alpha_{ff}(n)$, 0,2 s antes")
box(66, 4, 21, 6.5, "Sensor de pressão\n" + "leitura em tempo real")
ax.text(18, 34, r"$n(t)$" + "\ncomando dos bicos", ha="center", va="center")
arrow([(6.5, y), (10.2, y)])
arrow([(13.8, y), (19.5, y)], r"$e = P - P_{ref}$", (16.5, y + 4.6))
arrow([(32.5, y), (39.2, y)])
arrow([(42.8, y), (46.5, y)], r"$\alpha_c$", (44.6, y + 0.5))
arrow([(59.5, y), (61.5, y)])
arrow([(78.5, y), (81.5, y)], r"$\alpha$", (80, y + 0.5))
arrow([(95.5, y), (100.5, y)], r"$P$", (98.8, y + 0.5))
arrow([(97.5, y), (97.5, 4), (76.5, 4)])
arrow([(55.5, 4), (12, 4), (12, y - 1.8)], r"$P$ medida", (30, 4.4))
arrow([(25, 34), (34, 34)])
arrow([(41, 30.75), (41, y + 1.8)])
arrow([(18, 36.5), (18, 40), (88.5, 40), (88.5, y + 3.75)], "perturbação", (70, 40.3))
arrow([(53, y - 3.75), (53, 10.5), (26, 10.5), (26, y - 4)], ls="--")
ax.text(39.5, 10.0, "limite de posição (anti-windup)", ha="center", va="top", fontsize=8.5)
fig.savefig("fig/fig07.png", dpi=250, bbox_inches="tight", facecolor="white")
