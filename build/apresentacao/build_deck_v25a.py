"""Monta a apresentação da banca (TCC v25, 20 min) sobre o modelo institucional da UNEMAT.
v25: parte de controle em 8 slides (estratégia, α_ff, linearização, Laplace, L(s)/T_n, leitura das FTs,
alocação de polos, forma discreta + conferência); FF antecipado 0,2 s; Tabela 9 só com % fora e IAE;
slide novo da antecipação (Fig. 24). Versões anteriores: build_deck_v20.py, build_deck_v19.py, build_deck_v15.py."""
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


def duplica_fundo(src):
    """Novo slide com o mesmo layout e o mesmo fundo (imagem) de src; vai para o fim da lista."""
    novo = prs.slides.add_slide(src.slide_layout)
    bg = src._element.cSld.bg
    if bg is not None:
        bg = copy.deepcopy(bg)
        for el in bg.iter(qn("a:blip")):
            rel = src.part.rels[el.get(qn("r:embed"))]
            el.set(qn("r:embed"), novo.part.relate_to(rel._target, rel.reltype))
        novo._element.cSld.insert(0, bg)
    return novo


# v25: 26 slides de conteúdo + capa = 27; o modelo tem 20 → 7 cópias
slides += [duplica_fundo(slides[2]) for _ in range(7)]
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
    {"t": "Sintonizar P e PI por alocação de polos e acrescentar o feedforward antecipado", "bullet": True},
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
                                     ("R² = 0,9999", "curva da fonte (mínimos quadrados)", NAVY)]):
    stat(s, 0.6, 2.55 + i * 1.5, 4.0, big, lab, color=cor, big_size=36 if i < 2 else 30)
image(s, FIGS / "b_fonte_carga.png", 4.95, 2.5, h=3.75, name="Fonte e carga")
text(s, 10.05, 2.6, 2.75, 3.6, [
    {"t": "Regra de projeto", "b": True, "s": 16, "c": NAVY},
    {"t": "A válvula de alívio só baixa a pressão: a referência tem de ficar abaixo do que a fonte sustenta com 7 bicos (3,56 kgf/cm²).", "s": 14},
    {"t": "Adotado: Pref = 3,5 kgf/cm²", "b": True, "s": 15, "c": ORANGE}], name="Regra de projeto")
caption(s, 4.95, 6.3, 5.0, "Cruzamento da curva da fonte com as curvas de carga = ponto de operação.")
simbolos(s, [('P_{ref}', 'pressão de referência (valor desejado)')])
notes(s, "Com a constante do bico e a curva da fonte, o modelo reproduziu os sete pontos com erro de até 0,7% na pressão e 2,3% na vazão. A curva de segundo grau da fonte teve R² de 0,9999; uma reta teria erro doze vezes maior. Uma consequência: como a válvula só alivia, a referência tem de ficar abaixo de 3,56; foi escolhido 3,5.")

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
title(s, "Estratégia de controle: três controladores, uma equação")
image(s, BFIG / "fig07.png", 0.6, 2.4, w=7.3, name="Diagrama de blocos")
caption(s, 0.6, 2.4 + 7.3 / 2.32 + 0.02, 7.3, "Figura 12 do TCC: diagrama de blocos do controle proposto.")
text(s, 0.6, 5.95, 7.3, 1.0, [
    {"runs": [("Controlada: ", True, NAVY), ("pressão P  ·  ", False, INK), ("manipulada: ", True, NAVY),
              ("abertura α  ·  ", False, INK), ("perturbação: ", True, NAVY), ("nº de bicos n(t)", False, INK)], "s": 14, "space": 3},
    {"t": "Erro e = P − Pref (ao contrário do usual): pressão acima da referência pede ABRIR a válvula.", "s": 14, "c": MUTED}],
    name="Variáveis")
box(s, 8.15, 2.4, 4.6, 1.55, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Equação geral")
text(s, 8.3, 2.43, 4.3, 0.3, [{"t": "Comando da válvula (Eq. 3.19)", "b": True, "s": 13, "c": GREEN}], name="Cab eq geral")
add_eq(s, "eq319", "\\alpha_c = \\alpha_{ff}[n(t+T_{ant})] + K_c\\left[e + \\frac{1}{T_i}\\int_0^t e\\,d\\tau\\right]",
       8.3, 2.85, size=19, max_w=4.35)
text(s, 8.3, 3.55, 4.3, 0.35, [{"t": "base + proporcional + integral", "s": 12, "c": MUTED, "i": True}], name="Leitura eq")
for i, (cab, desc, cor) in enumerate([
        ("P", "Ti → ∞ e base fixa α₀ = 0,023:  αc = α₀ + Kc·e", GREEN),
        ("PI", "com a integral, base ainda fixa em α₀", ORANGE),
        ("PI + FF", "base αff(n) do nº de bicos daqui a Tant = 0,2 s", NAVY)]):
    y = 4.1 + i * 0.95
    box(s, 8.15, y, 4.6, 0.85, name=f"Cartão {cab}")
    text(s, 8.25, y + 0.05, 1.05, 0.75, [{"t": cab, "b": True, "s": 16, "c": cor}], anchor=MSO_ANCHOR.MIDDLE, name="Cab")
    text(s, 9.3, y + 0.05, 3.4, 0.75, [{"t": desc, "s": 13}], anchor=MSO_ANCHOR.MIDDLE, name="Desc")
simbolos(s, [('e', 'erro, P − Pref'), ('K_{c}, T_{i}', 'ganho e tempo integral'), ('α_{ff}', 'abertura de equilíbrio (feedforward)'), ('T_{ant}', 'antecipação do feedforward (0,2 s)')])
notes(s, "Os três controladores saem de uma só equação, a 3.19: uma base, uma parcela proporcional ao erro e uma proporcional ao erro acumulado. No P, só a base fixa e o proporcional; no PI entra a integral; no PI+FF a base passa a ser a abertura de equilíbrio do número de bicos que haverá daqui a 0,2 segundo. O erro é P menos Pref, porque pressão alta pede abrir a válvula. O anti-windup congela a integral quando o comando bate no limite de posição.")

# ================================================================ 11. abertura de equilíbrio
s = next(cont)
title(s, "Abertura de equilíbrio: o feedforward sai do modelo estático")
box(s, 0.6, 2.4, 6.9, 3.15, name="Dedução aff")
text(s, 0.8, 2.45, 6.5, 0.35, [{"t": "No equilíbrio do nó, com P = Pref, toda a vazão da fonte sai pelos bicos e pela válvula:",
                                 "s": 14, "c": INK}], name="Passo 1")
add_eq(s, "aff1", "Q_s(P_{ref}) = \\left[n\\,K + K_{v,max}\\,\\alpha\\right]\\sqrt{P_{ref}}", 0.95, 3.0, size=21, max_w=5.5)
text(s, 0.8, 3.65, 6.5, 0.3, [{"t": "Dividindo por √Pref e isolando α (Eq. 3.14):", "s": 14}], name="Passo 2")
add_eq(s, "aff2", "\\alpha_{ff}(n) = \\frac{1}{K_{v,max}}\\left[\\frac{Q_s(P_{ref})}{\\sqrt{P_{ref}}} - n\\,K\\right]",
       0.95, 4.05, size=23, max_w=5.8, color="#E88A0C")
box(s, 0.6, 5.65, 6.9, 1.25, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Reta")
add_eq(s, "aff3", "\\frac{d\\alpha_{ff}}{dn} = -\\frac{K}{K_{v,max}} = -\\frac{0{,}425}{3{,}5} = -0{,}121", 0.85, 5.75, size=20, max_w=4.6)
text(s, 0.8, 6.38, 6.5, 0.5, [{"t": "Uma reta: 0,121 de abertura deixa passar o mesmo que um bico.", "b": True, "s": 14, "c": GREEN}], name="Leitura reta")
for i, (big, lab) in enumerate([("0,023", "7 bicos (α₀)"), ("0,388", "4 bicos"), ("0,752", "1 bico")]):
    stat(s, 7.85 + i * 1.66, 2.4, 1.56, big, lab, color=NAVY, big_size=26)
text(s, 7.85, 3.85, 4.9, 0.4, [{"t": "Qs(Pref)/√Pref = 5,72/1,871 = 3,057", "s": 13, "c": MUTED}], name="Conta")
box(s, 7.85, 4.3, 4.9, 2.6, name="Antecipação")
text(s, 8.05, 4.36, 4.55, 2.5, [
    {"t": "Por que antecipar 0,2 s", "b": True, "s": 15, "c": ORANGE},
    {"t": "Para compensar um bico a válvula anda 0,121 a 0,5 s⁻¹: 0,121/0,5 ≈ 0,24 s.", "bullet": True, "s": 13, "space": 3},
    {"t": "O sistema que comanda os bicos já sabe a troca antes (mapa + posição).", "bullet": True, "s": 13, "space": 3},
    {"t": "0,2 s a 15 km/h ≈ 0,8 m de barra andando.", "bullet": True, "s": 13, "space": 3},
    {"t": "Em regime, é o F = −G₂/Gp de Castrucci et al. (2018, seção 7.8.1).", "bullet": True, "s": 13}], name="Texto antecipação")
simbolos(s, [('Q_{s}', 'vazão da fonte'), ('K', 'constante do bico (0,425)'), ('K_{v,max}', 'constante da válvula aberta (3,5)'), ('α_{0}', 'abertura inicial')])
notes(s, "A abertura de equilíbrio é a abertura que mantém a pressão exatamente na referência para cada número de bicos. No nó, com P igual a Pref, a vazão da fonte tem de sair toda pelos bicos e pela válvula. Dividindo por raiz de Pref e isolando alfa sai a Equação 3.14. Ela é uma reta em n: cada bico que fecha pede 0,121 a mais de abertura, que é K sobre Kv,max. Com sete bicos a válvula fica quase fechada, 0,023; com um bico, três quartos aberta. Como a válvula leva cerca de 0,24 segundo para andar esses 0,121, o feedforward foi comandado 0,2 segundo antes da troca, o que é possível porque quem fecha os bicos sabe disso antes.")

# ================================================================ 12. linearização
s = next(cont)
title(s, "Linearização: cada vazão vira a sua reta tangente")
text(s, 0.6, 2.32, 7.2, 0.35, [{"t": "Ponto de operação nominal: 7 bicos, P = Pref = 3,5, α₀ = 0,023, C = 3,057, Qs = 5,72 L/min",
                                 "s": 13, "c": MUTED, "i": True}], name="Ponto nominal")
linhas_lin = [
    ("Bicos", "Q_{barra} = n\\,K\\sqrt{P}", "\\Delta Q_{barra} = 0{,}795\\,\\Delta N + 0{,}795\\,\\Delta P"),
    ("Válvula", "Q_v = K_{v,max}\\,\\alpha\\sqrt{P}", "\\Delta Q_v = 6{,}55\\,\\Delta\\alpha + 0{,}022\\,\\Delta P"),
    ("Fonte", "Q_s = Q_s(P)", "\\Delta Q_s = -1{,}645\\,\\Delta P"),
]
box(s, 0.6, 2.72, 7.2, 0.42, fill=NAVY, name="Cab tabela lin")
for x, t in ((0.72, "Peça"), (1.95, "Não linear"), (4.35, "Reta tangente (Tabela 3)")):
    text(s, x, 2.74, 3.4, 0.38, [{"t": t, "b": True, "s": 13, "c": WHITE}], anchor=MSO_ANCHOR.MIDDLE, name="Cab col")
for i, (peca, nl, lin) in enumerate(linhas_lin):
    y = 3.2 + i * 0.62
    box(s, 0.6, y, 7.2, 0.56, fill=TINT if i % 2 == 0 else WHITE, name=f"Linha {peca}")
    text(s, 0.72, y + 0.05, 1.2, 0.46, [{"t": peca, "b": True, "s": 14, "c": NAVY}], anchor=MSO_ANCHOR.MIDDLE, name="Peça")
    add_eq(s, f"lin_nl{i}", nl, 1.95, y + 0.11, size=16, max_w=2.25)
    add_eq(s, f"lin_l{i}", lin, 4.35, y + 0.11, size=16, max_w=3.35)
text(s, 0.6, 5.1, 7.2, 0.3, [{"t": "Somando no nó (fonte = bicos + válvula) e isolando ΔP:", "s": 14}], name="Soma")
add_eq(s, "lin_soma", "-1{,}645\\,\\Delta P = 0{,}795\\,\\Delta N + 0{,}795\\,\\Delta P + 6{,}55\\,\\Delta\\alpha + 0{,}022\\,\\Delta P",
       0.75, 5.48, size=17, max_w=6.9)
add_eq(s, "lin_res", "\\Delta P = -\\frac{6{,}55}{2{,}462}\\,\\Delta\\alpha - \\frac{0{,}795}{2{,}462}\\,\\Delta N = -2{,}66\\,\\Delta\\alpha - 0{,}323\\,\\Delta N",
       0.75, 6.0, size=18, max_w=6.9, color="#E88A0C")
box(s, 8.1, 2.4, 4.65, 2.75, name="Ganhos")
text(s, 8.3, 2.45, 4.3, 0.35, [{"t": "Os dois ganhos (Eqs. 3.15 e 3.16)", "b": True, "s": 15, "c": NAVY}], name="Cab ganhos")
add_eq(s, "lin_D", "D = \\frac{C}{2\\sqrt{P}} - \\frac{dQ_s}{dP} = 0{,}817 + 1{,}645 = 2{,}462", 8.3, 2.9, size=17, max_w=4.3)
add_eq(s, "lin_kg", "K_g = \\frac{\\partial P}{\\partial \\alpha} = -\\frac{K_{v,max}\\sqrt{P}}{D} = -2{,}66", 8.3, 3.55, size=18, max_w=4.3, color="#E88A0C")
add_eq(s, "lin_kn", "K_n = \\frac{\\partial P}{\\partial n} = -\\frac{K\\sqrt{P}}{D} = -0{,}323", 8.3, 4.35, size=18, max_w=4.3, color="#E88A0C")
box(s, 8.1, 5.28, 4.65, 1.62, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Independe de n")
text(s, 8.3, 5.32, 4.3, 1.55, [
    {"t": "Não dependem do número de bicos", "b": True, "s": 14, "c": GREEN, "space": 3},
    {"t": "Com 4 bicos: bicos 0,454 + válvula 0,363 = 0,817, a mesma soma. D, Kg e Kn não mudam: uma única sintonia serve para todo n.", "s": 13}],
    name="Texto independe")
simbolos(s, [('ΔP, Δα, ΔN', 'desvios em torno do ponto nominal'), ('D', 'denominador comum'), ('K_{g}', 'ganho da planta'), ('K_{n}', 'ganho do distúrbio (por bico)')])
notes(s, "Para usar a teoria de controle linear, cada vazão do nó foi trocada pela sua reta tangente no ponto nominal, com sete bicos e a pressão na referência. Os coeficientes são as derivadas parciais, como em Ogata. Somando as retas no nó, a variação da fonte é igual à soma das variações dos bicos e da válvula. Passando tudo em delta P para um lado, aparece o denominador 2,462: são os dois efeitos que seguram a pressão quando ela sobe, as saídas deixando passar mais e a fonte entregando menos. O resultado é delta P igual a menos 2,66 delta alfa menos 0,323 delta N. Kg é o ganho da planta e Kn o do distúrbio, ambos negativos. Quando muda o número de bicos, a parcela dos bicos cai e a da válvula sobe na mesma quantidade, então a soma não muda: a sintonia vale para qualquer n.")

# ================================================================ 13. Laplace
s = next(cont)
title(s, "Domínio de Laplace: planta, válvula e controlador")
w13, h13 = image(s, BFIG / "fig12_freq.png", 0.6, 2.4, w=7.4, name="Diagrama em Laplace")
caption(s, 0.6, 2.4 + h13 + 0.02, 7.4, "Figura 13 do TCC: malha linearizada no ponto nominal; ΔN entra por dois caminhos.")
yb = 2.4 + h13 + 0.4
box(s, 0.6, yb, 7.4, 6.9 - yb, name="Fora do modelo")
text(s, 0.8, yb + 0.06, 7.0, 6.9 - yb - 0.1, [
    {"t": "Referência fixa: a única entrada é ΔN, perturbação em degrau com referência nula (Castrucci et al., 2018, seção 3.11.3).", "bullet": True, "s": 13, "space": 3},
    {"t": "Saturação, limite de velocidade e anti-windup não são lineares: ficam só no simulador.", "bullet": True, "s": 13, "space": 3},
    {"t": "Controlador tratado como contínuo: atualiza a cada 1 ms, 200× menos que τa.", "bullet": True, "s": 13}], name="Texto fora")
cards13 = [
    ("Planta (H6: pressão instantânea)", "\\Delta P(s) = K_g\\,\\Delta A(s) + K_n\\,\\Delta N(s)", "Eq. 3.17: estática, só ganhos"),
    ("Válvula (1ª ordem)", "\\tau_a\\dot{\\alpha} + \\alpha = \\alpha_c \\ \\Rightarrow\\ \\frac{\\Delta A}{\\Delta A_c} = \\frac{1}{\\tau_a s + 1}", "Eq. 3.18: polo em −1/τa = −5"),
    ("Controlador PI", "G_c(s) = K_c\\left(1 + \\frac{1}{T_i\\,s}\\right)", "Eq. 3.22; P: Ti → ∞"),
    ("Feedforward", "\\Delta A_{ff} = -\\frac{K_n}{K_g}\\,\\Delta N = +0{,}121 \\ \\mathrm{por\\ bico\\ fechado}", "= −G₂/Gp com ganhos estáticos"),
]
for i, (cab, tex, rod) in enumerate(cards13):
    y = 2.4 + i * 1.13
    box(s, 8.3, y, 4.45, 1.03, name=f"Cartão {cab}")
    text(s, 8.42, y + 0.03, 4.2, 0.3, [{"t": cab, "b": True, "s": 13, "c": NAVY}], name="Cab")
    add_eq(s, f"lap{i}", tex, 8.45, y + 0.36, size=16, max_w=4.15)
    text(s, 8.42, y + 0.76, 4.2, 0.26, [{"t": rod, "s": 11, "c": MUTED}], name="Nota")
simbolos(s, [('s', 'variável de Laplace'), ('ΔA, ΔA_{c}', 'abertura e comando'), ('τ_{a}', 'constante de tempo da válvula (0,2 s)'), ('G_{c}(s)', 'controlador')])
notes(s, "Com as retas, a malha pode ir para o domínio de Laplace. A planta é estática pela hipótese H6, então a transformada só carrega os ganhos Kg e Kn. A válvula, sem o limite de velocidade, é de primeira ordem: tau a vezes alfa ponto mais alfa igual ao comando, que vira 1 sobre tau a s mais 1. O PI é Kc vezes 1 mais 1 sobre Ti s. O feedforward é menos Kn sobre Kg vezes delta N, mais 0,121 por bico fechado, que é o compensador ideal do Castrucci escrito com ganhos estáticos. No diagrama, o número de bicos entra por dois caminhos: direto na pressão, pelo bloco do distúrbio, e no comando, pelo feedforward. As não linearidades ficam fora e são tratadas só no simulador.")

# ================================================================ 14. L(s) e T_n
s = next(cont)
title(s, "Fechando a malha: ganho de malha e resposta aos bicos")
w14, h14 = image(s, BFIG / "fig_malha_L.png", 0.6, 2.35, w=6.1, name="Malha L(s)")
caption(s, 0.6, 2.35 + h14 + 0.0, 6.1, "Figura 14 do TCC: (a) malha com L(s); (b) bloco equivalente.")
box(s, 7.35, 2.38, 5.4, 2.6, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Dedução malha")
text(s, 7.5, 2.42, 5.1, 0.3, [{"t": "Substituindo válvula e controlador na planta:", "s": 13, "c": INK}], name="Passo malha")
add_eq(s, "m1", "\\Delta P = K_n\\Delta N + \\frac{K_g}{\\tau_a s + 1}\\left[G_c\\,\\Delta P + \\Delta A_{ff}\\right]", 7.5, 2.78, size=17, max_w=5.1)
add_eq(s, "m2", "L(s) = \\frac{G_c(s)\\,|K_g|}{\\tau_a s + 1}", 7.5, 3.45, size=18, max_w=2.6, color="#E88A0C")
text(s, 10.2, 3.5, 2.5, 0.5, [{"t": "controlador × válvula × planta: uma volta na malha", "s": 11, "c": MUTED, "i": True}], name="Leitura L")
add_eq(s, "m3", "T_n(s) = \\frac{\\Delta P}{\\Delta N} = \\frac{K_n}{1 + L(s)}", 7.5, 4.2, size=19, max_w=4.0, color="#E88A0C")
text(s, 11.55, 4.28, 1.2, 0.4, [{"t": "(3.25)", "s": 12, "c": MUTED}], name="Num 325")
tfs = [("P (3.26)", "T_{n,P} = \\frac{K_n(\\tau_a s + 1)}{\\tau_a s + 1 + K_c|K_g|}", GREEN),
       ("PI (3.27)", "T_{n,PI} = \\frac{K_n\\,T_i s(\\tau_a s + 1)}{\\tau_a T_i s^2 + T_i(1 + K_c|K_g|)s + K_c|K_g|}", ORANGE),
       ("PI+FF sem antecipação (3.28)", "T_{n,PI+FF} = \\frac{K_n\\,\\tau_a T_i s^2}{\\tau_a T_i s^2 + T_i(1 + K_c|K_g|)s + K_c|K_g|}", NAVY)]
xs = (0.6, 4.02, 8.42)
ws = (3.27, 4.25, 4.33)
for (cab, tex, cor), x, w in zip(tfs, xs, ws):
    box(s, x, 5.42, w, 1.48, name=f"FT {cab}")
    text(s, x + 0.1, 5.45, w - 0.2, 0.3, [{"t": cab, "b": True, "s": 13, "c": cor}], name="Cab FT")
    add_eq(s, f"tf_{cab[:2]}", tex, x + 0.12, 5.85, size=16, max_w=w - 0.25)
simbolos(s, [('L(s)', 'ganho de malha'), ('T_{n}(s)', 'função de transferência bicos → pressão'), ('|K_{g}|', 'módulo do ganho da planta (2,66)')])
notes(s, "Substituindo a válvula e o controlador na planta, aparece delta P dos dois lados. Como Kg é negativo, o produto dos blocos na volta, o ganho de malha L, entra com sinal de menos: é realimentação negativa. Passando para o lado esquerdo, delta P vezes 1 mais L é igual ao efeito do bico. Então a resposta aos bicos é T n igual a Kn sobre 1 mais L: o efeito do bico fica dividido por 1 mais o ganho de malha. Tirando as frações, saem as três funções embaixo. O ponto importante: o PI e o PI com feedforward têm o mesmo denominador; o que muda é só o numerador.")

# ================================================================ 15. leitura das FTs
s = next(cont)
title(s, "O que as funções de transferência mostram")
cards15 = [
    ("O P deixa erro (valor final)", GREEN,
     "\\Delta P(\\infty) = -\\frac{K_n}{1 + K_c|K_g|} = \\frac{0{,}323}{1 + 2{,}2} = +0{,}101",
     "kgf/cm² por bico fechado; simulador: 3,60 (0,10 acima). Sobra 1/(1+K) da perturbação (Castrucci, Tab. 3.4)."),
    ("O PI zera o erro", ORANGE,
     "T_{n,PI}(s) \\propto s \\ \\Rightarrow\\ T_{n,PI}(0) = 0",
     "O integrador põe um s no numerador: depois da troca, a pressão volta exatamente a Pref."),
    ("A pressão salta na troca (valor inicial)", NAVY,
     "s \\to \\infty:\\ \\ \\Delta P(0^+) = K_n\\,\\Delta N",
     "Numerador e denominador de mesmo grau: o salto de um bico (0,333 no simulador) acontece com QUALQUER controlador. O controle só define a volta."),
    ("O FF não muda a estabilidade", MUTED,
     "K_n\\left[1 - \\frac{1}{\\tau_a s + 1}\\right] = K_n\\,\\frac{\\tau_a s}{\\tau_a s + 1}",
     "Mesmo denominador do PI. Sem antecipação, cancela o bico em regime mas não no instante; antecipar usa o futuro e foi avaliado só no simulador."),
]
for i, (cab, cor, tex, desc) in enumerate(cards15):
    x = 0.6 + (i % 2) * 6.15
    y = 2.4 + (i // 2) * 2.3
    box(s, x, y, 6.0, 2.15, name=f"Cartão {cab}")
    text(s, x + 0.18, y + 0.06, 5.7, 0.35, [{"t": cab, "b": True, "s": 16, "c": cor}], name="Cab")
    add_eq(s, f"ft_le{i}", tex, x + 0.25, y + 0.5, size=19, max_w=5.5)
    text(s, x + 0.18, y + 1.25, 5.7, 0.88, [{"t": desc, "s": 13, "c": INK}], name="Texto")
simbolos(s, [('ΔP(∞)', 'valor final (t → ∞)'), ('ΔP(0+)', 'valor logo após a troca'), ('K_{c}|K_{g}|', 'ganho de malha em regime (2,2)')])
notes(s, "Sem simular nada, as funções de transferência já dizem quatro coisas. Primeiro, pelo teorema do valor final, o P deixa 0,101 kgf/cm² de erro por bico: sobra 1 sobre 1 mais o ganho de malha da perturbação, como na tabela 3.4 do Castrucci. Segundo, o PI tem um s no numerador, então o valor final é zero. Terceiro, pelo teorema do valor inicial, logo depois da troca a pressão muda o efeito inteiro do bico, Kn, com qualquer controlador, porque a correção ainda não passou pela válvula. O controlador não evita o salto; ele define a volta. Quarto, o feedforward sem antecipação deixa um resíduo Kn tau a s sobre tau a s mais 1: some em regime, mas não no instante. E o denominador é o mesmo, então o feedforward não muda a estabilidade.")

# ================================================================ 16. alocação de polos
s = next(cont)
title(s, "Sintonia por alocação de polos")
box(s, 0.6, 2.4, 7.55, 4.5, name="Equações sintonia")
text(s, 0.8, 2.45, 7.2, 0.35, [{"t": "1. Especificação: ζ = 0,7 e ts = 0,5 s (critério de 2%)", "b": True, "s": 14, "c": NAVY}], name="Passo 1")
add_eq(s, "wn", "\\omega_n = \\frac{4}{\\zeta\\,t_s} = \\frac{4}{0{,}7 \\times 0{,}5} = 11{,}43\\ \\mathrm{rad/s}", 0.95, 2.85, size=18, max_w=4.6)
text(s, 0.8, 3.55, 7.2, 0.35, [{"t": "2. Igualar o denominador comum (÷ τa Ti) à forma padrão", "b": True, "s": 14, "c": NAVY}], name="Passo 2")
add_eq(s, "car", "s^2 + \\frac{1 + K_c|K_g|}{\\tau_a}\\,s + \\frac{K_c|K_g|}{\\tau_a T_i} = s^2 + 2\\zeta\\omega_n s + \\omega_n^2", 0.95, 3.95, size=19, max_w=6.9)
text(s, 0.8, 4.68, 7.2, 0.35, [{"t": "3. Termo a termo, isolar Kc e Ti", "b": True, "s": 14, "c": NAVY}], name="Passo 3")
add_eq(s, "kc", "K_c = \\frac{2\\zeta\\omega_n\\tau_a - 1}{|K_g|} = \\frac{2{,}20}{2{,}66} = 0{,}827", 0.95, 5.1, size=18, max_w=3.6, color="#E88A0C")
add_eq(s, "ti", "T_i = \\frac{K_c|K_g|}{\\tau_a\\,\\omega_n^2} = \\frac{2{,}20}{26{,}1} = 0{,}084\\ \\mathrm{s}", 4.6, 5.1, size=18, max_w=3.45, color="#E88A0C")
add_eq(s, "pol", "s^2 + 16{,}0\\,s + 130{,}6 = 0 \\ \\Rightarrow\\ s = -8{,}0 \\pm j\\,8{,}2", 0.95, 6.1, size=19, max_w=6.0)
w16, h16 = image(s, FIGS / "i_plano_s.png", 8.45, 2.38, h=4.15, name="Plano s")
caption(s, 8.35, 2.38 + h16 + 0.02, 4.4, "Figura 19 do TCC: polos e zeros no plano s.")
simbolos(s, [('ζ, ω_{n}', 'amortecimento e frequência natural'), ('t_{s}', 'tempo de acomodação (2%)'), ('τ_{a}', 'constante de tempo da válvula'), ('s', 'variável de Laplace')])
notes(s, "A sintonia é feita de trás para frente. Escolhi amortecimento 0,7, perto do que acomoda mais rápido, e acomodação em meio segundo. Pela fórmula do Ogata, ts igual a 4 sobre zeta omega n, a frequência natural fica 11,43. O denominador comum das funções de transferência, dividido por tau a Ti, é comparado termo a termo com a forma padrão de segunda ordem: o termo em s dá Kc igual a 0,827 e o termo independente dá Ti igual a 0,084 segundo. Os polos ficam em menos 8 mais ou menos j 8,2. Na figura, a região sombreada é onde a especificação é atendida: à esquerda de menos 8 e dentro do ângulo de 45,6 graus. Os polos do PI ficam no canto. O polo da válvula sozinha é menos 5 e o do P é menos 16. Os círculos são os zeros, em 0 e menos 5: não mudam os polos, mas mudam a forma da curva. O P usa o mesmo Kc, para a comparação mostrar só o efeito da integral, e a derivativa não foi usada porque o salto de cada troca viraria um pico no comando.")

# ================================================================ 17. forma discreta + conferência
s = next(cont)
title(s, "Do papel ao simulador: forma discreta e conferência")
box(s, 0.6, 2.4, 6.6, 2.55, name="Forma discreta")
text(s, 0.8, 2.45, 6.3, 0.35, [{"t": "A cada passo Δt = 1 ms (soma de retângulos)", "b": True, "s": 14, "c": NAVY}], name="Cab discreta")
add_eq(s, "d1", "I_k = I_{k-1} + e_k\\,\\Delta t", 0.95, 2.9, size=19, max_w=3.0)
text(s, 4.3, 2.92, 2.8, 0.35, [{"t": "(3.20)", "s": 12, "c": MUTED}], name="Num 320")
add_eq(s, "d2", "\\alpha_{c,k} = \\alpha_{ff}[n(t_k + T_{ant})] + K_c\\left(e_k + \\frac{I_k}{T_i}\\right)", 0.95, 3.45, size=19, max_w=5.4)
text(s, 0.8, 4.3, 6.3, 0.6, [{"t": "Anti-windup: Ik não é atualizada quando o comando está no limite de posição e o erro pede para ir além.", "s": 12, "c": MUTED, "i": True}], name="AW")
box(s, 0.6, 5.05, 6.6, 1.85, fill=RGBColor(0xE6, 0xF2, 0xEA), name="Exemplo")
text(s, 0.8, 5.08, 6.3, 0.32, [{"t": "Exemplo: 7 bicos, P = 3,6 (e = +0,1), I = 0", "b": True, "s": 14, "c": GREEN}], name="Cab exemplo")
add_eq(s, "d3", "\\alpha_c = 0{,}023 + 0{,}827\\left(0{,}1 + \\frac{0{,}0001}{0{,}084}\\right) = 0{,}107", 0.95, 5.5, size=18, max_w=5.6)
text(s, 0.8, 6.15, 6.3, 0.72, [{"t": "A válvula recebe ordem de abrir de 2,3% para 10,7%. Com e constante, a parcela integral iguala a proporcional depois de Ti = 0,084 s.", "s": 13}], name="Leitura exemplo")
w17, h17 = image(s, FIGS / "g_funcao_transferencia.png", 7.4, 2.35, h=3.45, name="FT x simulador")
caption(s, 7.4, 2.35 + h17 + 0.0, 3.6, "Figura 20 do TCC: um bico fechando.")
text(s, 10.95, 2.42, 1.85, 3.4, [
    {"t": "Sem limite de velocidade", "b": True, "s": 12, "c": NAVY, "space": 1},
    {"t": "ts = 0,44 s (pedido 0,5); simulador a < 0,01 da FT", "s": 12, "space": 6},
    {"t": "Com 0,5 s⁻¹", "b": True, "s": 12, "c": ORANGE, "space": 1},
    {"t": "ts = 0,63 s; passa 41% do salto abaixo", "s": 12}], name="Leitura fig 20")
box(s, 7.45, 6.14, 5.3, 0.78, name="Gargalo")
add_eq(s, "d4", "\\frac{K_c|K_n|}{\\tau_a} = \\frac{0{,}827 \\times 0{,}323}{0{,}2} = 1{,}34\\ \\mathrm{s^{-1}} \\ \\approx 3\\,\\omega_{max}", 7.6, 6.22, size=17, max_w=5.0)
simbolos(s, [('I_{k}', 'soma do erro (integral discreta)'), ('e_{k}', 'erro no passo k'), ('Δt', 'passo de 1 ms'), ('ω_{max}', 'velocidade máxima da válvula (0,5 s⁻¹)')])
notes(s, "No programa, a integral vira uma soma de retângulos a cada milissegundo, oitenta vezes menos que Ti, e o comando é a Equação 3.21. Um exemplo com números: pressão em 3,6, erro de 0,1; a válvula recebe ordem de abrir de 2,3 para 10,7 por cento. Para conferir o projeto, a figura mostra um bico fechando no simulador completo. Sem o limite de velocidade, que é o que o modelo linear descreve, o PI acomoda em 0,44 segundo, dentro do pedido, e fica a menos de 0,01 da função de transferência: a linearização é boa. Com o limite real, o controlador pede 1,34 por segundo, quase três vezes o que a válvula consegue; ela anda em rampa, o integrador continua somando, e a acomodação vai para 0,63 segundo. Ou seja: o modelo linear acerta os polos, mas quem define o tempo real é a velocidade da válvula.")

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
    {"t": "Tempo fora da faixa ±10%, de 3,15 a 3,85 kgf/cm² (Eq. 3.33)", "bullet": True},
    {"t": "IAE: área entre P e Pref, soma de retângulos (Eq. 3.34)", "bullet": True},
    {"t": "Configurações", "b": True, "s": 18, "c": NAVY},
    {"t": "Malha aberta, P, PI e PI+FF antecipado 0,2 s", "bullet": True},
    {"t": "C2 e C3 também com a válvula 2× e 4× mais rápida", "bullet": True}], size=16)
simbolos(s, [('IAE', 'integral do erro absoluto'), ('C1, C2, C3', 'cenários de simulação')])
notes(s, "Três cenários, do mais simples ao mais difícil. O critério principal é o tempo fora da faixa de ±10%: com a máquina em velocidade constante, é a fração da área aplicada fora da tolerância.")

# ================================================================ 15. resultados gerais
s = next(cont)
title(s, "Resultados: tempo com a pressão fora da faixa")
cab = ("Cenário", "Configuração", "Tempo fora da faixa", "IAE [kgf/cm²·s]")
# (valores, colunas em negrito) — mesmo destaque da Tabela 9 do TCC (v25)
linhas = [
    (("C1", "Malha aberta", "69,2%", "24,72"), ()),
    (("C1", "P", "38,5%", "7,41"), ()),
    (("C1", "PI", "0,0%", "0,78"), (2,)),
    (("C1", "PI+FF", "0,0%", "0,73"), (2, 3)),
    (("C2", "Malha aberta", "85,7%", "18,38"), ()),
    (("C2", "P", "46,3%", "5,90"), ()),
    (("C2", "PI", "6,8%", "0,83"), ()),
    (("C2", "PI+FF", "5,1%", "0,65"), (2, 3)),
    (("C3", "Malha aberta", "90,5%", "23,26"), ()),
    (("C3", "P", "50,1%", "7,06"), ()),
    (("C3", "PI", "8,3%", "3,15"), ()),
    (("C3", "PI+FF", "4,4%", "2,70"), (2, 3)),
]
larg = (1.1, 2.1, 2.3, 2.3)
NC = len(cab)
gt = s.shapes.add_table(len(linhas) + 1, NC, Inches(0.6), Inches(2.45), Inches(sum(larg)), Inches(0.3 * 13))
gt.name = "Tabela 9 desempenho"
tab = gt.table
for c, wc in enumerate(larg):
    tab.columns[c].width = Inches(wc)
cor_cfg = {"Malha aberta": MUTED, "P": GREEN, "PI": ORANGE, "PI+FF": NAVY}
faixa = {"C1": WHITE, "C2": TINT, "C3": WHITE}
for r in range(len(linhas) + 1):
    tab.rows[r].height = Inches(0.36 if r == 0 else 0.29)
    vals, negrito = (cab, range(NC)) if r == 0 else linhas[r - 1]
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
caption(s, 0.6, 2.45 + 0.36 + 12 * 0.29 + 0.05, 7.8,
        "Negrito: melhor valor de cada cenário. PI+FF = feedforward antecipado em 0,2 s. Fonte: Tabela 9 do TCC.")
text(s, 8.75, 2.55, 4.0, 4.5, [
    {"t": "P", "b": True, "s": 17, "c": GREEN},
    {"t": "Melhora muito a malha aberta, mas deixa erro permanente (o valor final previsto).", "s": 14},
    {"t": "PI", "b": True, "s": 17, "c": ORANGE},
    {"t": "Zera o erro: 100% do tempo na faixa no C1 e 92% no C3.", "s": 14},
    {"t": "PI + FF antecipado", "b": True, "s": 17, "c": NAVY},
    {"t": "Melhor nos três cenários: C3 cai quase pela metade, de 8,3% para 4,4%.", "s": 14}], name="Leitura")
notes(s, "Esta é a Tabela 9 do trabalho, com as duas métricas. Sem controle, a pressão fica de 69% a 91% do tempo fora da faixa. O P reduz bastante, mas deixa o erro que o valor final previa. O PI elimina o erro: 100% na faixa no C1 e cerca de 92% no C3. O PI com feedforward antecipado em 0,2 segundo foi o melhor nos três: no C1 empata em 0% com IAE menor, no C2 cai de 6,8 para 5,1% e no C3 quase pela metade, de 8,3 para 4,4%.")

# ================================================================ 16–18. um slide por cenário
TAB10 = linhas          # linhas da Tabela 10 (slide anterior)
CENARIOS = [
    ("C1", "c_C1.png", 21, "um bico por vez", GREEN,
     "7 → 1 → 7, um bico por vez, a cada 2 s (26 s): passa por toda a faixa de operação",
     [{"runs": [("Cada troca dá um salto de cerca de 9,5% (o Kn do valor inicial), ", False, INK), ("dentro da faixa", True, INK)]},
      {"runs": [("P: ", True, GREEN), ("para acima de 3,5 a cada degrau e sai da faixa a partir do 4º bico fechado (3,91 kgf/cm² com 3 bicos)", False, INK)]},
      {"runs": [("PI e PI+FF: ", True, ORANGE), ("100% do tempo na faixa; o PI+FF antecipado erra menos (IAE 0,73 contra 0,78)", False, INK)]}],
     "No C1, os bicos fecham um de cada vez, de sete até um, e depois abrem de volta, a cada 2 segundos. Cada troca dá um salto de cerca de 9,5% na pressão, que é o salto que o teorema do valor inicial previa, e ainda fica dentro da faixa. O P, em verde, para acima de 3,5 a cada degrau, e o erro cresce conforme os bicos fecham: a partir do quarto bico fechado ele já sai da faixa. O PI e o PI com feedforward ficam 100% do tempo na faixa; o feedforward antecipado erra um pouco menos, IAE de 0,73 contra 0,78."),
    ("C2", "c_C2.png", 22, "degraus de três bicos", NAVY,
     "7 → 4 em t = 2 s → 1 em t = 8 s (14 s): repete a sequência do ensaio de Rosa, Terra e Drews Jr (2019)",
     [{"runs": [("P: ", True, GREEN), ("para em 3,81 e 4,12 kgf/cm²; a conta d/(1 + KcKg) previa 3,82 e 4,13", False, INK)]},
      {"runs": [("PI: ", True, ORANGE), ("6,8% fora; ", False, INK), ("PI+FF antecipado: ", True, NAVY), ("5,1%", False, INK)]},
      {"runs": [("O pico não some: ", True, INK), ("a pressão salta para 4,54 antes de a válvula se mover; com a antecipação, 4,36", False, INK)]}],
     "No C2, três bicos fecham de uma vez em 2 segundos e mais três em 8 segundos, como no ensaio da bancada. O P para em 3,81 e 4,12, praticamente o que a conta do erro com o ganho de malha previa, 3,82 e 4,13. O PI fica 6,8% do tempo fora da faixa, e o feedforward antecipado 5,1%. O pico não some: a pressão salta para 4,54 no instante em que os bicos fecham, porque a válvula ainda está na posição antiga. Com a antecipação de 0,2 s, o pico baixa para 4,36, ainda fora; para sumir, a antecipação teria de ser de cerca de 0,7 s, o tempo da rampa inteira."),
    ("C3", "d_C3.png", 23, "trocas aleatórias rápidas", ORANGE,
     "Um bico sorteado troca a cada 0,1–0,5 s, com n entre 1 e 7 (20 s, 66 trocas): imita a aplicação localizada",
     [{"runs": [("PI: ", True, ORANGE), ("8,3% fora da faixa; ", False, INK), ("PI+FF antecipado: 4,4%", True, NAVY)]},
      {"runs": [("As saídas da faixa ", False, INK), ("acontecem quando várias trocas no mesmo sentido chegam seguidas", True, INK)]},
      {"runs": [("Sem antecipação, o FF ficava pior que o PI (9,5%): ", False, INK), ("antecipar é o que faz a diferença", True, INK)]}],
     "O C3 imita a aplicação localizada: a cada 0,1 a 0,5 segundo um bico sorteado troca de estado, 66 trocas em 20 segundos, mais rápido do que a malha acomoda. O PI fica 8,3% do tempo fora; as saídas acontecem quando várias trocas no mesmo sentido chegam seguidas e a válvula não consegue acompanhar. O feedforward antecipado cai quase pela metade, 4,4%. Sem a antecipação, o mesmo feedforward ficava pior que o PI, 9,5%."),
]
cab_mini = ("Configuração", "Fora da faixa", "IAE")
for cod, arq, nfig, sub, cor, desc, leitura, nota in CENARIOS:
    s = next(cont)
    title(s, f"Cenário {cod}: {sub}")
    hfig = 4.55
    wfig, _ = image(s, FIGS / arq, 0.6, 2.35, h=hfig, name=f"Resposta {cod}")
    caption(s, 0.6, 2.35 + hfig + 0.02, wfig + 0.4, f"Figura {nfig} do TCC. Pressão (faixa de ±10% em verde), abertura da válvula e nº de bicos.")
    x0 = 0.6 + wfig + 0.35
    wr = 12.75 - x0
    box(s, x0, 2.4, wr, 0.78, name="Descrição cenário")
    text(s, x0 + 0.15, 2.43, wr - 0.3, 0.72, [{"t": desc, "s": 14, "c": INK}], anchor=MSO_ANCHOR.MIDDLE, name="Texto descrição")
    rows = [r for r in TAB10 if r[0][0] == cod]
    gt = s.shapes.add_table(len(rows) + 1, 3, Inches(x0), Inches(3.32), Inches(wr), Inches(0.31 * 5))
    gt.name = f"Tabela {cod}"
    tab = gt.table
    for c, wc in enumerate((wr - 2.9, 1.6, 1.3)):
        tab.columns[c].width = Inches(wc)
    for r in range(len(rows) + 1):
        tab.rows[r].height = Inches(0.31)
        if r == 0:
            vals, negrito = cab_mini, range(3)
        else:
            (_, cfg, fora, iae), neg = rows[r - 1]
            vals, negrito = (cfg, fora, iae), {c - 1 for c in neg}
        for c, v in enumerate(vals):
            cell = tab.cell(r, c); cell.text = v
            cell.margin_top = cell.margin_bottom = Inches(0.01)
            cell.margin_left = cell.margin_right = Inches(0.05)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]; rn = p.runs[0]
            rn.font.name = FONT; rn.font.size = Pt(11.5 if r == 0 else 12.5)
            rn.font.bold = r == 0 or c == 0 or c in negrito
            p.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.CENTER
            cell.fill.solid()
            if r == 0:
                rn.font.color.rgb = WHITE; cell.fill.fore_color.rgb = NAVY
            else:
                rn.font.color.rgb = cor_cfg[vals[0]] if c == 0 else INK
                cell.fill.fore_color.rgb = TINT if r % 2 else WHITE
    caption(s, x0, 3.32 + 0.31 * 5 + 0.03, wr, "Negrito: melhor valor do cenário. Fonte: Tabela 9 do TCC.")
    text(s, x0, 5.3, wr, 1.75, [dict(it, bullet=True, s=14.5, space=5) for it in leitura], name="Leitura")
    notes(s, nota)

# ================================================================ antecipação (Fig. 24)
s = next(cont)
title(s, "Por que antecipar: um bico fechando com a válvula real")
w24, h24 = image(s, FIGS / "j_antecipacao.png", 0.6, 2.35, h=4.25, name="Antecipação")
caption(s, 0.6, 2.35 + h24 + 0.02, w24, "Figura 24 do TCC: PI, PI+FF sem antecipação e PI+FF antecipado em 0,2 s.")
x24 = 0.6 + w24 + 0.35
for i, (big, lab, cor) in enumerate([("0,071", "IAE do PI", ORANGE), ("0,083", "FF sem antecipar", MUTED), ("0,064", "FF antecipado 0,2 s", NAVY)]):
    stat(s, x24 + i * ((12.75 - x24) / 3), 2.4, (12.75 - x24) / 3 - 0.1, big, lab, color=cor, big_size=28)
text(s, x24, 3.9, 12.75 - x24, 3.0, [
    {"runs": [("Sem antecipar, o FF não ajuda: ", True, NAVY), ("o PI, lendo em tempo real, já manda abrir no instante da troca; os dois somados passam do ponto (s² no numerador da Eq. 3.28).", False, INK)], "bullet": True, "s": 14, "space": 5},
    {"runs": [("Antecipando, ", True, NAVY), ("a válvula começa a abrir em t = 0,3 s; a pressão cai a 3,44 (dentro da faixa) e o salto vai a 3,79 em vez de 3,83.", False, INK)], "bullet": True, "s": 14, "space": 5},
    {"runs": [("Não há atraso puro para aproveitar ", True, NAVY), ("(o Ex. 7.4 de Castrucci tem): o ganho vem de usar a informação do futuro.", False, INK)], "bullet": True, "s": 14}],
    name="Leitura antecipação")
simbolos(s, [('IAE', 'integral do erro absoluto da troca'), ('T_{ant}', 'antecipação (0,2 s)')])
notes(s, "Esta figura mostra um bico fechando em meio segundo, com a válvula real. Sem antecipação, o feedforward não ajuda: o PI já reage na hora, e somando as duas correções a pressão passa do ponto, o que na função de transferência aparece como o s ao quadrado no numerador. Com a antecipação, a válvula começa a abrir 0,2 segundo antes; a pressão cai um pouco, para 3,44, ainda dentro da faixa, e quando o bico fecha o salto é menor. O IAE dessa troca foi 0,064, contra 0,071 do PI e 0,083 do feedforward sem antecipar. No C3, com 66 trocas, esse ganho se soma.")

# ================================================================ velocidade da válvula
s = next(cont)
title(s, "O gargalo é a velocidade da válvula")
linhas = [("Velocidade máxima da válvula", "C2: PI", "C2: PI+FF", "C3: PI", "C3: PI+FF"),
          ("0,5 s⁻¹ (estimado, curso em 2 s)", "6,8%", "5,1%", "8,3%", "4,4%"),
          ("1,0 s⁻¹ (2× mais rápida)", "3,4%", "2,7%", "0,4%", "0,1%"),
          ("2,0 s⁻¹ (4× mais rápida)", "1,7%", "1,4%", "0,2%", "0,1%")]
gt = s.shapes.add_table(4, 5, Inches(0.6), Inches(2.75), Inches(7.4), Inches(2.4))
gt.name = "Tabela velocidade"
tab = gt.table
for c, wc in enumerate((2.9, 1.125, 1.125, 1.125, 1.125)):
    tab.columns[c].width = Inches(wc)
melhor = {(1, 2), (1, 4), (2, 2), (2, 4), (3, 2), (3, 4)}
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
stat(s, 8.35, 2.55, 4.4, "≈ 0,7 s", "rampa da válvula para 3 bicos (0,36 a 0,5 s⁻¹); a pressão fica fora da faixa 0,4 a 0,5 s", color=ORANGE, big_size=44)
text(s, 8.35, 4.1, 4.4, 2.95, [
    {"t": "O salto da troca acontece com qualquer controlador (valor inicial = Kn·ΔN).", "bullet": True},
    {"t": "O PI pede 1,34 s⁻¹ para um bico; a válvula dá 0,5: anda em rampa.", "bullet": True},
    {"t": "Dobrar a velocidade leva o C3 de 8,3% para 0,4% (PI) e de 4,4% para 0,1% (PI+FF).", "bullet": True}], size=15)
notes(s, "A velocidade da válvula é o que mais pesa no resultado. O salto da troca acontece com qualquer controlador, como o teorema do valor inicial mostrou; o controlador só define a volta, e a volta é limitada pela rampa da válvula: para três bicos ela precisa andar 0,36, cerca de 0,7 segundo. Com a válvula duas vezes mais rápida, o C3 cai para 0,4% com o PI e 0,1% com o feedforward antecipado. O feedforward continua na frente em todas as velocidades.")

# ================================================================ 18. conclusões
s = next(cont)
title(s, "Conclusões")
for i, (cab, desc, cor) in enumerate([
        ("Modelo", "Uma constante de bico (R₁/n²) e uma curva de fonte reproduzem a bancada com erro ≤ 0,7% na pressão", GREEN),
        ("Sintonia", "Ganho da planta igual para todo número de bicos: uma única sintonia por alocação de polos serve para todos os casos", NAVY),
        ("Controle", "O PI zera o erro (C1 100% na faixa); o PI + FF antecipado 0,2 s é o melhor: C3 de 8,3% para 4,4% fora", ORANGE),
        ("Limite", "Três bicos fechando juntos tiram a pressão da faixa por 0,4 s (FF) a 0,5 s (PI): a válvula não é rápida o bastante", MUTED)]):
    y = 2.5 + i * 1.12
    box(s, 0.6, y, 12.15, 1.0, name=f"Conclusão {cab}")
    text(s, 0.8, y + 0.08, 2.1, 0.85, [{"t": cab, "b": True, "s": 19, "c": cor}], anchor=MSO_ANCHOR.MIDDLE, name="Cab")
    text(s, 2.95, y + 0.08, 9.6, 0.85, [{"t": desc, "s": 16}], anchor=MSO_ANCHOR.MIDDLE, name="Texto")
text(s, 0.6, 6.95, 12.15, 0.45, [{"t": "Hipótese confirmada em parte e só em simulação: τa, ωmax e a curva da válvula foram estimados; falta medir a pressão no tempo em bancada.",
                                  "b": True, "s": 15, "c": NAVY}], name="Veredito")
notes(s, "A hipótese foi confirmada em parte e só em simulação. O modelo simples funcionou; como o ganho da planta não depende do número de bicos, uma única sintonia por alocação de polos serve para todos os casos. O PI zera o erro, e o feedforward antecipado em 0,2 segundo foi o melhor dos três. Mas três bicos fechando juntos ainda tiram a pressão da faixa por cerca de meio segundo, e os parâmetros da válvula precisam ser medidos na bancada.")

# ================================================================ 19. trabalhos futuros + obrigado
s = next(cont)
title(s, "Trabalhos futuros")
text(s, 0.6, 2.55, 7.4, 4.4, [
    {"t": "Medir em bancada a velocidade e a curva de abertura da válvula", "bullet": True},
    {"t": "Medir a resposta da malha na bancada e ajustar ζ e ts considerando o ruído do sensor", "bullet": True},
    {"t": "Válvula mais rápida e antecipação ajustada ao tamanho da troca (≈ 0,7 s para 3 bicos)", "bullet": True},
    {"t": "Congelar a integral do PI durante a janela de antecipação", "bullet": True},
    {"t": "Anti-windup também no limite de velocidade (C3 com PI: 8,3% → 3,2% num teste)", "bullet": True},
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
assert next(cont, None) is None, "sobrou slide do modelo"
out = TCC / "docs" / "Apresentacao_Banca_TCC_v25.pptx"
prs.save(str(out))
print("salvo", out)
