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

## 6.3 Real Example: Testing a REST API (Requests + Pytest)

File: `06/scripts/test_api.py`

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
    payload = {"title": "QA", "body": "test", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 201
    assert r.json()["id"] is not None

def test_not_found():
    r = requests.get(f"{BASE}/posts/999999")
    assert r.status_code == 404
```

## 6.4 Schema Validation (Pydantic)

```python
from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

def test_schema():
    r = requests.get(f"{BASE}/posts/1").json()
    post = Post(**r)  # raises error if field missing
    assert post.userId > 0
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

> **Next module**: [Module 07: Performance and Load Testing](07/PT/indice.md)