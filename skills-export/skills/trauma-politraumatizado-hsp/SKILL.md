---
name: trauma-politraumatizado-hsp
description: |
  Skill especializada no atendimento ao politraumatizado adulto e pediátrico, seguindo o protocolo do Dr. Diego Adão (UNIFESP/EPM – Hospital São Paulo). Use esta skill SEMPRE que o usuário pedir: apresentação de caso de trauma, passagem de plantão de trauma, preenchimento do iMIST3AMBO, avaliação XABCDE, HD de trauma, checklist de atendimento ao politraumatizado, ou qualquer simulação/exercício de sala de emergência com paciente traumatizado. Também acione quando o usuário descrever sinais vitais de cena + mecanismo de trauma e pedir conduta, ou quando mencionar "politrauma", "sala de trauma", "FAST", "shock index", "transfusão maciça", "ácido tranexâmico em trauma", "protocolo de trauma HSP/EPM", ou "avaliação primária".
---

# Skill: Atendimento ao Politraumatizado — HSP/EPM (Diego Adão)

## Visão Geral

Esta skill implementa o protocolo de atendimento ao politraumatizado adulto e pediátrico utilizado na UNIFESP/EPM (Hospital São Paulo), conforme o método do Dr. Diego Adão. Cobre:

1. **Passagem de caso pré-hospitalar**: mnemônico iMIST3AMBO
2. **Avaliação na sala de emergência**: mnemônico XABCDE
3. **Construção do HD** (lista de problemas diagnósticos) no estilo Diego Adão
4. **Checklist completo** de procedimentos por letra
5. **Formato de saída no padrão prontuário Tasy do PS CG** (Templates A e B)

> **Regra-mestra de output:** o formato de saída segue SEMPRE o padrão real do PS CG HSP (Templates A/B abaixo), não o layout genérico do ATLS. O ATLS permanece como base teórica/de prova; o que vai para o Tasy é o padrão HSP.

---

## 1. Definições Essenciais

- **Trauma**: transmissão de energia além da tolerância anatômica/fisiológica.
- **Politrauma** (mortalidade ≥ 30%): ≥ 2 lesões com AIS ≥ 3 **+** ≥ 1 critério de gravidade:
  - Idade ≥ 70 anos
  - Glasgow ≤ 8
  - PAS ≤ 90 mmHg
  - BE ≤ −6 mEq/L
  - RNI ≥ 1,4

---

## 2. Passagem de Caso — iMIST3AMBO

Use para handover APH → Sala de Emergência ou passagem de plantão.

**Ordem real dos 3 Ts no padrão HSP: Transporte → Tempo → Tratamento APH.**
Em trauma focal de extremidade, **AMBO e o 3º T (tratamento APH) podem ser omitidos** se não houver dado — não forçar campo vazio.

| Letra | Campo | Conteúdo Obrigatório |
|-------|-------|----------------------|
| **i** | Identificação | Iniciais, idade, peso estimado |
| **M** | Mecanismo | Tipo, velocidade/limite da via, altura, tempo submerso; quedas >3m (pediátrico) e colisões >30km/h = maior gravidade |
| **I** | Injúrias | Lesões identificadas na cena (deformidades, sangramento, perda de consciência) |
| **S** | Sinais Vitais da cena | FR, FC, PA, SpO₂, TEC, Glasgow, Dextro |
| **T** | Transporte | SAMU / Bombeiros / GRAU / particular / meios próprios |
| **T** | Tempo | Hora do acidente → chegada ao hospital; **hora de ouro** e **10 minutos de platina** |
| **T** | Tratamento APH | Colar cervical, prancha, volume, analgesia, torniquete, acesso venoso, ácido tranexâmico (omitir se ausente) |
| **A** | Alergias | Sobretudo analgésicos e antibióticos |
| **M** | Medicações | Anticoagulantes + data da última dose; última alimentação |
| **B** | Background | Comorbidades, vacinação, ascite (FAST falso+), déficit/cirurgia neurológica prévia (ex.: craniectomia) |
| **O** | Outros | Hipotermia, intoxicação, restrições religiosas (transfusão), tabagismo/etilismo, condições ambientais |

---

## 3. HD — Lista de Problemas Diagnósticos (Estilo Diego Adão)

**Regras obrigatórias:**
- Evento-âncora (mecanismo) no topo; eixos de lesão subordinados com `>`
- Listar do mais grave ao menos grave
- Procedimentos subordinados ao problema que trataram
- Separar scores de diagnósticos (Glasgow/SI são dado, não diagnóstico)
- Itens sem diagnóstico fechado → "a esclarecer"
- Trauma: organizar por eixo de lesão (neuro, torácico, abdominal, vascular, ortopédico)

**Exemplo trauma (padrão HSP real):**
```
HD:
Atropelamento por ônibus
> Trauma facial
> TCE leve com sinais de alarme (amnésia lacunar)
> Trauma contuso de extremidades
```

---

## 4. Avaliação XABCDE — Sala de Emergência

> No output, usar as **frases-padrão de normalidade** abaixo e editar apenas o que mudou. Quando o dado não foi examinado, usar `[a confirmar]` — nunca cravar normalidade não verificada (ex.: não escrever "Glasgow 15, pupilas isocóricas" em paciente com perda de consciência sem ter examinado).

### X — Hemorragia Externa Ameaçadora à Vida
Frase-padrão: *Sem sangramento ameaçador à vida.*
- Comprimir ativamente toda fonte visível; torniquete **proximal** à lesão (sem contraindicação se < 60 min)
- Principal causa de morte **prevenível** no trauma — entra antes do A

### A — Via Aérea + Coluna Cervical
Frase-padrão: *Via aérea pérvia, sem enfisema ou hematoma cervical, sem desvio de traqueia.*
- Glasgow < 8 → via aérea definitiva (cânula + cuff + fixada + O₂ + pressão positiva)
- Colar sistemático dificulta ventilação/intubação; avaliar caso a caso; se remover → **MILS**
- Intubação guiada por **ePOCUS**
- **Pediátrico**: coxim no dorso; Guedel sem rotação 180°; cricotireoidostomia cirúrgica contraindicada < 12 anos

### B — Respiração / Tórax
Frase-padrão: *FR: __. SO2: __ aa. Expansibilidade torácica simétrica, sem enfisema de subcutâneo.*
- Inspeção/palpação/percussão/ausculta; **ePOCUS (BLUE, Z1–Z3)**
- Pneumotórax simples/hipertensivo, hemotórax simples/maciço
- Alívio: 2º EIC LMC → drenagem 5º EIC entre LAA e LAM; O₂ se SpO₂ < 94%
- **Pediátrico**: principal causa de PCR = hipóxia; tunelizar dreno

### C — Circulação / Hemodinâmica
Frase-padrão: *PA __/__; FC __, sem dor à palpação abdominal, pelve estável, TEC < 3 segundos.*
- Macro: FC, PA, TEC, pulso radial (some com PAS < 90 em > 12 anos); **SI = FC/PAS** (SIPA pediátrico)
- Micro: BE < −6 = pior prognóstico + preditor de transfusão maciça
- Fontes ocultas: pericárdio, peritônio, retroperitônio, pelve, ossos longos
- Acesso: **periférico > intra-ósseo > femoral**
- Ressuscitação: RL aquecido 10 mL/kg bolus → respondedor / transitório / não-respondedor (→ hemocomponentes 1:1:1 + PTM)
- **NÃO** infundir 20–30 mL/kg empírico
- **ATX**: trauma < 3h + sangramento → 15 mg/kg IV (máx 1g) bolus → 2 mg/kg/h por 8h
- **PTM**: RABT > 1 (adultos) / BIS > 0 (crianças)
- **Hipotensão permissiva de Cannon**: PAS alvo = 50 + 2×idade
- Coleta no acesso: HMG, tipagem, βHCG, coag (AP/TTPa/fibrinogênio), Cr/U, Na/K/Ca iônico

### D — Neurológico / Consciência
Frase-padrão: *Glasgow 15 (O:4 V:5 M:6), pupilas isocóricas e fotorreagentes. Sem déficits focais.*
- Glasgow + pupilas → **Glasgow-P**; ePOCUS nervo óptico > 5,5 mm → suspeita HIC
- Evitar 2ª lesão: SaO₂ < 92% e PAS < 110
- Cushing sem descompressão imediata → manitol 2 g/kg IV bolus
- **Pediátrico**: critérios PECARN
- **Atenção a neurocirurgia prévia** (craniectomia/cranioplastia): exame basal pode vir alterado; documentar estado prévio

### E — Exposição + Ambiente
Frase-padrão: *Dorso sem desalinhamento e sem lesões cutâneas. Pulsos 4/4+ presentes bilateralmente.*
- Expor + rotação em bloco; prevenir hipotermia (passivo + ativo)

---

## 5. Medidas Complementares da Avaliação Primária

Toque retal · SNG (contraindicada via nasal em fratura de base de crânio) · SVD (contraindicada em fratura de pelve) · gasometria (BE) · glicemia capilar · eletrocardioscopia · Rx cervical/tórax/pelve · whole-body CT.

---

## 6. Avaliação Secundária

- História **AMPLA**
- Scores: **RTS**, **ISS**, **TRISS** → calculadora: https://www.mdapp.co/trauma-injury-severity-score-triss-calculator-277/

---

## 7. Formato de Saída — TEMPLATE A (Admissão Trauma)

```
PENDÊNCIAS:


# PS CIRURGIA GERAL

PROTOCOLO TRAUMA


I: [iniciais, idade, peso estimado __ kg]
M: [mecanismo + limite da via/altura].
I: [injúrias da cena].
S: PA __x__mmHg; FC __bpm; FR __; SpO2 __%; Dextro __.
T: [SAMU / Bombeiros / GRAU / particular / próprios]
T: Há cerca de __.
T: [tratamento APH]            ← omitir se não houve


A: [nega / __].
M: [medicações / nega] [anticoagulante? última dose __].
B: [comorbidades / cirurgia neuro prévia / nega].
O: [tabagista __ maços-ano / etilista / nega].


X: Sem sangramento ameaçador à vida.
A: Via aérea pérvia, sem enfisema ou hematoma cervical, sem desvio de traqueia.
B: FR: __. SO2: __ aa. Expansibilidade torácica simétrica, sem enfisema de subcutâneo.
C: PA __/__; FC __, sem dor à palpação abdominal, pelve estável, TEC < 3 segundos.
D: Glasgow 15 (O:4 V:5 M:6), pupilas isocóricas e fotorreagentes. Sem déficits focais.
E: Dorso sem desalinhamento e sem lesões cutâneas. Pulsos 4/4+ presentes bilateralmente. [achados].


# CONDUTA:
[bloco C1/C2/C3]


https://www.mdapp.co/trauma-injury-severity-score-triss-calculator-277/
```

## 8. Formato de Saída — TEMPLATE B (Nota Completa de Trauma)

```
# PS CIRURGIA GERAL

HD:
[evento-âncora]
> [eixo 1]
> [eixo 2]
> [eixo 3]

# HPMA: [narrativa, 1 parágrafo].

SSVV ENTRADA: FR __  SAT __%  PA __/__  FC __  GCS __

# EXAMES DE IMAGEM:
TC [região] (DD/MM): [transcrição verbatim].

# LABORATÓRIOS:
[aguardo / valores]

# CONTROLES: PAS __-__ // PAD __-__ // PAM __-__ // FC __-__ // FR __-__ // Tax __-__ // SatO2 __-__ // GLI __-__

# EVOLUÇÃO: [reexame, queixas, pendências de especialidade].

# CONDUTA[, conforme discutido com preceptoria]:
[bloco C1/C2/C3]
```

## 9. Blocos de CONDUTA

**C1 — Ativa (em investigação)**
```
- Jejum + SMB.
- Sintomáticos.
- Solicito exames laboratoriais na urgência.
- Solicito radiografia de [___].
- Reavaliaremos após exames de imagem.
```

**C2 — Liberação da Cirurgia Geral (trauma focal)**
```
- Sintomáticos.
- Suporte clínico.
- Solicito exames laboratoriais.
- Solicito radiografia de [___].
- Paciente com mecanismo de trauma isolado em [segmento], sem sinais de TCE, trauma
  torácico ou abdominal, com fluxo distal preservado, portanto sem condutas pela Cirurgia Geral.
- Aos cuidados da [especialidade].
- Reconvocar se necessário.
```

**C3 — Aguardando especialidade / preceptoria**
```
- Sem condutas da Cirurgia neste momento, reavaliar após retorno do paciente da [especialidade].
- Aguardo avaliação da [especialidade].
- Mantenho sintomáticos.
- Paciente e família cientes e de acordo com tratamento.
```

---

## 10. Referências

- Material didático: Dr. Diego Adão — UNIFESP/EPM, Disciplina de Gastroenterologia Cirúrgica, HSP
- Checklist Atendimento ao Politraumatizado — ligadotrauma.epm@gmail.com
- ATLS 10ª edição (base teórica)
- Protocolo BLUE (ePOCUS torácico) · PECARN (pediátrico) · RABT/BIS (transfusão maciça)
- Calculadora TRISS: https://www.mdapp.co/trauma-injury-severity-score-triss-calculator-277/

> Para casos pediátricos, leia também: `references/trauma-pediatrico.md`
