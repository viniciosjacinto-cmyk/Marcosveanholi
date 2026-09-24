# Exportação das skills — Marcos (Cirurgia Geral UNIFESP/HSP)

As 13 skills de uso diário, prontas para levar para outras IAs.

## Arquivos

| Arquivo | Para quê |
|---|---|
| `INSTRUCOES-CURTAS.md` | ~2.500 caracteres. Colar no campo de instruções (limite de ~8.000 no ChatGPT e no Gemini). Tem o perfil e o gatilho de cada skill. |
| `SKILLS-COMPLETO.md` | Tudo num arquivo só: perfil, índice, as 13 skills na íntegra e os anexos de referência (tabelas AAST, temas UNIFESP, exemplos). Subir como **arquivo de conhecimento**. |
| `zips/<skill>.zip` | Uma skill por zip, no formato de upload de skill do Claude (pasta com `SKILL.md`). |
| `zips/TODAS-AS-SKILLS.zip` | Pacote completo (todas as pastas + o consolidado). |
| `skills/` | As pastas originais, incluindo scripts Python e templates. |

## Onde colocar cada um

**ChatGPT (GPT personalizado ou Projeto)**
1. Explorar GPTs → Criar → Configurar.
2. Instruções: colar `INSTRUCOES-CURTAS.md`.
3. Conhecimento: subir `SKILLS-COMPLETO.md`.
4. Ativar "Interpretador de código" se quiser que ele rode os scripts de PDF/.apkg da pasta `skills/`.

**Gemini (Gem)**
1. Gems → Novo Gem.
2. Instruções: colar `INSTRUCOES-CURTAS.md`.
3. Conhecimento: subir `SKILLS-COMPLETO.md`.

**Claude (outra conta ou claude.ai)**
- Configurações → Capacidades → Skills → Fazer upload: um `.zip` por skill, de `zips/`.
- Ou, num Projeto: `INSTRUCOES-CURTAS.md` nas instruções e `SKILLS-COMPLETO.md` nos arquivos.

**Qualquer outra IA sem base de conhecimento**
- Colar `INSTRUCOES-CURTAS.md` no começo da conversa e, quando for usar uma skill específica, colar só a seção `# SKILL: nome` do `SKILLS-COMPLETO.md`.

## Skills incluídas

- **Prontuário e plantão:** nota-cirurgica-hsp · registro-lab-padronizado · laudo-imagem · trauma-politraumatizado-hsp · logbook-cirurgico-r2
- **Raciocínio clínico e segurança:** raciocinio-dd-cirurgico · anti-alucinacao-ia
- **Técnica operatória:** mapa-cirurgico-mnemonico · passo-a-passo-cirurgia-iniciante
- **Estudo para R+:** questao-unifesp · simulado-unifesp-pdf · simulado-site-interativo · anki-cloze-medico

## Ficaram de fora

- Skills genéricas da Anthropic (pdf, docx, xlsx, pptx, canvas-design, skill-creator, navegador etc.): as outras IAs já têm equivalente.
- `manutencao-cirgeral22`: depende da pasta local do site CIRGERAL 22 no seu Mac.
- `agente-llm-conectado-ao-whatsapp` e `mapa-de-oportunidades-de-automacao`: não são do fluxo clínico.

## Observações

- Os scripts (PDF do simulado, site interativo, mapa em PDF, gerador .apkg) só rodam em IA com execução de Python. Sem isso, a IA entrega o conteúdo em texto no mesmo formato.
- Arquivos citados mas ausentes na origem: `trauma-politraumatizado-hsp/references/trauma-pediatrico.md` e `laudo-imagem/scripts/extrair_frames.py`.
- `logbook-cirurgico-r2` tem seu nome completo e CRM. Tire antes de compartilhar com outra pessoa.
