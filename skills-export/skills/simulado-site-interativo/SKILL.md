---
name: simulado-site-interativo
description: >
  Transforma um simulado de questões num site interativo de arquivo único que abre
  no celular e no computador, funciona offline e salva o progresso. Correção
  instantânea ao tocar na alternativa, análise abrindo dentro delas, marcação de
  confiança, marca-texto amarelo, eliminação de alternativas por descarte, controle
  de tamanho do texto e um resultado que cruza confiança com acerto. Use SEMPRE que o Marcos pedir: "faz um site", "site
  de questões", "site pra responder", "versão interativa", "coloca esse simulado
  num site", "mesmo modelo do site anterior", "página pra fazer as questões", "app
  das questões", "quiz interativo". Acione também quando ele já tiver um simulado
  em markdown ou PDF e pedir para "deixar mais fácil de responder", "mais visual"
  ou "responder no celular" — e sempre que pedir um site para qualquer lote de
  questões, mesmo sem citar simulado. Para o PDF impresso do mesmo simulado, use
  `simulado-unifesp-pdf`; as duas partem do mesmo markdown.
---

# Site interativo de simulado

Gera um HTML único a partir do markdown do simulado. Nada de servidor, nada de
build, nada de dependência externa em tempo de execução — o arquivo abre com dois
toques e funciona no avião.

O modelo visual e as decisões de interação já foram testados e aprovados pelo
Marcos. **Reproduza-os; não redesenhe.** `references/design.md` explica o porquê de
cada escolha e o que quebra se for mexido.

## Fluxo

O markdown do simulado é a fonte. Se ele ainda não existir, escreva-o primeiro
seguindo a skill `simulado-unifesp-pdf` — o parser depende daquele formato.

```bash
S=/mnt/skills/.../simulado-site        # raiz desta skill
python3 $S/scripts/parse_simulado.py simulado.md questoes.json
python3 $S/scripts/build_site.py questoes.json config.json simulado.html
```

O parser **falha alto**: se faltar gabarito, pérola, enunciado ou se o número de
análises não bater com o de alternativas, ele lista os problemas e para. Corrija o
markdown em vez de contornar o parser — o defeito está no material, não no script.

Depois, presente o HTML com `present_files`. Presentear é obrigatório: um arquivo
escrito e não apresentado é inalcançável no celular.

## O config.json

O template é genérico; tudo que é específico do simulado vive aqui. O
docstring de `build_site.py` traz o formato completo. Os campos que exigem
julgamento:

- **`chave`** — identificador do armazenamento. **Use uma chave nova para cada
  simulado** (`simulado3:v1`), senão o progresso de um sobrescreve o do outro.
  Mudou o conteúdo de um simulado já entregue? Suba a versão (`:v2`), ou o
  progresso salvo vai repintar respostas em questões que já não são as mesmas.
- **`faixas`** — três faixas de desempenho, testadas de cima para baixo com
  `acertos >= limite`. Escreva o texto como orientação do que fazer em seguida,
  não como elogio ou reprimenda.
- **`discriminam`** — as questões que mais separam quem domina de quem decorou, e
  uma frase dizendo o que cada uma testa. Escolha pelo tipo de raciocínio (cutoff
  numérico, hierarquia de escalonamento, armadilha de completude), não pela
  dificuldade aparente.
- **`rodape`** — o que o simulado **não** cobre. Essa linha existe para impedir
  que uma nota alta seja lida como preparo completo.

## O que o site faz

**Responder.** Uma questão por tela. A confiança (Certeza / Dúvida entre duas /
Chute) vem antes das alternativas, porque marcada depois do gabarito ela não vale
nada — mas não trava: tocar direto na alternativa responde e registra como não
marcada.

**Corrigir na hora.** O toque na alternativa é a resposta. Aparece a faixa de
certo/errado no topo e a análise das quatro abre dentro delas. A alternativa
tocada fica ancorada na mesma altura da tela, então a expansão não desloca a
leitura.

**Codificar o tipo de erro.** A régua colorida à esquerda de cada alternativa sai
do próprio veredito escrito no gabarito: verde para a correta, âmbar com etiqueta
*armadilha*, vinho escuro com *erro grave*, violeta com *sobretratamento*, cinza
para errada simples. O fundo mostra o que a pessoa marcou; a régua mostra que tipo
de erro a alternativa é. São duas informações independentes e é assim que devem
continuar.

**Riscar alternativas.** Um `✕` em cada alternativa, antes de responder, elimina
por descarte: a alternativa ganha linha no meio e desbota, mas continua legível. O
botão vira `↺` para restaurar, e uma alternativa riscada não responde ao toque —
proteção contra marcar por engano o que já foi eliminado. Se a riscada era a
correta, a correção avisa.

**Grifar.** Seleção de texto em qualquer zona `[data-hz]` faz surgir o botão
Grifar. O grifo do usuário é amarelo forte; o amarelo pálido da pérola é o
curado por Claude. Toque no grifo apaga.

**Ajustar o texto.** Cinco níveis de 88% a 150%, nos botões A−/A+ da barra do topo
e na capa. Escala só o texto de leitura — a numeração grande da questão e o título
da capa ficam fixos, senão o layout quebra.

**Ler o desempenho.** A tela final cruza confiança com acerto. A linha "errou tendo
certeza" fica destacada porque é a única que representa conceito consolidado
errado, e essa não se corrige repetindo flashcard. "Acertou no chute" também
aparece, porque infla a nota sem representar domínio.

## Verificação antes de entregar

Nunca entregue sem abrir. Um erro de JS deixa a página em branco e isso não
aparece na inspeção do HTML.

```bash
pip install playwright --break-system-packages -q && python3 -m playwright install --with-deps chromium
```

Rode `references/verificar.py`, que dirige o site inteiro num navegador headless:
capa, resposta, grifo, zoom, as questões todas e o resultado, capturando erros de
console. Ele imprime um relatório e sai com código diferente de zero se algo
falhar. Tire também duas ou três capturas e olhe — layout quebrado não dispara
erro nenhum.

## Erros que já aconteceram aqui

**Edição incremental do gerador.** Aplicar remendos sucessivos por substituição de
texto num arquivo grande duplicou um bloco inteiro sem aviso. Se o arquivo gerado
crescer muito de um passo para o outro, conte as ocorrências de `</html>` e das
funções principais antes de seguir. Quando a edição ficar confusa, reescreva o
arquivo do zero em vez de remendar.

**Especificidade de CSS.** `#railtop button` vence `.zoom button` e apagou o estilo
dos botões de tamanho. Ao acrescentar controles dentro de um container com id,
qualifique o seletor com o id.

**`pointer-events:none` mata a seleção de texto.** Foi o que impediu o marca-texto
nas alternativas já respondidas. Para travar um botão sem perder a seleção, guarde
no manipulador de clique, não no CSS.

**Botão flutuante fora da tela.** Posicione o botão Grifar com limites no topo e
na base do viewport; sem isso ele some quando a seleção está perto das bordas.

## Fora do escopo

Não use armazenamento do navegador (`localStorage`, `sessionStorage`): não funciona
nos artefatos e o template já usa a API `window.storage` com tolerância a falha.
Não adicione framework, bundler nem CDN de JavaScript — o arquivo tem que continuar
sendo um só e abrindo offline.
