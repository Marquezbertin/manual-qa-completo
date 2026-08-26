# docs/05/scripts/conftest.py
"""Configuração local dos testes de demonstração.

- Torna o pacote `pages` importável.
- Define o fixture `page` (Playwright) sem depender de pytest-playwright,
  bastando `pip install playwright` + `playwright install chromium`.
  (Opcionalmente, se usar `pytest-playwright`, ele já fornece `page`.)
"""
import sys
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

