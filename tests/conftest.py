import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture
def url_login(base_url: str) -> str:
    return base_url + "/"


@pytest.fixture
def url_inventario(base_url: str) -> str:
    return base_url + "/inventory.html"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    pagina = LoginPage(page)
    pagina.abrir()
    return pagina
