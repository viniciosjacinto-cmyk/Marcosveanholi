# O modelo visual — e por que cada escolha existe

Este documento existe para impedir redesenho acidental. Tudo aqui foi testado com
o usuário e ajustado a pedido dele. Se for mudar algo, saiba o que está trocando.

## Paleta

| Token | Hex | Papel |
|---|---|---|
| `--tinta` | `#1B2430` | texto e botões primários — azul-ardósia, não preto tingido |
| `--papel` | `#F5F6F4` | fundo, branco levemente frio |
| `--vinho` | `#7A1420` | âncora da identidade, herdada do PDF |
| `--verde` | `#176B54` | alternativa correta |
| `--ambar` | `#8A5A00` | armadilha |
| `--sangue` | `#6A0F17` | erro grave |
| `--roxo` | `#5B3A9B` | sobretratamento |
| `--ocre` | `#9A6B08` | régua e rótulo da pérola |

O vinho vem do PDF que o usuário já aprovou — é continuidade deliberada, não
default. O fundo é frio de propósito: creme quente (`#F4F1EA`) somado a serifada
de alto contraste é o visual mais genérico que existe hoje.

## Tipografia

- **Newsreader** (serifada) nos enunciados. É texto clínico longo, lido com
  atenção; serifada com entrelinha generosa sustenta isso melhor.
- **IBM Plex Sans** na interface, alternativas e análises. Tem caráter técnico e
  não é o Inter, que aparece em toda parte.
- Ambas com fallback para as fontes do sistema. Se o Google Fonts não carregar
  (offline, hospital com rede ruim), o site continua legível.

## Os três amarelos, que não são a mesma coisa

1. **Negrito, sem fundo,** no enunciado marca o dado que decide a questão. Já teve
   fundo amarelo; o usuário pediu para tirar — ficava carregado demais junto com o
   resto.
2. **Amarelo pálido `#FBEEB0`** (`mark.hl`) na pérola: a regra a levar. Vem do
   marcador `==` do markdown.
3. **Amarelo forte `#FCE96A`** (`mark.um`): o grifo do usuário. Precisa ser o mais
   saturado dos três, porque é o único que ele controla.

O vermelho `mark.trap` (marcador `!!`) é armadilha, e só isso.

## Codificação do erro

A régua lateral e a etiqueta saem da função `verdictKind()`, que lê o texto do
veredito já escrito no gabarito — não é metadado à parte, é o próprio comentário
classificado. Isso significa que **a qualidade da codificação depende de como os
vereditos foram escritos no markdown**: "Errada — e é a armadilha central" vira
âmbar; "Errada" seco vira cinza. Escreva os vereditos com essa vocação.

Fundo e régua carregam informações diferentes e não devem ser fundidos:

- **fundo** — o que a pessoa marcou (verde se acertou, vinho se errou)
- **régua** — que tipo de alternativa aquela é, independentemente do que foi marcado

## Interação

**Correção instantânea.** Tocar é responder. Houve uma versão com botão
"Confirmar"; o usuário pediu para tirar. A confiança subiu para antes das
alternativas por consequência — depois do gabarito ela seria contaminada.

**Sem travas.** A confiança é solicitada, não exigida. Pular registra "não
marcada", que tem linha própria no resultado.

**Âncora de rolagem.** Ao revelar, `answer()` mede a posição da alternativa tocada
antes e depois do re-render e compensa a diferença. Sem isso a expansão joga a
leitura para outro ponto da página, o que no celular é desorientador.

**Riscar alternativa.** Cada alternativa tem um `✕` no canto, só antes de
responder. Riscada, ela ganha linha no meio da letra e do texto e cai para 46% de
opacidade — continua legível, mas sai do primeiro plano. O botão vira `↺` para
restaurar. Duas decisões deliberadas:

- **Riscada não responde ao toque.** Quem eliminou não quer marcar por engano.
  Para responder é preciso restaurar antes, e o `↺` deixa isso óbvio.
- **O risco sobrevive à resposta,** sem a opacidade, para a análise ficar legível.
  Se a eliminada era a correta, a faixa de correção avisa: "Você tinha riscado a
  alternativa certa." É o erro de raciocínio mais caro e merece ser nomeado.

O botão `✕` fica como irmão do `<button class="alt">` dentro do `<li>`, posicionado
por absoluto — nunca aninhado dentro dele. Botão dentro de botão é HTML inválido e
quebra o clique em alguns navegadores.

**Grifo.** Zonas marcadas com `data-hz` guardam o HTML original em `dataset.orig` e
armazenam intervalos em offsets de caractere sobre o texto puro. Assim o grifo
atravessa negritos e outros grifos sem quebrá-los, e sobrevive ao re-render.
Nunca armazene Range do DOM.

## O que a tela de resultado precisa ter

A nota sozinha mente nos dois sentidos. A matriz confiança × acerto é o elemento
que justifica o site existir em vez de um PDF, e não deve ser removida nem
simplificada. Duas células importam mais que a nota:

- **errou tendo certeza** — conceito consolidado errado; vai para a ficha, não para
  o flashcard
- **acertou chutando** — infla a nota sem representar domínio

O rodapé com o que o simulado não cobre também é obrigatório, pelo mesmo motivo.

## Acessibilidade e robustez, sem alarde

Responsivo até 360px. Foco de teclado visível. `prefers-reduced-motion`
respeitado. Teclado: A–D respondem, Shift+A–D riscam, setas navegam, `+`/`−` mudam o tamanho.
Contraste conferido nos textos secundários. Áreas de toque com no mínimo 44px de
altura nos controles principais.
