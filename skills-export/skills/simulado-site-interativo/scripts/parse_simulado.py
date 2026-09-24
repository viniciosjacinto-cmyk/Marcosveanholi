#!/usr/bin/env python3
"""
Converte o markdown de um simulado (padrao da skill `simulado-unifesp-pdf`)
no JSON que o site consome.

    python3 parse_simulado.py simulado.md questoes.json

Estrutura esperada no markdown:

    # PARTE I ...
    ### QUESTÃO 1
    *Tema: Bloco · Subtópico: Assunto*
    [paragrafos do enunciado]
    [pergunta fechada]
    **A)** ...
    **B)** ...
    ---
    # PARTE II ...
    ### Q1 — Gabarito B
    - **A) Errada.** ...
    - **B) Correta.** ...
    🔑 **Pérola:** ...

Marcadores convertidos: **negrito**, *italico*, ==amarelo==, !!armadilha!!,
🎯 vira etiqueta de tema orfao. O badge PEROLA e removido (o site ja rotula).
"""
import json
import re
import sys


def inline(t: str) -> str:
    t = t.strip()
    t = re.sub(r'<span class="bd key">PEROLA</span>\s*', '', t)
    t = t.replace('\U0001F511', '')
    t = re.sub(r'<span class="bd orf">ORFAO</span>', '<b class="tag-orf">órfão</b>', t)
    t = t.replace('\U0001F3AF', '<b class="tag-orf">órfão</b>')
    t = re.sub(r'==(.+?)==', r'<mark class="hl">\1</mark>', t, flags=re.S)
    t = re.sub(r'!!(.+?)!!', r'<mark class="trap">\1</mark>', t, flags=re.S)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t, flags=re.S)
    t = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', r'<i>\1</i>', t)
    return t


def parse(src: str):
    caderno = src.split('# PARTE I')[1].split('# PARTE II')[0]
    questions = []
    for block in re.split(r'\n### QUESTÃO ', caderno)[1:]:
        num = int(re.match(r'(\d+)', block).group(1))
        body = block.split('\n', 1)[1].split('\n---')[0]
        tema = re.search(r'\*Tema:\s*(.+?)\s*·\s*Subtópico:\s*(.+?)\*', body)
        alts = re.findall(r'\*\*([A-E])\)\*\*\s*(.+?)(?=\n\n\*\*[A-E]\)|\Z)', body, re.S)
        stem_raw = re.sub(r'\*Tema:.+?\*\n', '', body[:body.index('**A)**')], count=1)
        paras = [p.strip() for p in stem_raw.strip().split('\n\n') if p.strip()]
        questions.append({
            'n': num,
            'area': tema.group(1) if tema else '',
            'sub': tema.group(2) if tema else '',
            'stem': [inline(p) for p in paras[:-1]],
            'ask': inline(paras[-1]),
            'alts': {k: inline(v) for k, v in alts},
        })

    gab = src.split('# PARTE II')[1]
    pat = r'### Q(\d+) — Gabarito ([A-E])\n(.*?)(?=\n### Q\d+ — Gabarito|\n## |\Z)'
    for m in re.finditer(pat, gab, re.S):
        num, correct, body = int(m.group(1)), m.group(2), m.group(3)
        q = next(x for x in questions if x['n'] == num)
        q['correct'] = correct
        q['analysis'] = {}
        for am in re.finditer(r'^- \*\*([A-E])\)\s*(.+?)\*\*\s*(.*?)$', body, re.M):
            q['analysis'][am.group(1)] = {
                'verdict': am.group(2).strip().rstrip('.'),
                'text': inline(am.group(3)),
            }
        pm = re.search(r'\*\*Pérola:\*\*\s*(.+?)(?=\n\n|\Z)', body, re.S)
        q['pearl'] = inline(pm.group(1)) if pm else ''
    return questions


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    qs = parse(open(sys.argv[1], encoding='utf-8').read())

    problemas = []
    for q in qs:
        if 'correct' not in q:
            problemas.append(f"Q{q['n']}: sem gabarito")
        elif len(q.get('analysis', {})) != len(q['alts']):
            problemas.append(f"Q{q['n']}: {len(q.get('analysis', {}))} análises "
                             f"para {len(q['alts'])} alternativas")
        if not q.get('pearl'):
            problemas.append(f"Q{q['n']}: sem pérola")
        if not q['stem']:
            problemas.append(f"Q{q['n']}: enunciado vazio")
    if problemas:
        print('PROBLEMAS ENCONTRADOS:')
        for x in problemas:
            print('  -', x)
        sys.exit('Corrija o markdown antes de gerar o site.')

    json.dump(qs, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(qs)} questões OK -> {sys.argv[2]}')
    print('gabarito:', ''.join(q['correct'] for q in qs))


if __name__ == '__main__':
    main()
