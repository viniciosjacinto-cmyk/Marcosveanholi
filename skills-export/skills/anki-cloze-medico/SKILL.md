---
name: anki-cloze-medico
description: >
  Gerador especializado de flashcards Anki Cloze em formato .apkg para estudo médico,
  residência médica e provas (como REVALIDA, concursos de residência, provas de título).
  Use este skill SEMPRE que o usuário enviar um texto médico, artigo, PDF, resumo, imagem
  transcrita ou questão e pedir flashcards, cards Anki, deck Anki, baralho Anki ou qualquer
  variação. Também acione quando o usuário mencionar "criar cards", "gerar Anki", "exportar
  .apkg", "cloze médico" ou quiser transformar conteúdo em material de revisão ativa.
  Produz arquivo .apkg real, importável diretamente no Anki desktop/mobile, sem genanki,
  usando apenas sqlite3 e zipfile do Python padrão.
---

# Anki Cloze Médico — Gerador de Flashcards .apkg

## Visão Geral

Transforma qualquer conteúdo médico em flashcards Anki Cloze de alto rendimento,
priorizando pontos cobrados em provas de residência. Entrega um arquivo `.apkg` real,
importável diretamente no Anki.

---

## Regras de Geração de Flashcards

### Quantidade
- **Padrão**: 10 flashcards por chamada, salvo instrução explícita do usuário.
- Se o usuário pedir número diferente, respeitar exatamente.

### Seleção de Conteúdo
Para textos longos, identificar primeiro os **10 pontos de maior probabilidade de cobrança**:
- Definições diagnósticas e critérios
- Limiares e valores de corte
- Condutas de primeira linha e exceções
- Diferenças conceituais e pegadinhas clássicas de prova
- Mensagens-chave de guidelines (preferencialmente atualizados)
- Classificações com implicação conduta

### Formato dos Flashcards

**Campo `Texto`** (frente + lacuna Cloze):
```
A {{c1::resposta}} é o critério diagnóstico principal para X.
```
- Curto, direto, uma ideia por card
- Preferencialmente **uma única lacuna** `{{c1::...}}`
- Linguagem técnica, médica, em português
- Evitar cards longos ou redundantes

**Campo `Extra`** (verso — explicação):
- Máximo 2–3 linhas
- Contexto clínico objetivo, útil para prova
- Incluir **"Pérola de prova:"** quando relevante
- Pode incluir diferencial ou exceção importante

### Exemplo de Card Bem Feito
```
Texto:
No GRADE, a imprecisão deve ser julgada pelo {{c1::intervalo de confiança em relação ao limiar de decisão clínica}}, e não apenas pelo valor de p.

Extra:
O IC 95% é comparado ao limiar de decisão (MID). Pérola de prova: significância estatística ≠ relevância clínica.
```

---

## Geração do Arquivo .apkg

**OBRIGATÓRIO**: Usar o script em `scripts/gerar_apkg.py`.  
**PROIBIDO**: Usar `genanki` — usar apenas bibliotecas padrão Python.

### Executar o script

```bash
python /home/claude/anki-cloze-medico/scripts/gerar_apkg.py \
  --cards '<JSON_DOS_CARDS>' \
  --deck-name '<NOME DO BARALHO>' \
  --output '/mnt/user-data/outputs/<nome_arquivo>.apkg'
```

O argumento `--cards` recebe uma string JSON com lista de dicts:
```json
[
  {"texto": "O {{c1::X}} é...", "extra": "Explicação. Pérola: ..."},
  ...
]
```

### Nomenclatura Padrão
- **Nome do baralho**: `CX`
- **Nome do arquivo**: `[tema_principal]_cloze.apkg` (sem espaços, sem acentos)

### Tags obrigatórias em todos os cards
`cloze`, `prova`, `residencia`, `medicina`  
Adicionar tags temáticas do conteúdo (ex: `pancreatite`, `trauma`, `antibioticos`).

---

## Processo Completo (passo a passo)

1. **Analisar o conteúdo** recebido e identificar os N pontos de maior rendimento para prova.
2. **Redigir os cards** no formato Cloze descrito acima.
3. **Montar o JSON** com lista `[{"texto": ..., "extra": ...}, ...]`.
4. **Executar `gerar_apkg.py`** com os parâmetros corretos.
5. **Verificar** que o arquivo foi gerado em `/mnt/user-data/outputs/`.
6. **Responder ao usuário** com mensagem curta + link de download.

---

## Resposta Final ao Usuário

Formato obrigatório (curto):

```
Pronto. Arquivo .apkg gerado com X flashcards Anki Cloze.

⬇️ [nome_do_arquivo.apkg](sandbox:/mnt/user-data/outputs/nome_do_arquivo.apkg)
```

Não adicionar listas longas de cards na resposta — o usuário vai estudar pelo Anki.  
Pode listar os temas cobertos em 1–2 linhas se quiser contextualizar.

---

## Tratamento de Erros

| Situação | Ação |
|---|---|
| `genanki` não disponível | Ignorar; usar sempre `gerar_apkg.py` com sqlite3 |
| Erro no script | Reportar linha exata do erro; não tentar workaround silencioso |
| Conteúdo muito curto (<5 pontos relevantes) | Gerar menos cards e informar |
| Arquivo não gerado em outputs | Verificar permissões; tentar `/tmp/` e copiar |

---

## Verificação de Qualidade (antes de entregar)

- [ ] Cada card testa **uma única ideia**
- [ ] Campo `Texto` tem `{{c1::...}}` válido
- [ ] Campo `Extra` tem ≤ 3 linhas
- [ ] Arquivo `.apkg` existe e tem tamanho > 0 bytes
- [ ] Nome do arquivo sem espaços ou acentos
