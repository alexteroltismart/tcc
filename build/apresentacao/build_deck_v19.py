"""Monta a apresentação da banca (TCC v19) sobre o modelo institucional da UNEMAT.
v19: sintonia por alocação de polos, malha em Laplace com duas entradas (superposição),
controlador com leitura em tempo real (sem amostragem). Versão anterior: build_deck_v15.py."""
import copy
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt, Emu

AQUI = Path(__file__).parent
TCC = Path("D:/tech/tcc")
EQ = AQUI / "eq"; EQ.mkdir(exist_ok=True)

NAVY = RGBColor(0x1B, 0x35, 0x57)
GREEN = RGBColor(0x1E, 0x7B, 0x3C)
ORANGE = RGBColor(0xE8, 0x8A, 0x0C)
INK = RGBColor(0x26, 0x2B, 0x33)
MUTED = RGBColor(0x5B, 0x66, 0x70)
TINT = RGBColor(0xEE, 0xF4, 0xF8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Calibri"

prs = Presentation(str(AQUI / "base.pptx"))
SW, SH = prs.slide_width, prs.slide_height
slides = list(prs.slides)
assert len(slides) == 20, len(slides)
cont = iter(slides[1:])


# ---------------------------------------------------------------- helpers
def eq_png(nome, tex, size=22, color="#1B3557"):
    """Equação LaTeX (mathtext) → PNG transparente; devolve (caminho, largura_pol, altura_pol)."""
    plt.rcParams["mathtext.fontset"] = "cm"
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, f"${tex}$", fontsize=size, color=color)
    out = EQ / f"{nome}.png"
    plt.rcParams["mathtext.fontset"] = "cm"
    fig.savefig(out, dpi=300, transparent=True, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    from PIL import Image
    w, h = Image.open(out).size
    return out, w / 300, h / 300


def add_eq(slide, nome, tex, x, y, size=22, max_w=None, color="#1B3557"):
    p, w, h = eq_png(nome, tex, size, color)
    if max_w and w > max_w:
        h, w = h * max_w / w, max_w
    pic = slide.shapes.add_picture(str(p), Inches(x), Inches(y), Inches(w), Inches(h))
    pic.name = f"Eq {nome}"
    return w, h


def _bullet(p, char="•", color=GREEN, level=0):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(Emu(Inches(0.28 + 0.3 * level))))
    pPr.set("indent", str(-Emu(Inches(0.24))))
    for tag in ("a:buNone", "a:buChar", "a:buAutoNum"):
        for el in pPr.findall(qn(tag)):
            pPr.remove(el)
    buClr = pPr.makeelement(qn("a:buClr"), {})
    srgb = buClr.makeelement(qn("a:srgbClr"), {"val": str(color)})
    buClr.append(srgb)
    pPr.append(buClr)
    bu = pPr.makeelement(qn("a:buChar"), {"char": char})
    pPr.append(bu)


def text(slide, x, y, w, h, items, size=16, color=INK, anchor=MSO_ANCHOR.TOP, name="Texto", align=PP_ALIGN.LEFT):
    """items: lista de str ou dicts {t, b, c, s, bullet, runs, space}."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    first = True
    for it in items:
        if isinstance(it, str):
            it = {"t": it}
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = it.get("align", align)
        p.space_after = Pt(it.get("space", 6))
        runs = it.get("runs") or [(it.get("t", ""), it.get("b", False), it.get("c", color))]
        for rt, rb, rc in runs:
            r = p.add_run()
            r.text = rt
            f = r.font
            f.name = FONT; f.size = Pt(it.get("s", size)); f.bold = rb; f.color.rgb = rc
            f.italic = it.get("i", False)
        if it.get("bullet"):
            _bullet(p, level=it.get("level", 0))
    return tb


def title(slide, t, sub=None):
    text(slide, 0.6, 1.62, 12.1, 0.62, [{"t": t, "b": True, "s": 30, "c": NAVY}], name="Título",
         anchor=MSO_ANCHOR.MIDDLE)
    if sub:
        text(slide, 0.62, 2.22, 12.0, 0.4, [{"t": sub, "s": 16, "c": MUTED, "i": True}], name="Subtítulo")


def box(slide, x, y, w, h, fill=TINT, name="Cartão", line=None):
    s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.name = name
    s.adjustments[0] = 0.06
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line:
        s.line.color.rgb = line; s.line.width = Pt(1.25)
    else:
        s.line.fill.background()
    s.shadow.inherit = False
    return s


def stat(slide, x, y, w, big, label, color=GREEN, big_size=40):
    box(slide, x, y, w, 1.35, name=f"Destaque {label[:12]}")
    text(slide, x + 0.1, y + 0.08, w - 0.2, 0.75, [{"t": big, "b": True, "s": big_size, "c": color, "align": PP_ALIGN.CENTER}],
         name="Número", anchor=MSO_ANCHOR.MIDDLE)
    text(slide, x + 0.1, y + 0.82, w - 0.2, 0.48, [{"t": label, "s": 13, "c": MUTED, "align": PP_ALIGN.CENTER}],
         name="Rótulo")


def image(slide, path, x, y, w=None, h=None, name="Figura"):
    from PIL import Image
    iw, ih = Image.open(path).size
    if w and not h:
        h = w * ih / iw
    elif h and not w:
        w = h * iw / ih
    pic = slide.shapes.add_picture(str(path), Inches(x), Inches(y), Inches(w), Inches(h))
    pic.name = name
    return w, h


def caption(slide, x, y, w, t):
    text(slide, x, y, w, 0.3, [{"t": t, "s": 11, "c": MUTED, "i": True}], name="Fonte")


def style_chart(ch, legend=True):
    ch.font.name = FONT; ch.font.size = Pt(12); ch.font.color.rgb = INK
    ch.has_legend = legend
    if legend:
        ch.legend.position = XL_LEGEND_POSITION.BOTTOM
        ch.legend.include_in_layout = False
        ch.legend.font.size = Pt(12)
    va = ch.value_axis
    va.has_major_gridlines = True
    va.major_gridlines.format.line.color.rgb = RGBColor(0xDD, 0xE3, 0xE8)
    va.format.line.fill.background()
    va.tick_labels.font.size = Pt(12); va.tick_labels.font.color.rgb = MUTED
    ca = ch.category_axis
    ca.tick_labels.font.size = Pt(12); ca.tick_labels.font.color.rgb = MUTED
    ca.format.line.color.rgb = RGBColor(0xBB, 0xC4, 0xCC)


def notes(slide, t):
    slide.notes_slide.notes_text_frame.text = t



def _runs_simbolo(par, s, cor, bold):
    """'P_{ref}' -> runs com subscrito; texto normal sem '_'."""
    import re as _re
    pos = 0
    for m in _re.finditer(r"_\{([^}]*)\}|_(\w)", s):
        if m.start() > pos:
            r = par.add_run(); r.text = s[pos:m.start()]
            r.font.size = Pt(11); r.font.bold = bold; r.font.color.rgb = cor; r.font.name = FONT
            r.font.italic = bold
        r = par.add_run(); r.text = m.group(1) or m.group(2)
        r.font.size = Pt(11); r.font.bold = bold; r.font.color.rgb = cor; r.font.name = FONT; r.font.italic = bold
        r.font._element.set("baseline", "-25000")
        pos = m.end()
    if pos < len(s):
        r = par.add_run(); r.text = s[pos:]
        r.font.size = Pt(11); r.font.bold = bold; r.font.color.rgb = cor; r.font.name = FONT
        r.font.italic = bold and len(s) < 12


def simbolos(slide, pares, y=6.98, x=0.6, w=12.15):
    """Faixa no rodapé com o significado de cada símbolo novo (Lista de Símbolos do TCC)."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(0.45))
    tb.name = "Símbolos"
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.04); tf.margin_top = tf.margin_bottom = Inches(0)
    par = tf.paragraphs[0]
    r = par.add_run(); r.text = "Símbolos: "; r.font.size = Pt(11); r.font.bold = True
    r.font.color.rgb = GREEN; r.font.name = FONT
    for i, (sim, sig) in enumerate(pares):
        if i:
            r = par.add_run(); r.text = "  ·  "; r.font.size = Pt(11); r.font.color.rgb = MUTED; r.font.name = FONT
        _runs_simbolo(par, sim, NAVY, True)
        r = par.add_run(); r.text = " – " + sig; r.font.size = Pt(11); r.font.color.rgb = MUTED; r.font.name = FONT
    return tb

IMG = TCC / "img"; FIGS = TCC / "simulacao/figuras"; BFIG = TCC / "build/fig"

# ================================================================ 1. título
s = next(cont)
text(s, 0.9, 1.95, 11.5, 1.5, [{"t": "Modelagem de sistema de controle para pulverização agrícola de precisão",
                                "b": True, "s": 36, "c": NAVY}], name="Título", anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.9, 3.45, 11.5, 0.6, [{"t": "Controle da pressão de uma barra bico a bico com válvula de alívio, modelo de resistência fluídica e simulação",
                                "s": 20, "c": GREEN, "i": True}], name="Subtítulo")
text(s, 0.9, 4.55, 7.5, 1.9, [
    {"t": "Alex de Jesus Terolti", "b": True, "s": 22, "c": INK},
    {"t": "Orientador: Prof. Dr. Rogério Bastos Quirino", "s": 18, "c": INK},
    {"t": "Bacharelado em Engenharia Elétrica · UNEMAT, câmpus de Sinop", "s": 16, "c": MUTED},
    {"t": "Trabalho de Conclusão de Curso II", "s": 16, "c": MUTED}], name="Autor")
notes(s, "Apresentar-se, o orientador e o tema: manter a pressão de uma barra de pulverização bico a bico usando uma válvula de alívio, com um modelo simples e controladores clássicos, tudo em simulação.")

# ================================================================ 2. problema
s = next(cont)
title(s, "O problema: a pressão muda quando os bicos trocam")
text(s, 0.6, 2.65, 5.6, 4.4, [
    {"t": "Na pulverização localizada, cada bico abre e fecha sozinho.", "bullet": True},
    {"t": "Com alimentação em série, uma mangueira alimenta todos os bicos: quando bicos fecham, sobra líquido e a pressão sobe.", "bullet": True},
    {"t": "Na bancada de Rosa, Terra e Drews Jr (2019), a pressão foi de 3,57 para 5,58 kgf/cm² (+56%) ao fechar seis dos sete bicos.", "bullet": True},
    {"t": "Pressão errada muda a vazão de cada bico (q ∝ √P) e o tamanho das gotas: sobredose, subdose e deriva.", "bullet": True},
], size=17)
image(s, IMG / "fig05_ensaio.png", 7.55, 2.45, h=4.45, name="Ensaio de regulação")
caption(s, 7.3, 6.93, 5.5, "Ensaio de regulação da pressão pela válvula de alívio. Fonte: Rosa, Terra e Drews Jr (2019).")
simbolos(s, [('q', 'vazão de um bico'), ('P', 'pressão manométrica na barra')], w=6.4)
notes(s, "Motivação. O controle bico a bico economiza produto, mas cada troca de bico muda a pressão dos outros. A figura é o ensaio da bancada de referência: fechando três bicos a pressão sobe de 4,0 para 5,8, e abrindo a válvula à mão ela volta; com a válvula fechada, de 7 para 1 bico, a pressão sobe 56%. Como a vazão do bico varia com a raiz da pressão, isso muda a dose.")

# ================================================================ 3. objetivo e hipótese
s = next(cont)
title(s, "Objetivo e hipótese")
box(s, 0.6, 2.55, 7.3, 1.75, name="Hipótese")
text(s, 0.85, 2.65, 6.9, 1.6, [
    {"t": "Hipótese", "b": True, "s": 18, "c": NAVY},
    {"t": "Um modelo de resistências fluídicas, com os bicos em paralelo, a curva da bomba e a válvula de alívio, mais a dinâmica da válvula, basta para projetar um controlador simples que mantenha a pressão dentro de ±10% da referência.", "s": 16}],
    name="Texto hipótese")
text(s, 0.6, 4.5, 7.4, 2.6, [
    {"t": "Objetivos específicos", "b": True, "s": 18, "c": NAVY},
    {"t": "Modelar pressão × vazão × número de bicos e comparar com os dados publicados", "bullet": True},
    {"t": "Acrescentar a dinâmica da válvula (curso e velocidade limitados)", "bullet": True},
    {"t": "Sintonizar P e PI por alocação de polos e acrescentar o feedforward", "bullet": True},
    {"t": "Comparar os controladores em simulação", "bullet": True}], size=16)
stat(s, 8.5, 2.55, 4.2, "±10%", "tolerância de pressão adotada\nISO 16122-2:2015, item 4.5.4", color=ORANGE, big_size=54)
stat(s, 8.5, 4.15, 4.2, "≈ ±5%", "na vazão de cada bico, porque\nq = K·√P (√0,9 ≈ 0,95)", color=GREEN, big_size=44)
text(s, 8.5, 5.75, 4.2, 1.2, [{"t": "Tudo em simulação, com parâmetros ajustados à bancada de 7 bicos de Rosa, Terra e Drews Jr (2019).", "s": 14, "c": MUTED, "i": True}],
     name="Escopo")
simbolos(s, [('K', 'constante de vazão de um bico')])
notes(s, "A hipótese é que um modelo simples basta para projetar um controlador que segure a pressão dentro de ±10%, a tolerância da norma de inspeção de pulverizadores. ±10% na pressão dá cerca de ±5% na vazão do bico.")

# ================================================================ 4. roteiro
s = next(cont)
title(s, "Roteiro do trabalho em sete etapas")
w, h = image(s, BFIG / "fig_etapas.png", 0.6, 2.45, h=4.6, name="Figura etapas")
text(s, 0.75 + w, 2.6, 12.7 - (0.75 + w), 4.4, [
    {"t": "Cada etapa entrega a entrada da seguinte.", "b": True, "s": 17, "c": NAVY},
    {"t": "O modelo estático é a base: dá a pressão para qualquer número de bicos e abertura da válvula.", "bullet": True},
    {"t": "Ele é reaproveitado no simulador e no projeto do controle.", "bullet": True},
    {"t": "Tudo roda num único programa em Python (numpy e matplotlib), com conferências automáticas.", "bullet": True}], size=16)
notes(s, "Esta é a ordem da apresentação: dados da bancada, modelo estático, modelo dinâmico, abertura de equilíbrio e ganho da planta, controladores e sintonia, simulação e avaliação. O programa em Python executa essas etapas em sequência.")

# ================================================================ 5. bancada
s = next(cont)
title(s, "Bancada de referência (Rosa, Terra e Drews Jr, 2019)")
image(s, IMG / "overview barra.png", 0.6, 2.55, w=6.2, name="Foto bancada")
caption(s, 0.6, 2.55 + 6.2 / 3.69 + 0.02, 6.2, "Barra de 5 m com sete bicos. Fonte: Rosa, Terra e Drews Jr (2019).")
image(s, IMG / "fig04_fluxograma.png", 0.6, 4.6, w=4.3, name="Fluxograma bancada")
caption(s, 0.6, 4.6 + 4.3 / 2.19 + 0.02, 4.8, "Fluxograma de processo. Fonte: Rosa, Terra e Drews Jr (2019).")
text(s, 7.2, 2.5, 5.6, 1.6, [
    {"t": "Bomba de pistão de 14 L/min com válvula de mola (PCV)", "bullet": True, "space": 3},
    {"t": "Sete bicos FanTip 0,2/110° com solenoide", "bullet": True, "space": 3},
    {"t": "Válvula agulha de alívio (HV) com servomotor: o atuador", "bullet": True, "space": 3}], size=15)
dados = [("n", "P [kgf/cm²]", "Q [L/min]", "P/Q²"),
         ("7", "3,57", "5,60", "0,114"), ("6", "3,88", "5,07", "0,151"), ("5", "4,24", "4,40", "0,219"),
         ("4", "4,64", "3,60", "0,358"), ("3", "4,96", "2,80", "0,633"), ("2", "5,27", "2,00", "1,318"),
         ("1", "5,58", "1,00", "5,580")]
gt = s.shapes.add_table(len(dados), 4, Inches(7.2), Inches(4.12), Inches(5.55), Inches(2.6))
gt.name = "Tabela dados Rosa"
tab = gt.table
for c, wc in enumerate((0.85, 1.75, 1.55, 1.4)):
    tab.columns[c].width = Inches(wc)
for r, linha in enumerate(dados):
    tab.rows[r].height = Inches(0.32)
    for c, v in enumerate(linha):
        cell = tab.cell(r, c); cell.text = v
        cell.margin_top = cell.margin_bottom = Inches(0.02)
        p = cell.text_frame.paragraphs[0]; rn = p.runs[0]
        rn.font.size = Pt(13); rn.font.name = FONT; rn.font.bold = (r == 0)
        rn.font.color.rgb = WHITE if r == 0 else INK
        p.alignment = PP_ALIGN.CENTER
        cell.fill.solid(); cell.fill.fore_color.rgb = NAVY if r == 0 else (TINT if r % 2 else WHITE)
caption(s, 7.2, 6.77, 5.55, "Válvula de alívio fechada. Fonte: Rosa, Terra e Drews Jr (2019), Tabela 1.")
simbolos(s, [('n', 'número de bicos abertos'), ('Q', 'vazão volumétrica'), ('P/Q²', 'resistência fluídica equivalente (R_{F})')])
notes(s, "A bancada foi escolhida porque é uma barra bico a bico em série, tem dados publicados de pressão e vazão e já usa uma válvula de alívio. A tabela traz os dados usados para ajustar o modelo: com a válvula fechada, fechando bicos a pressão sobe e a vazão cai, e a resistência P/Q² cresce muito depressa. Os autores ajustaram a válvula à mão e deixaram o controle automático como trabalho futuro.")

# ================================================================ 6. modelo estático
s = next(cont)
title(s, "Modelo estático: balanço de vazões num nó de pressão")
image(s, BFIG / "fig06.png", 2.35, 2.4, w=8.6, name="Circuito equivalente")
y0 = 2.4 + 8.6 / 6.32 + 0.14
cards = [("Bico (lei de orifício)", "q = K\\sqrt{P}", "K = 0,425 (média da Tabela 1)"),
         ("Fonte (bomba + PCV)", "P = a_2 Q_s^2 + a_1 Q_s + a_0", "mínimos quadrados, R² = 0,9999"),
         ("Válvula de alívio", "Q_v = K_{v,max}\\,\\alpha\\,\\sqrt{P}", "linear na abertura (H5)")]
for i, (cab, tex, rod) in enumerate(cards):
    x = 0.6 + i * 4.1
    box(s, x, y0, 3.9, 1.45, name=f"Cartão {cab}")
    text(s, x + 0.15, y0 + 0.08, 3.6, 0.4, [{"t": cab, "b": True, "s": 15, "c": NAVY}], name="Cabeçalho")
    add_eq(s, f"est{i}", tex, x + 0.2, y0 + 0.48, size=20, max_w=3.5)
    text(s, x + 0.15, y0 + 1.04, 3.6, 0.4, [{"t": rod, "s": 12, "c": MUTED}], name="Nota")
yb = y0 + 1.57
box(s, 0.6, yb, 12.1, 1.38, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Modelo explícito")
text(s, 0.8, yb + 0.1, 4.6, 0.62, [{"t": "Modelo estático em forma explícita (Eq. 3.11)", "b": True, "s": 15, "c": GREEN},
                                   {"t": "entra = sai no nó, resolvido para P", "s": 12, "c": MUTED}], name="Modelo explícito texto")
add_eq(s, "cap_saida", "C(n,\\alpha) = n\\,K + K_{v,max}\\,\\alpha", 0.95, yb + 0.8, size=20, max_w=4.3)
add_eq(s, "p_explicito", "P(n,\\alpha) = \\left[\\frac{a_1C + \\sqrt{a_1^2C^2 + 4a_0\\left(1 - a_2C^2\\right)}}{2\\left(1 - a_2C^2\\right)}\\right]^2",
       5.75, yb + 0.12, size=21, max_w=6.8)
simbolos(s, [('C', 'capacidade total de saída (bicos abertos mais válvula)'), ('Q_{s}', 'vazão fornecida pela fonte'), ('a_{2}, a_{1}, a_{0}', 'coeficientes da curva da fonte'), ('Q_{v}', 'vazão desviada pela válvula de alívio'), ('K_{v,max}', 'constante de vazão da válvula toda aberta'), ('α', 'abertura da válvula (0 a 1)')])
notes(s, "Três caminhos se encontram num único nó de pressão: a fonte empurra líquido, os bicos e a válvula deixam sair. Em regime, entra = sai. Juntando bicos e válvula na capacidade de saída C e substituindo na curva da fonte, sai uma equação de segundo grau em raiz de P; a fórmula de Bhaskara dá a pressão de forma explícita, a Equação 3.11. A pressão só depende de C: quando bicos fecham, a válvula abre até C voltar ao valor de antes. Hipóteses: escoamento permanente, perda na barra desprezível, bicos iguais, fonte de segundo grau, válvula linear.")

# ================================================================ 7. R1/n²
s = next(cont)
title(s, "Resistência equivalente da barra: modelo R₁/n²")
box(s, 0.6, 2.45, 6.1, 1.42, name="Modelo deste trabalho")
text(s, 0.8, 2.5, 5.8, 0.36, [{"t": "Este trabalho: modelo físico, 1 parâmetro (K)", "b": True, "s": 14, "c": GREEN}], name="Cab modelo")
add_eq(s, "r1n2", "R_{eq}(n) = \\frac{R_1}{n^2}, \\qquad R_1 = \\frac{1}{K^2}", 0.95, 2.92, size=24, max_w=5.4)
box(s, 0.6, 4.0, 6.1, 1.25, name="Modelo de Rosa et al.")
text(s, 0.8, 4.05, 5.8, 0.36, [{"t": "Rosa, Terra e Drews Jr (2019): ajuste empírico, 4 coeficientes", "b": True, "s": 14, "c": ORANGE}], name="Cab Rosa")
add_eq(s, "rosa", "R_F(n) = 42{,}59\\,e^{-2{,}335\\,n} + 2{,}307\\,e^{-0{,}4591\\,n}", 0.95, 4.5, size=22, max_w=5.6)
text(s, 0.6, 5.4, 6.1, 1.5, [
    {"t": "n bicos iguais em paralelo: a resistência de um bico dividida por n²; dobrar os bicos divide a resistência por quatro", "bullet": True},
    {"t": "Um parâmetro com significado físico no lugar de quatro coeficientes ajustados", "bullet": True}], size=15)
image(s, FIGS / "a_resistencia_n.png", 7.45, 2.45, h=3.2, name="Gráfico resistência")
stat(s, 6.95, 5.75, 2.8, "5,9%", "erro máximo do modelo R₁/n²", color=GREEN, big_size=30)
stat(s, 9.95, 5.75, 2.8, "18,5%", "erro da fórmula empírica (n = 7)", color=ORANGE, big_size=30)
simbolos(s, [('R_{eq}(n)', 'resistência equivalente da barra com n bicos abertos'), ('R_{1}', 'resistência de um bico'), ('R_{F}(n)', 'resistência fluídica da barra pela fórmula empírica de Rosa et al. (Eq. 2.5)'), ('e', 'número de Euler (base exponencial)')])
notes(s, "A contribuição do modelo estático: com n bicos em paralelo, a resistência equivalente é a de um bico dividida por n ao quadrado. Embaixo está a fórmula de Rosa, Terra e Drews Junior: uma soma de duas exponenciais, com quatro coeficientes ajustados sem significado físico. O modelo deste trabalho usa um único parâmetro físico. O erro relativo máximo foi 5,9%, contra 18,5% da fórmula empírica.")

# ================================================================ 8. validação
s = next(cont)
title(s, "O modelo estático reproduz os dados medidos")
for i, (big, lab, cor) in enumerate([("0,7%", "erro máximo na pressão", GREEN), ("2,3%", "erro máximo na vazão", GREEN),
                                     ("0,9% | 2,7%", "validação cruzada (deixa um de fora)", NAVY)]):
    stat(s, 0.6, 2.55 + i * 1.5, 4.0, big, lab, color=cor, big_size=36 if i < 2 else 30)
image(s, FIGS / "b_fonte_carga.png", 4.95, 2.5, h=3.75, name="Fonte e carga")
text(s, 10.05, 2.6, 2.75, 3.6, [
    {"t": "Regra de projeto", "b": True, "s": 16, "c": NAVY},
    {"t": "A válvula de alívio só baixa a pressão: a referência tem de ficar abaixo do que a fonte sustenta com 7 bicos (3,56 kgf/cm²).", "s": 14},
    {"t": "Adotado: Pref = 3,5 kgf/cm²", "b": True, "s": 15, "c": ORANGE}], name="Regra de projeto")
caption(s, 4.95, 6.3, 5.0, "Cruzamento da curva da fonte com as curvas de carga = ponto de operação.")
simbolos(s, [('P_{ref}', 'pressão de referência (valor desejado)')])
notes(s, "Com a constante do bico e a curva da fonte, o modelo reproduziu os sete pontos com erro de até 0,7% na pressão e 2,3% na vazão; prevendo cada ponto sem usá-lo no ajuste, 0,9% e 2,7%. Uma consequência: como a válvula só alivia, a referência tem de ficar abaixo de 3,56; foi escolhido 3,5.")

# ================================================================ 9. modelo dinâmico
s = next(cont)
title(s, "Modelo dinâmico: a pressão é instantânea, a válvula demora")
# coluna esquerda: H6
box(s, 0.6, 2.45, 6.35, 2.12, name="H6")
text(s, 0.82, 2.56, 6.0, 0.4, [{"t": "1. Pressão instantânea (hipótese H6)", "b": True, "s": 16, "c": NAVY}], name="Cab H6")
add_eq(s, "merritt", "\\sum Q_{ent} - \\sum Q_{sai} = \\frac{V}{\\beta}\\,\\frac{dP}{dt}", 0.95, 3.0, size=22, max_w=4.2)
text(s, 0.82, 3.72, 6.0, 0.95, [
    {"t": "Mangueira curta (5 m) e cheia: V/β pequeno, a pressão acompanha a válvula quase na hora (Merritt, 1967, p. 53). A cada instante, P = equilíbrio do modelo estático.", "s": 13, "space": 2},
    {"t": "Conferido com a mangueira modelada: diferença ≤ 0,4 ponto percentual.", "s": 13, "c": GREEN, "b": True}], name="Texto H6")
# coluna esquerda: válvula
box(s, 0.6, 4.68, 6.35, 2.2, name="Válvula")
text(s, 0.82, 4.74, 6.0, 0.4, [{"t": "2. Válvula de primeira ordem com velocidade limitada", "b": True, "s": 16, "c": NAVY}], name="Cab válvula")
add_eq(s, "valvula", "\\frac{d\\alpha}{dt} = \\frac{\\alpha_c - \\alpha}{\\tau_a}, \\qquad \\left|\\frac{d\\alpha}{dt}\\right| \\leq \\omega_{max}, \\qquad 0 \\leq \\alpha \\leq 1", 0.95, 5.16, size=20, max_w=5.8)
text(s, 0.82, 5.92, 6.0, 0.95, [
    {"t": "Longe do comando: rampa, a 0,5 por segundo. Perto: aproximação exponencial, τa = 0,2 s.", "s": 13, "space": 2},
    {"t": "τa e ωmax são estimados (a bancada não informa a velocidade da válvula).", "s": 13, "c": ORANGE, "i": True}], name="Texto válvula")
# coluna direita: gráfico + passo a passo
image(s, IMG / "valv agulha.png", 8.05, 2.45, h=3.2, name="Válvula agulha")
caption(s, 7.4, 5.7, 5.4, "Válvula agulha de 1/4\" com servomotor (o atuador). Fonte: Rosa, Terra e Drews Jr (2019).")
box(s, 7.25, 6.2, 5.5, 0.85, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Passo a passo")
text(s, 7.4, 6.22, 5.25, 0.8, [
    {"t": "A cada 1 ms (Euler):", "b": True, "s": 13, "c": GREEN, "space": 1},
    {"t": "controlador lê P em tempo real → válvula: αk+1 = αk + Δt·(dα/dt) → pressão pela bissecção", "s": 13}],
    name="Texto passo a passo", anchor=MSO_ANCHOR.MIDDLE)
simbolos(s, [('ΣQ_{ent}, ΣQ_{sai}', 'vazões que entram e saem da linha'), ('V', 'volume da linha'), ('β', 'módulo de compressibilidade efetivo'), ('α_{c}', 'abertura comandada'), ('τ_{a}, ω_{max}', 'constante de tempo e velocidade máxima do atuador'), ('Δt', 'passo da simulação')])
notes(s, "A dinâmica tem duas partes. Primeiro, a pressão: pela continuidade com compressibilidade, a pressão só demora para mudar por causa do termo V sobre beta, a capacitância da linha. Como a mangueira é curta e cheia, esse termo é pequeno e a pressão foi tratada como instantânea; conferi com um modelo que inclui a mangueira e a diferença foi de no máximo 0,4 ponto percentual. Segundo, a válvula: ela segue um sistema de primeira ordem, com constante de tempo de 0,2 segundo, mas o motor tem velocidade máxima de 0,5 por segundo. Por exemplo, quando três bicos fecham, a abertura precisa subir 0,36: a válvula anda meio segundo em rampa e depois se aproxima do comando, cerca de 0,7 segundo só para ela chegar. Esses dois parâmetros são estimados. A simulação avança de 1 em 1 milissegundo pelo método de Euler, e o controlador lê a pressão em todo passo, em tempo real.")

# ================================================================ 10. estratégia de controle
s = next(cont)
title(s, "Estratégia de controle: P, PI e PI com feedforward")
image(s, BFIG / "fig07.png", 0.6, 2.45, w=7.4, name="Diagrama de blocos")
text(s, 0.6, 2.45 + 7.4 / 2.32 + 0.1, 7.4, 1.0, [
    {"t": "Erro e = P − Pref: abrir a válvula baixa a pressão. Sensor e controlador em tempo real (sem amostragem); anti-windup por integração condicional no limite de posição (Fernandes; Goldemberg, 2001).",
     "s": 13, "c": MUTED}], name="Nota erro")
for i, (cab, tex, rod, cor) in enumerate([
        ("P", "\\alpha_c = \\alpha_0 + K_c\\,e", "abertura fixa α₀ = 0,023", GREEN),
        ("PI", "\\alpha_c = \\alpha_0 + K_c\\left(e + \\frac{1}{T_i}\\int e\\,dt\\right)", "a integral zera o erro", NAVY),
        ("PI + FF", "\\alpha_c = \\alpha_{ff}(n) + K_c\\left(e + \\frac{1}{T_i}\\int e\\,dt\\right)", "abertura antecipada pelo nº de bicos", ORANGE)]):
    y = 2.5 + i * 1.5
    box(s, 8.3, y, 4.45, 1.35, name=f"Cartão {cab}")
    text(s, 8.45, y + 0.06, 4.2, 0.35, [{"t": cab, "b": True, "s": 16, "c": cor}], name="Cab")
    add_eq(s, f"ctl{i}", tex, 8.5, y + 0.45, size=17, max_w=4.1)
    text(s, 8.45, y + 0.98, 4.2, 0.33, [{"t": rod, "s": 12, "c": MUTED}], name="Nota")
simbolos(s, [('e', 'erro de pressão, P − P_{ref}'), ('K_{c}, T_{i}', 'ganho proporcional e tempo integral'), ('α_{0}', 'abertura fixa inicial (0,023)'), ('α_{ff}', 'abertura de equilíbrio (feedforward)')])
notes(s, "A pressão é a variável controlada, a abertura da válvula a manipulada e o número de bicos a perturbação. Três controladores, cada um acrescentando algo: P, PI e PI com feedforward, em que a abertura antecipada vem do próprio modelo estático. O sensor e o controlador leem a pressão em tempo real. A ação derivativa ficou de fora: amplifica o ruído, o salto de pressão de cada troca vira um pico no comando, e o PI já coloca os dois polos onde se quer.")

# ================================================================ 11. alpha_ff e Kg
s = next(cont)
title(s, "O modelo estático dá o feedforward e o ganho da planta")
box(s, 0.6, 2.55, 6.0, 4.45, name="Alpha ff")
text(s, 0.85, 2.65, 5.6, 0.45, [{"t": "Abertura de equilíbrio", "b": True, "s": 18, "c": NAVY}], name="Cab aff")
add_eq(s, "aff", "\\alpha_{ff}(n) = \\frac{1}{K_{v,max}}\\left[\\frac{Q_s(P_{ref})}{\\sqrt{P_{ref}}} - n\\,K\\right]", 0.9, 3.15, size=26, max_w=5.4)
text(s, 0.85, 4.35, 5.6, 2.5, [
    {"t": "Uma reta: cada bico que fecha pede +0,121 de abertura", "bullet": True},
    {"t": "7 bicos: 0,023 · 1 bico: 0,752", "bullet": True},
    {"t": "É o compensador ideal Gd/Gp em regime: −Kn/Kg (Liu et al., 2018)", "bullet": True}], size=15)
box(s, 6.95, 2.55, 5.8, 4.45, name="Kg")
text(s, 7.2, 2.65, 5.4, 0.45, [{"t": "Ganho da planta e do distúrbio", "b": True, "s": 18, "c": NAVY}], name="Cab kg")
add_eq(s, "dpdc", "\\frac{dP}{dC} = \\frac{-\\sqrt{P}}{\\frac{C}{2\\sqrt{P}} - \\frac{dQ_s}{dP}} = -0{,}760", 7.25, 3.1, size=22, max_w=5.3)
add_eq(s, "kg", "K_g = K_{v,max}\\,\\frac{dP}{dC} = -2{,}66", 7.25, 4.05, size=22, max_w=5.3, color="#E88A0C")
add_eq(s, "kn", "K_n = K\\,\\frac{dP}{dC} = -0{,}323", 7.25, 4.65, size=22, max_w=5.3, color="#E88A0C")
text(s, 7.2, 5.35, 5.4, 1.6, [
    {"t": "Derivada implícita do equilíbrio do nó (Eq. 3.19)", "bullet": True},
    {"t": "Iguais para qualquer número de bicos: uma única sintonia serve para todos os casos", "bullet": True, "b": True}], size=15)
simbolos(s, [('K_{g}', 'ganho da planta (pressão por unidade de abertura)'), ('K_{n}', 'ganho do distúrbio (pressão por bico)'), ('C', 'capacidade de saída'), ('G_{d}/G_{p}', 'efeito do distúrbio / efeito do comando')])
notes(s, "Invertendo o modelo estático com P igual à referência, sai a abertura de equilíbrio para cada número de bicos: uma reta, 0,121 por bico. Esse é o feedforward. Os ganhos saem da derivada implícita do equilíbrio do nó: a pressão só depende da capacidade de saída C, e dP/dC vale −0,760. A válvula entra em C com peso Kv,max e o bico com peso K, então o ganho da planta é −2,66 por unidade de abertura e o do distúrbio é −0,323 por bico. Como o ponto de operação tem sempre a mesma pressão, esses ganhos não dependem do número de bicos, e uma sintonia serve para todos.")

# ================================================================ 12. Laplace: duas entradas e superposição
s = next(cont)
title(s, "Malha em Laplace: referência e bicos, separados e somados")
w12, h12 = image(s, BFIG / "fig12_freq.png", 0.6, 2.4, w=7.3, name="Diagrama em Laplace")
caption(s, 0.6, 2.4 + h12 + 0.02, 7.3, "Malha linearizada em torno de 7 bicos e P = Pref (Figura 13 do TCC).")
yb = 2.4 + h12 + 0.4
box(s, 0.6, yb, 7.3, 6.85 - yb, name="Leitura")
text(s, 0.8, yb + 0.08, 7.0, 6.85 - yb - 0.1, [
    {"t": "Mesmo denominador 1 + L(s): mesmos polos, uma sintonia para as duas entradas", "bullet": True, "s": 13, "space": 2},
    {"t": "P: segue só 69% da mudança de referência e deixa +0,101 por bico", "bullet": True, "s": 13, "space": 2},
    {"t": "PI: erro final zero nas duas; o FF não muda os polos", "bullet": True, "s": 13, "space": 2}], name="Texto leitura")
add_eq(s, "lmalha", "L(s) = \\frac{G_c(s)\\,|K_g|}{\\tau_a s + 1}", 8.3, 2.45, size=22, max_w=4.4)
box(s, 8.2, 3.3, 4.55, 1.05, name="Tr")
text(s, 8.32, 3.33, 4.3, 0.3, [{"t": "Só a referência (ΔN = 0)", "b": True, "s": 13, "c": GREEN}], name="Cab Tr")
add_eq(s, "tr", "T_r(s) = \\frac{\\Delta P}{\\Delta P_{ref}} = \\frac{L}{1 + L}", 8.35, 3.65, size=20, max_w=4.3)
box(s, 8.2, 4.45, 4.55, 1.05, name="Tn")
text(s, 8.32, 4.48, 4.3, 0.3, [{"t": "Só os bicos (ΔPref = 0)", "b": True, "s": 13, "c": ORANGE}], name="Cab Tn")
add_eq(s, "tn", "T_n(s) = \\frac{\\Delta P}{\\Delta N} = \\frac{K_n}{1 + L}", 8.35, 4.8, size=20, max_w=4.3)
box(s, 8.2, 5.6, 4.55, 1.25, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Soma")
text(s, 8.32, 5.63, 4.3, 0.3, [{"t": "Superposição (Ogata, 2010, p. 22)", "b": True, "s": 13, "c": NAVY}], name="Cab soma")
add_eq(s, "soma", "\\Delta P = T_r\\,\\Delta P_{ref} + T_n\\,\\Delta N", 8.35, 6.05, size=21, max_w=4.3)
simbolos(s, [('L(s)', 'ganho de malha'), ('T_{r}, T_{n}', 'resposta da pressão à referência e aos bicos'), ('ΔP_{ref}, ΔN', 'mudança da referência e do nº de bicos'), ('G_{c}(s)', 'controlador')])
notes(s, "Para projetar, a malha foi linearizada em torno de sete bicos e escrita no domínio de Laplace. Ela tem duas entradas: a referência e o número de bicos. Como o modelo linearizado é linear, vale a superposição: calculo o efeito de cada entrada com a outra zerada e somo no fim. A resposta à referência é T_r, igual a L sobre 1 mais L, e a resposta aos bicos é T_n, igual a K_n sobre 1 mais L. O denominador é o mesmo: os polos são os mesmos, então uma única sintonia serve para seguir a referência e para rejeitar os bicos. O P segue só 69% de uma mudança de referência e deixa 0,101 por bico; o PI zera o erro nas duas. O sensor lê em tempo real, então a realimentação é direta.")

# ================================================================ 13. alocação de polos
s = next(cont)
title(s, "Sintonia por alocação de polos")
box(s, 0.6, 2.45, 6.4, 4.4, name="Equações sintonia")
text(s, 0.82, 2.52, 6.0, 0.4, [{"t": "Especificação: ζ = 0,7 e ts = 0,5 s (critério de 2%)", "b": True, "s": 15, "c": NAVY}], name="Cab espec")
add_eq(s, "car", "s^2 + \\frac{1 + K_c|K_g|}{\\tau_a}\\,s + \\frac{K_c|K_g|}{\\tau_a T_i} = s^2 + 2\\zeta\\omega_n s + \\omega_n^2", 0.85, 3.0, size=20, max_w=5.95)
add_eq(s, "wn", "\\omega_n = \\frac{4}{\\zeta\\,t_s} = 11{,}43", 0.85, 3.75, size=20, max_w=2.9)
add_eq(s, "kc", "K_c = \\frac{2\\zeta\\omega_n\\tau_a - 1}{|K_g|} = 0{,}827", 0.85, 4.45, size=20, max_w=3.5)
add_eq(s, "ti", "T_i = \\frac{K_c|K_g|}{\\tau_a\\,\\omega_n^2} = 0{,}084\\ \\mathrm{s}", 0.85, 5.2, size=20, max_w=3.5)
text(s, 4.55, 3.85, 2.35, 2.2, [
    {"t": "Polos do PI", "b": True, "s": 14, "c": GREEN},
    {"t": "−8,0 ± j8,2", "b": True, "s": 20, "c": ORANGE},
    {"t": "O P usa o mesmo Kc", "s": 13, "c": MUTED},
    {"t": "Degrau de referência: zero do PI → sobressinal 10,7%", "s": 13, "c": MUTED}], name="Polos")
text(s, 0.82, 6.05, 6.0, 0.75, [{"t": "Leitura em tempo real: a malha é estável para qualquer Kc > 0; o limite prático é a velocidade da válvula e o ruído.", "s": 13, "c": MUTED, "i": True}], name="Nota estabilidade")
image(s, FIGS / "g_funcao_transferencia.png", 7.45, 2.42, h=4.45, name="FT x simulador")
simbolos(s, [('ζ, ω_{n}', 'amortecimento e frequência natural'), ('t_{s}', 'tempo de acomodação (2%)'), ('τ_{a}', 'constante de tempo da válvula'), ('s', 'variável de Laplace')])
notes(s, "A sintonia foi feita de trás para frente, por alocação de polos, segundo o Ogata. Escolhi amortecimento 0,7 e acomodação em 0,5 segundo. Igualando a equação característica do PI à forma padrão de segunda ordem, saem Kc igual a 0,827 e Ti igual a 0,084 segundo, com polos em −8 ± j8,2. O P usa o mesmo Kc, para a comparação mostrar só o efeito da ação integral. Para uma mudança de referência, o zero do PI leva o sobressinal a 10,7%. A figura compara a função de transferência com o simulador para um bico fechando: sem o limite de velocidade, o simulador fica em cima da função de transferência; com o limite, a válvula anda em rampa e a correção demora mais.")

# ================================================================ 14. cenários e métricas
s = next(cont)
title(s, "Cenários de simulação e critério de avaliação")
for i, (cab, desc, cor) in enumerate([
        ("C1", "7 → 1 → 7, um bico por vez, a cada 2 s (26 s): toda a faixa de operação", GREEN),
        ("C2", "Degraus de três bicos, como no ensaio de Rosa (14 s)", NAVY),
        ("C3", "Um bico sorteado troca a cada 0,1–0,5 s (20 s, 66 trocas): aplicação localizada", ORANGE)]):
    y = 2.55 + i * 1.45
    box(s, 0.6, y, 6.6, 1.3, name=f"Cenário {cab}")
    text(s, 0.75, y + 0.1, 1.1, 1.1, [{"t": cab, "b": True, "s": 30, "c": cor, "align": PP_ALIGN.CENTER}], anchor=MSO_ANCHOR.MIDDLE, name="Rótulo")
    text(s, 1.95, y + 0.12, 5.1, 1.1, [{"t": desc, "s": 16}], anchor=MSO_ANCHOR.MIDDLE, name="Descrição")
text(s, 7.6, 2.6, 5.2, 4.4, [
    {"t": "Métricas", "b": True, "s": 18, "c": NAVY},
    {"t": "Tempo fora da faixa ±10% (3,15 a 3,85 kgf/cm²)", "bullet": True},
    {"t": "IAE: área entre P e Pref", "bullet": True},
    {"t": "Desvio máximo", "bullet": True},
    {"t": "Acomodação em ±2%", "bullet": True},
    {"t": "Configurações", "b": True, "s": 18, "c": NAVY},
    {"t": "Malha aberta, P, PI e PI+FF", "bullet": True},
    {"t": "C2 e C3 também com a válvula 2× e 4× mais rápida", "bullet": True}], size=16)
simbolos(s, [('IAE', 'integral do erro absoluto'), ('C1, C2, C3', 'cenários de simulação')])
notes(s, "Três cenários, do mais simples ao mais difícil. O critério principal é o tempo fora da faixa de ±10%: com a máquina em velocidade constante, é a fração da área aplicada fora da tolerância.")

# ================================================================ 15. resultados gerais
s = next(cont)
title(s, "Resultados: tempo com a pressão fora da faixa")
cab = ("Cenário", "Configuração", "Tempo fora da faixa", "IAE [kgf/cm²·s]", "Desvio máximo", "Acomodação média (±2%)")
# (valores, colunas em negrito) — mesmo destaque da Tabela 10 do TCC
linhas = [
    (("C1", "Malha aberta", "69,2%", "24,72", "57,8%", "não acomoda (11 de 12)"), ()),
    (("C1", "P", "38,5%", "7,41", "24,7%", "não acomoda (11 de 12)"), ()),
    (("C1", "PI", "0,0%", "0,78", "9,5%", "0,44 s"), (2, 3, 4, 5)),
    (("C1", "PI+FF", "0,0%", "0,86", "9,5%", "0,48 s"), (2, 4)),
    (("C2", "Malha aberta", "85,7%", "18,38", "57,8%", "não acomoda"), ()),
    (("C2", "P", "46,3%", "5,90", "38,9%", "não acomoda"), ()),
    (("C2", "PI", "6,8%", "0,83", "29,7%", "1,02 s"), (2, 3, 5)),
    (("C2", "PI+FF", "6,8%", "0,83", "29,6%", "1,02 s"), (2, 3, 4, 5)),
    (("C3", "Malha aberta", "90,5%", "23,26", "57,8%", "—"), ()),
    (("C3", "P", "50,1%", "7,06", "25,1%", "—"), ()),
    (("C3", "PI", "8,3%", "3,15", "18,8%", "—"), (2, 3, 4)),
    (("C3", "PI+FF", "9,5%", "3,27", "20,6%", "—"), ()),
]
larg = (0.85, 1.35, 1.35, 1.35, 1.25, 2.15)
gt = s.shapes.add_table(len(linhas) + 1, 6, Inches(0.6), Inches(2.45), Inches(sum(larg)), Inches(0.3 * 13))
gt.name = "Tabela 10 desempenho"
tab = gt.table
for c, wc in enumerate(larg):
    tab.columns[c].width = Inches(wc)
cor_cfg = {"Malha aberta": MUTED, "P": GREEN, "PI": ORANGE, "PI+FF": NAVY}
faixa = {"C1": WHITE, "C2": TINT, "C3": WHITE}
for r in range(len(linhas) + 1):
    tab.rows[r].height = Inches(0.36 if r == 0 else 0.29)
    vals, negrito = (cab, range(6)) if r == 0 else linhas[r - 1]
    for c, v in enumerate(vals):
        cell = tab.cell(r, c); cell.text = v
        cell.margin_top = cell.margin_bottom = Inches(0.01)
        cell.margin_left = cell.margin_right = Inches(0.05)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = cell.text_frame.paragraphs[0]; rn = p.runs[0]
        rn.font.name = FONT; rn.font.size = Pt(11.5 if r == 0 else 12.5)
        rn.font.bold = c in negrito
        p.alignment = PP_ALIGN.LEFT if c in (0, 1) else PP_ALIGN.CENTER
        cell.fill.solid()
        if r == 0:
            rn.font.color.rgb = WHITE; cell.fill.fore_color.rgb = NAVY
        else:
            rn.font.color.rgb = cor_cfg[vals[1]] if c == 1 else INK
            if c == 1:
                rn.font.bold = True
            cell.fill.fore_color.rgb = faixa[vals[0]]
caption(s, 0.6, 2.45 + 0.36 + 12 * 0.29 + 0.05, 8.6,
        "Negrito: melhor valor de cada cenário. C3: trocas mais rápidas que a acomodação. Fonte: Tabela 10 do TCC.")
text(s, 9.55, 2.55, 3.25, 4.5, [
    {"t": "P", "b": True, "s": 17, "c": GREEN},
    {"t": "Melhora muito a malha aberta, mas deixa erro permanente.", "s": 14},
    {"t": "PI", "b": True, "s": 17, "c": ORANGE},
    {"t": "Zera o erro: 100% do tempo na faixa no C1 e 92% no C3.", "s": 14},
    {"t": "PI + FF", "b": True, "s": 17, "c": NAVY},
    {"t": "Não supera o PI: empata no C2 e piora um pouco no C3.", "s": 14}], name="Leitura")
notes(s, "A tabela é a Tabela 10 do trabalho. Sem controle, a pressão fica de 69% a 91% do tempo fora da faixa. O P reduz bastante, mas deixa erro: não acomoda nos degraus. O PI elimina o erro: 100% na faixa no C1, com acomodação de 0,44 s, e cerca de 92% no C3. O feedforward não supera o PI: empata no C2, fica um pouco mais lento no C1 e piora no C3, de 8,3% para 9,5%. Como o controlador lê a pressão em tempo real, o PI já reage no instante da troca e a válvula anda em rampa nos dois casos.")

# ================================================================ 16. três cenários
s = next(cont)
title(s, "Respostas no tempo nos três cenários")
cen = [("C1", "c_C1.png", "Um bico por vez", GREEN,
        "PI e PI+FF ficam 100% na faixa; o P para acima de 3,5 a cada degrau."),
       ("C2", "c_C2.png", "Degraus de três bicos", NAVY,
        "P para em 3,81 e 4,12 (previsto 3,82 e 4,13); PI volta em ≈ 1,0 s; o pico de ≈ 30% não some."),
       ("C3", "d_C3.png", "Trocas aleatórias rápidas", ORANGE,
        "PI fica 92% do tempo na faixa; as saídas acontecem quando várias trocas no mesmo sentido chegam seguidas.")]
lw = 3.95
for i, (cod, arq, sub, cor, msg) in enumerate(cen):
    x = 0.6 + i * (lw + 0.15)
    text(s, x, 2.38, lw, 0.36, [{"runs": [(cod + "  ", True, cor), (sub, False, MUTED)], "s": 15}], name=f"Cab {cod}")
    image(s, FIGS / arq, x + 0.12, 2.74, w=lw - 0.24, name=f"Resposta {cod}")
    box(s, x, 2.74 + (lw - 0.24) / 1.143 + 0.06, lw, 0.88, name=f"Leitura {cod}")
    text(s, x + 0.1, 2.74 + (lw - 0.24) / 1.143 + 0.09, lw - 0.2, 0.82, [{"t": msg, "s": 12.5}],
         anchor=MSO_ANCHOR.MIDDLE, name=f"Texto {cod}")
notes(s, "Os três gráficos têm o mesmo formato: em cima a pressão, com a faixa de ±10% em verde; no meio a abertura da válvula; embaixo o número de bicos. No C1, um bico por vez, o PI e o PI com feedforward ficam sempre na faixa, e o P para acima da referência a cada degrau. No C2, três bicos fecham de uma vez: o P para em 3,81 e 4,12, como a conta do erro previa; o PI volta à referência em cerca de um segundo; e o pico de cerca de 30% não some, porque a pressão salta antes de a válvula se mover. No C3, com trocas rápidas, o PI fica 92% do tempo na faixa.")

# ================================================================ 17. velocidade da válvula
s = next(cont)
title(s, "O gargalo é a velocidade da válvula")
linhas = [("Velocidade máxima da válvula", "C2: PI", "C2: PI+FF", "C3: PI", "C3: PI+FF"),
          ("0,5 s⁻¹ (estimado, curso em 2 s)", "6,8%", "6,8%", "8,3%", "9,5%"),
          ("1,0 s⁻¹ (2× mais rápida)", "3,4%", "3,4%", "0,4%", "1,5%"),
          ("2,0 s⁻¹ (4× mais rápida)", "1,7%", "1,7%", "0,2%", "0,3%")]
gt = s.shapes.add_table(4, 5, Inches(0.6), Inches(2.75), Inches(7.4), Inches(2.4))
gt.name = "Tabela velocidade"
tab = gt.table
for c, wc in enumerate((2.9, 1.125, 1.125, 1.125, 1.125)):
    tab.columns[c].width = Inches(wc)
melhor = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
for r, lin in enumerate(linhas):
    tab.rows[r].height = Inches(0.6)
    for c, v in enumerate(lin):
        cell = tab.cell(r, c); cell.text = v; cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        pp = cell.text_frame.paragraphs[0]; rn = pp.runs[0]
        rn.font.name = FONT; rn.font.size = Pt(14 if r else 13); rn.font.bold = (r == 0 or (r, c) in melhor)
        rn.font.color.rgb = WHITE if r == 0 else INK
        pp.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.CENTER
        cell.fill.solid(); cell.fill.fore_color.rgb = NAVY if r == 0 else (TINT if r % 2 else WHITE)
text(s, 0.6, 2.35, 7.4, 0.4, [{"t": "Tempo com a pressão fora da faixa", "b": True, "s": 15, "c": NAVY}], name="Cab tabela")
caption(s, 0.6, 5.25, 7.4, "Negrito: melhor de cada cenário em cada velocidade. Fonte: seção 4.6 do TCC.")
stat(s, 8.35, 2.55, 4.4, "75%", "do tempo do C3 a válvula anda na velocidade máxima (PI+FF)", color=ORANGE, big_size=44)
text(s, 8.35, 4.1, 4.4, 2.95, [
    {"t": "O PI, lendo em tempo real, já reage na troca: a válvula anda em rampa com ou sem FF.", "bullet": True},
    {"t": "Nas trocas rápidas, o FF manda a válvula para alvos que mudam antes de ela chegar.", "bullet": True},
    {"t": "Dobrar a velocidade leva o PI no C3 de 8,3% para 0,4%.", "bullet": True}], size=15)
notes(s, "A velocidade da válvula é o que mais pesa no resultado. No C3 a válvula passa 75% do tempo na velocidade máxima com o feedforward. Como o PI lê a pressão em tempo real, ele já manda abrir a válvula no instante da troca, e o feedforward não tem o que adiantar: no C2 os dois empatam em todas as velocidades. Com a válvula duas vezes mais rápida, o PI no C3 cai de 8,3% para 0,4%.")

# ================================================================ 18. conclusões
s = next(cont)
title(s, "Conclusões")
for i, (cab, desc, cor) in enumerate([
        ("Modelo", "Uma constante de bico (R₁/n²) e uma curva de fonte reproduzem a bancada com erro ≤ 0,7% na pressão", GREEN),
        ("Sintonia", "Ganho da planta igual para todo n e mesmos polos para referência e bicos: uma sintonia por alocação de polos serve para tudo", NAVY),
        ("Controle", "O PI zera o erro e mantém a pressão na faixa 100% do tempo no C1 e 92% no C3; o feedforward não trouxe ganho", ORANGE),
        ("Limite", "Trocas simultâneas de vários bicos ainda tiram a pressão da faixa: a válvula não é rápida o bastante", MUTED)]):
    y = 2.5 + i * 1.12
    box(s, 0.6, y, 12.15, 1.0, name=f"Conclusão {cab}")
    text(s, 0.8, y + 0.08, 2.1, 0.85, [{"t": cab, "b": True, "s": 19, "c": cor}], anchor=MSO_ANCHOR.MIDDLE, name="Cab")
    text(s, 2.95, y + 0.08, 9.6, 0.85, [{"t": desc, "s": 16}], anchor=MSO_ANCHOR.MIDDLE, name="Texto")
text(s, 0.6, 6.95, 12.15, 0.45, [{"t": "Hipótese confirmada em parte e só em simulação: τa, ωmax e a curva da válvula foram estimados, e falta validar com medições no tempo.",
                                  "b": True, "s": 15, "c": NAVY}], name="Veredito")
notes(s, "A hipótese foi confirmada em parte e só em simulação. O modelo simples funcionou, uma única sintonia por alocação de polos serve para todos os números de bicos e também para mudanças de referência, e o PI atende a tolerância na maior parte do tempo; o feedforward não trouxe ganho sobre ele. Mas as trocas simultâneas ainda tiram a pressão da faixa, e os parâmetros da válvula precisam ser medidos.")

# ================================================================ 19. trabalhos futuros + obrigado
s = next(cont)
title(s, "Trabalhos futuros")
text(s, 0.6, 2.55, 7.4, 4.4, [
    {"t": "Medir em bancada a velocidade e a curva de abertura da válvula", "bullet": True},
    {"t": "Medir a resposta da malha na bancada e ajustar ζ e ts considerando o ruído do sensor", "bullet": True},
    {"t": "Válvula mais rápida ou comando da válvula antes das solenoides, contra os picos", "bullet": True},
    {"t": "Anti-windup também no limite de velocidade (C3: 8,3% → 3,2% num teste)", "bullet": True},
    {"t": "Barras comerciais: perda ao longo da barra e capacitância da mangueira", "bullet": True},
    {"t": "Validar com registros de pulverizadores em campo", "bullet": True}], size=17)
box(s, 8.4, 2.55, 4.35, 4.4, fill=NAVY, name="Agradecimento")
text(s, 8.6, 2.85, 3.95, 3.8, [
    {"t": "Obrigado!", "b": True, "s": 40, "c": WHITE, "align": PP_ALIGN.CENTER},
    {"t": "Alex de Jesus Terolti", "s": 18, "c": WHITE, "align": PP_ALIGN.CENTER},
    {"t": "Perguntas da banca", "s": 16, "c": RGBColor(0xBF, 0xD9, 0xC6), "i": True, "align": PP_ALIGN.CENTER}],
    anchor=MSO_ANCHOR.MIDDLE, name="Texto obrigado")
notes(s, "Fechar com os trabalhos futuros, começando pelo mais importante: medir a válvula. Agradecer e abrir para perguntas.")

prs.core_properties.title = "Modelagem de sistema de controle para pulverização agrícola de precisão"
prs.core_properties.author = "Alex de Jesus Terolti"
out = TCC / "docs" / "Apresentacao_Banca_TCC_v19.pptx"
prs.save(str(out))
print("salvo", out)
