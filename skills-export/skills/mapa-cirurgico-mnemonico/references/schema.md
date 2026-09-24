# Schema do JSON de entrada (`build_mapa_pdf.py`)

Exemplo completo abaixo (hemitireoidectomia). Todos os campos são obrigatórios exceto onde indicado.

```json
{
  "cirurgia": "Hemitireoidectomia · mapa mnemônico",
  "subtitulo": "5 TEMPOS CIRÚRGICOS  ·  4 ESTRUTURAS-TABU",

  "tempos": [
    {
      "titulo": "ACESSO",
      "linhas": [
        "Coxim interescapular + hiperextensão cervical",
        "Kocher 2 cm acima da fúrcula (4–6 cm)",
        "Retalhos subplatismais: notch tireoideo ↔ fúrcula"
      ]
    },
    {
      "titulo": "EXPOSIÇÃO",
      "linhas": [
        "Abrir linha alba cervical (entre pré-tireoidianos)",
        "Afastar esterno-hióideo e esterno-tireoideo",
        "Ligar veia tireoidiana média → rotação medial"
      ]
    },
    {
      "titulo": "PÓLO SUPERIOR",
      "linhas": [
        "Abrir espaço avascular de Reeve",
        "Ligar ATS rente à glândula",
        ""
      ],
      "alerta": "Protege ramo externo do n. laríngeo superior (voz aguda)"
    },
    {
      "titulo": "PÓLO INFERIOR + NLR + PARATIREOIDES",
      "linhas": [
        "Identificar NLR no sulco traqueoesofágico",
        "Localizar paratireoides + preservar pedículo",
        "Ligar AIT rente à cápsula"
      ],
      "alerta": "Triângulo de Beahrs / lig. Berry = zona de risco do NLR"
    },
    {
      "titulo": "LIBERAÇÃO + SÍNTESE",
      "linhas": [
        "Liberar lig. de Berry com cautela (NLR adjacente)",
        "Seccionar istmo · retirar peça · revisão + Valsalva",
        "Síntese: pré-tireoideos · platisma · intradérmica"
      ]
    }
  ],

  "estruturas_tabu": [
    {
      "titulo": "N. laríngeo recorrente",
      "linhas": [
        "Sulco traqueoesofágico → lig. Berry",
        "Lesão uni: rouquidão",
        "Lesão bi: dispneia / traqueostomia"
      ]
    },
    {
      "titulo": "Ramo ext. do n. laríngeo sup.",
      "linhas": [
        "Junto à a. tireoidiana superior",
        "Inerva o cricotireóideo",
        "Lesão: perda do tom agudo (cantor)"
      ]
    },
    {
      "titulo": "Paratireoides",
      "linhas": [
        "Sup.: face post., constante",
        "Inf.: junto à a. tireoid. inferior",
        "Em dúvida: autoimplante no ECM"
      ]
    },
    {
      "titulo": "Traqueia / Esôfago",
      "linhas": [
        "Risco maior no lig. de Berry",
        "Cautério com economia próximo à traqueia",
        ""
      ]
    }
  ],

  "regra_pearl": {
    "titulo": "REGRA DOS \"RENTES\"",
    "linhas": [
      "ATS → rente à GLÂNDULA (poupa NLS-RE)",
      "AIT → rente à CÁPSULA (poupa paratireoide)",
      "NLR → NUNCA pinçar antes de ver"
    ],
    "italic": "Veja o nervo antes de cortar o vaso"
  },

  "checklist": [
    "NLR visualizado e íntegro?",
    "Paratireoides preservadas (coloração)?",
    "Hemostasia revisada com Valsalva (PEEP)?",
    "Pólo sup. ligado rente à glândula?",
    "AIT ligada rente à cápsula?",
    "Peça orientada para AP (fio no pólo)?",
    "Necessidade de dreno? (só se hemostasia duvidosa)"
  ],

  "alertas_pos_op": [
    "PÓS-OP IMEDIATO: voz + sinais de hematoma cervical",
    "EM 24 h: Ca iônico/total se sintomas de hipocalcemia"
  ],

  "mnemonico": {
    "titulo": "MNEMÔNICO  A·E·P·P·L",
    "linhas": [
      "A  Acesso (Kocher + retalhos)",
      "E  Exposição (linha alba + V. média)",
      "P  Pólo superior (ATS rente)",
      "P  Pólo inferior (NLR + AIT)",
      "L  Liberação (Berry + istmo + síntese)"
    ],
    "frase": "Acessei, Expus, ligo o Pólo de cima, vejo o nervo no Pólo de baixo, Libero."
  },

  "footer_left": "Marcos · Residência Cirurgia Geral · revisão pré-operatória",
  "footer_right": "v1 · A4 · imprimível"
}
```

## Regras de Conteúdo

- **`tempos`**: exatamente **5** itens. Posições 3 e 4 podem ter `alerta` (em vermelho). T1, T2, T5 não usam alerta.
- **`estruturas_tabu`**: exatamente **4** itens.
- **`linhas`** dentro de cada tempo/tabu: máximo 3 linhas. Se uma linha for vazia (`""`) ela é renderizada como espaço.
- **`checklist`**: máximo 7 itens (sem `☐` no início — o script adiciona).
- **`alertas_pos_op`**: máximo 2 itens, sempre em vermelho.
- **`mnemonico.linhas`**: máximo 5 itens (uma letra por linha).
- **`mnemonico.frase`**: até ~100 caracteres. Se passar de 50 caracteres, o script quebra automaticamente em 2 linhas no espaço mais próximo.

## Tamanho máximo de string por linha

Para caber na largura do PDF sem cortar:
- Linhas de tempo (esquerda, 400 px de caixa): **~55 caracteres**
- Linhas de tabu (direita, 260 px de caixa): **~38 caracteres**
- Itens do checklist: **~50 caracteres**
- Linhas do mnemônico: **~40 caracteres**

Se uma linha passar do limite, ela é renderizada mesmo assim mas pode estourar a caixa. Prefira encurtar usando as abreviações da residência (NLR, AIT, ATS, ECM, AMS etc.).
