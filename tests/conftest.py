import pytest
from playwright.sync_api import Page

from data.usuarios import PASSWORD, USUARIO_ESTANDAR
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def url_login(base_url: str) -> str:
    return base_url + LoginPage.RUTA


@pytest.fixture
def url_inventario(base_url: str) -> str:
    return base_url + InventoryPage.RUTA


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    pagina = LoginPage(page)
    pagina.abrir()
    return pagina


@pytest.fixture
def iniciar_sesion(page: Page, login_page: LoginPage):
    """Devuelve una función que inicia sesión y deja al test en el inventario."""

    def _iniciar_sesion(usuario: str = USUARIO_ESTANDAR) -> InventoryPage:
        login_page.login(usuario, PASSWORD)
        return InventoryPage(page)

    return _iniciar_sesion
