"""Malha da Figura 15 redesenhada com o ganho de malha L(s) num bloco só (seção 3.5.4, v22).
Sem feedforward (P e PI): (a) malha com L(s) na realimentação; (b) bloco equivalente T_n(s).
Rodar a partir de build/: py -3 fig/fig_malha_L.py"""
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
plt.rcParams.update({"font.family": "Arial", "font.size": 9.5, "mathtext.fontset": "custom",
                     "mathtext.rm": "Arial", "mathtext.it": "Arial:italic"})
fig, ax = plt.subplots(figsize=(10.5, 4.6)); ax.set_xlim(0, 105); ax.set_ylim(0, 46); ax.axis("off")


def box(x, y, w, h, titulo, eq, ref=None, fs=12):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0", fc="white", ec="black", lw=1.1))
    if titulo:
        ax.text(x, y + h/2 - 1.0, titulo, ha="center", va="top", fontsize=9)
    ax.text(x, y - 0.9 if titulo else y, eq, ha="center", va="center", fontsize=fs)
    if ref:
        ax.text(x, y - h/2 + 0.5, ref, ha="center", va="bottom", fontsize=7.5, color="0.35")


def summ(x, y, r=1.8):
    ax.add_patch(Circle((x, y), r, fc="white", ec="black", lw=1.1)); ax.text(x, y, "Σ", ha="center", va="center")


def arrow(pts, label=None, lpos=None, va="bottom", fs=9.5):
    for (x0, y0), (x1, y1) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x0, x1], [y0, y1], color="black", lw=1.1)
    ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="-|>", lw=1.1, color="black",
                                                                  shrinkA=0, shrinkB=0, mutation_scale=12))
    if label:
        ax.text(*lpos, label, ha="center", va=va, fontsize=fs)


# ---------------- (a) malha com L(s)
y = 32
ax.text(2, 44.5, "(a) Malha com o ganho de malha L(s)", ha="left", va="top", fontsize=10, weight="bold")
ax.text(5, y + 1.0, r"$\Delta N(s)$", ha="center", va="bottom")
arrow([(1, y), (11, y)])
box(17, y, 12, 8, "Distúrbio", r"$K_n$", "Eq. (3.17)")
arrow([(23, y), (37.2, y)])
ax.text(35.3, y + 0.6, "+", ha="center", va="bottom", fontsize=11)
summ(39, y)
arrow([(40.8, y), (60, y)], r"$\Delta P(s)$", (49, y + 0.6))
# realimentação: derivação em x = 54, entra no bloco pela direita, sai pela esquerda e sobe ao Σ
ax.plot([54, 54], [y, 15], color="black", lw=1.1)
ax.plot(54, y, "ko", ms=3)
arrow([(54, 15), (48, 15)])
box(39, 15, 18, 10, None, r"$L(s) = \frac{G_c(s)\,|K_g|}{\tau_a\,s + 1}$", fs=11)
arrow([(30, 15), (25, 15), (25, 24), (39, 24), (39, y - 1.8)])
ax.text(41.2, y - 3.6, "−", ha="center", va="center", fontsize=13)
ax.text(39, 8.6, "controlador × válvula × planta (em módulo):", ha="center", va="top", fontsize=8.5, color="0.25")
ax.text(39, 5.9, "o ganho de uma volta completa pela malha", ha="center", va="top", fontsize=8.5, color="0.25")

# ---------------- (b) bloco equivalente
ax.plot([63, 63], [3, 45], color="0.7", lw=0.8, ls=":")
ax.text(66, 44.5, "(b) Bloco equivalente", ha="left", va="top", fontsize=10, weight="bold")
ax.text(70, y + 1.0, r"$\Delta N(s)$", ha="center", va="bottom")
arrow([(65, y), (75, y)])
box(85, y, 20, 11, None, r"$T_n(s) = \frac{K_n}{1 + L(s)}$", fs=12)
arrow([(95, y), (104, y)], r"$\Delta P(s)$", (100, y + 0.6))
ax.text(85, y - 7, "Eq. (3.25)", ha="center", va="top", fontsize=7.5, color="0.35")
ax.text(85, 17, "o efeito de um bico na pressão\nfica dividido por 1 + L(s)", ha="center", va="top",
        fontsize=8.5, color="0.25")

fig.savefig(Path(__file__).with_name("fig_malha_L.png"), dpi=250, bbox_inches="tight", facecolor="white")
