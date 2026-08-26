# pages/login_page.py
"""Page Object para a tela de login (demonstração offline).

Seletores estáveis via data-testid (recomendado em 5.6).
"""
from playwright.sync_api import Page


class LoginPage:
    URL = "login.html"

    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_test_id("email")
        self.senha = page.get_by_test_id("senha")
        self.entrar = page.get_by_test_id("entrar")
        self.erro = page.get_by_test_id("erro")
        self.dashboard = page.get_by_test_id("dashboard")

    def abrir(self, base_url: str):
        self.page.goto(f"{base_url}/{self.URL}")

    def fazer_login(self, usuario: str, senha: str):
        self.email.fill(usuario)
        self.senha.fill(senha)
        self.entrar.click()

    @property
    def mensagem_erro_visivel(self) -> bool:
        return self.erro.is_visible()

    @property
    def dashboard_visivel(self) -> bool:
        return self.dashboard.is_visible()
