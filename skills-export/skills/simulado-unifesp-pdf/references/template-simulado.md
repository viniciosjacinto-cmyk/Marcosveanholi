# Template do markdown do simulado

Copie o esqueleto abaixo e preencha. Os marcadores estruturais (`#`, `###`, `---`, `==`, `!!`)
são lidos pelo `build_simulado_pdf.py` — mudá-los quebra o layout.

Regras de sintaxe que o script corrige sozinho, mas que é melhor já escrever certo:
listas precisam de **linha em branco antes**; rótulos `**Assim:**` consecutivos precisam de
linha em branco entre eles; nunca use dois `---` seguidos (viram um título "---").

---

```markdown
# SIMULADO DIRIGIDO — N QUESTÕES
### [subtítulo: de onde vieram as questões]

---

**Como usar:** responda a **Parte I** inteira sem olhar a Parte II. Marque também o seu
**grau de confiança** (Certeza / Dúvida entre duas / Chute). Depois confira a **Parte II**.

**Nota sobre o formato:** usei **4 alternativas (A–D)**. As provas de 2022 a 2026 usaram A–D;
apenas 2020 teve cinco. Como a prova-alvo é 2027, A–D é a aposta correta.

**Composição:** [quantas de cada tema, e por quê]

---

# PARTE I — CADERNO DE QUESTÕES

---

### QUESTÃO 1
*Tema: [Bloco] · Subtópico: [Subtópico específico]*

[Enunciado de 8–14 linhas: idade, sexo, queixa, tempo de evolução, antecedentes relevantes,
sinais vitais numéricos, exames com valores reais. O achado pivô em **negrito discreto**.]

Qual a conduta mais adequada?

**A)** [alternativa]

**B)** [alternativa]

**C)** [alternativa]

**D)** [alternativa]

---

### QUESTÃO 2
[...repetir até a última questão...]

---

# PARTE II — GABARITO COMENTADO

---

## Gabarito rápido

| Q | Gab | Q | Gab | Q | Gab | Q | Gab |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | **C** | 7 | **C** | 13 | **B** | 19 | **B** |
| 2 | **B** | 8 | **C** | 14 | **C** | 20 | **B** |

---

### Q1 — Gabarito C

- **A) Errada.** [motivo]
- **B) Tentadora.** [por que atrai e onde falha]
- **C) Correta.** [o discriminador explicitado]
- **D) Errada.** [motivo]

🔑 **Pérola:** ==[regra memorável com o número]== ⚠ [ressalva]

---

### Q2 — Gabarito B
[...]

---

## LEITURA DO SEU DESEMPENHO

| Faixa | Interpretação |
|---|---|
| **≥ 82%** | Zona de aprovação confortável nestes temas. |
| **64–77%** | Diagnóstico correto, escalonamento inconsistente. Refazer as fichas dos erros. |
| **< 60%** | Rever o conteúdo antes de fazer flashcards: o problema é de conceito. |

**Erros que valem mais que os outros:** [listar as questões de cutoff, escalonamento e completude]

**Este simulado não cobre:** [ser explícito sobre as lacunas]
```

---

## Variações

**Simulado de tema único (10 questões):** mesma estrutura, sem a seção de composição.
No lugar da leitura de desempenho, feche com as três questões que mais discriminam o tema.

**Questões extraídas de material-fonte:** acrescente, sob o subtítulo, uma linha dizendo de
onde cada questão veio (ficha, caso do PS, prova de que ano). Isso permite rastrear o
discriminador de volta à origem quando ele for contestado.

**Simulado misto de 50 questões (formato da prova real):** distribua pelos pesos verificados
em `formato-questao.md`, seção 5, e cronometre 75 minutos.
