"""Monta a apresentação da banca (TCC v25, 20 min) sobre o modelo institucional da UNEMAT.
Versão simples (18/11/2026): sem cartões coloridos nem números em destaque, texto em bullets curtos,
equações em preto, tabelas em grade simples; slide "o que as FTs mostram" retirado; slide introdutório de pulverização e slide da simulação em Python (28 slides).
Versão polida do mesmo dia: build_deck_v25a.py. Anteriores: build_deck_v20.py, build_deck_v19.py, build_deck_v15.py."""
import copy
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt, Emu

AQUI = Path(__file__).parent
TCC = Path("D:/tech/tcc")
EQ = AQUI / "eq"; EQ.mkdir(exist_ok=True)

NAVY = RGBColor(0x1B, 0x35, 0x57)
INK = RGBColor(0x20, 0x20, 0x20)
MUTED = RGBColor(0x60, 0x60, 0x60)
CINZA = RGBColor(0xE4, 0xE4, 0xE4)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Calibri"

prs = Presentation(str(AQUI / "base.pptx"))
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


# 27 slides de conteúdo + capa = 28; o modelo tem 20 → 8 cópias
slides += [duplica_fundo(slides[2]) for _ in range(8)]
cont = iter(slides[1:])


# ---------------------------------------------------------------- helpers
def eq_png(nome, tex, size=22, color="#000000"):
    plt.rcParams["mathtext.fontset"] = "cm"
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, f"${tex}$", fontsize=size, color=color)
    out = EQ / f"{nome}.png"
    fig.savefig(out, dpi=300, transparent=True, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    from PIL import Image
    w, h = Image.open(out).size
    return out, w / 300, h / 300


def eq(slide, nome, tex, x, y, size=20, max_w=None):
    p, w, h = eq_png(nome, tex, size)
    if max_w and w > max_w:
        h, w = h * max_w / w, max_w
    pic = slide.shapes.add_picture(str(p), Inches(x), Inches(y), Inches(w), Inches(h))
    pic.name = f"Eq {nome}"
    return w, h


def _bullet(p, level=0):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(Emu(Inches(0.28 + 0.3 * level))))
    pPr.set("indent", str(-Emu(Inches(0.24))))
    for tag in ("a:buNone", "a:buChar", "a:buAutoNum"):
        for el in pPr.findall(qn(tag)):
            pPr.remove(el)
    pPr.append(pPr.makeelement(qn("a:buChar"), {"char": "•" if level == 0 else "–"}))


def text(slide, x, y, w, h, items, size=17, color=INK, name="Texto"):
    """items: str = bullet; '# texto' = linha sem bullet em negrito; '- texto' = sub-bullet; '~ texto' = linha simples."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(6)
        bold, bullet, level, t = False, True, 0, it
        if it.startswith("# "):
            bold, bullet, t = True, False, it[2:]
        elif it.startswith("- "):
            level, t = 1, it[2:]
        elif it.startswith("~ "):
            bullet, t = False, it[2:]
        r = p.add_run(); r.text = t
        f = r.font; f.name = FONT; f.size = Pt(size - (1 if level else 0)); f.bold = bold; f.color.rgb = color
        if bullet:
            _bullet(p, level)
    return tb


def title(slide, t):
    text(slide, 0.6, 1.62, 12.1, 0.62, [f"# {t}"], size=30, color=NAVY, name="Título")


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
    text(slide, x, y, w, 0.3, [f"~ {t}"], size=11, color=MUTED, name="Fonte")


def tabela(slide, x, y, larg, linhas, size=13, alt=0.3, name="Tabela"):
    gt = slide.shapes.add_table(len(linhas), len(larg), Inches(x), Inches(y), Inches(sum(larg)), Inches(alt * len(linhas)))
    gt.name = name
    tab = gt.table
    tab.first_row = False; tab.horz_banding = False
    for c, wc in enumerate(larg):
        tab.columns[c].width = Inches(wc)
    for r, lin in enumerate(linhas):
        tab.rows[r].height = Inches(alt)
        for c, v in enumerate(lin):
            cell = tab.cell(r, c); cell.text = v
            cell.margin_top = cell.margin_bottom = Inches(0.01)
            cell.margin_left = cell.margin_right = Inches(0.06)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]; rn = p.runs[0]
            rn.font.name = FONT; rn.font.size = Pt(size); rn.font.bold = (r == 0); rn.font.color.rgb = INK
            p.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.CENTER
            cell.fill.solid(); cell.fill.fore_color.rgb = CINZA if r == 0 else WHITE
    return gt


def notes(slide, t):
    slide.notes_slide.notes_text_frame.text = t


def simbolos(slide, t, y=6.98):
    text(slide, 0.6, y, 12.15, 0.4, [f"~ {t}"], size=11, color=MUTED, name="Símbolos")


IMG = TCC / "img"; FIGS = TCC / "simulacao/figuras"; BFIG = TCC / "build/fig"

# ================================================================ 2. título
s = next(cont)
text(s, 0.9, 2.0, 11.5, 1.4, ["# Modelagem de sistema de controle para pulverização agrícola de precisão"], size=34, color=NAVY, name="Título")
text(s, 0.9, 3.5, 11.5, 0.6, ["~ Controle da pressão de uma barra bico a bico com válvula de alívio"], size=20)
text(s, 0.9, 4.55, 8.0, 1.9, ["~ Alex de Jesus Terolti", "~ Orientador: Prof. Dr. Rogério Bastos Quirino",
                              "~ Engenharia Elétrica – UNEMAT, Sinop", "~ TCC II"], size=18, name="Autor")
notes(s, "Apresentar o nome, o orientador e o tema.")

# ================================================================ 3. introdução
s = next(cont)
title(s, "Pulverização agrícola")
text(s, 0.6, 2.45, 6.1, 4.45, [
    "pulverizador de barras: tanque → bomba → mangueiras e válvulas → bicos",
    "aplica defensivos e fertilizantes em forma de gotas",
    "aplicação convencional: mesma dose na área toda, mas daninhas e pragas aparecem em manchas",
    "pulverização localizada: aplica só onde precisa (sensores, imagens, mapas)",
    "controle por seções (grupos de bicos) ou bico a bico (cada bico sozinho)",
    "bico a bico em série: uma mangueira alimenta todos os bicos"], size=16)
image(s, IMG / "sprayer.png", 6.95, 2.4, w=3.1, name="Pulverizador")
caption(s, 6.95, 2.4 + 3.1 / 1.5 + 0.02, 3.1, "Fonte: Kuhn ([2025]).")
image(s, IMG / "fig02_secoes_bicos.png", 10.2, 2.4, w=2.55, name="Seções e bicos")
caption(s, 10.2, 2.4 + 2.55 / 1.24 + 0.02, 2.6, "Seções × bico a bico. Fonte: adaptado de Rosa et al. (2019).")
text(s, 6.95, 4.95, 5.8, 1.95, [
    "a pressão define a vazão de cada bico e o tamanho da gota",
    "no bico a bico, cada troca muda a vazão que a barra pede → a pressão varia",
    "pressão errada → sobredose, subdose e deriva"], size=15)
notes(s, "O pulverizador de barras leva a calda do tanque, pela bomba e pelas mangueiras, até os bicos, que quebram o líquido em gotas. Na aplicação convencional a dose é a mesma na área toda, mas as daninhas e pragas aparecem em manchas. Na pulverização localizada só se aplica onde precisa, desligando seções ou bicos. O bico a bico é o mais preciso, mas, como uma mangueira alimenta todos os bicos, cada troca muda a vazão pedida e a pressão varia. E a pressão é que define quanto sai de cada bico e o tamanho da gota.")

# ================================================================ 4. problema
s = next(cont)
title(s, "Problema")
text(s, 0.6, 2.5, 6.4, 4.4, [
    "quando bicos fecham, sobra líquido na linha e a pressão sobe; quando abrem, cai",
    "bancada de Rosa, Terra e Drews Jr (2019): 3,57 → 5,58 kgf/cm² (+56%) de 7 para 1 bico",
    "no ensaio: fechar 3 bicos leva 4,0 → 5,8; abrindo a válvula de alívio à mão, a pressão volta",
    "vazão do bico q ∝ √P → muda a dose",
    "problema do trabalho: manter a pressão perto do valor desejado enquanto os bicos abrem e fecham"])
image(s, IMG / "fig05_ensaio.png", 7.4, 2.45, h=4.3, name="Ensaio")
caption(s, 7.4, 6.78, 5.4, "Ensaio de regulação pela válvula de alívio. Fonte: Rosa, Terra e Drews Jr (2019).")
notes(s, "Na bancada de referência, de 7 para 1 bico a pressão sobe 56%. No ensaio da figura, fechando três bicos ela vai de 4,0 para 5,8, e abrindo a válvula de alívio à mão ela volta. O problema do trabalho é fazer isso automaticamente.")

# ================================================================ 4. objetivo e hipótese
s = next(cont)
title(s, "Objetivo e hipótese")
text(s, 0.6, 2.5, 12.1, 4.4, [
    "# Hipótese",
    "~ Um modelo de resistências fluídicas (bicos em paralelo, bomba, válvula de alívio) + a dinâmica da válvula basta para projetar um controlador simples que mantenha a pressão em ±10% da referência.",
    "# Objetivos",
    "modelar pressão × vazão × nº de bicos e comparar com os dados publicados",
    "acrescentar a dinâmica da válvula",
    "sintonizar P e PI por alocação de polos e acrescentar o feedforward antecipado",
    "comparar em simulação",
    "~ Tolerância: ±10% na pressão (ISO 16122-2, item 4.5.4) ≈ ±5% na vazão do bico"])
notes(s, "±10% na pressão é a tolerância da norma de inspeção; dá uns 5% na vazão, porque q = K√P.")

# ================================================================ 5. roteiro
s = next(cont)
title(s, "Etapas do trabalho")
w, h = image(s, BFIG / "fig_etapas.png", 0.6, 2.45, h=4.4, name="Figura etapas")
text(s, 0.9 + w, 2.6, 12.7 - (0.9 + w), 4.3, [
    "cada etapa usa o resultado da anterior",
    "o modelo estático é usado no simulador e no projeto do controle",
    "tudo em Python (numpy e matplotlib)"], size=16)
caption(s, 0.6, 2.45 + h + 0.02, w, "Fonte: TCC, Figura 4.")
notes(s, "Ordem da apresentação: dados, modelo estático, modelo dinâmico, controle, simulação.")

# ================================================================ 6. bancada
s = next(cont)
title(s, "Bancada de referência (Rosa, Terra e Drews Jr, 2019)")
image(s, IMG / "overview barra.png", 0.6, 2.5, w=6.0, name="Foto bancada")
caption(s, 0.6, 2.5 + 6.0 / 3.69 + 0.02, 6.0, "Barra de 5 m com 7 bicos. Fonte: Rosa, Terra e Drews Jr (2019).")
image(s, IMG / "fig04_fluxograma.png", 0.6, 4.55, w=4.2, name="Fluxograma bancada")
caption(s, 0.6, 4.55 + 4.2 / 2.19 + 0.02, 4.8, "Fluxograma. Fonte: Rosa, Terra e Drews Jr (2019).")
text(s, 7.0, 2.45, 5.8, 1.5, [
    "bomba de pistão 14 L/min com válvula de mola",
    "7 bicos FanTip 0,2/110° com solenoide",
    "válvula agulha (alívio) com servomotor = atuador"], size=15)
tabela(s, 7.0, 4.0, (0.8, 1.6, 1.5, 1.3), [
    ("n", "P [kgf/cm²]", "Q [L/min]", "P/Q²"),
    ("7", "3,57", "5,60", "0,114"), ("6", "3,88", "5,07", "0,151"), ("5", "4,24", "4,40", "0,219"),
    ("4", "4,64", "3,60", "0,358"), ("3", "4,96", "2,80", "0,633"), ("2", "5,27", "2,00", "1,318"),
    ("1", "5,58", "1,00", "5,580")], size=12, alt=0.32, name="Tabela 1")
caption(s, 7.0, 6.6, 5.4, "Válvula de alívio fechada. Fonte: Rosa, Terra e Drews Jr (2019), Tabela 1.")
notes(s, "Os sete pontos da tabela foram usados para ajustar o modelo. Os autores ajustaram a válvula à mão.")

# ================================================================ 7. modelo estático
s = next(cont)
title(s, "Modelo estático")
image(s, BFIG / "fig06.png", 0.6, 2.4, w=6.6, name="Circuito equivalente")
caption(s, 0.6, 2.4 + 6.6 / 6.32 + 0.02, 6.6, "Fonte: TCC, Figura 11.")
text(s, 7.5, 2.4, 5.3, 0.4, ["~ bico (lei de orifício), K = 0,425:"], size=15)
eq(s, "est0", "q = K\\sqrt{P}", 7.8, 2.8, size=20)
text(s, 7.5, 3.35, 5.3, 0.4, ["~ fonte (bomba + válvula de mola), mínimos quadrados:"], size=15)
eq(s, "est1", "P = a_2 Q_s^2 + a_1 Q_s + a_0", 7.8, 3.75, size=20)
text(s, 7.5, 4.3, 5.3, 0.4, ["~ válvula de alívio, linear na abertura:"], size=15)
eq(s, "est2", "Q_v = K_{v,max}\\,\\alpha\\,\\sqrt{P}", 7.8, 4.7, size=20)
text(s, 0.6, 4.25, 6.6, 0.8, [
    "em regime: entra = sai no nó",
    "juntando bicos e válvula em C, a pressão sai explícita (Eq. 3.11):"], size=15)
eq(s, "cap_saida", "C = n\\,K + K_{v,max}\\,\\alpha", 0.9, 5.15, size=19)
eq(s, "p_explicito", "P(n,\\alpha) = \\left[\\frac{a_1C + \\sqrt{a_1^2C^2 + 4a_0\\left(1 - a_2C^2\\right)}}{2\\left(1 - a_2C^2\\right)}\\right]^2",
   0.9, 5.65, size=19, max_w=6.5)
text(s, 7.5, 5.5, 5.3, 1.2, ["a pressão só depende de C"], size=15)
simbolos(s, "C: capacidade de saída · Qs: vazão da fonte · a2, a1, a0: coef. da fonte · Qv: vazão da válvula · Kv,max: constante da válvula aberta · α: abertura (0 a 1)")
notes(s, "Fonte empurra, bicos e válvula deixam sair. Em regime entra = sai. Com C, sai uma equação de 2º grau em √P e a pressão fica explícita. A pressão só depende de C.")

# ================================================================ 8. R1/n²
s = next(cont)
title(s, "Resistência da barra: R₁/n²")
text(s, 0.6, 2.45, 6.4, 0.4, ["~ este trabalho (1 parâmetro, K):"], size=16)
eq(s, "r1n2", "R_{eq}(n) = \\frac{R_1}{n^2}, \\qquad R_1 = \\frac{1}{K^2}", 0.9, 2.9, size=22, max_w=5.0)
text(s, 0.6, 3.95, 6.4, 0.4, ["~ Rosa, Terra e Drews Jr (2019) (ajuste, 4 coeficientes):"], size=16)
eq(s, "rosa", "R_F(n) = 42{,}59\\,e^{-2{,}335\\,n} + 2{,}307\\,e^{-0{,}4591\\,n}", 0.9, 4.4, size=20, max_w=5.6)
text(s, 0.6, 5.2, 6.4, 1.7, [
    "n bicos iguais em paralelo: resistência de 1 bico ÷ n²",
    "erro relativo máx.: 5,9% (R₁/n²) contra 18,5% (fórmula empírica, n = 7)"], size=16)
image(s, FIGS / "a_resistencia_n.png", 7.3, 2.45, h=4.2, name="Gráfico resistência")
caption(s, 7.3, 6.67, 5.4, "Fonte: TCC, Figura 17.")
notes(s, "Com n bicos em paralelo a resistência é a de um bico dividida por n ao quadrado. Um parâmetro físico em vez de quatro coeficientes; erro máximo 5,9% contra 18,5%.")

# ================================================================ 9. validação
s = next(cont)
title(s, "Validação do modelo estático")
text(s, 0.6, 2.5, 4.6, 4.4, [
    "7 pontos medidos",
    "erro máx. na pressão: 0,7%",
    "erro máx. na vazão: 2,3%",
    "a válvula de alívio só baixa a pressão → Pref < 3,56 kgf/cm² (fonte com 7 bicos)",
    "adotado Pref = 3,5 kgf/cm²"])
image(s, FIGS / "b_fonte_carga.png", 5.5, 2.45, h=4.2, name="Fonte e carga")
caption(s, 5.5, 6.67, 6.5, "Curva da fonte × curvas de carga. Fonte: TCC, Figura 18.")
notes(s, "O modelo reproduziu os sete pontos com erro de até 0,7% na pressão e 2,3% na vazão. Como a válvula só alivia, a referência tem de ficar abaixo de 3,56; foi escolhido 3,5.")

# ================================================================ 10. modelo dinâmico
s = next(cont)
title(s, "Modelo dinâmico")
text(s, 0.6, 2.45, 6.6, 0.4, ["~ pressão (continuidade):"], size=16)
eq(s, "merritt", "\\sum Q_{ent} - \\sum Q_{sai} = \\frac{V}{\\beta}\\,\\frac{dP}{dt}", 0.9, 2.9, size=22, max_w=4.6)
text(s, 0.6, 3.9, 6.6, 0.4, ["~ válvula:"], size=16)
eq(s, "valvula", "\\frac{d\\alpha}{dt} = \\frac{\\alpha_c - \\alpha}{\\tau_a}, \\qquad \\left|\\frac{d\\alpha}{dt}\\right| \\leq \\omega_{max}", 0.9, 4.35, size=21, max_w=5.6)
text(s, 0.6, 5.35, 6.6, 1.6, [
    "pressão considerada instantânea (mangueira curta, V/β pequeno)",
    "válvula: 1ª ordem, τa = 0,2 s, velocidade máx. 0,5 s⁻¹",
    "τa e ωmax estimados",
    "simulação: Euler, passo de 1 ms"], size=16)
image(s, IMG / "valv agulha.png", 8.0, 2.45, h=3.6, name="Válvula agulha")
caption(s, 7.6, 6.1, 5.2, "Válvula agulha com servomotor. Fonte: Rosa, Terra e Drews Jr (2019).")
simbolos(s, "V: volume da linha · β: módulo de compressibilidade · αc: abertura comandada · τa: constante de tempo · ωmax: velocidade máxima da válvula")
notes(s, "A pressão só demora por causa de V sobre beta; a mangueira é curta, então foi tratada como instantânea. A válvula é de primeira ordem com velocidade limitada. Os dois parâmetros são estimados.")

# ================================================================ 11. estratégia
s = next(cont)
title(s, "Estratégia de controle")
image(s, BFIG / "fig07.png", 0.6, 2.4, w=7.3, name="Diagrama de blocos")
caption(s, 0.6, 2.4 + 7.3 / 2.32 + 0.02, 7.3, "Fonte: TCC, Figura 12.")
text(s, 0.6, 5.95, 7.3, 1.0, [
    "controlada: P · manipulada: α · perturbação: n(t)",
    "erro e = P − Pref (pressão alta → abrir a válvula)"], size=15)
text(s, 8.2, 2.4, 4.6, 0.4, ["~ comando (Eq. 3.19):"], size=16)
eq(s, "eq319", "\\alpha_c = \\alpha_{ff}[n(t+T_{ant})] + K_c\\left[e + \\frac{1}{T_i}\\int_0^t e\\,d\\tau\\right]", 8.3, 2.85, size=19, max_w=4.4)
text(s, 8.2, 3.75, 4.6, 3.1, [
    "P: base fixa α₀ = 0,023 e sem integral",
    "PI: base fixa α₀ + integral",
    "PI+FF: base αff do nº de bicos daqui a 0,2 s",
    "anti-windup: integral para no limite de posição"], size=15)
notes(s, "Os três controladores saem da Eq. 3.19: base + proporcional + integral. O P usa base fixa e sem integral; o PI acrescenta a integral; o PI+FF troca a base pela abertura de equilíbrio, 0,2 s antes.")

# ================================================================ 12. abertura de equilíbrio
s = next(cont)
title(s, "Abertura de equilíbrio (feedforward)")
text(s, 0.6, 2.4, 7.0, 0.4, ["~ no nó, com P = Pref:"], size=16)
eq(s, "aff1", "Q_s(P_{ref}) = \\left[n\\,K + K_{v,max}\\,\\alpha\\right]\\sqrt{P_{ref}}", 0.9, 2.85, size=21, max_w=5.5)
text(s, 0.6, 3.55, 7.0, 0.4, ["~ isolando α (Eq. 3.14):"], size=16)
eq(s, "aff2", "\\alpha_{ff}(n) = \\frac{1}{K_{v,max}}\\left[\\frac{Q_s(P_{ref})}{\\sqrt{P_{ref}}} - n\\,K\\right]", 0.9, 4.0, size=22, max_w=5.8)
text(s, 0.6, 5.3, 7.0, 0.4, ["~ é uma reta:"], size=16)
eq(s, "aff3", "\\frac{d\\alpha_{ff}}{dn} = -\\frac{K}{K_{v,max}} = -\\frac{0{,}425}{3{,}5} = -0{,}121", 0.9, 5.75, size=20, max_w=5.0)
text(s, 7.9, 2.4, 4.9, 4.5, [
    "Qs(Pref)/√Pref = 5,72/1,871 = 3,057",
    "αff(7) = 0,023",
    "αff(4) = 0,388",
    "αff(1) = 0,752",
    "0,121 de abertura ≈ 1 bico",
    "válvula leva 0,121/0,5 ≈ 0,24 s → antecipar 0,2 s",
    "0,2 s a 15 km/h ≈ 0,8 m"], size=16)
simbolos(s, "Qs: vazão da fonte · K: constante do bico (0,425) · Kv,max: constante da válvula aberta (3,5)")
notes(s, "No nó, com a pressão na referência, a vazão da fonte sai toda pelos bicos e pela válvula. Isolando alfa sai a Eq. 3.14, uma reta: 0,121 por bico. A válvula leva uns 0,24 s para andar isso, por isso o FF é comandado 0,2 s antes.")

# ================================================================ 13. linearização
s = next(cont)
title(s, "Linearização")
text(s, 0.6, 2.35, 12.0, 0.4, ["~ ponto nominal: 7 bicos, P = 3,5, α₀ = 0,023, C = 3,057, Qs = 5,72 L/min"], size=15, color=MUTED)
tabela(s, 0.6, 2.85, (1.4, 2.6, 3.6), [
    ("Peça", "Não linear", "Reta tangente"),
    ("Bicos", "Qbarra = nK√P", "0,795 ΔN + 0,795 ΔP"),
    ("Válvula", "Qv = Kv,max α √P", "6,55 Δα + 0,022 ΔP"),
    ("Fonte", "Qs(P)", "−1,645 ΔP")], size=14, alt=0.38, name="Tabela 3")
text(s, 0.6, 4.55, 7.6, 0.4, ["~ somando no nó e isolando ΔP:"], size=16)
eq(s, "lin_soma", "-1{,}645\\,\\Delta P = 0{,}795\\,\\Delta N + 0{,}795\\,\\Delta P + 6{,}55\\,\\Delta\\alpha + 0{,}022\\,\\Delta P",
   0.8, 5.0, size=17, max_w=7.0)
eq(s, "lin_res", "\\Delta P = -\\frac{6{,}55}{2{,}462}\\,\\Delta\\alpha - \\frac{0{,}795}{2{,}462}\\,\\Delta N = -2{,}66\\,\\Delta\\alpha - 0{,}323\\,\\Delta N",
   0.8, 5.55, size=18, max_w=7.0)
eq(s, "lin_D", "D = \\frac{C}{2\\sqrt{P}} - \\frac{dQ_s}{dP} = 2{,}462", 8.6, 2.85, size=18, max_w=4.0)
eq(s, "lin_kg", "K_g = -\\frac{K_{v,max}\\sqrt{P}}{D} = -2{,}66", 8.6, 3.65, size=18, max_w=4.0)
eq(s, "lin_kn", "K_n = -\\frac{K\\sqrt{P}}{D} = -0{,}323", 8.6, 4.45, size=18, max_w=4.0)
text(s, 8.5, 5.3, 4.3, 1.6, [
    "Kg e Kn não mudam com n (soma 0,817 fica igual)",
    "→ uma sintonia só para todo n"], size=15)
simbolos(s, "ΔP, Δα, ΔN: desvios em torno do ponto nominal · D: denominador comum · Kg: ganho da planta · Kn: ganho do distúrbio (por bico)")
notes(s, "Cada vazão vira a sua reta tangente (derivadas parciais). Somando no nó e isolando delta P, sai o denominador 2,462 e os ganhos Kg = −2,66 e Kn = −0,323. Com 4 bicos a parcela dos bicos cai e a da válvula sobe, mas a soma é a mesma, então os ganhos não dependem de n.")

# ================================================================ 14. Laplace
s = next(cont)
title(s, "Domínio de Laplace")
w14, h14 = image(s, BFIG / "fig12_freq.png", 0.6, 2.4, w=7.4, name="Diagrama em Laplace")
caption(s, 0.6, 2.4 + h14 + 0.02, 7.4, "Fonte: TCC, Figura 13.")
text(s, 0.6, 2.4 + h14 + 0.45, 7.4, 1.4, [
    "referência fixa: a entrada é só ΔN",
    "saturação, limite de velocidade e anti-windup ficam só no simulador"], size=15)
text(s, 8.3, 2.4, 4.5, 0.35, ["~ planta (Eq. 3.17):"], size=15)
eq(s, "lap0", "\\Delta P(s) = K_g\\,\\Delta A(s) + K_n\\,\\Delta N(s)", 8.5, 2.75, size=17, max_w=4.2)
text(s, 8.3, 3.35, 4.5, 0.35, ["~ válvula (Eq. 3.18):"], size=15)
eq(s, "lap1", "\\frac{\\Delta A}{\\Delta A_c} = \\frac{1}{\\tau_a s + 1}", 8.5, 3.7, size=18, max_w=4.2)
text(s, 8.3, 4.45, 4.5, 0.35, ["~ PI (Eq. 3.22):"], size=15)
eq(s, "lap2", "G_c(s) = K_c\\left(1 + \\frac{1}{T_i\\,s}\\right)", 8.5, 4.8, size=18, max_w=4.2)
text(s, 8.3, 5.55, 4.5, 0.35, ["~ feedforward:"], size=15)
eq(s, "lap3", "\\Delta A_{ff} = -\\frac{K_n}{K_g}\\,\\Delta N", 8.5, 5.9, size=18, max_w=4.2)
simbolos(s, "s: variável de Laplace · ΔA, ΔAc: abertura e comando · τa: constante de tempo da válvula (0,2 s) · Gc(s): controlador")
notes(s, "A planta é estática (só ganhos). A válvula vira 1 sobre tau a s mais 1. O PI é Kc(1 + 1/Ti s). O FF é −Kn/Kg vezes delta N, 0,121 por bico. No diagrama os bicos entram direto na pressão e pelo FF.")

# ================================================================ 15. L(s) e T_n
s = next(cont)
title(s, "Malha fechada")
w15, h15 = image(s, BFIG / "fig_malha_L.png", 0.6, 2.35, w=6.1, name="Malha L(s)")
caption(s, 0.6, 2.35 + h15, 6.1, "Fonte: TCC, Figura 14.")
text(s, 7.0, 2.35, 5.8, 0.4, ["~ substituindo válvula e controlador na planta:"], size=15)
eq(s, "m1", "\\Delta P = K_n\\Delta N + \\frac{K_g}{\\tau_a s + 1}\\left[G_c\\,\\Delta P + \\Delta A_{ff}\\right]", 7.2, 2.8, size=17, max_w=5.4)
eq(s, "m2", "L(s) = \\frac{G_c(s)\\,|K_g|}{\\tau_a s + 1}", 7.2, 3.55, size=18, max_w=3.0)
eq(s, "m3", "T_n(s) = \\frac{\\Delta P}{\\Delta N} = \\frac{K_n}{1 + L(s)}", 7.2, 4.3, size=19, max_w=4.0)
text(s, 0.6, 5.4, 12.0, 0.35, ["~ tirando as frações (Eqs. 3.26 a 3.28):"], size=15)
eq(s, "tf_P", "T_{n,P} = \\frac{K_n(\\tau_a s + 1)}{\\tau_a s + 1 + K_c|K_g|}", 0.8, 5.85, size=16, max_w=3.2)
eq(s, "tf_PI", "T_{n,PI} = \\frac{K_n\\,T_i s(\\tau_a s + 1)}{\\tau_a T_i s^2 + T_i(1 + K_c|K_g|)s + K_c|K_g|}", 4.25, 5.85, size=16, max_w=4.1)
eq(s, "tf_FF", "T_{n,PI+FF} = \\frac{K_n\\,\\tau_a T_i s^2}{\\tau_a T_i s^2 + T_i(1 + K_c|K_g|)s + K_c|K_g|}", 8.6, 5.85, size=16, max_w=4.15)
simbolos(s, "L(s): ganho de malha · Tn(s): bicos → pressão · |Kg| = 2,66 · PI+FF aqui é sem antecipação")
notes(s, "Substituindo, delta P aparece dos dois lados. O produto dos blocos na volta é o ganho de malha L. Fica Tn = Kn/(1+L). PI e PI+FF têm o mesmo denominador.")

# ================================================================ 16. alocação de polos
s = next(cont)
title(s, "Sintonia por alocação de polos")
text(s, 0.6, 2.4, 7.6, 0.4, ["~ especificação: ζ = 0,7 e ts = 0,5 s (2%)"], size=16)
eq(s, "wn", "\\omega_n = \\frac{4}{\\zeta\\,t_s} = \\frac{4}{0{,}7 \\times 0{,}5} = 11{,}43\\ \\mathrm{rad/s}", 0.9, 2.85, size=18, max_w=4.6)
text(s, 0.6, 3.6, 7.6, 0.4, ["~ denominador ÷ τa Ti = forma padrão:"], size=16)
eq(s, "car", "s^2 + \\frac{1 + K_c|K_g|}{\\tau_a}\\,s + \\frac{K_c|K_g|}{\\tau_a T_i} = s^2 + 2\\zeta\\omega_n s + \\omega_n^2", 0.9, 4.05, size=19, max_w=6.9)
eq(s, "kc", "K_c = \\frac{2\\zeta\\omega_n\\tau_a - 1}{|K_g|} = 0{,}827", 0.9, 4.95, size=18, max_w=3.4)
eq(s, "ti", "T_i = \\frac{K_c|K_g|}{\\tau_a\\,\\omega_n^2} = 0{,}084\\ \\mathrm{s}", 4.5, 4.95, size=18, max_w=3.3)
eq(s, "pol", "s^2 + 16{,}0\\,s + 130{,}6 = 0 \\ \\Rightarrow\\ s = -8{,}0 \\pm j\\,8{,}2", 0.9, 5.85, size=19, max_w=6.0)
w16, h16 = image(s, FIGS / "i_plano_s.png", 8.45, 2.38, h=4.15, name="Plano s")
caption(s, 8.45, 2.38 + h16 + 0.02, 4.3, "Fonte: TCC, Figura 19.")
simbolos(s, "ζ: amortecimento · ωn: frequência natural · ts: tempo de acomodação · o P usa o mesmo Kc")
notes(s, "Escolhi zeta 0,7 e ts 0,5 s. Omega n = 11,43. Comparando termo a termo com a forma padrão: Kc = 0,827 e Ti = 0,084 s. Polos em −8 ± j8,2, no canto da região da especificação. O P usa o mesmo Kc.")

# ================================================================ 17. forma discreta + conferência
s = next(cont)
title(s, "Forma discreta e conferência no simulador")
text(s, 0.6, 2.4, 6.6, 0.4, ["~ a cada passo de 1 ms:"], size=16)
eq(s, "d1", "I_k = I_{k-1} + e_k\\,\\Delta t", 0.9, 2.85, size=19, max_w=3.0)
eq(s, "d2", "\\alpha_{c,k} = \\alpha_{ff}[n(t_k + T_{ant})] + K_c\\left(e_k + \\frac{I_k}{T_i}\\right)", 0.9, 3.45, size=19, max_w=5.4)
text(s, 0.6, 4.35, 6.6, 0.4, ["~ exemplo: 7 bicos, P = 3,6 (e = 0,1), I = 0:"], size=16)
eq(s, "d3", "\\alpha_c = 0{,}023 + 0{,}827\\left(0{,}1 + \\frac{0{,}0001}{0{,}084}\\right) = 0{,}107", 0.9, 4.8, size=18, max_w=5.6)
text(s, 0.6, 5.6, 6.6, 1.3, [
    "anti-windup: Ik não soma quando o comando está no limite de posição",
    "PI pede 0,827 × 0,323 / 0,2 = 1,34 s⁻¹, a válvula só anda 0,5 s⁻¹"], size=15)
w17, h17 = image(s, FIGS / "g_funcao_transferencia.png", 7.5, 2.35, h=3.6, name="FT x simulador")
caption(s, 7.5, 2.35 + h17, 3.7, "Fonte: TCC, Figura 20.")
text(s, 11.2, 2.4, 1.6, 3.6, [
    "# sem limite:",
    "~ ts = 0,44 s",
    "~ FT ≈ simulador",
    "# com limite:",
    "~ ts = 0,63 s"], size=13)
simbolos(s, "Ik: integral discreta · ek: erro no passo k · Δt: 1 ms")
notes(s, "A integral vira soma de retângulos. No exemplo a válvula vai de 2,3% para 10,7%. Sem limite de velocidade o PI acomoda em 0,44 s e bate com a FT; com o limite real vai para 0,63 s, porque o PI pede 1,34 por segundo e a válvula dá 0,5.")

# ================================================================ simulação em Python
s = next(cont)
title(s, "Simulação em Python")
w_sim, h_sim = image(s, BFIG / "fig15_simular.png", 0.6, 2.35, h=4.5, name="Laço simular")
x_sim = 0.6 + w_sim + 0.4
text(s, x_sim, 2.4, 12.75 - x_sim, 1.9, [
    "um arquivo só: simulacao/modelo_barra.py (Python 3, numpy e matplotlib)",
    "sem biblioteca de controle: o laço no tempo está escrito no código",
    "ordem: ajusta o modelo estático → ganhos e sintonia → modelo linear → cenários"], size=15)
text(s, x_sim, 3.7, 12.75 - x_sim, 0.4, ["# a cada passo de 1 ms (figura ao lado):"], size=15)
text(s, x_sim + 0.2, 4.08, 12.75 - x_sim, 2.0, [
    "~ 1. troca o nº de bicos se chegou a hora",
    "~ 2. controlador: erro, integral (anti-windup) e comando",
    "~ 3. move a válvula (Euler, limitada a ±ωmax e entre 0 e 1)",
    "~ 4. pressão nova pela bissecção",
    "~ 5. guarda t, P, α e n"], size=14)
text(s, x_sim, 6.0, 12.75 - x_sim, 0.4, ["saída: resultados.json e figuras; conferências automáticas; código no Apêndice A"], size=15)
caption(s, x_sim, 6.55, 12.75 - x_sim, "Figura: laço da função simular. Fonte: TCC, Figura 16.")
notes(s, "Tudo foi feito num único arquivo em Python, só com numpy e matplotlib, sem biblioteca de controle, para cada passo ficar visível no código. O programa ajusta o modelo estático, calcula os ganhos e a sintonia, roda o modelo linear e depois os cenários. A simulação em si é este laço: a cada milissegundo troca os bicos se for a hora, roda o controlador, move a válvula pelo método de Euler com os limites, calcula a pressão nova pela bissecção e guarda os valores. No fim, as séries no tempo dão as métricas e os gráficos.")

# ================================================================ 18. cenários e métricas
s = next(cont)
title(s, "Cenários e métricas")
text(s, 0.6, 2.5, 12.1, 4.4, [
    "C1: 7 → 1 → 7, um bico por vez a cada 2 s (26 s)",
    "C2: degraus de 3 bicos, como no ensaio de Rosa (14 s)",
    "C3: um bico sorteado troca a cada 0,1–0,5 s (20 s, 66 trocas)",
    "métricas: tempo fora da faixa ±10% (3,15 a 3,85 kgf/cm²) e IAE",
    "configurações: malha aberta, P, PI e PI+FF antecipado 0,2 s",
    "C2 e C3 também com a válvula 2× e 4× mais rápida"])
notes(s, "Três cenários, do mais simples ao mais difícil. Critério principal: tempo fora da faixa de ±10%.")

# ================================================================ 19. resultados
s = next(cont)
title(s, "Resultados")
TAB9 = [
    ("C1", "Malha aberta", "69,2%", "24,72"), ("C1", "P", "38,5%", "7,41"), ("C1", "PI", "0,0%", "0,78"), ("C1", "PI+FF", "0,0%", "0,73"),
    ("C2", "Malha aberta", "85,7%", "18,38"), ("C2", "P", "46,3%", "5,90"), ("C2", "PI", "6,8%", "0,83"), ("C2", "PI+FF", "5,1%", "0,65"),
    ("C3", "Malha aberta", "90,5%", "23,26"), ("C3", "P", "50,1%", "7,06"), ("C3", "PI", "8,3%", "3,15"), ("C3", "PI+FF", "4,4%", "2,70"),
]
tabela(s, 0.6, 2.45, (1.0, 2.0, 2.2, 2.2), [("Cenário", "Configuração", "Fora da faixa", "IAE [kgf/cm²·s]")] + TAB9,
       size=13, alt=0.31, name="Tabela 9")
caption(s, 0.6, 2.45 + 13 * 0.31 + 0.05, 7.4, "PI+FF = feedforward antecipado 0,2 s. Fonte: TCC, Tabela 9.")
text(s, 8.4, 2.5, 4.4, 4.4, [
    "P: melhora, mas deixa erro permanente",
    "PI: zera o erro (C1 100% na faixa)",
    "PI+FF antecipado: melhor nos 3 cenários (C3: 8,3% → 4,4%)"])
notes(s, "Sem controle, 69 a 91% do tempo fora. O P reduz mas deixa erro. O PI zera o erro. O PI+FF antecipado é o melhor nos três; no C3 cai quase pela metade.")

# ================================================================ 20–22. um slide por cenário
CENARIOS = [
    ("C1", "c_C1.png", 21, "um bico por vez",
     ["7 → 1 → 7, um bico a cada 2 s",
      "cada troca: salto de cerca de 9,5%, dentro da faixa",
      "P sai da faixa a partir do 4º bico fechado",
      "PI e PI+FF: 100% na faixa (IAE 0,78 e 0,73)"],
     "Cada troca dá um salto de cerca de 9,5%, dentro da faixa. O P sai da faixa a partir do quarto bico fechado. PI e PI+FF ficam 100% na faixa; o FF erra um pouco menos."),
    ("C2", "c_C2.png", 22, "degraus de três bicos",
     ["7 → 4 em 2 s → 1 em 8 s",
      "P para em 3,81 e 4,12 (conta: 3,82 e 4,13)",
      "PI 6,8% fora, PI+FF 5,1%",
      "pico 4,54 com o PI, 4,36 com o PI+FF antecipado"],
     "O P para em 3,81 e 4,12, como a conta do erro previa. PI 6,8% fora, PI+FF 5,1%. O pico não some porque a pressão salta antes de a válvula andar; com a antecipação ele baixa para 4,36."),
    ("C3", "d_C3.png", 23, "trocas aleatórias",
     ["66 trocas em 20 s",
      "PI 8,3% fora, PI+FF antecipado 4,4%",
      "sai da faixa quando várias trocas no mesmo sentido vêm seguidas",
      "FF sem antecipar: 9,5% (pior que o PI)"],
     "PI 8,3% fora, PI+FF antecipado 4,4%. As saídas acontecem quando várias trocas no mesmo sentido chegam seguidas. Sem antecipar, o FF ficava pior que o PI."),
]
for cod, arq, nfig, sub, itens, nota in CENARIOS:
    s = next(cont)
    title(s, f"Cenário {cod}: {sub}")
    wfig, hfig = image(s, FIGS / arq, 0.6, 2.35, h=4.5, name=f"Resposta {cod}")
    caption(s, 0.6, 2.35 + hfig + 0.02, wfig, f"Pressão, abertura e nº de bicos. Fonte: TCC, Figura {nfig}.")
    x0 = 0.6 + wfig + 0.35
    linhas = [("Config.", "Fora", "IAE")] + [(c, f, i) for (k, c, f, i) in TAB9 if k == cod]
    tabela(s, x0, 2.45, (12.75 - x0 - 2.6, 1.3, 1.3), linhas, size=13, alt=0.31, name=f"Tabela {cod}")
    text(s, x0, 4.2, 12.75 - x0, 2.7, itens, size=15)
    notes(s, nota)

# ================================================================ 23. antecipação
s = next(cont)
title(s, "Feedforward antecipado")
w23, h23 = image(s, FIGS / "j_antecipacao.png", 0.6, 2.35, h=4.3, name="Antecipação")
caption(s, 0.6, 2.35 + h23 + 0.02, w23, "Um bico fechando em t = 0,5 s. Fonte: TCC, Figura 24.")
text(s, 0.95 + w23, 2.45, 12.75 - (0.95 + w23), 4.4, [
    "IAE da troca: PI 0,071 · FF sem antecipar 0,083 · FF antecipado 0,064",
    "sem antecipar, PI e FF corrigem juntos e passam do ponto",
    "antecipando, a válvula começa a abrir em t = 0,3 s",
    "a pressão cai a 3,44 antes e o salto vai a 3,79 (contra 3,83)"], size=15)
notes(s, "Sem antecipar, o FF não ajuda: o PI já reage na hora e a soma passa do ponto. Antecipando 0,2 s a válvula começa a abrir antes e o salto fica menor. IAE 0,064 contra 0,071 do PI.")

# ================================================================ 24. velocidade da válvula
s = next(cont)
title(s, "Velocidade da válvula")
tabela(s, 0.6, 2.5, (3.0, 1.15, 1.15, 1.15, 1.15), [
    ("ωmax", "C2 PI", "C2 PI+FF", "C3 PI", "C3 PI+FF"),
    ("0,5 s⁻¹ (estimado)", "6,8%", "5,1%", "8,3%", "4,4%"),
    ("1,0 s⁻¹ (2×)", "3,4%", "2,7%", "0,4%", "0,1%"),
    ("2,0 s⁻¹ (4×)", "1,7%", "1,4%", "0,2%", "0,1%")], size=14, alt=0.45, name="Tabela velocidade")
caption(s, 0.6, 4.35, 7.6, "Tempo fora da faixa. Fonte: TCC, seção 4.6.")
text(s, 8.4, 2.5, 4.4, 4.4, [
    "o salto acontece com qualquer controlador",
    "3 bicos: válvula anda 0,36 → ≈ 0,7 s de rampa",
    "válvula 2× mais rápida: C3 cai para 0,4% (PI) e 0,1% (PI+FF)"], size=16)
notes(s, "A velocidade da válvula é o que mais pesa. Para três bicos a rampa leva uns 0,7 s. Com a válvula duas vezes mais rápida o C3 fica quase zero.")

# ================================================================ 25. conclusões
s = next(cont)
title(s, "Conclusões")
text(s, 0.6, 2.5, 12.1, 4.4, [
    "modelo com 1 constante de bico (R₁/n²) + curva da fonte reproduz a bancada (erro ≤ 0,7% na pressão)",
    "ganho da planta não depende do nº de bicos → uma sintonia por alocação de polos serve para todos",
    "PI zera o erro; PI+FF antecipado 0,2 s foi o melhor (C3: 8,3% → 4,4%)",
    "3 bicos fechando juntos: pressão fora da faixa por 0,4 s (FF) a 0,5 s (PI), a válvula é lenta",
    "hipótese confirmada em parte e só em simulação: τa, ωmax e curva da válvula estimados, falta medir a pressão no tempo na bancada"])
notes(s, "Modelo simples funcionou, uma sintonia serve para todos, o FF antecipado foi o melhor. Trocas triplas ainda saem da faixa. Hipótese confirmada em parte, só em simulação.")

# ================================================================ 26. trabalhos futuros
s = next(cont)
title(s, "Trabalhos futuros")
text(s, 0.6, 2.5, 12.1, 3.9, [
    "medir a velocidade e a curva de abertura da válvula",
    "medir a resposta da malha na bancada e ajustar ζ e ts com o ruído do sensor",
    "válvula mais rápida e antecipação conforme o tamanho da troca (≈ 0,7 s para 3 bicos)",
    "congelar a integral do PI durante a antecipação",
    "anti-windup também no limite de velocidade (C3 com PI: 8,3% → 3,2% num teste)",
    "barras comerciais: perda ao longo da barra e mangueira",
    "validar com registros de campo"], size=17)
text(s, 0.6, 6.4, 12.1, 0.5, ["# Obrigado!"], size=24, color=NAVY, name="Obrigado")
notes(s, "Começar pelo mais importante: medir a válvula. Agradecer e abrir para perguntas.")

assert next(cont, None) is None, "sobrou slide do modelo"
prs.core_properties.title = "Modelagem de sistema de controle para pulverização agrícola de precisão"
prs.core_properties.author = "Alex de Jesus Terolti"
out = TCC / "docs" / "Apresentacao_Banca_TCC_v25.pptx"
prs.save(str(out))
print("salvo", out)
