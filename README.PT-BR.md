# Manual Completo de QA

> **Um guia passo-a-passo da rotina de um Analista de Testes / QA**, com exemplos práticos, scripts reais, cenários de teste e modelos de documentos da indústria — em **Português (BR)** e **English**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-brightgreen)](https://playwright.dev/)
[![CI](https://github.com/Marquezbertin/manual-qa-completo/actions/workflows/ci.yml/badge.svg)](https://github.com/Marquezbertin/manual-qa-completo/actions/workflows/ci.yml)

---

## 📑 Índice

- [Sobre este Manual](#-sobre-este-manual)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Hub de Scripts Executáveis](#-hub-de-scripts-executáveis)
- [Como Executar](#-como-executar)
- [Tecnologias](#-tecnologias)
- [Licença](#-licença)

---

## 📖 Sobre este Manual

Este repositório é um **manual de referência** para Analistas de QA, cobrindo desde os fundamentos teóricos até a prática diária com ferramentas modernas. O conteúdo é dividido em módulos autônomos, com exemplos práticos, **scripts testados e verificados**, e templates prontos para uso.

### 🎯 Objetivo
- Base de conhecimento organizada para QAs de todos os níveis
- Documentar a rotina completa: do planejamento aos relatórios finais
- Oferecer scripts e templates usáveis imediatamente
- Material de estudo para certificações (ISTQB, ASTFC-AICS, SCRUM)

### 👤 Público-alvo
- Iniciantes em QA que querem aprender do zero
- QAs experientes que querem reorganizar o conhecimento
- Estudantes de Computação e cursos correlatos
- Profissionais em preparação para certificações de qualidade

### 🌐 Idiomas
- **Português (BR)** — foco no mercado nacional e certificações locais (`*/PT/`)
- **English** — termos internacionais (ISTQB) e práticas globais (`*/EN/`)

---

## 📁 Estrutura do Repositório

11 módulos, cada um com versão PT e EN. A coluna **Scripts** indica módulos que trazem código executável verificado.

| Módulo | Título | Conteúdo Principal | Scripts |
|--------|--------|-------------------|---------|
| `01` | Visão Geral do QA | QA vs QC, 7 princípios ISTQB, Custo da Qualidade, STLC | — |
| `02` | Fundamentais da Qualidade | ISO 25010, V-Model, atributos de qualidade mensuráveis | — |
| `03` | Planejamento de Testes | Policy/Strategy/Plan, estimativa PERT, mini Test Plan | `estimate.py` ✅ |
| `04` | Testes Manuais e Exploratórios | Casos de teste, SBTM, Severidade×Prioridade, Nielsen | `triage.py` ✅ |
| `05` | Testes Automatizados | Pirâmide, Page Objects, Playwright + Pytest | suíte pytest ✅ |
| `06` | Testes de API | Verbos HTTP, requests, validação de contrato (jsonschema) | suíte pytest ✅ |
| `07` | Performance e Carga | Locust/k6, percentis p95/p99, análise | `percentile.py` ✅ |
| `08` | Qualidade de Código e CI/CD | Cobertura, lint, quality gates, SAST, GitHub Actions | `quality_gate.py` ✅ |
| `09` | Gestão de Qualidade e Processos | TMMi, ISO 25010, KPIs, Risk-Based Testing, PDCA | `kpi.py` ✅ |
| `10` | Templates e Apêndices | Test Plan, Bug Report, Test Case, Charter, Matriz, Glossário | — |
| `11` | Testes de Segurança (OWASP) | OWASP Top 10, SAST/DAST, secret scan | `secret_scan.py` ✅ |

Cada módulo contém:
- **PT/** e **EN/** — versões em português e inglês
- Exemplos de código reais e verificados
- Templates prontos para download
- Citações técnicas com referências

---

## 🚀 Hub de Scripts Executáveis

Scripts reais e **validados** ao longo do manual. Rode localmente:

| Script | Módulo | Comando |
|--------|--------|---------|
| `03/scripts/estimate.py` | M03 — Estimativa PERT | `python 03/scripts/estimate.py` |
| `04/scripts/triage.py` | M04 — Severidade×Prioridade (SLA) | `python 04/scripts/triage.py` |
| `05/scripts/` | M05 — Login UI (Page Object) | `cd 05/scripts && pytest` |
| `06/scripts/` | M06 — API REST local | `cd 06/scripts && pytest` |
| `07/scripts/percentile.py` | M07 — p95/p99 | `python 07/scripts/percentile.py` |
| `08/scripts/quality_gate.py` | M08 — Quality Gates | `python 08/scripts/quality_gate.py` |
| `09/scripts/kpi.py` | M09 — KPIs de qualidade | `python 09/scripts/kpi.py` |

> **Status de verificação:** 9 testes pytest (M05: 6, M06: 3) + 7 scripts standalone, todos executados com sucesso na escrita deste manual.

---

## 🛠️ Como Executar

### 1. Clone
```bash
git clone https://github.com/Marquezbertin/manual-qa-completo.git
cd manual-qa-completo
```

### 2. Scripts standalone (sem dependências externas)
```bash
python 03/scripts/estimate.py
python 04/scripts/triage.py
python 07/scripts/percentile.py
python 08/scripts/quality_gate.py
python 09/scripts/kpi.py
```

### 3. Suítes pytest (automação e API)
```bash
# M05 — precisa de Playwright + Chromium
cd 05/scripts
pip install playwright && playwright install chromium
pytest

# M06 — precisa de requests + jsonschema
cd 06/scripts
pip install requests jsonschema
pytest
```

### 4. CI (GitHub Actions)
O pipeline em `.github/workflows/ci.yml` roda automaticamente em cada push/PR, executando os testes da raiz e validando a integridade do manual.

### Atalho
```bash
make all            # roda scripts standalone + validação mermaid + suíte M06
python run_all.py   # equivalente em Python (--suites para incluir M05/M06)
```

---

## 🧰 Tecnologias

- **Python 3.10+** — linguagem principal dos scripts
- **Playwright + pytest** — testes de UI modernos e estáveis
- **requests + jsonschema** — testes de API e validação de contrato
- **k6 / Locust** — testes de performance e carga
- **GitHub Actions** — integração contínua
- **Faker** — geração de dados de teste (pt-BR / en-US)
- **ruff, black, bandit, pytest-cov** — qualidade de código e cobertura

---

## 📜 Licença

Este projeto está licenciado sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> *"Quality is never an accident. It is always the result of intelligent effort."* — **John Ruskin**

---

🌐 **Site:** este manual também é publicado como site estático navegável via GitHub Pages (veja `mkdocs.yml` e o workflow `docs.yml`).

🤝 **Contribuições:** veja [CONTRIBUTING.md](CONTRIBUTING.md).

---

**Desenvolvido por Bruno Bertin Marquez — Analista de QA, certificações ASTFC-AICS e SCRUM.**
