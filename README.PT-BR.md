# Manual Completo de QA

> **Uma guia passo-a-passo da rotina de um Analista de Testes / QA**, com exemplos práticos, scripts reais, cenários de teste e modelos de documentos da indústria.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-brightgreen)](https://playwright.dev/)
[![Jest](https://img.shields.io/badge/Jest-29%2B-red)](https://jestjs.io/)
[![Allure](https://img.shields.io/badge/Allure-Reports-41d6d6)](https://allurereport.org/)

---

## 📖 **Sobre este Manual**

Este repositório foi criado para servir como um **manual de referência** para Analistas de QA, cobrindo desde os fundamentos teóricos até a prática diária com ferramentas modernas. O conteúdo é dividido em módulos autônomos, com exemplos práticos, scripts testados e templates prontos.

### 🎯 **Objetivo**
- Fornecer uma base de conhecimento organizada para QAs de todos os níveis
- Documentar a rotina completa: do planejamento aos relatórios finais
- Oferecer scripts e templates que podem ser usados imediatamente
- Servir como material de estudo para certificações (ASTFC-AICS, ISTQB, SCRUM)

### 👤 **Público-alvo**
- Iniciantes em QA que querem aprender do zero
- QAs experientes que querem reorganizar seu conhecimento
- Estudantes de Ciência da Computação e cursos relacionados
- Professionais que se preparam para certificações de qualidade

### 🌐 **Idiomas**
Este manual está disponível em duas versões:
- **Português (BR)**: Foco no mercado nacional, certificações ASTFC-AICS, legislação e boas práticas locais
- **English**: Termos internacionais (ISTQB), práticas globais e English técnico

---

## 📁 **Estrutura do Repositório**

O manual é organizado em 10 módulos, cada um focado em um aspecto da rotina de QA:

| Módulo | Título | Conteúdo Principal |
|--------|--------|-------------------|
| `01` | Visão Geral do QA | Papel do QA, certificações, carreiras |
| `02` | Fundamentais da Qualidade | ISTQB, modelos de qualidade, V-model, Agile/Scrum/Kanban |
| `03` | Planejamento de Testes | Policy/Strategy/Plan, estimativa 3 pontos, ambientes, critérios de saída |
| `04` | Testes Manuais e Exploratórios | Casos de teste, SBTM, checklists, bug reports, heurísticas de Nielsen |
| `05` | Testes Automatizados | Pirâmide de teste, Page Objects, Playwright + Pytest |
| `06` | Testes de API | Verbos HTTP, requests + Pytest, schema (Pydantic), Schemathesis |
| `07` | Performance e Carga | Locust, k6, load/stress/spike, análise de resultados |
| `08` | Qualidade de Código e CI/CD | Coverage, lint, quality gates, SAST, GitHub Actions |
| `09` | Gestão de Qualidade e Processos | TMMi, ISO 25010, KPIs, Risk-Based Testing, BDD |
| `10` | Templates e Apêndices | Test Plan, Bug Report, Test Case, Charter, Matriz, Glossário |

Cada módulo contém:
- **PT/**: Versão em Português do Brasil
- **EN/**: Versão em English (International)
- Exemplos de código reais
- Templates baixáveis
- Citações técnicas com referências

---

## 🚀 **Primeiros Passos**

### 1. Clone este repositório
```bash
git clone https://github.com/Marquezbertin/manual-qa-completo.git
cd manual-qa-completo
```

### 2. Instale as dependências
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
```

### 3. Execute o pipeline de CI (GitHub Actions)
```bash
# O pipeline roda automaticamente em cada push/PR
# Ele executa os testes e gera relatórios Allure
```

### 4. Explore os módulos
Navegue pelas pastas `01/` a `10/` e escolha o módulo que deseja estudar primeiro.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python 3.10+** - Linguagem principal para scripts e automação
- **Playwright** - Testes de interface (UI) modernos e estáveis
- **Pytest** - Framework de testes unitários e de aceitação
- **Allure** - Geração de relatórios detalhados
- **Jest** - Para exemplos de testes JavaScript (art-of-software-testing)
- **Git & GitHub Actions** - Integração contínua e entrega
- **Faker** - Geração de dados de teste realistas (pt-BR e en-US)
- **JSON Schema** - Validação de respostas de API

---

## 📜 **Licença**

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> *"Quality is never an accident. It is always the result of intelligent effort." - John Ruskin*

---

**Desenvolvido por Bruno Bertin Marquez – Analista de QA, certificações ASTFC-AICS e SCRUM.**