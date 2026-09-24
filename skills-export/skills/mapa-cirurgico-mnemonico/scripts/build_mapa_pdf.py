#!/usr/bin/env python3
"""
build_mapa_pdf.py
Gera um PDF A4 de uma página com o mapa mnemônico cirúrgico,
a partir de um JSON parametrizado.

Uso:
    python3 build_mapa_pdf.py --input dados.json --output mapa.pdf

Schema do JSON: ver references/schema.md
"""
import argparse
import json
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

# ============= Paleta fixa =============
NAVY = HexColor("#1f3a5f")
NAVY_TEXT = HexColor("#cfe1f7")
BLUE = HexColor("#2b6cb0")
RED = HexColor("#c1432a")
RED_BG = HexColor("#fff5f0")
YELLOW_BG = HexColor("#fffbe6")
YELLOW_LINE = HexColor("#d4b94a")
YELLOW_DARK = HexColor("#7a5b00")
YELLOW_ITALIC = HexColor("#5a4400")
GOLD = HexColor("#ffd89e")
BG = HexColor("#fafaf7")
WHITE = HexColor("#ffffff")
DARK = HexColor("#1a1a1a")
GRAY = HexColor("#333333")
LIGHT_GRAY = HexColor("#d4d4d0")
LINE_GRAY = HexColor("#9ca3af")
SOFT = HexColor("#e5e5e5")
FOOT = HexColor("#666666")

PAGE_W, PAGE_H = A4   # 595 x 842 pt
SVG_W, SVG_H = 720, 920

SCALE = min((PAGE_W - 40) / SVG_W, (PAGE_H - 40) / SVG_H)
OFFSET_X = (PAGE_W - SVG_W * SCALE) / 2
OFFSET_Y_TOP = 20


# ============= Helpers de coordenadas =============
def tx(x): return OFFSET_X + x * SCALE
def ty(y): return PAGE_H - OFFSET_Y_TOP - y * SCALE
def s(v): return v * SCALE


def stroke_rect(c, x, y, w, h, fill_color, stroke_color, stroke_w, radius=0):
    c.setFillColor(fill_color)
    c.setStrokeColor(stroke_color)
    c.setLineWidth(stroke_w * SCALE)
    c.roundRect(tx(x), ty(y + h), s(w), s(h), s(radius), stroke=1, fill=1)


def circle(c, cx, cy, r, color):
    c.setFillColor(color)
    c.setStrokeColor(color)
    c.circle(tx(cx), ty(cy), s(r), stroke=0, fill=1)


def text(c, x, y, txt, size, color, bold=False, italic=False, anchor='start'):
    font = "Helvetica"
    if bold and italic:
        font = "Helvetica-BoldOblique"
    elif bold:
        font = "Helvetica-Bold"
    elif italic:
        font = "Helvetica-Oblique"
    c.setFont(font, size * SCALE)
    c.setFillColor(color)
    px, py = tx(x), ty(y)
    if anchor == 'middle':
        c.drawCentredString(px, py, txt)
    elif anchor == 'end':
        c.drawRightString(px, py, txt)
    else:
        c.drawString(px, py, txt)


def line(c, x1, y1, x2, y2, color, width=1):
    c.setStrokeColor(color)
    c.setLineWidth(width * SCALE)
    c.line(tx(x1), ty(y1), tx(x2), ty(y2))


# ============= Geometria fixa dos blocos =============
TEMPO_LAYOUT = [
    # (y, h, warn)
    (110, 78, False),
    (200, 78, False),
    (290, 86, True),
    (388, 100, True),
    (500, 82, False),
]

TABU_LAYOUT = [
    (110, 98),
    (220, 98),
    (330, 98),
    (440, 86),
]


# ============= Render principal =============
def render(data, output_path):
    c = canvas.Canvas(str(output_path), pagesize=A4)

    # Background
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Header
    c.setFillColor(NAVY)
    c.rect(tx(0), ty(62), s(SVG_W), s(62), fill=1, stroke=0)
    text(c, 20, 30, data["cirurgia"], 20, WHITE, bold=True)
    text(c, 20, 50, data.get("subtitulo",
        "5 TEMPOS CIRÚRGICOS  ·  4 ESTRUTURAS-TABU"), 11, NAVY_TEXT)

    # Coluna esquerda — header
    text(c, 20, 92, "SEQUÊNCIA OPERATÓRIA", 12, NAVY, bold=True)
    line(c, 20, 98, 420, 98, NAVY, 1)

    # 5 tempos
    tempos = data["tempos"]
    assert len(tempos) == 5, "Schema requer exatamente 5 tempos"
    for i, tempo in enumerate(tempos):
        y, h, warn = TEMPO_LAYOUT[i]
        fill = RED_BG if warn else WHITE
        stroke = RED if warn else LIGHT_GRAY
        sw = 1.5 if warn else 1
        stroke_rect(c, 20, y, 400, h, fill, stroke, sw, radius=8)

        # número
        cx_circle = 50
        cy_circle = y + 39 if h == 78 else (y + 43 if h == 86 else (y + 49 if h == 100 else y + 41))
        circle(c, cx_circle, cy_circle, 20, BLUE)
        text(c, cx_circle, cy_circle + 8, str(i + 1), 22, WHITE, bold=True, anchor='middle')

        # título e linhas
        text(c, 82, y + 22, tempo["titulo"], 14, DARK, bold=True)
        linhas = tempo.get("linhas", [])
        for j, ln in enumerate(linhas[:3]):
            text(c, 82, y + 41 + j * 16, ln, 12, GRAY)

        # alerta (apenas em tempos warn)
        if warn and "alerta" in tempo:
            alerta_y = y + 41 + 3 * 16 + 4
            text(c, 82, alerta_y, "⚠ " + tempo["alerta"], 11, RED, bold=True)

        # conector vertical entre tempos
        if i < 4:
            line(c, 50, y + h, 50, TEMPO_LAYOUT[i + 1][0], LINE_GRAY, 1.5)

    # Coluna direita — header
    text(c, 440, 92, "ESTRUTURAS-TABU", 12, RED, bold=True)
    line(c, 440, 98, 700, 98, RED, 1)

    # 4 estruturas-tabu
    tabus = data["estruturas_tabu"]
    assert len(tabus) == 4, "Schema requer exatamente 4 estruturas-tabu"
    for i, tabu in enumerate(tabus):
        y, h = TABU_LAYOUT[i]
        stroke_rect(c, 440, y, 260, h, WHITE, RED, 1.3, radius=8)
        circle(c, 466, y + 26, 14, RED)
        text(c, 466, y + 31, str(i + 1), 13, WHITE, bold=True, anchor='middle')
        text(c, 488, y + 31, tabu["titulo"], 13, DARK, bold=True)
        linhas = tabu.get("linhas", [])
        for j, ln in enumerate(linhas[:3]):
            text(c, 452, y + 53 + j * 17, ln, 11, GRAY)

    # Regra dos "rentes" (caixa navy)
    regra = data.get("regra_pearl", {})
    stroke_rect(c, 440, 540, 260, 106, NAVY, NAVY, 0, radius=8)
    text(c, 452, 562, regra.get("titulo", "REGRA DOS \"RENTES\""), 12, WHITE, bold=True)
    linhas_regra = regra.get("linhas", [])
    for j, ln in enumerate(linhas_regra[:3]):
        text(c, 452, 584 + j * 18, ln, 11, NAVY_TEXT)
    if "italic" in regra:
        text(c, 452, 638, "\"" + regra["italic"] + "\"", 11, GOLD, italic=True)

    # Checklist
    text(c, 20, 612, "CHECKLIST MENTAL ANTES DE FECHAR", 12, NAVY, bold=True)
    line(c, 20, 618, 420, 618, NAVY, 1)
    stroke_rect(c, 20, 630, 400, 220, WHITE, LIGHT_GRAY, 1, radius=8)
    checklist = data.get("checklist", [])
    for j, item in enumerate(checklist[:7]):
        text(c, 36, 654 + j * 22, "☐  " + item, 12, DARK)
    line(c, 36, 798, 404, 798, SOFT, 1)
    alertas = data.get("alertas_pos_op", [])
    for j, alerta in enumerate(alertas[:2]):
        text(c, 36, 818 + j * 20, alerta, 11, RED, bold=True)

    # Mnemônico
    mn = data.get("mnemonico", {})
    stroke_rect(c, 440, 660, 260, 190, YELLOW_BG, YELLOW_LINE, 1.3, radius=8)
    text(c, 452, 682, mn.get("titulo", "MNEMÔNICO"), 12, YELLOW_DARK, bold=True)
    mn_linhas = mn.get("linhas", [])
    for j, ln in enumerate(mn_linhas[:5]):
        text(c, 452, 706 + j * 18, ln, 12, DARK)
    line(c, 452, 792, 688, 792, YELLOW_LINE, 1)
    frase = mn.get("frase", "")
    if frase:
        # Quebra a frase em até 2 linhas (~50 chars cada)
        if len(frase) > 50:
            metade = frase.rfind(" ", 0, 50)
            l1, l2 = frase[:metade], frase[metade + 1:]
            text(c, 452, 812, "\"" + l1 + ",", 11, YELLOW_ITALIC, italic=True)
            text(c, 452, 828, l2 + "\"", 11, YELLOW_ITALIC, italic=True)
        else:
            text(c, 452, 812, "\"" + frase + "\"", 11, YELLOW_ITALIC, italic=True)

    # Footer
    footer_left = data.get("footer_left", "Residência Cirurgia Geral · revisão pré-operatória")
    footer_right = data.get("footer_right", "v1 · A4 · imprimível")
    text(c, 20, 895, footer_left, 10, FOOT)
    text(c, 700, 895, footer_right, 10, FOOT, anchor='end')

    c.showPage()
    c.save()


def main():
    parser = argparse.ArgumentParser(description="Gera PDF do mapa cirúrgico mnemônico")
    parser.add_argument("--input", "-i", required=True, help="Caminho do JSON de entrada")
    parser.add_argument("--output", "-o", required=True, help="Caminho do PDF de saída")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    data = json.loads(in_path.read_text(encoding="utf-8"))
    render(data, out_path)
    print(f"OK {out_path}")


if __name__ == "__main__":
    main()
