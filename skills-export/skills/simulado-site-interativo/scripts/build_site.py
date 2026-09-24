#!/usr/bin/env python3
"""
Monta o site do simulado: template + questoes + configuracao -> um unico HTML.

    python3 build_site.py questoes.json config.json saida.html

O template fica em ../assets/template.html. Nada de externo alem das fontes
do Google Fonts, que tem fallback para as do sistema — o arquivo funciona
offline e sem servidor.

Formato do config.json (todos os campos sao obrigatorios):

{
  "titulo_pagina": "Simulado 2 — apostas inéditas · UNIFESP R+ Cirurgia",
  "chave": "simulado2:v2",
  "kicker": "UNIFESP R+ Cirurgia 2027",
  "titulo": "Simulado 2",
  "subtitulo": "apostas inéditas",
  "resumo": "Uma frase sobre a origem das questoes.",
  "numeros": [["23","questões"],["4","alternativas"],["9","áreas"]],
  "instrucoes": ["<p> um paragrafo", "outro paragrafo"],
  "faixas": [[19,"a","texto do desempenho alto"],
             [15,"b","texto do desempenho medio"],
             [0,"c","texto do desempenho baixo"]],
  "discriminam": {"numeros":[3,5,1], "texto":"Por que essas discriminam."},
  "rodape": "O que o simulado nao cobre."
}

`faixas` e testado de cima para baixo com `acertos >= limite`; as classes
"a"/"b"/"c" pintam o bloco de verde, ambar e vinho.
"""
import json
import pathlib
import sys

CAMPOS = ['titulo_pagina', 'chave', 'kicker', 'titulo', 'subtitulo', 'resumo',
          'numeros', 'instrucoes', 'faixas', 'discriminam', 'rodape']


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    qjson, cjson, out = sys.argv[1:4]

    questions = json.load(open(qjson, encoding='utf-8'))
    cfg = json.load(open(cjson, encoding='utf-8'))

    faltam = [c for c in CAMPOS if c not in cfg]
    if faltam:
        sys.exit('config.json sem os campos: ' + ', '.join(faltam))
    if not questions:
        sys.exit('questoes.json vazio')

    tpl = (pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'template.html')
    html = tpl.read_text(encoding='utf-8')
    html = html.replace('__TITULO__', cfg['titulo_pagina'])
    html = html.replace('__CFG__', json.dumps(cfg, ensure_ascii=False))
    html = html.replace('__DATA__', json.dumps(questions, ensure_ascii=False))

    for marca in ['__TITULO__', '__CFG__', '__DATA__']:
        assert marca not in html, 'sobrou marcador ' + marca

    pathlib.Path(out).write_text(html, encoding='utf-8')
    print(f'{len(questions)} questões -> {out} ({len(html)} bytes)')


if __name__ == '__main__':
    main()
