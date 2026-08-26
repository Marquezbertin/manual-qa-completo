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

## 6.3 Exemplo Real e Executável (Requests + Pytest)

Os scripts deste módulo são **rodáveis offline** (sem rede externa). Estrutura em `06/scripts/`:

```
06/scripts/
├── app.py          # mini API REST (stdlib, sobe em porta livre)
├── conftest.py     # fixture base_url (sobe a API)
└── test_api.py     # testes de status + schema
```

Pré-requisitos e execução:
```bash
cd 06/scripts
pip install requests jsonschema
pytest            # 3 testes passam
```

Trecho de `test_api.py`:
```python
import requests
from jsonschema import validate

POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}

def test_get_post(base_url):
    r = requests.get(f"{base_url}/posts/1")
    assert r.status_code == 200
    validate(instance=r.json(), schema=POST_SCHEMA)
```

### Exemplo com API pública real
Para testar uma API externa de verdade, troque `base_url` por:
```python
BASE = "https://jsonplaceholder.typicode.com"
# requests.get(f"{BASE}/posts/1")  # requer internet
```
> Use APIs públicas (jsonplaceholder, reqres.in) para praticar, mas prefira a suíte local para CI determinístico.

## 6.4 Validação de Schema (contrato)

Validar o **contrato** impede que mudanças quebrem os consumidores.

**Com jsonschema** (usado na suíte local):
```python
from jsonschema import validate
validate(instance=resposta_json, schema=POST_SCHEMA)
```

**Com Pydantic** (alternativa popular):
```python
from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

post = Post(**resposta_json)  # erro se faltar campo/tipo
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