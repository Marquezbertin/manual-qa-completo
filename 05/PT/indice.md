# Módulo 05: Testes Automatizados

## 5.1 Quando Automatizar?

Automatizar tudo é caro e ineficiente. Automatize:
- **Regressão** (executa sempre)
- **Smoke tests** (validação rápida)
- **Data-driven** (muitas combinações)
- **Performance/Carga** (impossível manual em escala)

Não automatize:
- Testes de usabilidade pura
- Features muito voláteis (custo de manutenção > benefício)
- Exploratório

## 5.2 Pirâmide de Teste (Mike Cohn)

```
        /\
       /  \      UI (poucos, lentos, frágeis)
      /----\
     /      \    API/Integração (médios)
    /--------\
   /          \  Unit (muitos, rápidos, estáveis)
  /------------\
```

Regra: mais testes na base (unidade), menos no topo (UI).

## 5.3 Padrão Page Object Model (POM)

Separa a lógica de interação da página dos testes. Benefícios: manutenção fácil, reuso, legibilidade.

```python
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
```

## 5.4 Exemplo Real: Teste de Login (Playwright + Pytest)

Arquivo: `05/scripts/test_login.py`

```python
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
```

## 5.5 Dados de Teste com Faker

```python
from faker import Faker
fake = Faker("pt_BR")
print(fake.name(), fake.cpf(), fake.email())
# Saída: João Silva 123.456.789-00 joao.silva@exemplo.com
```

## 5.6 Boas Práticas

- **Não use `time.sleep`** — prefira esperas explícitas (auto-wait do Playwright)
- **Seletores estáveis**: use `data-testid` ou IDs, evite XPath frágil
- **Independência**: cada teste deve rodar isolado
- **Relatórios**: Allure ou HTML para evidência
- **Versionar**: testes no mesmo repo da aplicação ou repo dedicado

## 5.7 Execução em CI

```yaml
# .github/workflows/ci.yml (resumo)
- run: pytest tests/ --alluredir=reports/allure
- uses: actions/upload-artifact@v4
  with:
    name: allure-report
    path: reports/allure
```

## 5.8 Citações e Referências

- **Cohn, M. (2009)** — "Succeeding with Agile" (Test Pyramid)
- **Martin, R. (2016)** — "Clean Architecture" (POM concept)
- **Playwright Docs** — https://playwright.dev/python/
- **ISTQB®** — "Test Automation" syllabus

---

## 5.9 Próximos Passos

Ao final deste módulo, o leitor deverá:
1. Explicar a pirâmide de teste
2. Implementar Page Objects
3. Escrever um teste de UI com Playwright
4. Gerar dados com Faker
5. Rodar testes em pipeline CI

---

> **Próximo módulo**: [Módulo 06: API Testing](06/PT/indice.md)