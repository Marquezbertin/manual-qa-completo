# Módulo 06: Testes de API

## 6.1 Por que testar API?

APIs são a "cola" entre sistemas. Testes de API:
- São **rápidos** (sem UI)
- **Estáveis** (menos flaky que UI)
- Validam **contratos** (schema, status, performance)
- Permitem testar cenários impossíveis via UI

## 6.2 Verbos HTTP e Status Codes

| Verbo | Uso | Status típico |
|-------|-----|---------------|
| GET | Ler | 200, 404 |
| POST | Criar | 201, 400, 409 |
| PUT/PATCH | Atualizar | 200, 204, 404 |
| DELETE | Remover | 204, 404 |

Classes: 2xx sucesso, 3xx redirecionamento, 4xx erro do cliente, 5xx erro do servidor.

## 6.3 Exemplo Real: Testando uma API REST (Requests + Pytest)

Arquivo: `06/scripts/test_api.py`

```python
import requests
import pytest

BASE = "https://jsonplaceholder.typicode.com"

def test_get_post():
    r = requests.get(f"{BASE}/posts/1")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert "title" in body

def test_create_post():
    payload = {"title": "QA", "body": "teste", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 201
    assert r.json()["id"] is not None

def test_not_found():
    r = requests.get(f"{BASE}/posts/999999")
    assert r.status_code == 404
```

## 6.4 Validação de Schema (Pydantic)

```python
from pydantic import BaseModel, ValidationError

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

def test_schema():
    r = requests.get(f"{BASE}/posts/1").json()
    post = Post(**r)  # levanta erro se faltar campo
    assert post.userId > 0
```

## 6.5 Autenticação e Tokens

```python
# JWT Bearer
token = obter_token()
headers = {"Authorization": f"Bearer {token}"}
r = requests.get(f"{BASE}/secure", headers=headers)
assert r.status_code == 200
```

## 6.6 Contratos: OpenAPI / Swagger

- **Swagger/OpenAPI** documenta endpoints, schemas, parâmetros
- Ferramentas: **Schemathesis** (testa conformidade do contrato gerando casos)
- **Postman/Newman** para coleções versionadas

```bash
# Schemathesis valida o contrato OpenAPI
st run --schema https://api.exemplo.com/openapi.json
```

## 6.7 Boas Práticas

- Teste **status, schema, tempo de resposta** (SLA)
- Use **fixtures** para dados e ambiente
- Separe testes positivos/negativos
- Versione a coleção Postman no repo

## 6.8 Citações e Referências

- **Fielding, R. (2000)** — REST Architectural Styles (Tese UC Irvine)
- **OpenAPI Initiative** — https://spec.openapis.org/
- **Richardson, M. (2008)** — "RESTful Web APIs" (Richardson Maturity Model)
- **Schemathesis Docs** — https://schemathesis.readthedocs.io/

---

## 6.9 Próximos Passos

Ao final deste módulo, o leitor deverá:
1. Testar verbos GET/POST/PUT/DELETE
2. Validar status e schema
3. Testar autenticação JWT
4. Usar Postman/Newman e Schemathesis
5. Validar SLA de tempo de resposta

---

> **Próximo módulo**: [Módulo 07: Testes de Performance e Carga](07/PT/indice.md)