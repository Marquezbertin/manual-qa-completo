# Module 05: Automated Testing

## 5.1 When to Automate?

Automating everything is expensive and inefficient. Automate:
- **Regression** (runs always)
- **Smoke tests** (fast validation)
- **Data-driven** (many combinations)
- **Performance/Load** (impossible manually at scale)

Do NOT automate:
- Pure usability testing
- Very volatile features (maintenance cost > benefit)
- Exploratory

## 5.2 Test Pyramid (Mike Cohn)

```
        /\
       /  \      UI (few, slow, fragile)
      /----\
     /      \    API/Integration (medium)
    /--------\
   /          \  Unit (many, fast, stable)
  /------------\
```

Rule: more tests at the base (unit), fewer at the top (UI).

## 5.3 Page Object Model (POM) Pattern

Separates page interaction logic from tests. Benefits: easy maintenance, reuse, readability.

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

## 5.4 Real Example: Login Test (Playwright + Pytest)

File: `05/scripts/test_login.py`

```python
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login(page):
    return LoginPage(page)

def test_login_sucesso(login):
    login.fazer_login("user@test.com", "Pass123")
    assert "dashboard" in login.page.url

def test_login_senha_invalida(login):
    login.fazer_login("user@test.com", "wrong")
    assert login.page.locator(".erro").is_visible()
```

## 5.5 Test Data with Faker

```python
from faker import Faker
fake = Faker("en_US")
print(fake.name(), fake.ssn(), fake.email())
# Output: John Smith 123-45-6789 john.smith@example.com
```

## 5.6 Best Practices

- **Don't use `time.sleep`** — prefer explicit waits (Playwright auto-wait)
- **Stable selectors**: use `data-testid` or IDs, avoid fragile XPath
- **Independence**: each test should run in isolation
- **Reports**: Allure or HTML for evidence
- **Versioning**: tests in same app repo or dedicated repo

## 5.7 CI Execution

```yaml
# .github/workflows/ci.yml (summary)
- run: pytest tests/ --alluredir=reports/allure
- uses: actions/upload-artifact@v4
  with:
    name: allure-report
    path: reports/allure
```

## 5.8 Citations and References

- **Cohn, M. (2009)** — "Succeeding with Agile" (Test Pyramid)
- **Martin, R. (2016)** — "Clean Architecture" (POM concept)
- **Playwright Docs** — https://playwright.dev/python/
- **ISTQB®** — "Test Automation" syllabus

---

## 5.9 Next Steps

At the end of this module, the reader should be able to:
1. Explain the test pyramid
2. Implement Page Objects
3. Write a UI test with Playwright
4. Generate data with Faker
5. Run tests in CI pipeline

---

> **Next module**: [Module 06: API Testing](06/PT/indice.md)