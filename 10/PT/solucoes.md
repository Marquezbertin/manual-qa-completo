# Soluções e Guia de Aprendizagem (PT)

Respostas-resumo dos objetivos de **"Próximos Passos"** de cada módulo. Use para autoavaliar o domínio do conteúdo.

## M01 — Visão Geral
1. **QA vs QC vs Teste**: QA previne (processo); QC detecta no produto; Teste é a técnica do QC.
2. **7 princípios ISTQB**: teste mostra presença, não ausência; exaustivo é impossível; antecipar economiza; defeitos concentram; pesticida; contexto; falácia da ausência de erros.
3. **Custo da Qualidade**: prevenção + avaliação < falha interna/externa; falha externa é a mais cara.
4. **QA no Scrum/Kanban/Cascata**: participa de Planning/Daily/Review/Retro; visualiza fluxo/WIP; revisa doc e homologa.
5. **STLC**: requisitos → planejamento → design → execução → fechamento.

## M02 — Fundamentais
1. **ISO 25010**: 8 características (funcional, desempenho, compatibilidade, usabilidade, confiabilidade, segurança, manutenibilidade, portabilidade).
2. **Atributo mensurável**: todo NFR precisa de número (ex: p95 < 800ms).
3. **V-Model**: cada fase de especificação tem teste espelhado.
4. **Matriz de rastreabilidade**: requisito ↔ teste ↔ resultado.
5. **Risk-Based Testing**: priorize o quadrante Crítico (alto impacto × alta prob.).

## M03 — Planejamento
1. **Policy/Strategy/Plan**: Policy (org) → Strategy (programa) → Plan (release).
2. **Test Plan**: objetivo, escopo, fora de escopo, abordagem, ambiente, cronograma, riscos, critérios, aprovações.
3. **PERT**: (Ot + 4·Rl + Ps) / 6.
4. **Critérios de saída**: ex: 100% executados, ≥95% pass, 0 crítico, cov ≥80%.
5. **Ambiente/dados**: isolado, anonimizado, igual ao build testado.

## M04 — Manuais e Exploratórios
1. **Caso de teste**: ID, pré-condição, passos, dados, resultado esperado, status.
2. **Charter SBTM**: missão, áreas, tempo, oportunidades, bug, debrief.
3. **Checklist homologação**: obrigatórios, formatos, erros, loading, responsivo, a11y, segurança.
4. **Bug report**: título, ambiente, passos, esperado, obtido, severidade, prioridade, evidência.
5. **Nielsen**: 10 heurísticas (visibilidade, mundo real, liberdade, consistência, prevenção, reconhecimento, eficiência, estética, erros, ajuda).

## M05 — Automatizados
1. **Pirâmide**: mais unidade, menos UI.
2. **Page Object**: separa seletores/lógica dos testes (data-testid).
3. **Playwright**: `test_login.py` roda 6 testes (login.html + POM).
4. **Data-driven**: `@pytest.mark.parametrize`.
5. **CI**: pipeline roda lint/testes/coverage.

## M06 — API
1. **Verbos**: GET/POST/PUT/DELETE + status codes.
2. **Schema**: `jsonschema.validate` ou Pydantic.
3. **Auth**: Bearer/JWT no header.
4. **Postman/Newman/Schemathesis**: contratos.
5. **SLA**: p95 < X ms, error rate < Y%.

## M07 — Performance
1. **Tipos**: load/stress/spike/endurance.
2. **Locust/k6**: `locustfile.py` ou `script.js`.
3. **Thresholds**: p95 < 500ms.
4. **Métricas**: throughput, p95/p99, error rate.
5. **Memory leak**: memória crescente em endurance.

## M08 — Qualidade e CI/CD
1. **Lint + coverage**: ruff, pytest-cov.
2. **Pipeline**: commit → lint → testes → coverage → SAST → deploy.
3. **Quality gates**: lint=0, cov≥80%, security=0 high.
4. **SAST**: bandit.
5. **Shift-left**: testar cedo, DoD com testes.

## M09 — Gestão
1. **TMMi**: 5 níveis (Inicial→Otimizado).
2. **KPIs**: defect density, leakage, cobertura, MTTR.
3. **Risk-Based Testing**: matriz 3×3.
4. **BDD**: Given/When/Then.
5. **Matriz rastreabilidade**: requisito ↔ teste ↔ resultado.

## M10 — Templates
Aplique os templates deste módulo em um projeto real (Test Plan, Bug Report, Test Case, Charter, Matriz, Glossário).
