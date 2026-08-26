# 06/scripts/conftest.py
"""Fixture que sobe a mini API local em porta livre para os testes."""
import pytest

from app import start_server


@pytest.fixture(scope="module")
def base_url():
    server = start_server(0)
    port = server.server_address[1]
    url = f"http://127.0.0.1:{port}"
    yield url
    server.shutdown()
