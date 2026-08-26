# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    URL = "/login"
    def __init__(self, page: Page):
        self.page = page
        self.email = page.locator("#email")
        self.senha = page.locator("#senha")
        self.entrar = page.locator("#entrar")

    def fazer_login(self, usuario, senha):
        self.page.goto(self.URL)
        self.email.fill(usuario)
        self.senha.fill(senha)
        self.entrar.click()
