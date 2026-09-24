---
name: simulado-unifesp-pdf
description: >
  Gera simulados e cadernos de questões no padrão da banca UNIFESP/EPM R+ Cirurgia
  e entrega em PDF A4 formatado (caderno de questões separado do gabarito comentado,
  destaques de pérola e armadilha, badges de prioridade, blocos que não quebram entre
  páginas). Use SEMPRE que o Marcos pedir: "simulado", "monta um simulado", "faz N questões",
  "questões sobre [tema]", "caderno de questões", "prova de treino", "me testa em bloco",
  "transforma isso em questões", "gera questões desse material/ficha/mapa/artigo",
  "questões em PDF", "mesmo padrão do PDF anterior", "prova impressa", "simulado semanal".
  Acione também quando ele enviar material de estudo (ficha, mapa, artigo, aula, resumo,
  transcrição, análise de casos) e pedir para converter em questões, e sempre que pedir
  mais de uma questão de uma vez — mesmo sem falar em PDF. Para UMA questão avulsa e
  interativa em chat, use a skill `questao-unifesp`; esta aqui é para lotes com entregável.
---

# Simulado UNIFESP R+ — questão e PDF

Produz dois artefatos numa mesma execução: um **caderno de questões** que o Marcos responde
sem ver o gabarito, e um **gabarito comentado** que analisa as quatro alternativas e fecha
com pérola. A separação existe porque um simulado com resposta ao lado da pergunta não é
simulado — é leitura passiva.

## Antes de escrever

Verifique três coisas no pedido. Não pergunte se der para inferir:

1. **Quantas questões e sobre o quê.** Se o pedido for "uma questão para cada X" de um
   material que está no contexto, conte os X e faça uma para cada. Se não houver número,
   proponha 10 para tema único e 20–25 para simulado de bloco.
2. **Se há material-fonte no contexto.** Fichas, mapas, análises de caso, artigos e PDFs
   das provas anteriores são a matéria-prima preferencial: as questões ficam ancoradas em
   discriminadores reais em vez de genéricas. Extraia daí o gatilho clínico, o discriminador
   e a armadilha.
3. **Se o pedido é de lote ou de questão avulsa.** Lote → esta skill, com PDF.
   Questão única e interativa (pergunta, espera resposta, corrige) → `questao-unifesp`.

## Formato da questão

Leia `references/formato-questao.md` antes de escrever a primeira questão. Ele traz as
regras de construção do enunciado, a calibragem dos distratores, os maneirismos da banca e
a lista de armadilhas recorrentes. É a parte que determina se a questão é indistinguível de
uma da prova real ou se é uma pergunta de livro-texto disfarçada.

O ponto que mais erra quem escreve rápido: **use quatro alternativas (A–D)**, não cinco.
As provas de 2022 a 2026 usaram A–D; só a de 2020 teve cinco. A prova-alvo é 2027.

## Estrutura do documento

Siga `references/template-simulado.md` — é o esqueleto markdown exato, com os marcadores
que o script de PDF reconhece. Em resumo, o arquivo tem quatro partes:

1. **Cabeçalho** — título, subtítulo, como usar, e uma nota curta sobre escolhas de formato
   que fujam do default (por exemplo, o motivo de usar A–D).
2. **`# PARTE I — CADERNO DE QUESTÕES`** — só enunciados e alternativas. Nenhuma pista.
3. **`# PARTE II — GABARITO COMENTADO`** — tabela de gabarito rápido, depois a análise
   alternativa por alternativa e a pérola de cada questão.
4. **Leitura de desempenho** — faixas de acerto interpretadas, quais erros pesam mais e
   uma linha honesta sobre o que o simulado **não** cobre.

Cada `# H1` começa em página nova automaticamente, o que mantém o gabarito longe do caderno.

## Marcadores que o PDF entende

| No markdown | No PDF |
|---|---|
| `==texto==` | destaque amarelo — pérolas, cutoffs numéricos, regras |
| `!!texto!!` | destaque vermelho negrito — armadilhas e erros graves |
| `🔑` | badge PEROLA (usar no início de cada pérola do gabarito) |
| `⚠` | triângulo de atenção — ressalvas, incertezas, exceções |
| `🎯` | badge ORFAO — tema que cai na prova e não está na apostila |
| `🔴 🟠 🟡` | badges P1/P2/P3 — prioridade de estudo |
| `**Rótulo:**` no início do parágrafo | rótulo em vinho, destacado do corpo |
| `> citação` | bloco laranja — usar para falas literais de preceptor |
| `---` | fecha o bloco da questão (impede quebra no meio) |

Emojis fora dessa lista **desaparecem** do PDF: as fontes do container não têm os glifos.
Se precisar de um novo, adicione ao dicionário `EMOJI_BADGES` do script em vez de usá-lo cru.

## Gerando o PDF

```bash
pip install weasyprint markdown --break-system-packages -q
python3 scripts/build_simulado_pdf.py simulado.md simulado.pdf \
  --header "UNIFESP R+ Cirurgia 2027 - Simulado 22 questoes" \
  --footer "PS CG HSP - uso interno de estudo"
```

Cabeçalho e rodapé são renderizados por CSS e **não aceitam emoji nem acento em posição
arriscada** — mantenha-os em texto simples ASCII quando possível.

Depois de gerar, **confira visualmente** ao menos duas páginas (uma do caderno, uma do
gabarito) rasterizando com PyMuPDF antes de entregar:

```python
import pymupdf
d = pymupdf.open("simulado.pdf")
d[1].get_pixmap(matrix=pymupdf.Matrix(1.4, 1.4)).save("p2.png")
```

Isso pega os dois defeitos que passam despercebidos no markdown: emoji sumido e lista que
virou texto corrido.

Entregue **o PDF e o markdown** com `present_files`, nessa ordem — o markdown serve para
colar no Notion e para editar depois sem refazer tudo.

## Rigor médico

Estas questões viram material de estudo para prova de acesso direto; um distrator errado
ensina errado. Três regras que valem mais que a estética:

- **Consistência interna.** Se a TC do enunciado mostra apêndice normal, o gabarito não
  pode tratar como apendicite. Releia o enunciado depois de escrever o gabarito.
- **Sinalize divergência.** Quando a conduta do serviço divergir do guideline (acontece), diga
  isso no comentário, identifique qual é qual, e aponte o elemento inegociável de prova.
  Não force uma conduta local a parecer consenso internacional.
- **Marque o que não confirmou.** Classificação, dose ou cutoff sobre o qual haja dúvida
  entra com `[a confirmar]` e uma linha dizendo o que precisa ser checado, com quem.

Nunca invente número. Um cutoff aproximado destrói uma questão inteira, porque é
exatamente o cutoff que a banca cobra.

## Erro de escrita mais comum

O distrator preguiçoso. Se uma alternativa é obviamente absurda, ela não testa nada e
reduz a questão a três opções. A meta é que **pelo menos duas alternativas sejam
defensáveis** para quem não domina o discriminador — e que a análise do gabarito explique
por que cada uma falha, não só por que a certa acerta.
