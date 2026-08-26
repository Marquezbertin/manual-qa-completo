# 05/scripts/test_login.py
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login(page):
    return LoginPage(page)

def test_login_sucesso(login):
    login.fazer_login("user@teste.com", "Senha123")
    assert "dashboard" in login.page.url

def test_login_senha_invalida(login):
    login.fazer_login("user@teste.com", "errada")
    assert login.page.locator(".erro").is_visible()
