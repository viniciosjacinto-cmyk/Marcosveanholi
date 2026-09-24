---
name: registro-lab-padronizado
description: >
  Registra exames laboratoriais de forma padronizada, agrupados por data, no formato utilizado na residência de Cirurgia Geral. Use esta skill SEMPRE que o usuário fornecer resultados de exames laboratoriais e pedir para: registrar, formatar, padronizar, organizar, transcrever, fazer o registro dos exames, "colocar no formato", "formatar o lab", "organiza os exames", "lab de hoje", ou qualquer variação. Também acione quando o usuário colar valores de laboratório e pedir conduta/evolução — a formatação dos exames é parte obrigatória do registro. Produz saída em texto limpo, sem negrito, sem unidades desnecessárias, no formato prontuário cirúrgico padrão.
---

# Registro Laboratorial Padronizado

Você é responsável por transcrever e formatar resultados de exames laboratoriais no padrão da residência de Cirurgia Geral.

## Regras fundamentais

**O que incluir:**
- Apenas exames que foram efetivamente realizados e têm resultado numérico disponível
- Se um exame está listado no pedido mas sem resultado, não incluir

**O que excluir obrigatoriamente:**
- Monócitos, eosinófilos e basófilos (mesmo que presentes no laudo)
- TFG (Taxa de Filtração Glomerular / eGFR)
- Valores de referência, exceto onde convencionalmente utilizados na prática (ex: "PCR ≤ 5", "LDL desejável")
- Unidades como /µL, mmol/L, mg/dL, U/L — apenas o valor numérico
- Negrito em qualquer parte da resposta

**Formato numérico:**
- Copiar os valores exatamente como estão no laudo — não arredondar, não interpretar, não deduzir
- Plaquetas sempre no valor completo com ponto separador de milhar: ex. 100.000 (nunca "100 mil")
- Relação N/L: calcular dividindo neutrófilos por linfócitos e arredondar para o inteiro mais próximo

## Formato de saída

Cada coleta recebe uma linha iniciada por hífen, com a data e horário arredondado (ex: 08h00), seguido dos exames disponíveis separados por "|":

```
- DD/MM/AAAA (HHh00): Hb [valor] | Leuco [valor] (N/L:[x]) | Plaq [valor] | Ur [valor] | Cr [valor] | Na [valor] | K [valor] | TGO [valor] | TGP [valor] | GGT [valor] | FA [valor] | BT [valor] | BD [valor] | BI [valor] | Ca Iônico [valor] | PCR [valor] | TSH [valor] | T4L [valor] | TTPa [valor] (R [valor]) | RNI [valor] | Gasometria: pH [valor], pCO2 [valor], pO2 [valor], HCO3 [valor], Lactato [valor] ([arterial/venosa])
```

**Regras de formatação:**
- Incluir apenas os exames que têm resultado — omitir os ausentes silenciosamente (sem deixar espaço ou placeholder)
- Após o valor de Leucócitos, inserir entre parênteses a relação N/L no formato: `(N/L:X)` — valor arredondado para inteiro
- Gasometria: indicar se é arterial ou venosa ao final entre parênteses
- TTPa: incluir o Ratio entre parênteses logo após o valor: `TTPa 45,3 (R 1,5)`
- Horário: arredondar para a hora cheia mais próxima (ex: 07h43 → 08h00; 14h20 → 14h00)

## Agrupamento por data/coleta

Quando houver múltiplas coletas no mesmo dia, cada uma gera uma linha separada com seu respectivo horário. Ordenar cronologicamente.

## Exames omitidos — aviso obrigatório

Ao final da resposta, se houver exames presentes no laudo que foram omitidos por uma das regras acima (monócitos, eosinófilos, basófilos, TFG) ou por qualquer outro motivo, listar obrigatoriamente:

```
Omitidos: [nome do exame] — [motivo]
```

Se nenhum exame foi omitido, não incluir esta seção.

## Em caso de laudo ilegível, incompleto ou resultado crítico ausente

Não registrar o exame em questão. Solicitar esclarecimento ao usuário informando qual exame está com problema.

## Exemplo de saída

Dado um laudo com coleta em 08/05/2025 às 06h30:
- Hb 10,2 | Ht 31 | Leuco 12.560 (N/L:5) | Plaq 234.000 | Ur 48 | Cr 1,2 | Na 138 | K 4,1 | PCR 87 | RNI 1,3

Omitidos: Monócitos — excluídos por padrão; Eosinófilos — excluídos por padrão; TFG — excluída por padrão.

---

## Dica de uso

O usuário pode colar o laudo bruto (texto, PDF transcrito ou imagem), especificar uma data, ou fornecer múltiplas coletas. Processe tudo o que for possível em uma única resposta organizada. Quando houver dúvida sobre a legibilidade de um valor, pergunte antes de registrar.
