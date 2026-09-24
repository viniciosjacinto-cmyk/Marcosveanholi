# Paleta Hex Fixa — Mapa Cirúrgico Mnemônico

**Nunca usar `var(--...)` no SVG do `show_widget`.** O usuário pode estar em tema escuro e os textos somem. Use sempre os hex abaixo.

## Estrutural

| Token       | Hex       | Uso |
|-------------|-----------|-----|
| BG          | `#fafaf7` | Fundo geral da página |
| WHITE       | `#ffffff` | Fundo das caixas neutras |
| DARK        | `#1a1a1a` | Texto principal (títulos, checklist) |
| GRAY        | `#333333` | Texto secundário (linhas de tempo, linhas de tabu) |
| LIGHT_GRAY  | `#d4d4d0` | Bordas das caixas neutras |
| LINE_GRAY   | `#9ca3af` | Linhas conectoras verticais entre tempos |
| SOFT        | `#e5e5e5` | Separador interno do checklist |
| FOOT        | `#666666` | Texto do footer |

## Acentos azuis (sequência operatória)

| Token       | Hex       | Uso |
|-------------|-----------|-----|
| NAVY        | `#1f3a5f` | Header band + caixa "Regra dos rentes" + títulos de seção |
| NAVY_TEXT   | `#cfe1f7` | Texto sobre fundo navy |
| BLUE        | `#2b6cb0` | Círculo numerado de cada tempo |
| GOLD        | `#ffd89e` | Frase-pearl em itálico dentro da caixa navy |

## Acentos vermelhos (estruturas-tabu)

| Token       | Hex       | Uso |
|-------------|-----------|-----|
| RED         | `#c1432a` | Bordas, círculos numerados das tabus, alertas em vermelho |
| RED_BG      | `#fff5f0` | Fundo das caixas de tempo críticas (T3 e T4) |

## Acentos amarelos (mnemônico)

| Token         | Hex       | Uso |
|---------------|-----------|-----|
| YELLOW_BG     | `#fffbe6` | Fundo da caixa do mnemônico |
| YELLOW_LINE   | `#d4b94a` | Borda da caixa + separador interno |
| YELLOW_DARK   | `#7a5b00` | Título "MNEMÔNICO A·E·P·P·L" |
| YELLOW_ITALIC | `#5a4400` | Frase narrativa em itálico no rodapé do mnemônico |

## Regra prática

- Texto sobre fundo claro → DARK ou GRAY.
- Texto sobre fundo navy → WHITE, NAVY_TEXT ou GOLD (apenas a frase).
- Bordas vermelhas (T3, T4 e todas as 4 tabus) marcam **risco anatômico** — não usar em caixas neutras.
