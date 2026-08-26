# Solutions & Learning Guide (EN)

Summary answers to the **"Next Steps"** objectives of each module. Use to self-assess mastery.

## M01 — Overview
1. **QA vs QC vs Testing**: QA prevents (process); QC detects in product; Testing is the QC technique.
2. **7 ISTQB principles**: shows presence not absence; exhaustive impossible; early saves; defect clustering; pesticide; context dependent; absence-of-errors fallacy.
3. **Cost of Quality**: prevention + appraisal < internal/external failure; external failure is costliest.
4. **QA in Scrum/Kanban/Waterfall**: Planning/Daily/Review/Retro; visualize flow/WIP; review docs and accept.
5. **STLC**: requirements → planning → design → execution → closure.

## M02 — Fundamentals
1. **ISO 25010**: 8 characteristics (functional, performance, compatibility, usability, reliability, security, maintainability, portability).
2. **Measurable attribute**: every NFR needs a number (e.g., p95 < 800ms).
3. **V-Model**: each spec phase has a mirrored test phase.
4. **Traceability matrix**: requirement ↔ test ↔ result.
5. **Risk-Based Testing**: prioritize the Critical quadrant (high impact × high probability).

## M03 — Planning
1. **Policy/Strategy/Plan**: Policy (org) → Strategy (program) → Plan (release).
2. **Test Plan**: objective, scope, out-of-scope, approach, environment, schedule, risks, criteria, approvals.
3. **PERT**: (Ot + 4·Rl + Ps) / 6.
4. **Exit criteria**: e.g., 100% executed, ≥95% pass, 0 critical, cov ≥80%.
5. **Environment/data**: isolated, anonymized, equal to tested build.

## M04 — Manual & Exploratory
1. **Test case**: ID, precondition, steps, data, expected result, status.
2. **SBTM charter**: mission, areas, time, opportunities, bug, debrief.
3. **Acceptance checklist**: required, formats, errors, loading, responsive, a11y, security.
4. **Bug report**: title, environment, steps, expected, actual, severity, priority, evidence.
5. **Nielsen**: 10 heuristics (visibility, real world, freedom, consistency, prevention, recognition, efficiency, aesthetics, errors, help).

## M05 — Automated
1. **Pyramid**: more unit, less UI.
2. **Page Object**: separates selectors/logic from tests (data-testid).
3. **Playwright**: `test_login.py` runs 6 tests (login.html + POM).
4. **Data-driven**: `@pytest.mark.parametrize`.
5. **CI**: pipeline runs lint/tests/coverage.

## M06 — API
1. **Verbs**: GET/POST/PUT/DELETE + status codes.
2. **Schema**: `jsonschema.validate` or Pydantic.
3. **Auth**: Bearer/JWT in header.
4. **Postman/Newman/Schemathesis**: contracts.
5. **SLA**: p95 < X ms, error rate < Y%.

## M07 — Performance
1. **Types**: load/stress/spike/endurance.
2. **Locust/k6**: `locustfile.py` or `script.js`.
3. **Thresholds**: p95 < 500ms.
4. **Metrics**: throughput, p95/p99, error rate.
5. **Memory leak**: rising memory in endurance.

## M08 — Quality & CI/CD
1. **Lint + coverage**: ruff, pytest-cov.
2. **Pipeline**: commit → lint → tests → coverage → SAST → deploy.
3. **Quality gates**: lint=0, cov≥80%, security=0 high.
4. **SAST**: bandit.
5. **Shift-left**: test early, DoD includes tests.

## M09 — Management
1. **TMMi**: 5 levels (Initial→Optimized).
2. **KPIs**: defect density, leakage, coverage, MTTR.
3. **Risk-Based Testing**: 3×3 matrix.
4. **BDD**: Given/When/Then.
5. **Traceability matrix**: requirement ↔ test ↔ result.

## M10 — Templates
Apply this module's templates in a real project (Test Plan, Bug Report, Test Case, Charter, Matrix, Glossary).
