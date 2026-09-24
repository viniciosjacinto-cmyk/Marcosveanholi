# Padronização de laudo — referência

Índice:
1. Formato fixo do bloco
2. Correção de ditado — o que se toca e o que não
3. O que preservar verbatim
4. Boilerplate a cortar
5. Checklist de omissão ativa por contexto
6. Armadilhas de redação do laudo
7. Auditoria de escores de trauma
8. Hedge do radiologista → exame dirigido
9. Exemplo calibrado completo

---

## 1. Formato fixo do bloco

```
> [MODALIDADE E COBERTURA] DD/MM/AA:
[achado 1 verbatim]

[achado 2 verbatim]

[negativas sistemáticas, uma por linha, ordem do laudo]

OPINIÃO:
- [conclusão item 1 verbatim]
- [conclusão item 2 verbatim]

Graduação: [AAST / WSES]
```

Três regras que quebram o formato se violadas:

1. **Ordem do laudo preservada.** Não reagrupe por região anatômica, não reordene por gravidade. A ordem em que o radiologista ditou é informação — é o que permite conferir linha a linha contra o original no PACS.
2. **Um achado por parágrafo.** Achados não viram prosa corrida. Negativas sistemáticas, sim, ficam em linhas consecutivas sem parágrafo entre elas.
3. **`Graduação:` é a única linha sua dentro do bloco.** Tudo mais que for seu — auditoria, omissões, divergências, escores, conduta — sai fora do bloco de código, sem exceção.

O motivo da regra 3 é operacional: o bloco é copiado inteiro e colado no Tasy. Qualquer análise sua que esteja dentro dele passa, no prontuário, por texto do radiologista.

---

## 2. Correção de ditado — o que se toca e o que não

Laudo de plantão vem de reconhecimento de voz e chega com erro. Corrigir é obrigação, não liberdade editorial.

**Corrija em silêncio dentro do bloco:**

| Erro típico | Correção |
|---|---|
| extravasameneto | extravasamento |
| hipertanuanetes / hipertanuantes | hiperatenuantes |
| Associa-sem | Associam-se |
| espontanamente | espontaneamente |
| contusao, lesao, opiniao | contusão, lesão, opinião |
| intrahepático, intrabdominal | intra-hepático, intra-abdominal |
| pontuação duplicada (`..`), espaço antes de vírgula | limpo |

**Liste as correções em uma linha fora do bloco.** O usuário assina o documento; ele precisa poder conferir que você não mexeu em conteúdo.

**Nunca toque:** conteúdo, ordem, medidas, lateralidade, segmento, linguagem de incerteza, estrutura das frases, redundância entre corpo e conclusão. Não enxugue, não resuma, não melhore a redação. Redundância aparente pode ser lesão distinta; frase truncada pode ser ditado interrompido que precisa voltar para a radiologia, não ser costurada por você.

---

## 3. O que preservar verbatim

- Medidas, com as duas ou três dimensões como estão, sem arredondar
- Lateralidade (direita/esquerda) e segmento anatômico (Couinaud, arcos costais numerados, níveis vertebrais)
- Distâncias de dispositivo (TOT à carina, ponta de cateter, posição de dreno por espaço intercostal)
- Grau de desvio de fratura
- Linguagem de incerteza: "compatível com", "sugestivo de", "não se podendo afastar", "no atual contexto clínico", "no atual protocolo de estudo", "provável", "inespecífico"

O último item importa mais do que parece: transformar "compatível com contusão" em "contusão" converte impressão em diagnóstico, e o prontuário passa a afirmar o que ninguém afirmou.

---

## 4. Boilerplate a cortar

Some sem perda de informação clínica:

- Fórmulas de técnica genérica: "estudo realizado em aparelho multislice", "cortes axiais com reconstruções multiplanares", "após injeção endovenosa de contraste iodado não iônico"
- Disclaimers: "sugere-se correlação clínica", "comparar com exames anteriores quando disponíveis"
- Descrição normal de estrutura irrelevante ao problema: tireoide normal em TC de trauma abdominal, alterações degenerativas de coluna em politraumatizado jovem
- Achado incidental sem consequência: cisto renal simples, cisto hepático simples, granuloma calcificado

**Não corte:**

- Achado incidental que gera conduta ou seguimento (nódulo pulmonar, massa adrenal, aneurisma, lesão focal indeterminada)
- "Exame limitado por artefato de movimento" quando limita achado específico — aí vira informação, não disclaimer
- **Negativas sistemáticas.** Em trauma elas são o corpo da leitura: "ausência de lesões intracranianas", "ausência de fraturas faciais", "ausência de lesões aórticas", "ausência de derrame pleural, pericárdico ou pneumotórax", "ausência de fraturas na cintura escapular, coluna vertebral, costelas e ossos da bacia". Todas ficam, na ordem ditada.

---

## 5. Checklist de omissão ativa por contexto

Depois de padronizar, liste separadamente o que não foi comentado. Ausência de menção ≠ normal. **Ordene por peso clínico, não pela ordem do laudo.**

### Trauma abdominal — ordem de prioridade

1. **Alças e mesentério** — densificação mesentérica, espessamento focal de parede, ar extraluminal, líquido livre desproporcional à lesão de órgão sólido. É a lesão que fura a CNO 12–24 h depois e a omissão mais grave que um laudo de trauma pode ter.
2. **Blush / extravasamento ativo** — presença **ou** ausência explícita
3. **Diafragma** — sobretudo com fratura de arcos baixos ou lesão hepática/esplênica de cúpula
4. **Via biliar** — lesão de via biliar principal é indicação absoluta de cirurgia em trauma hepático
5. **Retroperitônio com zoneamento do hematoma** (I central, II lateral, III pélvica) — a zona muda a conduta
6. **Pâncreas e adrenais**
7. Bexiga e ureteres
8. Pelve óssea

### Trauma torácico
- Aorta torácica e mediastino (obrigatório se fratura de 1º/2º arco, desaceleração ou esmagamento)
- Árvore traqueobrônquica
- Diafragma
- Contusão vs. laceração pulmonar (achados distintos)
- Posição de dispositivos (TOT, dreno, cateter central)
- Derrame pericárdico
- Coluna torácica

### Abdome agudo não traumático
- Ponto de transição e sofrimento de alça
- Pneumoperitônio, mesmo mínimo
- Ar em veia porta / pneumatose
- Patência de eixo mesentérico e portal
- Apêndice: visualizado ou não visualizado (não visualizado ≠ normal)
- Coleções e sua drenabilidade percutânea

### Oncológico / estadiamento
- Relação com estruturas vasculares (grau de contato circunferencial)
- Linfonodos por cadeia
- Fígado, pulmão, peritônio
- Comparação com exame prévio e critério usado

### Pós-operatório
- Coleção: características que separam seroma, hematoma, abscesso
- Integridade de anastomose, ar extraluminal
- Posição e trajeto de drenos
- Distinguir achado esperado para o tempo de PO de complicação

---

## 6. Armadilhas de redação do laudo

Aponte quando encontrar; não resolva por conta própria.

- **Divergência entre corpo e OPINIÃO.** A mais frequente e a mais silenciosa. Lateralidade que existe no achado e some na conclusão ("lesão da via coletora direita" no corpo, "lesão da via coletora" na OPINIÃO); achado presente na descrição e ausente na conclusão, ou o inverso; gravidade discordante entre as duas seções.
- **Negativa alocada na seção errada.** "Ausência de lesões aórticas" escrito na seção ABDOME não clareia a aorta torácica.
- **Nomenclatura sobreposta.** "Lobo esquerdo" e "segmento IV" listados como achados separados — segmento IV é lobo esquerdo. Ou são lesões distintas, ou é redundância. Muda a contagem de lesões e potencialmente o grau.
- **Medida sem o eixo que importa.** Duas dimensões planares não fornecem profundidade, que é o parâmetro do AAST. E nenhuma medida linear fornece percentual de lobo, que é o parâmetro do grau IV hepático.
- **Grau afirmado sem o parâmetro que o define.** O radiologista pode afirmar "grau IV" apoiado no contexto clínico. Transcreva o grau dele — mas registre fora do bloco qual parâmetro formal está faltando.
- **Negativa de escopo excedido.** "Ausência de fraturas" em estudo que não cobriu o segmento fraturado.
- **Fase não declarada** em estudo com pergunta vascular. Se o serviço roda split-bolus, fases arterial e portal se sobrepõem e "extravasamento ativo" não é separável de realce venoso com a mesma confiança. Confirme o protocolo antes de acionar hemodinâmica com base nesse achado isolado.

---

## 7. Auditoria de escores de trauma

Escore calculado na sala, com FAST e clínica, fica desatualizado depois da TC. E ele vai para o banco de trauma.

### O que recalcular, por frequência de erro

**ISS.** Todo achado novo da TC pode gerar AIS novo em região nova. As duas lesões que mais mudam o ISS depois da imagem são lesão de órgão sólido de alto grau e contusão pulmonar. ISS = soma dos quadrados dos três maiores AIS em regiões corporais **distintas**.

**RABT.** Componentes: shock index >1 · mecanismo penetrante · fratura de pelve · **FAST positivo**. Um ponto cada. FAST positivo registrado com RABT 0 é erro aritmético, não julgamento clínico — aponte. RABT ≥2 prediz necessidade de transfusão maciça.

**Shock index.** FC ÷ PAS. Confira a divisão; erro de digitação é comum.

**RTS.** GCS + PAS + FR codificados. Recalcule só se os vitais registrados forem internamente incoerentes.

### Regra de honestidade

**Se você não tiver certeza do valor de AIS de uma lesão específica, diga isso e dê a faixa.** Não invente pontuação para fechar a conta. A tabela AIS não é memorizável com precisão e errar para cima ou para baixo num escore que vai para registro é pior que declarar incerteza.

Faixas de referência úteis (confirmar em tabela AIS quando o número for para registro):

| Lesão | AIS aproximado |
|---|---|
| Laceração hepática ou esplênica AAST III | 3 |
| Laceração hepática ou esplênica AAST IV | 4 |
| Laceração hepática ou esplênica AAST V | 5 |
| Contusão pulmonar unilateral | 3 |
| Contusão pulmonar bilateral | 4 |
| Fratura de 2–3 arcos costais | 2 |
| Fratura de ≥3 arcos costais | 3 |
| Tórax instável (flail chest) | 4 |
| Contusão de parede / equimose isolada | 1 |

---

## 8. Hedge do radiologista → exame dirigido

Todo "não se podendo afastar" gera um exame nomeado. Nunca devolva "correlacionar clinicamente".

| Hedge no laudo | Exame dirigido que responde |
|---|---|
| "não se podendo afastar lesão da via coletora" | fase excretora dirigida (~8–10 min) + Urina I; se confirmar, urologia |
| "extravasamento ativo" sem fase declarada | confirmar protocolo com a radiologia; fase tardia separa extravasamento ativo de pseudoaneurisma |
| "opacidade inespecífica, não se podendo afastar contusão/laceração pulmonar" | janela pulmonar dedicada + reavaliação em 24–48 h (contusão piora antes de melhorar) |
| "líquido livre sem lesão de órgão sólido identificada" | reavaliação dirigida de alças e mesentério; TC de controle ou laparoscopia diagnóstica conforme clínica |
| lesão hepática/esplênica de cúpula sem comentário de diafragma | reconstrução coronal e sagital |
| "hematoma retroperitoneal" sem zona | revisão em estação para zoneamento (I / II / III) |
| lesão de segmento VII/VIII sem comentário de veias hepáticas | fase venosa dirigida — extensão à confluência ou à cava retro-hepática tira o caso do escopo da embolização |

---

## 9. Exemplo calibrado completo

Politraumatizada, colisão moto × moto >50 km/h, estável na admissão. Laudo saiu com erro de ditado.

### Saída — bloco padronizado

```
> TC DE CORPO INTEIRO 23/07/26:
Extensa região de hiporrealce no parênquima hepático, continuando-se para a
região subcapsular, com profundidade em cerca de 7,2 cm e maior diâmetro de
11,1 cm, que no atual contexto clínico, sugere laceração hepática grau IV.
Associam-se focos de extravasamento ativo de contraste intra-hepáticos,
indicando sangramento ativo.

Pequena quantidade de líquido livre peri-hepático, periesplênico e na goteira
parietocólica direita, por vezes com focos espontaneamente hiperatenuantes de
permeio, sugerindo conteúdo hemático (hemoperitônio).

Líquido livre hipoatenuante na região pararrenal anterior direita e na pelve.
Não se podendo afastar, no atual protocolo de estudo, lesão da via coletora
direita.

Opacidade laminar no parênquima pulmonar paravertebral direito, com diminutos
focos aéreos de permeio, inespecíficos, não se podendo, no atual contexto
clínico, afastar pequena contusão/laceração pulmonar.

Ausência de regiões de hiporrealce no baço.
Bexiga de contornos regulares e conteúdo homogêneo.
Ausência de lesões intracranianas.
Ausência de fraturas faciais.
Ausência de lesões aórticas.
Ausência de derrame pleural, pericárdico ou pneumotórax.
Ausência de fraturas na cintura escapular, coluna vertebral, costelas e ossos
da bacia.

OPINIÃO:
- Sinais de laceração hepática grau IV, associado a focos de extravasamento
  ativo de contraste intra-hepáticos, indicando sangramento ativo.
- Pequena quantidade de líquido livre peri-hepático, periesplênico e na goteira
  parietocólica direita, por vezes com focos espontaneamente hiperatenuantes de
  permeio, sugerindo conteúdo hemático (hemoperitônio).
- Líquido livre hipoatenuante na região pararrenal anterior direita e na pelve.
  Não se podendo afastar, no atual protocolo de estudo, lesão da via coletora.
- Opacidade laminar no parênquima pulmonar paravertebral direito, com diminutos
  focos aéreos de permeio, inespecíficos, não se podendo, no atual contexto
  clínico, afastar pequena contusão/laceração pulmonar.

Graduação: fígado AAST IV / WSES III (grave, hemodinamicamente estável).
```

Correções de ditado, fora do bloco: *extravasameneto→extravasamento*, *Associa-sem→Associam-se*, *hipertanuanetes→hiperatenuantes*, *espontanamente→espontaneamente*, *contusao→contusão*.

### Auditoria — fora do bloco

**Omissões, por peso:** alças e mesentério · diafragma · via biliar · retroperitônio sem zoneamento · pâncreas e adrenais · árvore traqueobrônquica.

**Ambiguidades:** corpo diz "via coletora **direita**", OPINIÃO diz só "via coletora" · fase de aquisição não declarada.

**Grau:** o laudo afirma AAST IV apoiado no contexto, mas fornece profundidade e diâmetro, não percentual de lobo — que é o parâmetro formal do IV. O extravasamento descrito é intra-hepático, o que sustenta IV; se algum foco extravasar para a cavidade, sobe para V.

**Escores:** ISS registrado 17. Com fígado AAST IV (AIS 4 = 16) + contusão pulmonar unilateral (AIS 3 = 9), ISS = **25**. RABT registrado 0 com FAST positivo — deveria ser ≥1.

**Exame dirigido:** fase excretora (~8–10 min) + Urina I para a via coletora direita.

### O que o exemplo demonstra

- Ordem e conteúdo do laudo intactos; só ditado corrigido, com as correções listadas fora
- Negativas sistemáticas preservadas em bloco, na ordem ditada
- `Graduação:` como única linha acrescentada dentro do bloco
- Toda a análise fora do bloco, de modo que o que se cola no Tasy é só o laudo
- Grau transcrito do radiologista, com o parâmetro faltante apontado por fora
- Distinção IV vs V ancorada em onde o sangramento está contido
- ISS recalculado com os achados novos da TC; RABT confrontado com o FAST
- Hedge convertido em exame nomeado, não em "correlacionar clinicamente"
