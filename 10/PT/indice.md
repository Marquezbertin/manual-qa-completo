# Módulo 10: Templates e Apêndices

Este módulo reúne **artefatos prontos para uso** em projetos reais de QA.

## 10.1 Índice de Templates

| Arquivo | Descrição |
|---------|-----------|
| `10/PT/test_plan_template.md` | Template completo de Test Plan |
| `10/PT/bug_report_template.md` | Template de Bug Report |
| `10/PT/test_case_template.md` | Template de Caso de Teste |
| `10/PT/charter_template.md` | Template de Charter (SBTM) |
| `10/PT/checklist_aceite.md` | Checklist de Homologação |
| `10/PT/matriz_rastreabilidade.md` | Matriz de Rastreabilidade |
| `10/PT/glossario.md` | Glossário PT/EN |
| `10/PT/solucoes.md` | Guia de soluções (autoavaliação) |

## 10.2 Como usar

1. Copie o template para seu projeto
2. Preencha os campos `[ENTRE COLCHETES]`
3. Versione no repositório do projeto
4. Adapte conforme a maturidade do time

## 10.2.1 Central de Scripts Executáveis

Scripts reais e verificados ao longo do manual (rode localmente):

| Script | Módulo | Comando |
|--------|--------|---------|
| `05/scripts/` (login POM) | M05 | `cd 05/scripts && pytest` |
| `06/scripts/` (API local) | M06 | `cd 06/scripts && pytest` |
| `03/scripts/estimate.py` | M03 | `python 03/scripts/estimate.py` |
| `04/scripts/triage.py` | M04 | `python 04/scripts/triage.py` |
| `07/scripts/percentile.py` | M07 | `python 07/scripts/percentile.py` |
| `08/scripts/quality_gate.py` | M08 | `python 08/scripts/quality_gate.py` |
| `09/scripts/kpi.py` | M09 | `python 09/scripts/kpi.py` |

> Todos foram executados e validados durante a escrita deste manual.

## 10.3 Apêndice: Stack Recomendada (Moderna)

- **UI Automation**: Playwright + pytest
- **API Testing**: requests + Schemathesis + Postman/Newman
- **Performance**: k6 / Locust
- **CI/CD**: GitHub Actions
- **Reports**: Allure, pytest-html
- **Quality**: ruff, black, bandit, pytest-cov
- **Management**: Jira / Azure DevOps

## 10.4 Apêndice: Roadmap de Aprendizado

```
Iniciante:  M01 → M02 → M04 (manual)
Intermediário: M03 → M05 (automação) → M06 (API)
Avançado: M07 (performance) → M08 (CI/CD) → M09 (gestão)
Referência contínua: M10 (templates)
```

## 10.5 Apêndice: Certificações Relevantes

- **ISTQB** (Foundation / Advanced)
- **Certified Agile Tester** (ISTQB)
- **AWS/Azure** (cloud para performance/CI)
- **Six Sigma** (processos)

## 10.6 Checklist do QA (Capstone)

O que todo analista de QA deve dominar ao fim deste manual:

- [ ] Explicar QA vs QC vs Teste e os 7 princípios (M01)
- [ ] Aplicar ISO 25010 e atributos de qualidade mensuráveis (M02)
- [ ] Escrever um Test Plan com critérios de saída (M03)
- [ ] Redigir casos de teste, charters e bug reports (M04)
- [ ] Automatizar UI com Page Objects (M05)
- [ ] Testar APIs com validação de contrato (M06)
- [ ] Interpretar p95/p99 e configurar carga (M07)
- [ ] Montar um pipeline CI com quality gates (M08)
- [ ] Calcular KPIs e aplicar Risk-Based Testing (M09)
- [ ] Usar os templates deste módulo em projeto real

## 10.7 Citações e Referências

- **ISTQB®** — https://www.istqb.org/
- **IEEE 829 (histórico)** — Test Documentation Standard
- **ISO/IEC/IEEE 29119** — Test Processes
- **Allure Docs** — https://allurereport.org/

---

> **Fim do Manual.** Volte a qualquer módulo para aprofundar. Bom QA! 🚀
