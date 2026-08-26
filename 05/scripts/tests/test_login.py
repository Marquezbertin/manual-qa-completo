# tests/test_login.py
"""Testes da tela de login usando o Page Object e dados data-driven.

Execute localmente (precisa de Playwright + chromium):
    cd 05/scripts
    pip install playwright && playwright install chromium
    pytest
"""
import pytest
from pathlib import Path

from pages.login_page import LoginPage

BASE_URL = Path(__file__).resolve().parent.parent.as_uri()


@pytest.fixture
def login(page):
    pg = LoginPage(page)
    pg.abrir(BASE_URL)
    return pg


# 5.4 — Exemplo básico
def test_login_sucesso(login):
    login.fazer_login("user@teste.com", "Senha123")
    assert login.dashboard_visivel
    assert not login.mensagem_erro_visivel


def test_login_senha_invalida(login):
    login.fazer_login("user@teste.com", "errada")
    assert login.mensagem_erro_visivel
    assert not login.dashboard_visivel


# 5.5 — Data-driven com parametrize (várias combinações)
@pytest.mark.parametrize(
    "usuario, senha, deve_logar",
    [
        ("user@teste.com", "Senha123", True),
        ("user@teste.com", "123", False),
        ("naoexiste@x.com", "Senha123", False),
        ("", "", False),
    ],
)
def test_login_parametrizado(login, usuario, senha, deve_logar):
    login.fazer_login(usuario, senha)
    assert login.dashboard_visivel is deve_logar
