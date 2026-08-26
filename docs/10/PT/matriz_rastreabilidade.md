# Matriz de Rastreabilidade

Relaciona requisitos → casos de teste → resultado.

| Req ID | Requisito | Caso de Teste | Status | Bugs |
|--------|-----------|---------------|--------|------|
| REQ-01 | Login válido | TC-LOGIN-001 | Pass | - |
| REQ-02 | Senha inválida | TC-LOGIN-002 | Pass | - |
| REQ-03 | Logout | TC-LOGIN-003 | Fail | BUG-120 |
| REQ-04 | Recuperar senha | TC-PWD-001 | Pass | - |

Cobertura = (Reqs com teste / total de Reqs) × 100
```
Cobertura = 4/4 = 100%
Defect Leakage = bugs em prod / total
```
