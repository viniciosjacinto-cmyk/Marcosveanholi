# Impressão da equipe (Modo C2) — referência

Roda quando há imagem do PACS e **não** há laudo. Objetivo: tornar sistemático o olhar que o cirurgião já dá antes do laudo sair.

Índice:
1. O que está dentro do alcance da captura
2. O que está fora, sempre
3. Roteiro de revisão na estação, por contexto
4. Como escrever sem virar laudo
5. Exemplo calibrado

---

## 1. O que está dentro do alcance da captura

Achado grosseiro, grande e de alto contraste. Estes podem sair marcados `[imagem]`:

| Achado | Por que passa |
|---|---|
| Pneumoperitônio volumoso | ar × tecido é o maior contraste que existe em TC |
| Líquido livre moderado a volumoso | diferença de densidade ampla, ocupa muitos cortes |
| Distensão de alças / padrão obstrutivo | alteração de calibre grosseira, reconhecível em série |
| Hemotórax ou pneumotórax volumoso | desde que a janela capturada permita |
| Coleção ou massa grande com efeito de massa | desvio de estrutura adjacente é reconhecível |
| Dispositivos — dreno, TOT, cateter, sonda | metal/alta densidade, trajeto grosseiro |
| Dilatação de via biliar ou de via urinária, quando marcada | contraste amplo com parênquima |
| Calibre aórtico grosseiramente aumentado | só como suspeita, nunca com medida |
| Ausência de órgão / anatomia pós-operatória evidente | mudança estrutural grande |

**Regra:** se o achado precisa de medida, de comparação de densidade ou de janela específica para existir, ele não está nesta lista.

---

## 2. O que está fora, sempre

Estes saem `[não resolvível]` em captura de tela, sem exceção e sem depender de quão boa a gravação pareça:

- **Blush / extravasamento ativo de contraste** — define angioembolização, e se define comparando densidade com a aorta na mesma janela
- **Grau AAST** — depende de profundidade de laceração e percentual de parênquima; nenhum dos dois é mensurável aqui
- **Qualquer medida em cm ou mm**
- Pneumoperitônio mínimo, pneumatose intestinal, ar em veia porta
- **Lesão de víscera oca** — os sinais são indiretos e finos (ar extraluminal puntiforme, espessamento focal, densificação mesentérica)
- Fratura fina, sobretudo arco costal posterior e não desviada
- Nódulo pulmonar, linfonodo, caracterização de realce
- **Fase de aquisição** — arterial, portal, tardia, split-bolus não são inferíveis dos frames
- Trombose venosa, dissecção de camada fina, pseudoaneurisma pequeno
- Integridade de anastomose

Se o usuário insistir em um desses, a resposta é o roteiro do item 3 — não uma estimativa.

---

## 3. Roteiro de revisão na estação, por contexto

Isto é o produto principal do C2. Entregue dirigido, não genérico.

### Trauma abdominal
- Janela abdome, rolar do diafragma à sínfise — líquido livre por espaço (Morison, periesplênico, goteiras, pelve)
- Fígado e baço em fase portal — laceração, hematoma subcapsular, área hipoperfundida
- Procurar blush ativamente: foco hiperdenso intraparenquimatoso ou no hematoma, com densidade comparável à aorta no mesmo corte. Comparar com fase tardia se houver
- Janela pulmonar nos cortes altos — pneumotórax, contusão de base
- Janela óssea — arcos costais, coluna, pelve
- Rins com fase excretora se houver hematúria; bexiga
- Mesentério: densificação, ar extraluminal, espessamento focal de alça
- Retroperitônio — zona do hematoma (I central, II lateral, III pélvica) muda a conduta

### Abdome agudo não traumático
- Ponto de transição — seguir alça calibrosa até a colabada
- Sinais de sofrimento: falha de realce parietal, pneumatose, ar portal, líquido interalças
- Pneumoperitônio em janela pulmonar — é onde o ar mínimo aparece
- Apêndice: visualizado ou não. Não visualizado ≠ normal
- Eixo mesentérico e portal — patência, na fase disponível
- Coleções: tamanho, loculação, janela de acesso percutâneo

### Pós-operatório
- Coleção — densidade, gás de permeio, realce de parede (separa seroma de abscesso)
- Ar extraluminal: esperado para o tempo de PO ou não
- Trajeto e posição de drenos
- Anastomose — descontinuidade, coleção adjacente, ar

### Oncológico
- Contato circunferencial com vaso, em graus
- Linfonodos por cadeia
- Fígado, pulmão, superfície peritoneal
- Exame prévio lado a lado — sem comparação não há resposta de resposta

---

## 4. Como escrever sem virar laudo

- **Cabeçalho com o rótulo, sempre.** Sem ele o texto migra.
- **Negativa só dentro da tabela do item 1.** Achado que a captura resolve pode ser negado, sempre com a coleira "nos cortes capturados" — ex.: "sem distensão de alças nos cortes capturados". Para tudo que está fora daquela tabela não existe "ausência de" em C2: existe `[não resolvível]`.
- **Nada de número.** Nem aproximado, nem "cerca de".
- **Nada de linguagem de laudo:** "compatível com", "sugestivo de", "aspecto de" são do radiologista.
- **Verbo na voz da equipe:** "na captura aparece", "não dá para resolver", "conferir na estação".
- A seção **Repercussão para a conduta** só existe se houver contexto clínico. Sem contexto, corte a seção — não a preencha com genérico.

---

## 5. Exemplo calibrado

**Entrada:** vídeo de 51 s do PACS, sem laudo, sem contexto clínico.

```
# IMPRESSÃO DA EQUIPE — TC de abdome e pelve com contraste EV, 25/07/26
Leitura de orientação sobre captura de PACS, pré-laudo. Não é laudo.

Substrato: 1040x722 · 51,4 s · 147 frames úteis · janela única de partes
moles (sem passada pulmonar ou óssea)

## Impressão
Laceração hepática em segmento IV, provável AAST III [a confirmar — falta
profundidade]. Baço com contorno preservado nos cortes capturados,
laceração fina não resolvível. Sem blush identificado nos cortes
capturados, mas fase não determinável — blush segue em aberto e é o que
decide angioembolização. Líquido livre peri-hepático em quantidade
moderada; pequena quantidade não é resolvível neste material. Sem
distensão de alças ou padrão obstrutivo nos cortes capturados. Rins com
realce simétrico, sem dilatação de vias urinárias nos cortes capturados.
Retroperitônio, diafragma, via biliar e pâncreas não resolvidos.

## Não resolvível neste material
Blush ou extravasamento ativo · líquido livre em pequena quantidade ·
pneumoperitônio mínimo · lesão de víscera oca · profundidade de laceração
e graduação AAST definitiva · fase de aquisição · via biliar · diafragma ·
fratura fina.
Nenhum destes está ausente — nenhum destes foi resolvido.

## Conferir na estação
1. Rolar do diafragma à sínfise em janela abdome, procurando líquido por
   espaço (Morison, periesplênico, goteiras, pelve)
2. Fígado e baço em fase portal — laceração, hematoma subcapsular
3. Blush: foco hiperdenso com densidade comparável à aorta no mesmo corte
4. Janela pulmonar nos cortes altos — pneumotórax, ar livre subdiafragmático
5. Janela óssea — arcos costais, coluna, pelve
6. Mesentério — densificação, ar extraluminal, espessamento focal
```

Sem contexto clínico, a seção de repercussão foi omitida. Com o quadro, ela entraria dizendo o que a imagem muda e o que não muda na decisão.

### O que o exemplo demonstra

- Impressão em prosa corrida, órgão a órgão, dominante primeiro — registro de equipe, não de laudo
- Grau afirmado com o parâmetro faltante explicitado no próprio texto, não omitido
- O item que decide conduta (blush) sai nomeado como aberto dentro da frase, não escondido na lista de baixo
- Negativa usada só para achado da tabela do item 1, sempre com "nos cortes capturados"
- Rótulo no cabeçalho e substrato quantificado antes de qualquer achado
- A frase que impede a leitura errada: "nenhum destes está ausente"
- Roteiro dirigido e numerado, com a janela certa em cada passo
- Seção de conduta omitida em vez de preenchida com genérico

---

## 6. Quando o laudo chega depois — retratação

Se um C2 já foi emitido nesta conversa e o laudo chega em seguida, a primeira
coisa do C1 é **reconciliar explicitamente**. Nomeie cada afirmação sua que o
laudo contradisse e diga que vale o laudo.

Os três achados que a captura quase sempre erra, e que o laudo rotineiramente
contradiz:

| O que o C2 costuma escrever | O que o laudo costuma trazer |
|---|---|
| "sem blush identificado nos cortes capturados" | extravasamento ativo presente |
| "baço com contorno preservado nos cortes capturados" | laceração fina, ou o inverso — baço íntegro quando havia suspeita |
| "sem fratura identificada" *(quando escrito indevidamente)* | fratura de arco costal posterior não desviada |

Isso é a skill funcionando como projetada, não erro a minimizar. A frase
`[não resolvível]` existe exatamente para que o C2 nunca tenha afirmado
ausência — e a retratação é o que impede que ela circule na conversa como se
tivesse afirmado.

Formato: uma linha por afirmação retratada, dentro da auditoria de proveniência,
com `[laudo]` sobrepondo-se ao que estava marcado `[não resolvível]`.

---

## 7. Revisão em estação não é C2

Se o usuário revisou as imagens na **estação de trabalho** — não na captura — e
ditou o que viu, isso não tem as limitações de substrato do C2. Os achados são
dele, saem afirmados, e podem incluir segmentação, blush e medida.

Cabeçalho:

```
# REVISÃO DA EQUIPE — [modalidade e cobertura], DD/MM/AA
Revisão direta em estação pela equipe de Cirurgia Geral, pré-laudo. Não é laudo.
```

Continua **fora** do formato de bloco de prontuário até o laudo sair. Curto — de
propósito. Impressão de equipe que fica longa vira laudo por acidente, e três
plantões depois alguém cita como se o radiologista tivesse escrito.

O que ainda sai marcado como pendente mesmo em revisão de estação: grau AAST
quando o percentual de lobo não foi medido, e a distinção entre extravasamento
ativo e pseudoaneurisma quando não houve fase tardia.
