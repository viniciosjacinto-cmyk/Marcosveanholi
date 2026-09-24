# Exemplos de Referência — Mapas Cirúrgicos

Três exemplos completos e auditados para usar como base ao gerar mapas de cirurgias semelhantes. Cole o JSON correspondente, ajuste a cirurgia-alvo e rode `build_mapa_pdf.py`.

---

## 1. Hemitireoidectomia (referência canônica)

Mnemônico: **A·E·P·P·L**
Lei do procedimento: ATS rente à glândula · AIT rente à cápsula · ver o nervo antes de cortar.

```json
{
  "cirurgia": "Hemitireoidectomia",
  "tempos": [
    {"titulo": "ACESSO", "linhas": ["Coxim + hiperextensão cervical", "Kocher 2 cm acima da fúrcula", "Retalhos subplatismais"]},
    {"titulo": "EXPOSIÇÃO", "linhas": ["Linha alba cervical aberta", "Afastar pré-tireoidianos", "Ligar veia tireoidiana média"]},
    {"titulo": "PÓLO SUPERIOR", "linhas": ["Espaço de Reeve", "Ligar ATS rente à glândula", ""], "alerta": "Protege ramo externo do NLS (voz aguda)"},
    {"titulo": "PÓLO INFERIOR + NLR", "linhas": ["Identificar NLR no sulco TE", "Preservar paratireoides", "Ligar AIT rente à cápsula"], "alerta": "Lig. Berry = zona de risco do NLR"},
    {"titulo": "LIBERAÇÃO + SÍNTESE", "linhas": ["Berry com cautela", "Secção do istmo + retirar peça", "Síntese: planos + intradérmica"]}
  ],
  "estruturas_tabu": [
    {"titulo": "N. laríngeo recorrente", "linhas": ["Sulco TE → lig. Berry", "Uni: rouquidão", "Bi: traqueostomia"]},
    {"titulo": "Ramo ext. do NLS", "linhas": ["Junto à ATS", "Cricotireóideo", "Lesão: tom agudo"]},
    {"titulo": "Paratireoides", "linhas": ["Sup.: face post.", "Inf.: junto AIT", "Dúvida: autoimplante ECM"]},
    {"titulo": "Traqueia/Esôfago", "linhas": ["Risco no lig. Berry", "Cautério econômico", ""]}
  ],
  "regra_pearl": {
    "titulo": "REGRA DOS \"RENTES\"",
    "linhas": ["ATS → rente à GLÂNDULA", "AIT → rente à CÁPSULA", "NLR → ver antes de pinçar"],
    "italic": "Veja o nervo antes de cortar o vaso"
  },
  "checklist": ["NLR íntegro?", "Paratireoides preservadas?", "Hemostasia com Valsalva?", "Pólo sup. rente à glândula?", "AIT rente à cápsula?", "Peça orientada p/ AP?", "Indicação de dreno?"],
  "alertas_pos_op": ["PÓS-OP: voz + hematoma cervical", "EM 24 h: Ca iônico se sintomas"],
  "mnemonico": {
    "titulo": "MNEMÔNICO  A·E·P·P·L",
    "linhas": ["A  Acesso", "E  Exposição", "P  Pólo superior (ATS)", "P  Pólo inferior (NLR + AIT)", "L  Liberação (Berry + síntese)"],
    "frase": "Acessei, Expus, ligo o Pólo de cima, vejo o nervo no Pólo de baixo, Libero."
  }
}
```

---

## 2. Colecistectomia Videolaparoscópica

Mnemônico: **P·T·C·D·L** (Posicionamento · Trocartes · Calot · Dissecção · Lavagem)
Lei do procedimento: Critical View of Safety (CVS) obrigatório · 2 estruturas só entrando na vesícula · cístico identificado antes de qualquer clipe.

```json
{
  "cirurgia": "Colecistectomia Videolaparoscópica",
  "tempos": [
    {"titulo": "ACESSO E POSICIONAMENTO", "linhas": ["Decúbito dorsal, Trendelenburg reverso 30°", "Pneumoperitônio CO2 12 mmHg", "Trocartes em losango francês"]},
    {"titulo": "EXPOSIÇÃO DO HILO", "linhas": ["Pinçar fundo da vesícula → diafragma", "Pinçar Hartmann → tração lateral/inf.", "Identificar lig. hepatoduodenal"]},
    {"titulo": "DISSECÇÃO DE CALOT (CVS)", "linhas": ["Abrir peritônio em janela hep-cístico", "Liberar terço inf. do leito vesicular", "Confirmar CVS: 2 estruturas → vesícula"], "alerta": "Sem CVS = NÃO clipar. Considerar conversão"},
    {"titulo": "CLIPAGEM E SECÇÃO", "linhas": ["Cístico: 2 clipes proximais + 1 distal", "A. cística: 2 clipes + secção", "Colangiografia se cálculo/cístico largo"], "alerta": "Cuidado com via biliar — 80% das lesões são por confusão anatômica"},
    {"titulo": "DISSECÇÃO DO LEITO + SAÍDA", "linhas": ["Vesícula do leito com gancho/cautério", "Hemostasia do leito + lavagem", "Retirada por trocarte umbilical em saco"]}
  ],
  "estruturas_tabu": [
    {"titulo": "Via biliar principal", "linhas": ["Hepatocolédoco", "Lesão: Strasberg A-E", "Sempre considerar variação anatômica"]},
    {"titulo": "Artéria hepática direita", "linhas": ["Atrás do cístico em 80%", "Lesão: necrose hepática parcial", "Cuidado com a. cística \"em alça\""]},
    {"titulo": "Veia porta", "linhas": ["Lig. hepatoduodenal post.", "Lesão: hemorragia maciça", "Não dissecar profundamente"]},
    {"titulo": "Duodeno / cólon transverso", "linhas": ["Aderências firmes em colecistite", "Lesão térmica frequente", "Cautério com economia"]}
  ],
  "regra_pearl": {
    "titulo": "CRITICAL VIEW OF SAFETY",
    "linhas": ["Triângulo hep-cístico LIMPO", "Terço inf. do leito EXPOSTO", "2 estruturas entrando na vesícula"],
    "italic": "Sem CVS, sem clipe — converter ou colangiografar"
  },
  "checklist": ["CVS confirmado antes de clipar?", "Cístico e a. cística clipados separadamente?", "Leito vesicular sem sangramento?", "Colangiografia indicada/realizada?", "Vesícula em saco para retirada?", "Drenos? (só em colecistite complicada)", "Cavidade lavada e seca?"],
  "alertas_pos_op": ["PÓS-OP: dor desproporcional → suspeitar lesão", "Bile na cavidade → reabordagem precoce"],
  "mnemonico": {
    "titulo": "MNEMÔNICO  P·T·C·D·L",
    "linhas": ["P  Posicionamento + pneumo", "T  Trocartes em losango", "C  Calot + CVS obrigatório", "D  Dissecção e clipagem", "L  Leito + lavagem + saída"],
    "frase": "Posicionei, Triangulei, fiz o CVS de Calot, Dissequei com cuidado, Lavei e saí."
  }
}
```

---

## 3. Apendicectomia Aberta (McBurney)

Mnemônico: **A·D·B·M·F** (Abordagem · Divulsão · Base · Mesoapêndice · Fechamento)
Lei do procedimento: identificar o ceco antes do apêndice · base do apêndice é a referência absoluta · ileo-apêndice fixa orienta tudo.

```json
{
  "cirurgia": "Apendicectomia Aberta",
  "tempos": [
    {"titulo": "ABORDAGEM", "linhas": ["Decúbito dorsal", "Incisão de McBurney oblíqua (3-5 cm)", "Pele → subcutâneo → aponeurose oblíquo ext."]},
    {"titulo": "DIVULSÃO MUSCULAR", "linhas": ["Divulsão dos oblíquos (sentido das fibras)", "Abrir peritônio entre pinças (rachi)", "Aspirar líquido + colher cultura"]},
    {"titulo": "EXPOSIÇÃO DO APÊNDICE", "linhas": ["Identificar tênias do ceco", "Seguir tênia ant. até base apendicular", "Exteriorizar e isolar com compressas"], "alerta": "Apêndice retrocecal exige mobilização do ceco"},
    {"titulo": "MESOAPÊNDICE + BASE", "linhas": ["Ligar a. apendicular no mesoapêndice", "Ligadura dupla da base apendicular", "Secção entre ligaduras"], "alerta": "Base necrosada/perfurada → considerar tiflectomia"},
    {"titulo": "FECHAMENTO", "linhas": ["Revisão de hemostasia + lavagem se peritonite", "Síntese: peritônio + planos musculares", "Pele: ponto separado (deixar aberta se purulento)"]}
  ],
  "estruturas_tabu": [
    {"titulo": "Ceco / cólon ascendente", "linhas": ["Risco de lesão na base", "Tiflectomia se necrose", "Sempre preservar válvula ileocecal"]},
    {"titulo": "Íleo terminal", "linhas": ["Imediatamente medial ao ceco", "Lesão: fístula entérica", "Não confundir com apêndice longo"]},
    {"titulo": "Artéria ileocólica", "linhas": ["Origem da a. apendicular", "Lesão: isquemia do íleo terminal", "Ligar a apendicular RENTE ao apêndice"]},
    {"titulo": "Ureter direito", "linhas": ["Retroperitônio post.-medial", "Risco em apêndice retrocecal", "Cuidado com cautério profundo"]}
  ],
  "regra_pearl": {
    "titulo": "REGRA DO CECO E DA BASE",
    "linhas": ["Achar a tênia anterior do ceco", "Seguir até a base do apêndice", "Mesoapêndice antes da base"],
    "italic": "Não tire o apêndice antes de ver o ceco"
  },
  "checklist": ["Base apendicular sadia?", "Ligadura dupla da base?", "A. apendicular ligada?", "Cavidade lavada se peritonite?", "Cultura colhida (se contaminado)?", "Necessidade de dreno? (raro)", "Pele: cicatriz primária ou aberta?"],
  "alertas_pos_op": ["PÓS-OP: febre + dor → abscesso ou fístula", "EM 48 h: avaliar trânsito + sinais de íleo"],
  "mnemonico": {
    "titulo": "MNEMÔNICO  A·D·B·M·F",
    "linhas": ["A  Abordagem (McBurney)", "D  Divulsão muscular", "B  Buscar ceco e base", "M  Mesoapêndice + a. apendicular", "F  Fechamento por planos"],
    "frase": "Abri, Divulsei, achei a Base, ligo o Meso e a artéria, e Fecho."
  }
}
```

---

## Como usar estes exemplos

1. Identifique a cirurgia que mais se aproxima da solicitada.
2. Copie o JSON para `/tmp/mapa_dados.json`.
3. Edite os 5 tempos, 4 tabus e o mnemônico conforme a técnica solicitada.
4. Rode `python3 scripts/build_mapa_pdf.py --input /tmp/mapa_dados.json --output /caminho/mapa.pdf`.
5. Renderize o SVG inline usando `mcp__visualize__show_widget` com o template adaptado.

Mantenha a Lei dos Rentes (ou equivalente) e o autoteste em 3 blocos — esses dois elementos são a marca registrada do mapa.
