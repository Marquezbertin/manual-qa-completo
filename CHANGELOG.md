# Changelog

Todas as mudanças notáveis deste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/).

## [1.0.0] - 2026-08-26

### Adicionado
- Manual completo de QA em Português (BR) e Inglês, com 11 módulos autônomos.
- Scripts executáveis e verificados em 8 módulos:
  - `docs/03/scripts/estimate.py` — estimativa PERT
  - `docs/04/scripts/triage.py` — severidade × prioridade (SLA)
  - `docs/05/scripts/` — suíte de login UI (Playwright + Page Object)
  - `docs/06/scripts/` — suíte de API REST local (requests + jsonschema)
  - `docs/07/scripts/percentile.py` — cálculo de p95/p99
  - `docs/08/scripts/quality_gate.py` — quality gates
  - `docs/09/scripts/kpi.py` — KPIs de qualidade
  - `docs/11/scripts/secret_scan.py` — secret scanning (OWASP)
- Templates prontos para uso: Test Plan, Bug Report, Test Case, Charter (SBTM),
  Checklist de Homologação, Matriz de Rastreabilidade e Glossário.
- Pipeline CI (`.github/workflows/ci.yml`): testes da raiz + job de scripts + validação de blocos Mermaid.
- Site estático via MkDocs Material + deploy em GitHub Pages (`.github/workflows/docs.yml`).
- `Makefile` e `run_all.py` para execução rápida dos scripts.
- `LICENSE` (MIT) e documentação de como executar tudo no README.

### Notas
- Os módulos 01, 02, 10 são teóricos/práticos sem scripts (templates/solucoes).
- Validação local: 9 testes pytest (M05: 6, M06: 3) + 7 scripts standalone, todos executados com sucesso.

### Alterado (pós-release)
- Conteúdo movido para `docs/` (MkDocs rejeita `docs_dir: .`); site publicado em GitHub Pages.
- `mkdocs.yml` usa `docs_dir: docs`; README e links de módulos atualizados para `docs/...` / `../`.
- Layout: cards de módulos na home, seletor PT/EN, footer de marca, callout `example`, roadmap Mermaid.
- `md_in_html` adicionado para renderizar o grid de cards; footer via JS (sem override de template).

