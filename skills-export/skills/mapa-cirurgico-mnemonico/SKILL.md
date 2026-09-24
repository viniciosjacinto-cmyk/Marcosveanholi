---
name: mapa-cirurgico-mnemonico
description: >
  Gera mapas mnemônicos visuais de procedimentos cirúrgicos no padrão do residente de Cirurgia Geral UNIFESP/HSP.
  Use SEMPRE que o usuário pedir: "fixar passos da cirurgia", "mapa mnemônico", "5 tempos cirúrgicos", "fluxograma da cirurgia", "como decorar a cirurgia", "revisão pré-operatória", "diagrama dos passos", "estruturas-tabu", "checklist intraoperatório", "vou operar amanhã me ajuda", "review da técnica cirúrgica", "material para fixar/memorizar/estudar para amanhã".
  Acione também quando o usuário citar uma cirurgia (hemitireoidectomia, colecistectomia, apendicectomia, herniorrafia, Whipple, gastrectomia, esplenectomia, mastectomia, Lichtenstein, tireoidectomia, hemicolectomia, retossigmoidectomia, esofagectomia, suprarrenalectomia etc.) e pedir revisão objetiva.
  Produz diagrama SVG inline (5 tempos + 4 estruturas-tabu + checklist + mnemônico) e opcionalmente PDF A4 imprimível. Cores fixas, padrão "uma página" para revisão pré-op de bolso.
---

# Mapa Cirúrgico Mnemônico — Padrão UNIFESP/HSP

Skill para produção de **mapas mnemônicos visuais** de procedimentos cirúrgicos, no formato de revisão pré-operatória de bolso. Pensada para o residente de Cirurgia Geral que precisa fixar a anatomia, a sequência operatória e os pontos de risco de uma técnica antes de operar.

---

## Princípios Gerais

- **Medular**: o objetivo é fixação, não exaustividade. Cada item deve caber em uma linha.
- **Hierárquico**: sempre 5 tempos cirúrgicos + 4 estruturas-tabu. Essa estrutura repetida cria padrão mental reutilizável.
- **Visual primeiro, prosa depois**: o diagrama é o produto. Texto na conversa só para autoteste e pearls.
- **Cores fixas**: nunca usar `var(--...)` no SVG — usar hex explícito. O usuário pode estar em tema escuro.
- **Uma página A4**: o PDF precisa caber em uma folha para ser imprimível e funcional.

---

## Estrutura Obrigatória do Mapa

Todo mapa segue **rigorosamente** este template:

### Coluna esquerda — SEQUÊNCIA OPERATÓRIA (5 tempos numerados)

1. **Acesso** — posicionamento, incisão, planos de dissecção iniciais
2. **Exposição** — mobilização e identificação do campo operatório
3. **Tempo crítico 1** — geralmente abordagem do pedículo principal ou estrutura-chave (CAIXA COM BORDA VERMELHA se houver risco anatômico)
4. **Tempo crítico 2** — geralmente identificação/preservação de estruturas nobres (CAIXA COM BORDA VERMELHA)
5. **Liberação + Síntese** — retirada da peça, hemostasia, fechamento

> Cada tempo tem: 1 título curto + 3 linhas de bullet (cada uma cabendo numa linha de ~55 caracteres). Tempos 3 e 4 ganham 1 linha extra de alerta em vermelho (`⚠`).

### Coluna direita — 4 ESTRUTURAS-TABU (que NÃO podem ser lesadas)

Cada estrutura-tabu tem:
- Número em círculo vermelho
- Nome da estrutura
- 3 linhas: localização anatômica, consequência da lesão leve, consequência da lesão grave

### Painel inferior esquerdo — CHECKLIST MENTAL ANTES DE FECHAR

7 perguntas em formato `☐  pergunta?`, finalizando com 2 alertas de pós-op em vermelho.

### Painel inferior direito — MNEMÔNICO

Acrônimo do tipo `A·E·P·P·L` (ou variante de 4–6 letras) com:
- A letra grande em destaque
- O significado de cada letra
- Uma frase narrativa em itálico no final (estilo "fiz isso, depois aquilo")

### Painel intermediário direito — REGRA DOS "RENTES" (ou equivalente)

Caixa azul-marinho com 3 regras-ouro do procedimento + 1 frase-pearl em itálico amarelo.

---

## Fluxo de Geração

Quando o usuário pedir um mapa, siga estes passos:

### Passo 1 — Coletar os 5 tempos da cirurgia em questão

Se o usuário não especificou a cirurgia, **pergunte qual** antes de gerar. Não chute.

Se a cirurgia é conhecida, monte mentalmente os 5 tempos seguindo:
- T1 sempre é ACESSO (posição + incisão + retalhos/planos)
- T2 sempre é EXPOSIÇÃO (afastamento, identificação do campo)
- T3 e T4 são os 2 tempos críticos (variam por cirurgia)
- T5 sempre é LIBERAÇÃO + SÍNTESE

### Passo 2 — Identificar as 4 estruturas-tabu

São as 4 estruturas anatômicas cuja lesão muda o desfecho do paciente. Exemplos por cirurgia:

| Cirurgia | Estruturas-tabu típicas |
|---|---|
| Hemitireoidectomia | NLR · NLS-RE · Paratireoides · Traqueia/esôfago |
| Colecistectomia | Via biliar · Artéria hepática · Veia porta · Duodeno |
| Whipple | Veia porta/AMS · Via biliar · AMC · Pâncreas (anastomose) |
| Hernioplastia inguinal | N. ilioinguinal · N. iliohipogástrico · Vasos epigástricos · Funículo |
| Apendicectomia | Ceco · Íleo terminal · A. ileocólica · Ureter direito |
| Gastrectomia | Pâncreas (cauda) · Baço · Esôfago · Duodeno (coto) |
| Mastectomia | N. torácico longo · N. toracodorsal · Vasos axilares · Pleura |
| Hemicolectomia D | Duodeno · Ureter direito · AMS · Vasos cólicos médios |
| Retossigmoidectomia | Ureteres · Nervos hipogástricos · Vasos ilíacos · Plexo presacral |
| Esplenectomia | Cauda do pâncreas · Estômago (vasos curtos) · Cólon · Vasos esplênicos |

### Passo 3 — Renderizar o SVG (visualização inline)

Use `mcp__visualize__show_widget` com o template SVG completo. **Sempre** use as cores hex fixas listadas em `references/cores.md`. Nunca usar `var(--text-...)`.

Estrutura de coordenadas do SVG (viewBox 720×920):

```
[0,0]      Header navy band (h=62)
[20,92]    "SEQUÊNCIA OPERATÓRIA"   →   [20,108..582]  5 caixas de tempo (78–100px de altura)
[440,92]   "ESTRUTURAS-TABU"         →   [440,110..526] 4 caixas tabu (~98px cada)
[440,540]  Caixa "REGRA DOS RENTES" (navy, 106px)
[20,612]   "CHECKLIST MENTAL"        →   [20,630..850]  Caixa 220px
[440,660]  Caixa mnemônico amarela (190px)
[20,895]   Footer cinza
```

O esqueleto completo do SVG está em `references/template.svg`. Adapte o conteúdo, mantenha a estrutura.

### Passo 4 — Oferecer o PDF

Após mostrar o SVG, ofereça espontaneamente: "Quer que eu gere um PDF A4 imprimível pra você abrir no celular ou levar no bolso do jaleco?"

Se aceitar, use o script `scripts/build_mapa_pdf.py` com um JSON parametrizado (formato em `references/schema.md`). O comando é:

```bash
python3 scripts/build_mapa_pdf.py --input /tmp/mapa_dados.json --output <OUTPUT_DIR>/mapa_<cirurgia>.pdf
```

### Passo 5 — Autoteste na conversa (em prosa, não no SVG)

Após o visual, sempre adicione **3 blocos de perguntas curtas** para autoteste em texto:

- **Bloco 1 — Anatomia** (5 perguntas com respostas curtas em itálico/parênteses)
- **Bloco 2 — Decisões intraoperatórias** (5 perguntas)
- **Bloco 3 — Pós-op imediato** (3 perguntas)

Finalize com **uma "Pearl visionária"** — 1–2 leis sintéticas que governam o procedimento (ex.: "Lei dos rentes" + "Lei do ver antes de cortar" para tireoide).

---

## Regras de Estilo (Não Negociáveis)

- **Linguagem**: português técnico brasileiro, padrão UNIFESP/EPM. Sem inglês desnecessário.
- **Abreviações**: usar as correntes da residência (NLR, NLS-RE, AIT, ATS, ECM, AMS, AMC, FAST, ATB, etc.)
- **Tom**: visionário, prático, didático. Tratamento direto, sem "talvez" ou "considere".
- **Sem floreios**: nada de "esperamos que esse material ajude" — vá direto ao mapa.
- **Citação de evidência**: só quando muda decisão (ex.: "AIT rente à cápsula preserva irrigação paratireoide — evidência clássica de Thompson").

---

## Exemplos Disparadores (devem acionar a skill)

- "Vou fazer uma colecistectomia amanhã, me ajuda a fixar os passos"
- "Crie um mapa mnemônico de Whipple"
- "Quero um diagrama dos 5 tempos de uma herniorrafia Lichtenstein"
- "Preciso revisar apendicectomia, faz aquele esquema medular"
- "Mapa cirúrgico de gastrectomia subtotal"
- "Estruturas-tabu da esplenectomia"
- "Como decorar a sequência de uma esofagectomia"
- "Vou operar uma mastectomia, me dá um material rápido pra revisar"

---

## Arquivos da Skill

- `scripts/build_mapa_pdf.py` — Gerador parametrizado de PDF A4 (entrada: JSON)
- `references/template.svg` — Esqueleto SVG com placeholders
- `references/schema.md` — Schema do JSON de entrada do PDF
- `references/cores.md` — Paleta hex fixa (não usar CSS vars)
- `references/exemplos.md` — 3 exemplos completos (tireoide, colecistectomia, apendicectomia) para referência rápida
