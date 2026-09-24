#!/usr/bin/env python3
"""
Converte um markdown de simulado/material de estudo no PDF A4 padrao
"UNIFESP R+ Cirurgia" (vinho/ardosia, blocos de questao que nao quebram
entre paginas, marcadores == e !! e badges de emoji).

Uso:
    python3 build_simulado_pdf.py entrada.md saida.pdf \
        --header "UNIFESP R+ Cirurgia 2027 - Simulado 22 questoes" \
        --footer "PS CG HSP - uso interno de estudo"

Dependencias: weasyprint, markdown  (pip install weasyprint markdown --break-system-packages)

Convencoes reconhecidas no markdown de entrada:
    ==texto==     -> destaque amarelo (perolas, cutoffs numericos)
    !!texto!!     -> destaque vermelho negrito (armadilhas)
    # H1          -> comeca em pagina nova (exceto o primeiro)
    ### H3        -> abre um bloco (questao/gabarito) que nao quebra entre paginas
    ---           -> fecha o bloco
    **Rotulo:**   -> no inicio do paragrafo, vira rotulo de campo em vinho
    emojis        -> convertidos em badges coloridos (ver EMOJI_BADGES)
"""

import argparse
import re
import sys

try:
    import markdown
    from weasyprint import HTML, CSS
except ImportError:  # pragma: no cover
    sys.exit("Faltam dependencias. Rode:\n"
             "  pip install weasyprint markdown --break-system-packages")


# As fontes do container nao tem glifos de emoji: sem esta troca eles somem
# silenciosamente do PDF e a informacao de prioridade se perde.
EMOJI_BADGES = {
    "\U0001F534": '<span class="bd p1">P1</span>',          # bola vermelha
    "\U0001F7E0": '<span class="bd p2">P2</span>',          # bola laranja
    "\U0001F7E1": '<span class="bd p3">P3</span>',          # bola amarela
    "\U0001F511": '<span class="bd key">PEROLA</span>',     # chave
    "\U0001F525": '<span class="bd hot">ALTO VALOR</span>', # fogo
    "\U0001F3AF": '<span class="bd orf">ORFAO</span>',      # alvo
    "\u26D4":     '<span class="bd zero">ZERO</span>',
    "\u274C":     '<span class="bd zero">NADA</span>',
    "\u2705":     '<span class="bd ok">CERTO</span>',
    "\u26A0":     '<span class="warn">&#9650;</span>',      # triangulo de atencao
    "\U0001F52A": "",                                        # bisturi (decorativo)
}

LIST_RE = re.compile(r"^(>\s*)?\s*([-*+]|\d+\.)\s+")
LABEL_RE = re.compile(r"^\*\*[^*]{2,42}:\*\*")

# Um bloco maior que isso nao cabe numa pagina A4; mante-lo indivisivel
# empurraria tudo para a pagina seguinte e deixaria uma pagina em branco.
MAX_NOBREAK_CHARS = 2600


def preprocess(md: str) -> str:
    """Corrige as tres armadilhas de markdown que quebram este layout."""
    # 1. Sequencias de '---' viram heading setext ("---" como titulo). Colapsa.
    md = re.sub(r"(?:^---\s*\n){2,}", "---\n", md, flags=re.M)

    out = []
    for ln in md.split("\n"):
        prev = out[-1] if out else ""
        is_list = bool(LIST_RE.match(ln))
        prev_list = bool(LIST_RE.match(prev))
        in_quote = ln.lstrip().startswith(">")
        # 2. Lista sem linha em branco antes vira texto corrido.
        #    Dentro de citacao, a "linha em branco" precisa ser '>'.
        if is_list and prev.strip() and not prev_list:
            out.append(">" if in_quote and prev.lstrip().startswith(">") else "")
        # 3. Rotulos em negrito consecutivos colapsam num paragrafo unico.
        if LABEL_RE.match(ln) and prev.strip() and not prev.startswith("#"):
            out.append("")
        out.append(ln)

    md = "\n".join(out)
    md = re.sub(r"==(.+?)==", r'<mark class="hl">\1</mark>', md, flags=re.S)
    md = re.sub(r"!!(.+?)!!", r'<mark class="trap">\1</mark>', md, flags=re.S)
    return md


def to_html(md: str) -> str:
    body = markdown.markdown(
        preprocess(md),
        extensions=["tables", "sane_lists", "attr_list", "md_in_html"],
    )
    # Agrupa cada questao/gabarito (do <h3> ate o proximo <hr>) para que o
    # enunciado nunca se separe das alternativas. Blocos longos ficam de fora:
    # break-inside:avoid num bloco maior que uma pagina gera pagina em branco.
    def wrap(m):
        block = m.group(0)
        if len(block) > MAX_NOBREAK_CHARS:
            return block
        return '<div class="q">' + block + '</div>'

    body = re.sub(r"<h3>.*?</h3>.*?(?=<hr\s*/?>)", wrap, body, flags=re.S)
    for emoji, badge in EMOJI_BADGES.items():
        body = body.replace(emoji, badge)
    # Rotulo de campo no inicio do paragrafo
    body = re.sub(r"<p><strong>([^<]{2,42}:)</strong>",
                  r'<p class="fld"><strong>\1</strong>', body)
    return body


def css_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def build_css(header: str, footer: str) -> str:
    return """
@page {
  size: A4; margin: 16mm 14mm 15mm 14mm;
  @top-right { content: "%s"; font-family: "DejaVu Sans"; font-size: 7pt; color: #94a3b8; }
  @bottom-right { content: counter(page) " / " counter(pages);
                  font-family: "DejaVu Sans"; font-size: 7.5pt; color: #94a3b8; }
  @bottom-left { content: "%s"; font-family: "DejaVu Sans"; font-size: 7pt; color: #cbd5e1; }
}
body { font-family: "DejaVu Serif", serif; font-size: 9pt; line-height: 1.4;
       color: #1e293b; text-align: justify; hyphens: auto; }
h1,h2,h3,h4 { font-family: "DejaVu Sans", sans-serif; text-align: left; hyphens: none; }

h1 { break-before: page; font-size: 18pt; line-height: 1.15; color: #7f1d1d;
     margin: 0 0 2mm 0; padding-bottom: 3mm; border-bottom: 2.5pt solid #7f1d1d; }
h1:first-of-type { break-before: avoid; }
h1 + h3 { font-size: 9.6pt; font-weight: normal; color: #64748b; font-style: italic;
     border: none; padding: 0; margin: 0 0 8mm 0; }
h2 { font-size: 12.2pt; color: #fff; background: #7f1d1d; padding: 2.3mm 3mm;
     margin: 8mm 0 3.5mm 0; border-radius: 1.2mm; break-after: avoid; }
h3 { font-size: 10.3pt; color: #7f1d1d; margin: 6mm 0 2mm 0; padding-left: 2.6mm;
     border-left: 3pt solid #dc2626; break-after: avoid; }
h4 { font-size: 9.4pt; color: #334155; margin: 3.5mm 0 1.5mm 0; break-after: avoid; }

p { margin: 0 0 2.2mm 0; }
p.fld { margin-bottom: 1.4mm; }
p.fld strong { color: #7f1d1d; font-family: "DejaVu Sans", sans-serif; font-size: 8.3pt; }
strong { color: #0f172a; }
em { color: #475569; }
ul, ol { margin: 0 0 2.6mm 0; padding-left: 5.5mm; }
li { margin-bottom: 1.1mm; }

blockquote { margin: 2.4mm 0; padding: 2.2mm 3.2mm; background: #fff8f1;
  border-left: 3pt solid #ea580c; color: #78350f; font-size: 8.6pt;
  border-radius: 0 1mm 1mm 0; break-inside: avoid; }
blockquote p { margin: 0 0 1.3mm 0; }
blockquote p:last-child { margin-bottom: 0; }

table { width: 100%%; border-collapse: collapse; margin: 3mm 0 4mm 0;
  font-family: "DejaVu Sans", sans-serif; font-size: 7.7pt; }
thead { display: table-header-group; }
th { background: #1e293b; color: #fff; text-align: left; padding: 1.7mm 2mm; font-size: 7.5pt; }
td { padding: 1.5mm 2mm; border-bottom: 0.4pt solid #e2e8f0; vertical-align: top; text-align: left; }
tbody tr:nth-child(even) { background: #f8fafc; }

mark.hl { background: #fef08a; color: #1e293b; padding: 0.3mm 0.7mm; border-radius: 0.6mm; }
mark.trap { background: #fee2e2; color: #991b1b; padding: 0.3mm 0.7mm;
            border-radius: 0.6mm; font-weight: bold; }

.bd { font-family: "DejaVu Sans", sans-serif; font-size: 6.6pt; font-weight: bold;
      color: #fff; padding: 0.4mm 1.3mm; border-radius: 0.8mm; letter-spacing: 0.2pt; }
.p1 { background: #b91c1c; } .p2 { background: #ea580c; } .p3 { background: #ca8a04; }
.key { background: #0f766e; } .hot { background: #15803d; }
.zero { background: #94a3b8; } .orf { background: #6d28d9; } .ok { background: #15803d; }
.warn { color: #b45309; font-family: "DejaVu Sans", sans-serif; font-size: 8pt; }

code { font-family: "DejaVu Sans Mono", monospace; font-size: 7.9pt;
       background: #f1f5f9; padding: 0.2mm 0.9mm; border-radius: 0.6mm; }
div.q { break-inside: avoid; }
hr { border: none; border-top: 0.6pt solid #e2e8f0; margin: 5mm 0; }
""" % (css_escape(header), css_escape(footer))


def main() -> None:
    ap = argparse.ArgumentParser(description="Markdown -> PDF padrao UNIFESP R+")
    ap.add_argument("input", help="arquivo .md de entrada")
    ap.add_argument("output", help="arquivo .pdf de saida")
    ap.add_argument("--header", default="UNIFESP R+ Cirurgia 2027",
                    help="texto do cabecalho (evite emojis)")
    ap.add_argument("--footer", default="uso interno de estudo",
                    help="texto do rodape a esquerda")
    args = ap.parse_args()

    md = open(args.input, encoding="utf-8").read()
    html = ('<html lang="pt-BR"><head><meta charset="utf-8"></head><body>'
            + to_html(md) + "</body></html>")
    HTML(string=html).write_pdf(args.output,
                                stylesheets=[CSS(string=build_css(args.header, args.footer))])
    print("PDF gerado: " + args.output)


if __name__ == "__main__":
    main()
