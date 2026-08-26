# 06/scripts/test_api.py
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
