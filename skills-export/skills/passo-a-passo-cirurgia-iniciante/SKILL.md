---
name: passo-a-passo-cirurgia-iniciante
description: >
  Gera passo a passo granular de cirurgias no padrão "para quem vai operar pela primeira vez" — residentes de Cirurgia Geral UNIFESP/HSP. Entrega 35–50 passos numerados com instrumental, posicionamento, fechamento por planos e pós-op. Complementa o mapa mnemônico (que fixa em 5 tempos).
  Acione SEMPRE para: "passo a passo para dummies", "passo a passo para quem vai pela primeira vez", "passo a passo iniciante", "guia detalhado/executável da cirurgia", "vou assistir/auxiliar/operar amanhã me passa tudo", "todos os passos", "como operar pela primeira vez", "tutorial cirúrgico". Também quando o usuário citar uma cirurgia + termo de iniciante ou pedido de detalhe ("colecistectomia para iniciante", "todos os tempos da hernioplastia", "passo a passo completo de apendicectomia").
  Produz texto estruturado em 6 blocos fixos (Antes da Sala / Posicionamento / Incisão e Acesso / Tempos Cirúrgicos / Fechamento / Pós-op quando aplicável) + Pérola final.
---

# Passo a Passo Cirurgia Iniciante — Padrão UNIFESP/HSP

Skill para produção de **guias cirúrgicos detalhados e executáveis**, no formato "para quem vai operar pela primeira vez". Pensada para o residente que assistirá ou auxiliará uma cirurgia nova e precisa de um material granular, com passos numerados, materiais por tempo e sinais de alarme pós-op.

---

## Princípio Central

O mapa mnemônico (`mapa-cirurgico-mnemonico`) fixa a cirurgia em 5 tempos para revisão pré-op. Esta skill é o **complemento granular**: 35–50 passos numerados, com instrumental por tempo, decisões em tempo real e pós-op imediato. É o material para ler na noite anterior, não para revisar nos 5 minutos antes de degermar.

**Diferenças com o mapa mnemônico:**

| Mapa mnemônico | Passo a passo iniciante |
|---|---|
| 5 tempos macro | 35–50 passos micro |
| Para fixar antes da prova/cirurgia | Para executar durante a cirurgia |
| Visual (SVG) | Texto estruturado |
| Estruturas-tabu como destaque | Decisões e instrumental em cada passo |
| 1 página A4 | 2–4 páginas |

---

## Estrutura Obrigatória do Output

Todo passo a passo deve ter **rigorosamente** estes 6 blocos, nesta ordem:

### Bloco 1 — ANTES DE ENTRAR NA SALA

Checklist pré-op em 3–6 itens cobrindo:
- Equipamentos críticos a confirmar (neuromonitor, energia, USG, fluoroscopia, equipamentos especiais)
- Materiais especiais (Lugol, ATB profilático, marcador)
- Imagem disponível e revisada
- Termo de consentimento e marcação do lado

Use bullets curtos (1 linha cada). Inicie cada item com verbo no imperativo ("Confirme", "Verifique", "Revise").

### Bloco 2 — POSICIONAMENTO

3–6 passos numerados cobrindo:
- Decúbito + uso de coxim/acessórios
- Posição dos braços e cabeça
- Marcação prévia da incisão (quando relevante)
- Antissepsia e campos
- Verificação de acessos venosos e equipamentos

### Bloco 3 — INCISÃO E ACESSO

5–10 passos numerados cobrindo:
- Incisão (instrumento + plano)
- Dissecção dos planos superficiais
- Identificação das estruturas-chave do acesso
- Afastamento e exposição inicial

### Bloco 4 — TEMPOS CIRÚRGICOS

15–30 passos numerados, agrupados em **subtítulos por tempo crítico** (ex.: "POLO SUPERIOR + NLS-RE", "TRIÂNGULO DE CALOT", "MOBILIZAÇÃO CECAL"). Cada passo deve:
- Começar com **verbo no imperativo** ("Ligue", "Divida", "Identifique", "Estimule")
- Citar instrumental quando relevante (harmônico, Bovie, clipe, laço 2-0)
- Sinalizar pontos de decisão com ⚠ ou negrito
- Ser **uma frase completa**, executável

### Bloco 5 — FECHAMENTO

5–10 passos numerados cobrindo cada plano:
- Conferência pré-fechamento (gaze, compressa, instrumental, hemostasia, Valsalva quando aplicável)
- Fechamento por planos com fio específico
- Curativo

### Bloco 6 — PÓS-OP IMEDIATO (apenas quando relevante)

**Não inclua este bloco em cirurgias eletivas simples** (ex.: apendicectomia não complicada, colecistectomia sem icterícia, hernioplastia inguinal eletiva). Inclua quando:
- Cirurgia com risco de complicação grave precoce (tireoidectomia, paratireoidectomia, suprarrenalectomia, esofagectomia, Whipple, gastrectomia)
- Cirurgia em pcte de alto risco
- Procedimento com necessidade de monitorização específica

Formato: tabela com 3 colunas — **O que monitorar | Quando | Por quê** — com 2–4 linhas.

### Pérola Final

Sempre encerre com uma **Pérola de prova** em itálico (1–2 frases), marcada com 🔑, sintetizando a lei central que governa a cirurgia.

---

## Regras de Estilo (Não Negociáveis)

- **Numeração contínua** ao longo de todos os blocos 2 a 5 (passo 1 começa em Posicionamento, segue até o fechamento). O paciente sente a cirurgia como sequência contínua — o material reflete isso.
- **Verbo no imperativo** abrindo cada passo. Sem "deve-se", "recomenda-se", "o cirurgião faz".
- **Instrumental explícito** quando importa (não dizer "sutura" — dizer "Vicryl 4-0 interrompido"). Quando não importa, omitir.
- **Linguagem técnica brasileira UNIFESP/EPM**: NLR, NLS-RE, AIT, ATS, ECM, AMS, AMC, EH, ET, JA, VA, LM, FAST, Bovie, harmônico.
- **Sem floreios**: nada de "agora vamos com calma para o próximo tempo". Vai direto.
- **Decisões em tempo real** marcadas com ⚠ ou em negrito. Ex.: "⚠ Se o sinal do NLR sumiu, considere não operar o lado contralateral hoje."
- **Pré-op tabela** (Bloco 6) só quando muda manejo nas primeiras 24 h.

---

## Fluxo de Geração

### Passo 1 — Identificar a cirurgia

Se o usuário não especificou claramente, pergunte qual cirurgia antes de gerar. Não chute.

### Passo 2 — Mapear os tempos críticos

Os tempos críticos variam por cirurgia. Use a tabela do `mapa-cirurgico-mnemonico` (mesma lista de estruturas-tabu por cirurgia) como base, mas neste formato cada tempo crítico vira **um subtítulo do Bloco 4** com seus próprios passos numerados.

### Passo 3 — Gerar o texto estruturado

Siga rigidamente os 6 blocos. Use markdown com:
- `###` para nome de cada bloco
- `####` para subtítulos dentro do Bloco 4 (cada tempo crítico)
- Passos numerados com `1.`, `2.`, `3.`...
- Tabela markdown apenas no Bloco 6
- Pérola final em itálico

### Passo 4 — Não ofereça PDF nem SVG

Este formato é texto-primeiro. O usuário pode pedir conversão para PDF posteriormente, mas não ofereça espontaneamente — o material vive bem em texto e é fácil de copiar para o app de notas.

### Passo 5 — Encerre com a Pérola

A Pérola é não-negociável. É a única "lei" da cirurgia, sintética, memorável.

---

## Referência Completa

Veja `references/exemplo_tireoidectomia.md` para um exemplo completo no formato esperado, com todos os 6 blocos preenchidos. Use como referência de tom, granularidade e estrutura ao gerar novos passos a passo.

---

## Exemplos Disparadores (devem acionar a skill)

- "Vou auxiliar uma colecistectomia amanhã, faz um passo a passo detalhado pra mim"
- "Passo a passo completo de apendicectomia para iniciante"
- "Tutorial de hernioplastia Lichtenstein passo a passo"
- "Vou pegar uma tireoidectomia amanhã, me passa tudo"
- "Passo a passo para dummies de gastrectomia"
- "Guia executável da retossigmoidectomia"
- "Vou assistir Whipple amanhã, preciso de todos os passos"
- "Como operar pela primeira vez uma esplenectomia"

---

## Arquivos da Skill

- `references/exemplo_tireoidectomia.md` — Exemplo completo no formato esperado (referência principal)
