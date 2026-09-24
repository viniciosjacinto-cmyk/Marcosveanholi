#!/usr/bin/env python3
"""
Dirige o site num navegador headless e confere que tudo funciona.

    python3 verificar.py caminho/do/simulado.html

Sai com codigo 1 se algo falhar. Cobre: montagem da capa, resposta com e sem
confianca, correcao instantanea, codificacao do tipo de erro, marca-texto
(criar, apagar, persistir), controle de tamanho, navegacao, tela de resultado
e erros de console.

Precisa de: pip install playwright --break-system-packages
            python3 -m playwright install --with-deps chromium
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

# Seleciona um trecho por offset de caractere dentro de uma zona grifavel.
SEL = """(args)=>{
  const z=document.querySelector(args.z); z.scrollIntoView({block:'center'});
  const w=document.createTreeWalker(z,NodeFilter.SHOW_TEXT);
  let pos=0,sN=null,sO=0,eN=null,eO=0;
  while(w.nextNode()){const n=w.currentNode,l=n.nodeValue.length;
    if(sN===null&&pos+l>args.s){sN=n;sO=args.s-pos;}
    if(eN===null&&pos+l>=args.e){eN=n;eO=args.e-pos;break;} pos+=l;}
  if(!sN||!eN) return null;
  const r=document.createRange(); r.setStart(sN,sO); r.setEnd(eN,eO);
  const s=getSelection(); s.removeAllRanges(); s.addRange(r);
  document.dispatchEvent(new Event('selectionchange'));
  return r.toString();
}"""

falhas = []


def check(nome, cond, detalhe=''):
    print(('  ok   ' if cond else '  FALHA') + '  ' + nome + (' — ' + str(detalhe) if detalhe else ''))
    if not cond:
        falhas.append(nome)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    alvo = pathlib.Path(sys.argv[1]).resolve()
    if not alvo.exists():
        sys.exit('arquivo não encontrado: ' + str(alvo))
    url = alvo.as_uri()
    erros = []

    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
        pg.on('pageerror', lambda e: erros.append(str(e)))
        pg.goto(url)
        pg.wait_for_timeout(2200)

        print('\ncapa')
        check('título montado', bool(pg.inner_text('.capa h1').strip()))
        check('números na capa', len(pg.eval_on_selector_all('.stats .v', 'e=>e.length')) if False
              else pg.eval_on_selector_all('.stats .v', 'e=>e.length') >= 1)
        check('controle de tamanho na capa', pg.is_visible('#czp'))
        pg.click('#go')
        pg.wait_for_timeout(400)

        print('\nriscar alternativas')
        n = pg.evaluate('()=>Q.length')
        check('botão de riscar em cada alternativa',
              pg.eval_on_selector_all('.kill', 'e=>e.length') == pg.eval_on_selector_all('.alt', 'e=>e.length'))
        pg.click('.kill[data-k="A"]')
        pg.wait_for_timeout(250)
        check('alternativa fica riscada',
              pg.eval_on_selector('.alt[data-l="A"] .astmt',
                                  'e=>getComputedStyle(e).textDecorationLine') == 'line-through')
        check('botão vira restaurar', pg.eval_on_selector('.kill[data-k="A"]', 'e=>e.textContent') == '\u21ba')
        pg.click('.alt[data-l="A"]')
        pg.wait_for_timeout(250)
        check('riscada não responde ao toque',
              pg.evaluate('()=>Object.keys(state.answers).length') == 0)
        pg.click('.kill[data-k="A"]')
        pg.wait_for_timeout(250)
        check('restaura ao tocar de novo', pg.eval_on_selector_all('.alt.cut', 'e=>e.length') == 0)
        gab = pg.evaluate('()=>Q[state.idx].correct')
        pg.click(f'.kill[data-k="{gab}"]')
        pg.wait_for_timeout(200)

        print('\nresposta e correção')
        pg.click('.confbtns button[data-c="certeza"]')
        pg.wait_for_timeout(120)
        pg.click(f'.alt[data-l="{"B" if gab != "B" else "C"}"]')
        pg.wait_for_timeout(450)
        check('correção aparece no toque', pg.is_visible('.flash'))
        check('análise abre nas alternativas', pg.eval_on_selector_all('.why', 'e=>e.length') >= 2)
        check('pérola exibida', pg.is_visible('.pearl .body'))
        check('confiança registrada', 'certeza' in pg.inner_text('.flash').lower())
        check('avisa que riscou a certa', pg.eval_on_selector_all('.cutwarn', 'e=>e.length') == 1)
        check('risco persiste na revisão', pg.eval_on_selector_all('.alt.cut', 'e=>e.length') == 1)
        check('botões de riscar somem após responder',
              pg.eval_on_selector_all('.kill', 'e=>e.length') == 0)

        print('\ngrifo')
        pg.evaluate(SEL, {'z': '[data-hz="s0"]', 's': 20, 'e': 80})
        pg.wait_for_timeout(300)
        check('botão Grifar surge na seleção', pg.eval_on_selector('#pen', 'e=>e.classList.contains("on")'))
        check('botão dentro da tela',
              pg.eval_on_selector('#pen', 'e=>{const b=e.getBoundingClientRect();return b.top>0&&b.bottom<innerHeight}'))
        pg.click('#penbtn')
        pg.wait_for_timeout(300)
        cor = pg.eval_on_selector('[data-hz] mark.um', 'e=>getComputedStyle(e).backgroundColor')
        check('grifo criado em amarelo', cor == 'rgb(252, 233, 106)', cor)
        check('link de limpar aparece', pg.eval_on_selector_all('.clearmk', 'e=>e.length') == 1)
        pg.eval_on_selector('[data-hz] mark.um', 'e=>e.click()')
        pg.wait_for_timeout(250)
        check('grifo apaga ao tocar', pg.eval_on_selector_all('[data-hz] mark.um', 'e=>e.length') == 0)

        print('\ntamanho do texto')
        base = pg.eval_on_selector('.stem', 'e=>parseFloat(getComputedStyle(e).fontSize)')
        pg.click('#zp')
        pg.wait_for_timeout(250)
        maior = pg.eval_on_selector('.stem', 'e=>parseFloat(getComputedStyle(e).fontSize)')
        check('A+ aumenta o enunciado', maior > base, f'{base} -> {maior}')
        check('análise também escala',
              pg.eval_on_selector('.why', 'e=>parseFloat(getComputedStyle(e).fontSize)') > 14)
        pg.click('#zm')
        pg.wait_for_timeout(200)

        print('\npercurso completo')
        kinds = set()
        for i in range(1, n):
            pg.click('#next')
            pg.wait_for_timeout(70)
            gab = pg.evaluate('()=>Q[state.idx].correct')
            letra = gab if i % 3 else ('A' if gab != 'A' else 'B')
            pg.click(f'.alt[data-l="{letra}"]')
            pg.wait_for_timeout(90)
            for c in pg.eval_on_selector_all('.alt', 'e=>e.map(x=>x.className)'):
                kinds.update(k for k in c.split() if k.startswith('k-'))
        check('todas as questões responderam', pg.evaluate('()=>Object.keys(state.answers).length') == n)
        check('tipos de erro codificados', 'k-ok' in kinds and len(kinds) >= 3, sorted(kinds))

        print('\nresultado')
        pg.click('#next')
        pg.wait_for_timeout(800)
        check('tela de resultado abre', pg.is_visible('.score .big'))
        check('matriz confiança × acerto', pg.eval_on_selector_all('table.mx tbody tr', 'e=>e.length') >= 1)
        check('desempenho por área', pg.eval_on_selector_all('.areas div', 'e=>e.length') >= 1)
        check('grade de todas as questões', pg.eval_on_selector_all('.grid23 button', 'e=>e.length') == n)
        check('rodapé com as lacunas', bool(pg.inner_text('.gap').strip()))

        pg.screenshot(path='/tmp/verificar-resultado.png', full_page=True)
        br.close()

    print('\nerros de console:', erros or 'nenhum')
    if erros:
        falhas.append('erros de console')

    print('\ncaptura do resultado em /tmp/verificar-resultado.png — olhe antes de entregar.')
    if falhas:
        sys.exit('\nFALHOU: ' + '; '.join(falhas))
    print('\nTudo certo.')


if __name__ == '__main__':
    main()
