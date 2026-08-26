# Complete QA Manual

> **A step-by-step guide to a QA Analyst's routine**, with practical examples, real (verified) scripts, test scenarios, and industry document templates — in **Portuguese (BR)** and **English**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-brightgreen)](https://playwright.dev/)
[![CI](https://github.com/Marquezbertin/manual-qa-completo/actions/workflows/ci.yml/badge.svg)](https://github.com/Marquezbertin/manual-qa-completo/actions/workflows/ci.yml)

---

## 📑 Table of Contents

- [About this Manual](#-about-this-manual)
- [Repository Structure](#-repository-structure)
- [Executable Scripts Hub](#-executable-scripts-hub)
- [How to Run](#-how-to-run)
- [Technologies](#-technologies)
- [License](#-license)

---

## 📖 About this Manual

This repository is a **reference manual** for QA Analysts, covering everything from theoretical foundations to daily practice with modern tools. Content is split into autonomous modules with practical examples, **tested and verified scripts**, and ready-to-use templates.

### 🎯 Goal
- Organized knowledge base for QAs at all levels
- Document the complete routine: from planning to final reports
- Provide scripts and templates usable immediately
- Study material for certifications (ISTQB, ASTFC-AICS, SCRUM)

### 👤 Target Audience
- QA beginners learning from scratch
- Experienced QAs reorganizing their knowledge
- Computer Science students and related courses
- Professionals preparing for quality certifications

### 🌐 Languages
- **Portuguese (BR)** — national market and local certifications (`*/PT/`)
- **English** — international terms (ISTQB) and global practices (`*/EN/`)

---

## 📁 Repository Structure

10 modules, each with PT and EN versions. The **Scripts** column flags modules that ship verified runnable code.

| Module | Title | Main Content | Scripts |
|--------|-------|-------------|---------|
| `01` | QA Overview | QA vs QC, 7 ISTQB principles, Cost of Quality, STLC | — |
| `02` | Quality Fundamentals | ISO 25010, V-Model, measurable quality attributes | — |
| `03` | Test Planning | Policy/Strategy/Plan, PERT estimate, mini Test Plan | `estimate.py` ✅ |
| `04` | Manual & Exploratory Testing | Test cases, SBTM, Severity×Priority, Nielsen | `triage.py` ✅ |
| `05` | Automated Testing | Test pyramid, Page Objects, Playwright + Pytest | pytest suite ✅ |
| `06` | API Testing | HTTP verbs, requests, contract validation (jsonschema) | pytest suite ✅ |
| `07` | Performance & Load | Locust/k6, p95/p99 percentiles, analysis | `percentile.py` ✅ |
| `08` | Code Quality & CI/CD | Coverage, lint, quality gates, SAST, GitHub Actions | `quality_gate.py` ✅ |
| `09` | Quality Management & Processes | TMMi, ISO 25010, KPIs, Risk-Based Testing, PDCA | `kpi.py` ✅ |
| `10` | Templates & Appendices | Test Plan, Bug Report, Test Case, Charter, Matrix, Glossary | — |

Each module contains:
- **PT/** and **EN/** — Portuguese and English versions
- Real, verified code examples
- Ready-to-download templates
- Technical citations with references

---

## 🚀 Executable Scripts Hub

Real scripts **validated** throughout the manual. Run them locally:

| Script | Module | Command |
|--------|--------|---------|
| `03/scripts/estimate.py` | M03 — PERT estimate | `python 03/scripts/estimate.py` |
| `04/scripts/triage.py` | M04 — Severity×Priority (SLA) | `python 04/scripts/triage.py` |
| `05/scripts/` | M05 — UI login (Page Object) | `cd 05/scripts && pytest` |
| `06/scripts/` | M06 — local REST API | `cd 06/scripts && pytest` |
| `07/scripts/percentile.py` | M07 — p95/p99 | `python 07/scripts/percentile.py` |
| `08/scripts/quality_gate.py` | M08 — Quality Gates | `python 08/scripts/quality_gate.py` |
| `09/scripts/kpi.py` | M09 — Quality KPIs | `python 09/scripts/kpi.py` |

> **Verification status:** 9 pytest tests (M05: 6, M06: 3) + 7 standalone scripts, all executed successfully when writing this manual.

---

## 🛠️ How to Run

### 1. Clone
```bash
git clone https://github.com/Marquezbertin/manual-qa-completo.git
cd manual-qa-completo
```

### 2. Standalone scripts (no external dependencies)
```bash
python 03/scripts/estimate.py
python 04/scripts/triage.py
python 07/scripts/percentile.py
python 08/scripts/quality_gate.py
python 09/scripts/kpi.py
```

### 3. Pytest suites (automation and API)
```bash
# M05 — needs Playwright + Chromium
cd 05/scripts
pip install playwright && playwright install chromium
pytest

# M06 — needs requests + jsonschema
cd 06/scripts
pip install requests jsonschema
pytest
```

### 4. CI (GitHub Actions)
The pipeline in `.github/workflows/ci.yml` runs automatically on every push/PR, executing the root tests and validating the manual's integrity.

---

## 🧰 Technologies

- **Python 3.10+** — main scripting language
- **Playwright + pytest** — modern, stable UI testing
- **requests + jsonschema** — API testing and contract validation
- **k6 / Locust** — performance and load testing
- **GitHub Actions** — continuous integration
- **Faker** — realistic test data (pt-BR / en-US)
- **ruff, black, bandit, pytest-cov** — code quality and coverage

---

## 📜 License

This project is licensed under the **MIT** license. See the [LICENSE](LICENSE) file for more details.

---

> *"Quality is never an accident. It is always the result of intelligent effort."* — **John Ruskin**

---

**Developed by Bruno Bertin Marquez — QA Analyst, ASTFC-AICS and SCRUM certified.**
