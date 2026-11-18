"""Converte contexto/NN.md em .docx usando o modelo da UNEMAT (Modelo_TCC_II).

Pré-textuais (capa, rosto, aprovação, ficha) e estilos vêm do modelo; o resto vem do .md.
Uso: py -3 md2docx.py 07   →  build/07_raw.docx (equações em formato linear; o
pós-processamento no Word, post.ps1, as monta e atualiza sumário, listas e numeração).
"""
import re
import struct
import sys
import zipfile
from urllib.parse import unquote
from xml.sax.saxutils import escape

VERSAO = sys.argv[1] if len(sys.argv) > 1 else "07"
MD = rf"D:\tech\tcc\contexto\{VERSAO}.md"
TPL = r"D:\tech\tcc\build\Modelo_TCC_II.docx"
OUT = rf"D:\tech\tcc\build\{VERSAO}_raw.docx"
FIGDIR = r"D:\tech\tcc\simulacao\figuras"
BUILDFIG = r"D:\tech\tcc\build\fig"

TITULO = "MODELAGEM DE SISTEMA DE CONTROLE PARA PULVERIZAÇÃO AGRÍCOLA DE PRECISÃO"
AUTOR = "ALEX DE JESUS TEROLTI"
ORIENTADOR = "Prof. Dr. Rogério Bastos Quirino"
ANO = "2026"
LARG = 9071          # largura útil (16 cm) em twips
EMU_CM = 360000

# ---------------------------------------------------------------------------
# Equações: LaTeX do .md → UnicodeMath (o Word converte para o formato profissional)
# ---------------------------------------------------------------------------
UM = {"alpha": "α", "beta": "β", "tau": "τ", "omega": "ω", "lambda": "λ", "theta": "θ", "varphi": "φ", "rho": "ρ",
      "mu": "μ", "Delta": "Δ", "partial": "∂", "cdot": "⋅", "approx": "≈", "le": "≤", "leq": "≤",
      "ge": "≥", "pm": "±", "Rightarrow": "⇒", "Longleftrightarrow": "⟺", "notin": "∉",
      "infty": "∞", "angle": "∠", "ldots": "…", "cdots": "⋯", "times": "×", "zeta": "ζ", "pi": "π", "omega": "ω", "pm": "±", "to": "→", "{": "{", "}": "}", "%": "%"}
EQ_EXC = {}          # tag → UnicodeMath escrito à mão, se a conversão automática não ficar boa


def _grupo_tex(s, i):
    """Lê {…} ou um único caractere/comando a partir de s[i]; devolve (conteúdo, novo i)."""
    while s[i] == " ":
        i += 1
    if s[i] == "{":
        nivel, j = 1, i + 1
        while nivel:
            nivel += {"{": 1, "}": -1}.get(s[j], 0)
            j += 1
        return s[i + 1:j - 1], j
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def tex2um(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", s[i:])
            cmd, i = m.group(1), i + len(m.group(0))
            if cmd.isalpha():
                while i < len(s) and s[i] == " ":
                    i += 1
            if cmd in ("frac", "tfrac", "dfrac"):
                a, i = _grupo_tex(s, i)
                b, i = _grupo_tex(s, i)
                # espaços isolam a fração; depois de ")" o Word ainda a junta ao termo anterior,
                # então entra um "vezes invisível" (U+2062)
                antes = "".join(out).rstrip()
                sep = "⁢" if antes.endswith((")", "]")) else " "
                num = tex2um(a).strip()
                simples = re.fullmatch(r"[\wͰ-Ͽ]+(_\([^()]*\))?", num)   # 1, K_(g), τ_(1)
                out.append(f"{sep}{num if simples else '(' + num + ')'}/({tex2um(b)}) ")
            elif cmd == "sqrt":
                a, i = _grupo_tex(s, i)
                r = tex2um(a)
                out.append(f"√{r} " if len(r) == 1 else f"√({r})")
            elif cmd in ("mathrm", "text"):
                a, i = _grupo_tex(s, i)
                out.append(f'"{a}"')
            elif cmd in ("max", "min"):
                out.append(f'"{cmd}"')
            elif cmd == "lim":
                if i < len(s) and s[i] == "_":
                    lim, i = _grupo_tex(s, i + 1)
                    out.append(f"lim┬({tex2um(lim)}) ")
                else:
                    out.append("lim ")
            elif cmd in ("sum", "int"):
                op = "∑" if cmd == "sum" else "∫"
                while i < len(s) and s[i] in "_^":
                    marca = s[i]
                    lim, i = _grupo_tex(s, i + 1)
                    op += f"{marca}({tex2um(lim)})"
                while i < len(s) and s[i] == " ":
                    i += 1
                if i < len(s) and s[i] == "{":
                    a, i = _grupo_tex(s, i)
                    out.append(f"{op}▒〖{tex2um(a)}〗")
                else:
                    out.append(op + "▒")
            elif cmd in ("left", "right"):
                continue
            elif cmd in ("quad", "qquad"):
                out.append('"\u2003\u2003" ')
            elif cmd in (",", ";", ":", " "):
                out.append(" ")
            elif cmd == "dot":
                a, i = _grupo_tex(s, i)
                out.append(tex2um(a) + "\u0307")
            elif cmd in UM:
                out.append(UM[cmd])
            else:
                raise ValueError(f"comando LaTeX sem tradução: \\{cmd}")
        elif c in "_^":
            a, i = _grupo_tex(s, i + 1)
            # o espaço final encerra o sub/sobrescrito (sem ele o Word engole o "(" seguinte),
            # exceto quando vem outro sub/sobrescrito logo depois (x_a^b)
            j = i
            while j < len(s) and s[j] == " ":
                j += 1
            fim = "" if j < len(s) and s[j] in "_^" else " "
            # rótulos com palavra (ref, max, ff) vão como texto: ficam em pé e o Word não os
            # trata como função ("max" virava função e desalinhava o parágrafo seguinte)
            rotulo = re.fullmatch(r"[A-Za-z0-9,]+", a) and re.search(r"[A-Za-z]{2,}", a)
            if a == "\\circ":
                out.append("°")
            else:
                out.append(f"{c}({chr(34) + a + chr(34) if rotulo else tex2um(a)}){fim}")
        elif c == "{":
            a, i = _grupo_tex(s, i)
            out.append('","' if a == "," else tex2um(a))
        elif c == " ":
            i += 1
        else:
            out.append(c)
            i += 1
    return "".join(out)

# ---------------------------------------------------------------------------
# XML básico
# ---------------------------------------------------------------------------
def x(t):
    return escape(t, {'"': "&quot;"})


def rpr(b=False, i=False, font=None, sz=None, vert=None, hl=None, color=None):
    s = ""
    if font:
        s += f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
    if b:
        s += "<w:b/><w:bCs/>"
    if i:
        s += "<w:i/><w:iCs/>"
    if color:
        s += f'<w:color w:val="{color}"/>'
    if sz:
        s += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    if hl:
        s += f'<w:highlight w:val="{hl}"/>'
    if vert:
        s += f'<w:vertAlign w:val="{vert}"/>'
    return f"<w:rPr>{s}</w:rPr>" if s else ""


def run(t, **k):
    return f'<w:r>{rpr(**k)}<w:t xml:space="preserve">{x(t)}</w:t></w:r>'


def para(content, style="Paragrafo", jc=None, ind=None, keep=False, pbb=False, num=None, spacing=None,
         extra=""):
    p = f'<w:pStyle w:val="{style}"/>'
    if keep:
        p += "<w:keepNext/>"
    if pbb:
        p += "<w:pageBreakBefore/>"
    if num is not None:
        p += f'<w:numPr><w:ilvl w:val="{num[1]}"/><w:numId w:val="{num[0]}"/></w:numPr>'
    p += extra
    if spacing:
        p += spacing
    if ind:
        p += ind
    if jc:
        p += f'<w:jc w:val="{jc}"/>'
    return f"<w:p><w:pPr>{p}</w:pPr>{content}</w:p>"


def field(instr, placeholder="Clique com o botão direito e escolha Atualizar campo."):
    return (f'<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
            f'<w:r><w:instrText xml:space="preserve"> {x(instr)} </w:instrText></w:r>'
            f'<w:r><w:fldChar w:fldCharType="separate"/></w:r>{run(placeholder)}'
            f'<w:r><w:fldChar w:fldCharType="end"/></w:r>')


# ---------------------------------------------------------------------------
# LaTeX inline → runs (itálico para variáveis, sub/sobrescrito)
# ---------------------------------------------------------------------------
SIMB = {"alpha": "α", "beta": "β", "tau": "τ", "omega": "ω", "lambda": "λ", "theta": "θ", "varphi": "φ", "rho": "ρ",
        "mu": "μ", "Delta": "Δ", "propto": "∝", "int": "∫", "le": "≤", "leq": "≤", "ge": "≥", "pm": "±",
        "cdot": "·", "times": "×", "Longleftrightarrow": "⟺", "approx": "≈", "ldots": "…", "cdots": "⋯",
        "infty": "∞", "Rightarrow": "⇒", "zeta": "ζ", "pi": "π", "to": "→", "partial": "∂", "quad": " ", "qquad": "  ", ",": " ",
        ";": " ", "!": "", "left": "", "right": "", "{": "{", "}": "}", "%": "%"}


def _grupo(s, i):
    """Lê {…} ou um único caractere/comando a partir de s[i]; devolve (conteúdo, novo i)."""
    if s[i] == "{":
        nivel, j = 1, i + 1
        while nivel:
            nivel += {"{": 1, "}": -1}.get(s[j], 0)
            j += 1
        return s[i + 1:j - 1], j
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def _math(s, vert=None, rm=False):
    """Devolve lista de (texto, itálico, vert)."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", s[i:])
            cmd, i = m.group(1), i + len(m.group(0))
            if cmd.isalpha():                       # como no LaTeX, espaço após comando é ignorado
                while i < len(s) and s[i] == " ":
                    i += 1
            if cmd in ("sqrt",):
                arg, i = _grupo(s, i)
                inner = _math(arg, vert, rm)
                txt = "".join(t for t, _, _ in inner)
                out.append(("√", False, vert))
                out += inner if len(txt) <= 1 else [("(", False, vert)] + inner + [(")", False, vert)]
            elif cmd in ("mathrm", "text"):
                arg, i = _grupo(s, i)
                out += _math(arg, vert, True)
            elif cmd in ("frac", "tfrac"):
                a, i = _grupo(s, i)
                b, i = _grupo(s, i)
                out += _math(a, vert, rm) + [("/", False, vert)] + _math(b, vert, rm)
            elif cmd in SIMB:
                ch = SIMB[cmd]
                out.append((ch, ch.isalpha() and ch.islower() and not rm, vert))
            else:
                out.append((cmd, False, vert))
        elif c in "_^":
            arg, i = _grupo(s, i + 1)
            v = "subscript" if c == "_" else "superscript"
            txt = re.sub(r"\\[A-Za-z]+", "x", arg)
            out += _math(arg, v, rm or len(txt) > 1)
        elif c == "{":
            arg, i = _grupo(s, i)
            out += _math(arg, vert, rm)
        elif c == "}":
            i += 1
        elif c == "-":
            out.append(("−", False, vert)); i += 1
        elif c.isalpha():
            out.append((c, not rm, vert)); i += 1
        else:
            out.append((c, False, vert)); i += 1
    return out


def math_runs(s, b=False):
    segs = _math(s)
    xml, cur = "", None
    for t, it, v in segs + [(None, None, None)]:
        if cur and (t is None or (it, v) != cur[1:]):
            xml += run(cur[0], b=b, i=cur[1], vert=cur[2])
            cur = None
        if t is None:
            break
        cur = (cur[0] + t, it, v) if cur else (t, it, v)
    return xml


# ---------------------------------------------------------------------------
# Código Python com cores (paleta parecida com a do VS Code, tema claro)
# ---------------------------------------------------------------------------
PY_KW = {"def", "return", "if", "else", "elif", "for", "while", "in", "and", "or", "not", "import",
         "from", "as", "with", "pass", "break", "continue", "lambda", "None", "True", "False"}
PY_BUILTIN = {"min", "max", "abs", "range", "len", "print", "float", "int", "sum"}
PY_COR = {"kw": "0000FF", "str": "A31515", "com": "008000", "num": "098658", "fn": "795E26"}
PY_TOK = re.compile(r"(?P<com>#.*$)|(?P<str>\"[^\"]*\"|'[^']*')|(?P<num>\b\d+(?:\.\d+)?\b)"
                    r"|(?P<id>[A-Za-z_]\w*)|(?P<out>.)", re.S)


def codigo_cor(linha):
    """Uma linha de código Python → runs coloridos (comentário, texto, número, palavra-chave, função)."""
    pedacos, ant = [], ""                  # [texto, cor]; pedaços seguidos da mesma cor viram um run só
    for m in PY_TOK.finditer(linha):
        tipo, t = m.lastgroup, m.group(0)
        cor = PY_COR.get(tipo)
        if tipo == "id":
            depois = linha[m.end():].lstrip()
            if t in PY_KW:
                cor = PY_COR["kw"]
            elif t in PY_BUILTIN or ant == "def" or depois.startswith("("):
                cor = PY_COR["fn"]
            ant = t
        if pedacos and pedacos[-1][1] == cor:
            pedacos[-1][0] += t
        else:
            pedacos.append([t, cor])
    return "".join(run(t, font="Courier New", sz=18, color=c) for t, c in pedacos)


NOTA = re.compile(r"(\[(?:REF\.|A CONFERIR|ANO|Versão)[^\]]*\])")


def inline(s, b0=False, i0=False, **k):
    """Markdown inline (**, *, `, $) → runs."""
    out, buf, b, it, i = "", "", b0, i0, 0

    def flush():
        nonlocal buf, out
        for parte in NOTA.split(buf):
            if parte:
                out += run(parte, b=b, i=it, hl="yellow" if NOTA.fullmatch(parte) else None, **k)
        buf = ""

    while i < len(s):
        if s.startswith("**", i):
            flush(); b = not b; i += 2
        elif s[i] == "*":
            flush(); it = not it; i += 1
        elif s[i] == "`":
            flush(); j = s.index("`", i + 1)
            out += run(s[i + 1:j], font="Courier New", sz=20); i = j + 1
        elif s[i] == "$":
            flush(); j = s.index("$", i + 1)
            out += math_runs(s[i + 1:j], b); i = j + 1
        else:
            buf += s[i]; i += 1
    flush()
    return out


# ---------------------------------------------------------------------------
# Imagens
# ---------------------------------------------------------------------------
class Midia:
    def __init__(self):
        self.itens = []          # (nome no zip, caminho local)

    def add(self, caminho, larg_cm=15.5, alt_max_cm=15.0):
        with open(caminho, "rb") as f:
            cab = f.read(24)
        w, h = struct.unpack(">II", cab[16:24])
        cx = int(larg_cm * EMU_CM)
        cy = int(cx * h / w)
        if cy > alt_max_cm * EMU_CM:
            cy = int(alt_max_cm * EMU_CM); cx = int(cy * w / h)
        n = len(self.itens) + 1
        self.itens.append((f"media/fig_{n}.png", caminho))
        rid = f"rIdFig{n}"
        return (f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
                f'<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{1000 + n}" name="Figura {n}"/>'
                f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
                f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                f'<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                f'<pic:nvPicPr><pic:cNvPr id="{1000 + n}" name="fig_{n}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
                f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
                f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
                f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
                f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')


# ---------------------------------------------------------------------------
# Tabelas
# ---------------------------------------------------------------------------
def celulas(linha):
    return [c.strip() for c in linha.strip().strip("|").split("|")]


def tabela(linhas):
    cab = celulas(linhas[0])
    corpo = [celulas(l) for l in linhas[2:]]
    ncol = len(cab)
    def peso(c):
        limpa = lambda t: re.sub(r"[$*`\\{}_]", "", t)
        textos = [limpa(r[c]) for r in corpo]
        palavra = max([len(p) + 2 for t in textos for p in t.split()]          # folga para a margem da célula
                      + [1.7 * len(p) for p in limpa(cab[c]).split()] + [1])   # cabeçalho em negrito
        return max(palavra + 2, min(max(len(t) for t in textos + [limpa(cab[c])]), 40), 8)
    tam = [peso(c) for c in range(ncol)]
    larg = [int(LARG * t / sum(tam)) for t in tam]
    larg[-1] = LARG - sum(larg[:-1])
    borda = '<w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
    xml = (f'<w:tbl><w:tblPr><w:tblW w:w="{LARG}" w:type="dxa"/><w:jc w:val="center"/>'
           f'<w:tblBorders>{borda}<w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/></w:tblBorders>'
           f'<w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>'
           + "".join(f'<w:gridCol w:w="{w}"/>' for w in larg) + "</w:tblGrid>")
    for k, row in enumerate([cab] + corpo):
        xml += '<w:tr><w:trPr><w:cantSplit/>' + ("<w:tblHeader/>" if k == 0 else "") + "</w:trPr>"
        for c, w in zip(row, larg):
            bc = ('<w:tcBorders><w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/></w:tcBorders>'
                  if k == 0 else "")
            # tabelas longas (12+ linhas) podem continuar na página seguinte, com o cabeçalho repetido;
            # as duas últimas linhas ficam presas à "Fonte" (desde a v25)
            solta = int(VERSAO) >= 25 and len(corpo) >= 12 and 1 <= k <= len(corpo) - 2
            xml += (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{bc}</w:tcPr>'
                    + para(inline(c, b0=(k == 0)), "TCCTabela", extra='<w:keepNext w:val="0"/>' if solta else "")
                    + "</w:tc>")
        xml += "</w:tr>"
    return xml + "</w:tbl>"


# ---------------------------------------------------------------------------
# Corpo a partir do Markdown
# ---------------------------------------------------------------------------
def legenda(tipo, titulo):
    return para(run(f"{tipo} ") + f'<w:fldSimple w:instr=" SEQ {tipo} \\* ARABIC ">{run("1")}</w:fldSimple>'
                + run(" – ") + inline(titulo), "TCCLegenda", keep=True)


def fonte(txt, jc="center"):
    return para(inline(txt), "TCCFonte", jc=jc)


def titulo_pre(txt):
    return para(run(txt.upper()), "TCCTituloPre", pbb=True)


def corpo(md, midia, sect1):
    linhas = md.split("\n")
    ini = next(i for i, l in enumerate(linhas)
               if l.startswith("## AGRADECIMENTOS") or l.startswith("## EPÍGRAFE") or l.startswith("## RESUMO"))
    fim = next(i for i, l in enumerate(linhas) if l.startswith("# NOTAS DE REVISÃO"))
    L = linhas[ini:fim]
    out, i, ultimo = [], 0, None       # ultimo: 'tabela' | 'figura' | None
    secao = None
    leg_pend = None                    # legenda de figura aguardando imagem/diagrama
    mermaid_png = {"6": "fig06.png", "7": "fig07.png", "8": "figA1.png", "A.1": "figA1.png",   # até a 08
                   "10": "fig06.png", "11": "fig07.png", "12": "figA1.png"}                   # a partir da 09
    if int(VERSAO) >= 13:                                     # a v13 ganhou a figura da válvula agulha (Fig. 3)
        mermaid_png.update({"11": "fig06.png", "12": "fig07.png"})
    if int(VERSAO) >= 15:                                     # a v15 ganhou a figura do roteiro (Fig. 5)
        mermaid_png.update({"11": "fig06.png", "12": "fig07.png"})   # roteiro entrou como Fig. 4 e saiu a antiga Fig. 4
    if int(VERSAO) >= 21:                                     # a v21 ganhou as Figs. 4 e 5 (linearização, plano s)
        mermaid_png.update({"13": "fig06.png", "14": "fig07.png"})
    if int(VERSAO) >= 25:                                     # a v25 tirou as Figs. 4 e 5 (reta tangente, plano s didático)
        mermaid_png.update({"11": "fig06.png", "12": "fig07.png"})
    while i < len(L):
        l = L[i]
        s = l.strip()
        if not s or s == "---":
            i += 1; continue
        # --- seções
        if l.startswith("## ") and not re.match(r"## \d", l):
            nome = l[3:].strip()
            secao = nome
            if nome == "LISTA DE ABREVIATURAS E SIGLAS":      # ordem do modelo: ilustrações, tabelas, siglas
                out.append(titulo_pre("Lista de ilustrações"))
                out.append(para(field('TOC \\h \\z \\c "Figura"'), "TCCSemInd"))
                out.append(titulo_pre("Lista de tabelas"))
                out.append(para(field('TOC \\h \\z \\c "Tabela"'), "TCCSemInd"))
                if "**Quadro " in md:
                    out.append(titulo_pre("Lista de quadros"))
                    out.append(para(field('TOC \\h \\z \\c "Quadro"'), "TCCSemInd"))
            if nome == "SUMÁRIO":
                out.append(titulo_pre("Sumário"))
                out.append(para(field('TOC \\o "1-3" \\h \\z \\u'), "TCCSemInd"))
                out.append(f"<w:p><w:pPr>{sect1}</w:pPr></w:p>")
                while i + 1 < len(L) and not L[i + 1].startswith("# "):
                    i += 1
                i += 1; continue
            if nome == "EPÍGRAFE":                            # sem título, no pé da página (NBR 14724)
                out.append(para("", "TCCSemInd", pbb=True, spacing='<w:spacing w:before="9600" w:after="0"/>'))
                i += 1; continue
            out.append(titulo_pre(nome))
            i += 1; continue
        if l.startswith("# "):
            nome = l[2:].strip()
            secao = nome
            numerado = bool(re.match(r"\d", nome))
            out.append(para(run(nome.upper()), "Ttulo1", jc=None if numerado else "center", pbb=True))
            i += 1; continue
        if l.startswith("## "):
            out.append(para(inline(l[3:].strip()), "Ttulo2", keep=True)); i += 1; continue
        if l.startswith("### "):
            out.append(para(inline(l[4:].strip()), "Ttulo3", keep=True)); i += 1; continue
        # --- siglas: tabela vira linhas "SIGLA – significado"
        if secao == "LISTA DE ABREVIATURAS E SIGLAS" and s.startswith("|"):
            for row in L[i + 2:]:
                if not row.startswith("|"):
                    break
                a, b = celulas(row)
                out.append(para(run(f"{a} – ") + inline(b), "TCCSemInd"))
                i += 1
            i += 2; continue
        # --- tabela
        if s.startswith("|"):
            j = i
            while j < len(L) and L[j].strip().startswith("|"):
                j += 1
            out.append(tabela(L[i:j]))
            ultimo = "tabela"; i = j; continue
        # --- equação destacada
        if s.startswith("$$"):
            mt = re.search(r"\\tag\{([^}]+)\}", s)       # sem \tag: conta intermediária, sem número
            tag = mt.group(1) if mt else None
            tex = re.sub(r"\\tag\{[^}]+\}", "", s.strip().strip("$"))
            um = (EQ_EXC.get(tag) or tex2um(tex)).rstrip()
            out.append(para('<m:oMathPara><m:oMath><m:r><m:t xml:space="preserve">'
                            + x(f"{um} #({tag})" if tag else um) + "</m:t></m:r></m:oMath></m:oMathPara>",
                            "TCCEquacao"))
            i += 1; continue
        # --- bloco de código / mermaid
        if s.startswith("```"):
            j = i + 1
            while not L[j].strip().startswith("```"):
                j += 1
            if s == "```mermaid":
                num = leg_pend
                out.append(para(midia.add(f"{BUILDFIG}\\{mermaid_png[num]}"), "TCCFigura", keep=True))
                ultimo = "figura"; leg_pend = None
            else:
                cod = L[i + 1:j]
                inteiro = (secao or "").startswith("APÊNDICE")   # código completo do apêndice: pode quebrar entre páginas
                for c in cod:                      # keepNext em todas: o bloco (e a "Fonte" logo depois) não se divide entre páginas
                    linha = (codigo_cor(c) if s == "```python"
                             else run(c, font="Courier New", sz=18))
                    out.append(para(linha, "TCCCodigo", keep=not inteiro, extra="" if inteiro else "<w:keepLines/>"))
            i = j + 1; continue
        # --- figura descrita (blockquote)
        if s.startswith(">"):
            j = i
            bloco = []
            while j < len(L) and L[j].strip().startswith(">"):
                bloco.append(L[j].strip().lstrip(">").strip()); j += 1
            m = re.match(r"\*\*Figura (\S+) – (.+?)\*\*$", bloco[0])
            out.append(legenda("Figura", m.group(2)))
            desc = bloco[1].strip("*").strip("[]")
            out.append(para(inline(desc, i0=True), "TCCDescricao", keep=True))
            out.append(fonte(bloco[2]))
            i = j; ultimo = "figura"; continue
        # --- legenda de figura/tabela
        m = re.match(r"\*\*(Figura|Tabela|Quadro) (\S+) – (.+?)\*\*$", s)
        if m:
            out.append(legenda(m.group(1), m.group(3)))
            if m.group(1) == "Figura":
                leg_pend = m.group(2)
            i += 1; continue
        # --- imagem
        m = re.match(r"!\[[^\]]*\]\(\.\./([^)]+)\)(?:\{width=(\d+)%(?:;altmax=(\d+))?\})?", s)
        if m:
            raiz = FIGDIR.rsplit("\\", 2)[0]                      # D:\tech\tcc
            arq = unquote(m.group(1)).replace("/", chr(92))
            larg = 15.5 * int(m.group(2)) / 100 if m.group(2) else 15.5   # {width=60%} → 60% da largura
            alt = float(m.group(3)) if m.group(3) else 15.0                  # {width=80%;altmax=21} → até 21 cm de altura
            out.append(para(midia.add(f"{raiz}\\{arq}", larg_cm=larg, alt_max_cm=alt), "TCCFigura", keep=True))
            leg_pend = None; ultimo = "figura"; i += 1; continue
        # --- fonte / nota de tabela
        if s.startswith("Fonte:") or (ultimo == "tabela" and "Fonte:" in s):
            out.append(fonte(s, "left" if ultimo == "tabela" else "center"))
            ultimo = None; i += 1; continue
        ultimo = None
        # --- listas
        m = re.match(r"^( *)- (.*)", l)
        if m:
            nivel = min(len(m.group(1)) // 2, 1)
            out.append(para(inline(m.group(2)), "Paragrafo", num=(90, nivel),
                            ind=f'<w:ind w:left="{720 + 360 * nivel}" w:hanging="360"/>'))
            i += 1; continue
        # --- parágrafos especiais
        if secao in ("RESUMO", "ABSTRACT"):
            out.append(para(inline(s), "TCCSemInd", spacing='<w:spacing w:after="240"/>'))
        elif secao == "EPÍGRAFE":
            out.append(para(inline(s), "TCCSemInd", jc="right",
                            ind='<w:ind w:left="2268"/>', spacing='<w:spacing w:after="0"/>'))
        elif secao == "REFERÊNCIAS":
            out.append(para(inline(s), "TCCRef"))
        else:
            out.append(para(inline(s), "Paragrafo"))
        i += 1
    return "".join(out)


# ---------------------------------------------------------------------------
# Pré-textuais do modelo
# ---------------------------------------------------------------------------
def troca_texto(p, novo, hl=None):
    runs = [m for m in re.finditer(r"<w:r[ >](?:(?!<w:r[ >]).)*?</w:r>", p, re.S) if "<w:t" in m.group(0)]
    r0 = runs[0].group(0)
    rp = re.search(r"<w:rPr>.*?</w:rPr>", r0, re.S)
    rp = rp.group(0) if rp else "<w:rPr></w:rPr>"
    if hl:
        rp = rp.replace("</w:rPr>", f'<w:highlight w:val="{hl}"/></w:rPr>')
    novo_r = f'<w:r>{rp}<w:t xml:space="preserve">{x(novo)}</w:t></w:r>'
    for m in reversed(runs[1:]):
        p = p[:m.start()] + p[m.end():]
    return p[:runs[0].start()] + novo_r + p[runs[0].end():]


def filhos_body(doc):
    """Elementos de primeiro nível de <w:body> (parágrafos podem conter caixas de texto aninhadas)."""
    body = doc[doc.find("<w:body>") + 8:doc.rfind("</w:body>")]
    itens, prof, ini = [], 0, 0
    for m in re.finditer(r"<(/?)w:(p|tbl|sectPr)([ >/])", body):
        fecha, auto = m.group(1) == "/", False
        if not fecha:
            fim_tag = body.index(">", m.start())
            auto = body[fim_tag - 1] == "/"
            if prof == 0:
                ini = m.start()
            if not auto:
                prof += 1
            elif prof == 0:
                itens.append(body[ini:fim_tag + 1])
        else:
            prof -= 1
            if prof == 0:
                itens.append(body[ini:body.index(">", m.start()) + 1])
    return itens


def pretextuais(doc):
    itens = filhos_body(doc)
    texto = ["".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)) for p in itens]
    ded = next(k for k, t in enumerate(texto) if "DEDICAT" in t)
    t = dict(enumerate(itens))
    sub = {7: AUTOR, 20: TITULO, 49: AUTOR, 62: TITULO,
           67: f"Orientador: {ORIENTADOR}",
           91: AUTOR, 94: TITULO,
           100: "Prof. Dr. André do Amaral Penteado Biscaro", 101: "Avaliador(a)",
           107: "Prof. Mr. Reginne Michelli Silva Iocca", 108: "Avaliador(a)",
           114: ORIENTADOR, 115: "Professor Orientador",
           121: "Prof. Dr. Adriana Souza Resende"}
    for k, novo in sub.items():
        t[k] = troca_texto(itens[k], novo)
    # ficha catalográfica: caixa de texto com parágrafos internos (pode aparecer 2× por compatibilidade)
    ficha = {"SOBRENOME": "TEROLTI, Alex de Jesus",
             "Título do Trabalho": "Modelagem de sistema de controle para pulverização agrícola de precisão / "
                                   "Alex de Jesus Terolti. Sinop, MT, 2026.",
             "Orientador:": f"Orientador: {ORIENTADOR}",
             "Sinop, ": "Sinop, [SEMESTRE] de 2026."}
    k = next(k for k, p in enumerate(itens) if "SOBRENOME" in p)

    def troca_ficha(m):
        p = m.group(0)
        txt = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
        for ini, novo in ficha.items():
            if txt.startswith(ini):
                return troca_texto(p, novo, hl="yellow" if "[" in novo else None)
        return p
    if int(VERSAO) < 25:   # desde a v25 a ficha fica igual ao modelo (pedido do autor): gerada depois no site da biblioteca
        t[k] = re.sub(r"<w:p[ >](?:(?!<w:p[ >]).)*?</w:p>", troca_ficha, itens[k], flags=re.S)
    for k in (41, 79):
        t[k] = troca_texto(itens[k], ANO)
    # curso e faculdade logo abaixo da universidade, na capa
    extra = "".join(troca_texto(itens[0], s) for s in
                    ("FACULDADE DE CIÊNCIAS EXATAS E TECNOLÓGICAS", "CURSO DE BACHARELADO EM ENGENHARIA ELÉTRICA"))
    ordem = [0, "extra"] + list(range(5, 80)) + list(range(87, ded))   # sem errata (80–86)
    return "".join(extra if k == "extra" else t[k] for k in ordem)


# ---------------------------------------------------------------------------
# Estilos e numeração acrescentados ao modelo
# ---------------------------------------------------------------------------
ARIAL = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'


def estilo(sid, nome, ppr, rpr_, base="Normal", outline=None):
    o = f'<w:outlineLvl w:val="{outline}"/>' if outline is not None else ""
    return (f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="{sid}"><w:name w:val="{nome}"/>'
            f'<w:basedOn w:val="{base}"/><w:qFormat/><w:pPr>{ppr}{o}</w:pPr><w:rPr>{ARIAL}{rpr_}</w:rPr></w:style>')


def estilos(sty):
    # título 1 do modelo: Arial 12, negrito, maiúsculas
    sty = re.sub(r'(<w:style [^>]*w:styleId="Ttulo1"[^>]*>.*?<w:rPr>).*?(</w:rPr>)',
                 lambda m: m.group(1) + ARIAL + '<w:b/><w:bCs/><w:caps/><w:sz w:val="24"/><w:szCs w:val="24"/>'
                 + m.group(2), sty, count=1, flags=re.S)
    sty = re.sub(r'(<w:style [^>]*w:styleId="Ttulo1"[^>]*>.*?<w:pPr>).*?(</w:pPr>)',
                 r'\1<w:keepNext/><w:spacing w:before="0" w:after="360" w:line="360" w:lineRule="auto"/>'
                 r'<w:outlineLvl w:val="0"/>\2', sty, count=1, flags=re.S)
    sz = '<w:sz w:val="24"/><w:szCs w:val="24"/>'
    sz10 = '<w:sz w:val="20"/><w:szCs w:val="20"/>'
    sp15 = '<w:spacing w:before="0" w:after="0" w:line="360" w:lineRule="auto"/>'
    sp1 = '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
    novos = [
        estilo("Ttulo2", "heading 2", '<w:keepNext/><w:spacing w:before="360" w:after="240" w:line="360" w:lineRule="auto"/>',
               "<w:b/><w:bCs/>" + sz, outline=1),
        estilo("Ttulo3", "heading 3", '<w:keepNext/><w:spacing w:before="240" w:after="240" w:line="360" w:lineRule="auto"/>',
               sz, outline=2),
        estilo("TCCTituloPre", "TCC Título pré-textual", '<w:spacing w:before="0" w:after="480"/><w:jc w:val="center"/>',
               "<w:b/><w:bCs/>" + sz),
        estilo("TCCSemInd", "TCC Texto sem recuo", sp15 + '<w:jc w:val="both"/>', sz),
        estilo("TCCLegenda", "TCC Legenda", '<w:keepNext/><w:spacing w:before="240" w:after="60"/><w:jc w:val="center"/>', sz10),
        estilo("TCCFonte", "TCC Fonte", '<w:spacing w:before="60" w:after="240"/>', sz10),
        estilo("TCCFigura", "TCC Figura", '<w:keepNext/><w:spacing w:before="0" w:after="0"/><w:jc w:val="center"/>', sz),
        estilo("TCCDescricao", "TCC Descrição de figura",
               '<w:keepNext/><w:pBdr><w:top w:val="dashed" w:sz="6" w:space="4" w:color="808080"/>'
               '<w:left w:val="dashed" w:sz="6" w:space="4" w:color="808080"/><w:bottom w:val="dashed" w:sz="6" w:space="4" w:color="808080"/>'
               '<w:right w:val="dashed" w:sz="6" w:space="4" w:color="808080"/></w:pBdr>'
               '<w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>' + sp1 + '<w:ind w:left="567" w:right="567"/><w:jc w:val="both"/>',
               '<w:color w:val="595959"/>' + sz10),
        estilo("TCCTabela", "TCC Tabela", '<w:keepNext/><w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>', sz10),
        estilo("TCCRef", "TCC Referência", '<w:spacing w:before="0" w:after="240" w:line="240" w:lineRule="auto"/>', sz),
        estilo("TCCCodigo", "TCC Código", sp1 + '<w:ind w:left="284"/>',
               '<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/>' + sz10),
        estilo("TCCEquacao", "TCC Equação",
               f'<w:tabs><w:tab w:val="center" w:pos="{LARG // 2}"/><w:tab w:val="right" w:pos="{LARG}"/></w:tabs>'
               '<w:spacing w:before="120" w:after="120"/>', sz),
    ]
    # sumário e listas em Arial 12 (toc 1 vem do modelo; toc 2/3 são acrescentados)
    sty = re.sub(r'(<w:style [^>]*w:styleId="Sumrio1"[^>]*>.*?)(</w:style>)',
                 lambda m: m.group(1) + '<w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9061"/></w:tabs>'
                 '<w:spacing w:after="60"/></w:pPr><w:rPr>' + ARIAL + "<w:b/><w:caps/>" + sz + "</w:rPr>" + m.group(2),
                 sty, count=1, flags=re.S)
    for n, ind in ((2, 240), (3, 480)):
        novos.append(f'<w:style w:type="paragraph" w:styleId="Sumrio{n}"><w:name w:val="toc {n}"/>'
                     f'<w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:unhideWhenUsed/>'
                     f'<w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9061"/></w:tabs><w:spacing w:after="60"/>'
                     f'<w:ind w:left="{ind}"/></w:pPr><w:rPr>{ARIAL}{sz}</w:rPr></w:style>')
    return sty.replace("</w:styles>", "".join(novos) + "</w:styles>")


def numeracao(num):
    lvl = "".join(
        f'<w:lvl w:ilvl="{k}"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="{c}"/>'
        f'<w:lvlJc w:val="left"/><w:pPr><w:ind w:left="{720 + 360 * k}" w:hanging="360"/></w:pPr>'
        f'<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:hint="default"/></w:rPr></w:lvl>'
        for k, c in enumerate("•–"))
    absn = f'<w:abstractNum w:abstractNumId="90"><w:multiLevelType w:val="hybridMultilevel"/>{lvl}</w:abstractNum>'
    k = num.find("<w:num ")
    num = num[:k] + absn + num[k:]
    return num.replace("</w:numbering>", '<w:num w:numId="90"><w:abstractNumId w:val="90"/></w:num></w:numbering>')


# ---------------------------------------------------------------------------
def main():
    zin = zipfile.ZipFile(TPL)
    doc = zin.read("word/document.xml").decode("utf-8")
    raiz = doc[:doc.find("<w:body>")]
    for pfx, uri in (("m", "http://schemas.openxmlformats.org/officeDocument/2006/math"),
                     ("wp", "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"),
                     ("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")):
        if f"xmlns:{pfx}=" not in raiz:
            raiz = raiz.replace("<w:document ", f'<w:document xmlns:{pfx}="{uri}" ', 1)
    sects = re.findall(r"<w:sectPr.*?</w:sectPr>", doc, re.S)
    sect1 = re.sub(r"<w:pgNumType[^>]*/>", "", sects[0])
    sect2 = sects[-1]

    midia = Midia()
    md = open(MD, encoding="utf-8").read().replace("não consta de `contexto/`", "não consta de contexto/")
    xml = raiz + "<w:body>" + pretextuais(doc) + corpo(md, midia, sect1) + sect2 + "</w:body></w:document>"

    rels = zin.read("word/_rels/document.xml.rels").decode("utf-8")
    rels = rels.replace("</Relationships>", "".join(
        f'<Relationship Id="rIdFig{n}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
        f'Target="{nome}"/>' for n, (nome, _) in enumerate(midia.itens, 1)) + "</Relationships>")
    ct = zin.read("[Content_Types].xml").decode("utf-8")
    if 'Extension="png"' not in ct:
        ct = ct.replace("<Default ", '<Default Extension="png" ContentType="image/png"/><Default ', 1)

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for item in zin.infolist():
            nome = item.filename
            dados = zin.read(nome)
            if nome == "word/document.xml":
                dados = xml.encode("utf-8")
            elif nome == "word/styles.xml":
                dados = estilos(dados.decode("utf-8")).encode("utf-8")
            elif nome == "word/numbering.xml":
                dados = numeracao(dados.decode("utf-8")).encode("utf-8")
            elif nome == "word/_rels/document.xml.rels":
                dados = rels.encode("utf-8")
            elif nome == "[Content_Types].xml":
                dados = ct.encode("utf-8")
            elif nome == "word/settings.xml" and int(VERSAO) >= 25:
                # não comprimir as imagens (o Word reduzia as figuras para ~200 ppi no PDF)
                st = dados.decode("utf-8")
                if "doNotAutoCompressPictures" not in st:
                    marcas = ["<w:forceUpgrade", "<w:captions", "<w:readModeInkLockDown", "<w:smartTagType",
                              "<sl:schemaLibrary", "<w:shapeDefaults", "<w:doNotEmbedSmartTags",
                              "<w:decimalSymbol", "<w:listSeparator", "</w:settings>"]
                    pos = min(st.index(m) for m in marcas if m in st)
                    st = st[:pos] + "<w:doNotAutoCompressPictures/>" + st[pos:]
                dados = st.encode("utf-8")
            z.writestr(item, dados)
        for nome, caminho in midia.itens:
            z.write(caminho, f"word/{nome}")
    print(f"{OUT}: {len(midia.itens)} imagens, {xml.count('<m:oMath>')} equações")


if __name__ == "__main__":
    main()
