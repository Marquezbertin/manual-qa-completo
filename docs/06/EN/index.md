# Module 06: API Testing

## 6.1 Why test APIs?

APIs are the "glue" between systems. API tests:
- Are **fast** (no UI)
- **Stable** (less flaky than UI)
- Validate **contracts** (schema, status, performance)
- Allow testing scenarios impossible via UI

## 6.2 HTTP Verbs and Status Codes

| Verb | Use | Typical status |
|------|-----|----------------|
| GET | Read | 200, 404 |
| POST | Create | 201, 400, 409 |
| PUT/PATCH | Update | 200, 204, 404 |
| DELETE | Remove | 204, 404 |

Classes: 2xx success, 3xx redirect, 4xx client error, 5xx server error.

## 6.3 Real and Runnable Example (Requests + Pytest)

The scripts in this module are **runnable offline** (no external network). Structure in `docs/06/scripts/`:

```
docs/06/scripts/
├── app.py          # mini REST API (stdlib, free port)
├── conftest.py     # base_url fixture (starts the API)
└── test_api.py     # status + schema tests
```

Prerequisites and execution:
```bash
cd 06/scripts
pip install requests jsonschema
pytest            # 3 tests pass
```

Snippet from `test_api.py`:
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

### Real public API example
To test a real external API, replace `base_url` with:
```python
BASE = "https://jsonplaceholder.typicode.com"
# requests.get(f"{BASE}/posts/1")  # requires internet
```
> Use public APIs (jsonplaceholder, reqres.in) for practice, but prefer the local suite for deterministic CI.

## 6.4 Schema Validation (contract)

Validating the **contract** prevents changes from breaking consumers.

**With jsonschema** (used in the local suite):
```python
from jsonschema import validate
validate(instance=response_json, schema=POST_SCHEMA)
```

**With Pydantic** (popular alternative):
```python
from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

post = Post(**response_json)  # error if field/type missing
```

## 6.5 Authentication and Tokens

```python
# JWT Bearer
token = obtain_token()
headers = {"Authorization": f"Bearer {token}"}
r = requests.get(f"{BASE}/secure", headers=headers)
assert r.status_code == 200
```

## 6.6 Contracts: OpenAPI / Swagger

- **Swagger/OpenAPI** documents endpoints, schemas, parameters
- Tools: **Schemathesis** (tests contract compliance generating cases)
- **Postman/Newman** for versioned collections

```bash
# Schemathesis validates the OpenAPI contract
st run --schema https://api.example.com/openapi.json
```

## 6.7 Best Practices

- Test **status, schema, response time** (SLA)
- Use **fixtures** for data and environment
- Separate positive/negative tests
- Version the Postman collection in the repo

## 6.8 Citations and References

- **Fielding, R. (2000)** — REST Architectural Styles (UC Irvine Thesis)
- **OpenAPI Initiative** — https://spec.openapis.org/
- **Richardson, M. (2008)** — "RESTful Web APIs" (Richardson Maturity Model)
- **Schemathesis Docs** — https://schemathesis.readthedocs.io/

---

## 6.9 Next Steps

At the end of this module, the reader should be able to:
1. Test GET/POST/PUT/DELETE verbs
2. Validate status and schema
3. Test JWT authentication
4. Use Postman/Newman and Schemathesis
5. Validate response time SLA

---

> **Next module**: [Module 07: Performance and Load Testing](../07/EN/index.md)
