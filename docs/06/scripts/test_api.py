# docs/06/scripts/test_api.py
"""Testes da mini API (offline, sem rede externa).

Execute:
    cd 06/scripts
    pip install requests jsonschema
    pytest
"""
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
    body = r.json()
    assert body["id"] == 1
    assert "title" in body
    validate(instance=body, schema=POST_SCHEMA)  # validação de contrato


def test_create_post(base_url):
    payload = {"title": "QA", "body": "teste", "userId": 1}
    r = requests.post(f"{base_url}/posts", json=payload)
    assert r.status_code == 201
    created = r.json()
    assert created["id"] is not None
    validate(instance=created, schema=POST_SCHEMA)


def test_not_found(base_url):
    r = requests.get(f"{base_url}/posts/999999")
    assert r.status_code == 404

