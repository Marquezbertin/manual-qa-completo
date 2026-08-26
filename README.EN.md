# Complete QA Manual

> **A step-by-step guide to a QA Analyst's routine**, with practical examples, real scripts, test scenarios, and industry document templates.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-brightgreen)](https://playwright.dev/)
[![Jest](https://img.shields.io/badge/Jest-29%2B-red)](https://jestjs.io/)
[![Allure](https://img.shields.io/badge/Allure-Reports-41d6d6)](https://allurereport.org/)

---

## 📖 **About this Manual**

This repository serves as a **reference manual** for QA Analysts, covering everything from theoretical foundations to daily practice with modern tools. The content is divided into autonomous modules, with practical examples, tested scripts, and ready-to-use templates.

### 🎯 **Goal**
- Provide organized knowledge base for QAs at all levels
- Document the complete routine: from planning to final reports
- Offer scripts and templates that can be used immediately
- Serve as study material for certifications (ASTFC-AICS, ISTQB, SCRUM)

### 👤 **Target Audience**
- QA beginners who want to learn from scratch
- Experienced QAs who want to reorganize their knowledge
- Computer Science students and related courses
- Professionals preparing for quality certifications

### 🌐 **Languages**
This manual is available in two versions:
- **Portuguese (BR)**: Focus on the national market, ASTFC-AICS certifications, local best practices
- **English**: International terms (ISTQB), global best practices

---

## 📁 **Repository Structure**

The manual is organized into 10 modules, each focusing on a different aspect of QA work:

| Module | Title | Main Content |
|--------|-------|--------------|
| `01` | QA Overview | QA role, certifications, careers |
| `02` | Quality Fundamentals | ISTQB, quality models, V-model, Agile/Scrum/Kanban |
| `03` | Test Planning | Policy/Strategy/Plan, 3-point estimate, environments, exit criteria |
| `04` | Manual & Exploratory Testing | Test cases, SBTM, checklists, bug reports, Nielsen heuristics |
| `05` | Automated Testing | Test pyramid, Page Objects, Playwright + Pytest |
| `06` | API Testing | HTTP verbs, requests + Pytest, schema (Pydantic), Schemathesis |
| `07` | Performance & Load | Locust, k6, load/stress/spike, result analysis |
| `08` | Code Quality & CI/CD | Coverage, lint, quality gates, SAST, GitHub Actions |
| `09` | Quality Management & Processes | TMMi, ISO 25010, KPIs, Risk-Based Testing, BDD |
| `10` | Templates & Appendices | Test Plan, Bug Report, Test Case, Charter, Matrix, Glossary |

Each module contains:
- **PT/**: Portuguese (Brazil) version
- **EN/**: English version
- Real code examples
- Downloadable templates
- Technical citations with references

---

## 🚀 **First Steps**

### 1. Clone this repository
```bash
git clone https://github.com/Marquezbertin/manual-qa-complete.git
cd manual-qa-complete
```

### 2. Install dependencies
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
```

### 3. Run the CI pipeline (GitHub Actions)
```bash
# The pipeline runs automatically on every push/PR
# It executes tests and generates Allure reports
```

### 4. Explore the modules
Navigate through folders `01/` to `10/` and choose the module you want to study first.

---

## 🛠️ **Technologies Used**

- **Python 3.10+** - Main language for scripts and automation
- **Playwright** - Modern and stable UI testing
- **Pytest** - Unit and acceptance testing framework
- **Allure** - Detailed report generation
- **Jest** - For JavaScript test examples (art-of-software-testing)
- **Git & GitHub Actions** - Continuous integration and delivery
- **Faker** - Realistic test data generation (pt-BR and en-US)
- **JSON Schema** - API response validation

---

## 📜 **License**

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more details.

---

> *"Quality is never an accident. It is always the result of intelligent effort." - John Ruskin*

---

**Developed by Bruno Bertin Marquez – QA Analyst, ASTFC-AICS and SCRUM certified.**