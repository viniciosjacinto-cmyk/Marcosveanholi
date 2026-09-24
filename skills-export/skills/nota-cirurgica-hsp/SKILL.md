---
name: nota-cirurgica-hsp
description: >
  Skill para geração de notas clínicas cirúrgicas no padrão do residente de Cirurgia Geral da UNIFESP/HSP.
  Use SEMPRE que o usuário pedir: evolução de paciente cirúrgico, canetada, conduta ambulatorial, nota de passagem de plantão, nota pós-operatória, registro em prontuário, ou qualquer texto para Tasy em formato de nota médica.
  Também acione quando o usuário descrever um cenário clínico e pedir "como escrever no prontuário", "como registrar", "faz a nota", "escreve a evolução", "canetada", "conduta", ou "nota ambulatorial".
  Produz texto técnico, direto e executável no padrão prontuário Tasy — sem floreios, sem redundâncias, compatível com prática cirúrgica/urológica baseada em evidência.
---

# Nota Cirúrgica HSP — Padrão UNIFESP/EPM

Skill para produção de notas clínicas no padrão do residente de Cirurgia Geral da UNIFESP, compatível com o sistema Tasy do Hospital São Paulo.

---

## Princípios Gerais

- **Direto e técnico**: padrão de prontuário, sem subjetividade ou floreios.
- **Sintético, porém completo**: apenas informações clinicamente relevantes.
- **Baseado em evidência**: compatível com prática cirúrgica/urológica atual.
- **Formato Tasy**: frases curtas, verbos no infinitivo para condutas (exceto CANETADA, ver abaixo).
- **Sem redundâncias**: cada dado aparece uma única vez.

---

## Tipos de Nota

### 1. EVOLUÇÃO (internação / pós-operatório)

**Estrutura interna (não usar como subtítulos — redigir em parágrafo único contínuo):**

1. Estado geral e consciência
2. Sinais vitais relevantes (febre, estabilidade hemodinâmica)
3. Queixas ativas ou ausência delas
4. Aceitação alimentar / diurese / função intestinal (quando pertinente)
5. Sítio cirúrgico / drenos / dispositivos
6. Intercorrências nas últimas 24h

**Regras de formato:**
- **Parágrafo único, contínuo.** Nunca usar tópicos, bullets ou subtítulos.
- Frases curtas, afirmativas e objetivas.
- Informar ausência de achados relevantes de forma ativa ("sem febre", "sem sinais de infecção").
- Não repetir dados da HD ou da anamnese inicial.

**Exemplo de EVOLUÇÃO:**
> Paciente consciente, orientada, afebril, hemodinamicamente estável. Boa aceitação alimentar, sem náuseas ou vômitos. Diurese espontânea adequada. Sem dor abdominal ou lombar no momento. Sítio cirúrgico sem sinais de infecção, curativo limpo e seco. Sem intercorrências nas últimas 24h.

---

### 2. CANETADA / CONDUTA (ambulatório / consultório / plantão)

**Estrutura em tópicos com travessão (–):**

1. O que foi revisado / checado (exames, imagens, documentação)
2. Relato do paciente (queixas, informações trazidas)
3. Avaliação objetiva (achado clínico, decisão diagnóstica)
4. Conduta clara e executável

**Regras de formato:**
- Verbos em **primeira pessoa do singular**: Solicito, Indico, Opto, Programo, Mantenho, Reavalio, Insiro, Oriento, Encaminho, Discuto, Aguardo.
- Frases curtas. Uma conduta por tópico.
- Condutas claras, executáveis e objetivas.
- Não usar linguagem de relatório ou texto corrido.

**Exemplo de CANETADA / CONDUTA:**
> – Revisada TC de controle.
> – Paciente comparece sem prontuário; refere contraindicação cirúrgica mencionada pela Hematologia, sem conhecer diagnóstico.
> – Solicito documentação e parecer formal de Hemato/Oncologia com diagnóstico e avaliação de risco cirúrgico.
> – Mantida na fila para mini-percutânea.
> – Retorno em 1 mês após parecer das especialidades.

---

### 3. NOTA DE PASSAGEM DE PLANTÃO

Combinar estrutura da EVOLUÇÃO (estado atual) + CANETADA (pendências e condutas ativas), em dois blocos sequenciais.

---

## Verbos Preferidos por Contexto

| Contexto | Verbos |
|---|---|
| Solicitações | Solicito, Peço, Requeiro |
| Decisão terapêutica | Indico, Opto por, Programo |
| Manutenção | Mantenho, Continuo |
| Vigilância | Reavalio, Monitoro, Aguardo |
| Procedimentos | Insiro, Realizo, Procedo |
| Orientação | Oriento, Informo |
| Encaminhamento | Encaminho, Discuto com, Aciono |

---

## Checklist antes de gerar a nota

- [ ] Identifiquei o tipo de nota solicitada (evolução / canetada / passagem)?
- [ ] Tenho dados suficientes do cenário clínico?
- [ ] A evolução está em parágrafo único e contínuo?
- [ ] A canetada usa verbos em 1ª pessoa do singular?
- [ ] Há redundâncias a eliminar?
- [ ] A linguagem está compatível com prontuário Tasy?

---

## Conduta quando faltam dados

Se o usuário não fornecer informações suficientes para preencher a nota, perguntar diretamente e de forma objetiva:
- Tipo de nota (evolução / canetada / passagem de plantão)?
- Estado geral do paciente + sinais vitais?
- Contexto clínico (pós-op, ambulatório, plantão)?
- Queixas ativas e achados ao exame?
- Condutas já tomadas e pendências?

Nunca inventar dados clínicos. Se dado for desconhecido, omitir ou usar placeholder entre colchetes: [informar].
