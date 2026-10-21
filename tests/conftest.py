import pytest
from playwright.sync_api import Page

from data.checkout import APELLIDO, CARRITO_A, CODIGO_POSTAL, NOMBRE
from data.usuarios import PASSWORD, USUARIO_ESTANDAR
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
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


# Estados de partida de casos/checkout.md. Cada test abre un navegador nuevo,
# así que el carrito empieza vacío y no hace falta limpiarlo.


@pytest.fixture
def carrito_a(page: Page, iniciar_sesion) -> CartPage:
    """Carrito A: sesión iniciada, solo "Sauce Labs Backpack" y "Sauce Labs Bike Light"; deja al test en /cart.html."""
    inventario = iniciar_sesion()
    for producto_id, *_ in CARRITO_A:
        inventario.agregar_al_carrito(producto_id)
    inventario.ir_al_carrito()
    return CartPage(page)


@pytest.fixture
def paso_1_carrito_a(page: Page, carrito_a: CartPage) -> CheckoutStepOnePage:
    """Paso 1 con Carrito A: deja al test en /checkout-step-one.html con los campos vacíos."""
    carrito_a.ir_al_checkout()
    return CheckoutStepOnePage(page)


@pytest.fixture
def paso_2_carrito_a(page: Page, paso_1_carrito_a: CheckoutStepOnePage) -> CheckoutStepTwoPage:
    """Paso 2 con Carrito A: datos válidos de referencia escritos; deja al test en /checkout-step-two.html."""
    paso_1_carrito_a.continuar(NOMBRE, APELLIDO, CODIGO_POSTAL)
    return CheckoutStepTwoPage(page)
