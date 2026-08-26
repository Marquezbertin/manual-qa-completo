# Contribuindo com o Manual Completo de QA

Obrigado pelo interesse em melhorar este manual! Este guia explica como contribuir.

## Formato dos módulos

Cada módulo vive em `XX/PT/indice.md` e `XX/EN/index.md` (PT e EN sempre em paralelo).
Ao alterar um, mantenha o outro sincronizado.

## Regras gerais

1. **Bilingue**: toda explicação técnica deve ter versão PT e EN.
2. **Scripts reais**: exemplos de código devem ser executáveis e verificados.
   - Scripts sem dependências: rode localmente antes do PR.
   - Suítes pytest (M05, M06): `cd <mod>/scripts && pytest`.
3. **Diagramas**: use blocos ` ```mermaid ` (validados no CI).
4. **Citações**: referencie normas/fontes reais (ISO, ISTQB, OWASP, etc.).
5. **Estilo**: sem comentários desnecessários em código; tom técnico e direto.

## Como enviar uma contribuição

1. Faça fork e crie uma branch: `git checkout -b melhoria/mXX-tema`
2. Implemente a mudança (PT + EN).
3. Rode localmente:
   ```bash
   python run_all.py          # scripts standalone
   python .github/scripts/check_mermaid.py
   pytest                      # integridade do manual
   ```
4. Abra um Pull Request descrevendo o que mudou e por quê.

## Ideias de contribuição

- Corrigir/atualizar referências e normas
- Adicionar novos módulos (ex: Mobile, Acessibilidade, Data/ETL QA)
- Traduzir exemplos ou ampliar exercícios
- Melhorar os templates de `10/`

## Conduta

Este projeto segue o espírito da comunidade aberta: respeito, colaboração e foco em
qualidade. Dúvidas? abra uma Issue.
