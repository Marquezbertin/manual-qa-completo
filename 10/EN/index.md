# Module 10: Templates and Appendices

This module gathers **ready-to-use artifacts** for real QA projects.

## 10.1 Template Index

| File | Description |
|------|-------------|
| `10/EN/test_plan_template.md` | Complete Test Plan template |
| `10/EN/bug_report_template.md` | Bug Report template |
| `10/EN/test_case_template.md` | Test Case template |
| `10/EN/charter_template.md` | Charter template (SBTM) |
| `10/EN/acceptance_checklist.md` | Acceptance Checklist |
| `10/EN/traceability_matrix.md` | Traceability Matrix |
| `10/EN/glossary.md` | PT/EN Glossary |
| `10/EN/solutions.md` | Solutions guide (self-assessment) |

## 10.2 How to Use

1. Copy the template to your project
2. Fill fields in `[BRACKETS]`
3. Version it in the project repo
4. Adapt to your team's maturity

## 10.2.1 Executable Scripts Hub

Real, validated scripts across the manual (run locally):

| Script | Module | Command |
|--------|--------|---------|
| `05/scripts/` (login POM) | M05 | `cd 05/scripts && pytest` |
| `06/scripts/` (local API) | M06 | `cd 06/scripts && pytest` |
| `03/scripts/estimate.py` | M03 | `python 03/scripts/estimate.py` |
| `04/scripts/triage.py` | M04 | `python 04/scripts/triage.py` |
| `07/scripts/percentile.py` | M07 | `python 07/scripts/percentile.py` |
| `08/scripts/quality_gate.py` | M08 | `python 08/scripts/quality_gate.py` |
| `09/scripts/kpi.py` | M09 | `python 09/scripts/kpi.py` |

> All were executed and validated while writing this manual.

## 10.3 Appendix: Recommended Modern Stack

- **UI Automation**: Playwright + pytest
- **API Testing**: requests + Schemathesis + Postman/Newman
- **Performance**: k6 / Locust
- **CI/CD**: GitHub Actions
- **Reports**: Allure, pytest-html
- **Quality**: ruff, black, bandit, pytest-cov
- **Management**: Jira / Azure DevOps

## 10.4 Appendix: Learning Roadmap

```
Beginner:  M01 → M02 → M04 (manual)
Intermediate: M03 → M05 (automation) → M06 (API)
Advanced: M07 (performance) → M08 (CI/CD) → M09 (management)
Continuous reference: M10 (templates)
```

## 10.5 Appendix: Relevant Certifications

- **ISTQB** (Foundation / Advanced)
- **Certified Agile Tester** (ISTQB)
- **AWS/Azure** (cloud for performance/CI)
- **Six Sigma** (processes)

## 10.6 QA Checklist (Capstone)

What every QA analyst should master by the end of this manual:

- [ ] Explain QA vs QC vs Testing and the 7 principles (M01)
- [ ] Apply ISO 25010 and measurable quality attributes (M02)
- [ ] Write a Test Plan with exit criteria (M03)
- [ ] Draft test cases, charters, and bug reports (M04)
- [ ] Automate UI with Page Objects (M05)
- [ ] Test APIs with contract validation (M06)
- [ ] Interpret p95/p99 and configure load (M07)
- [ ] Build a CI pipeline with quality gates (M08)
- [ ] Calculate KPIs and apply Risk-Based Testing (M09)
- [ ] Use this module's templates in a real project

## 10.7 Citations and References

- **ISTQB®** — https://www.istqb.org/
- **IEEE 829 (historical)** — Test Documentation Standard
- **ISO/IEC/IEEE 29119** — Test Processes
- **Allure Docs** — https://allurereport.org/

---

> **End of Manual.** Return to any module to deepen. Good QA! 🚀
