import pytest
from playwright.sync_api import Page, expect

from data.checkout import (
    APELLIDO,
    CARRITO_A,
    CODIGO_POSTAL,
    ERROR_SIN_SESION,
    NOMBRE,
    TITULO_CONFIRMACION,
    TITULO_PASO_1,
    TITULO_RESUMEN,
)
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.login_page import LoginPage

# Casos automatizados desde casos/checkout.md: solo los 🔴 sin "A confirmar",
# bug ni preguntas al PO en Notas.


def test_tc_checkout_001_entrar_al_checkout_con_productos(page: Page, base_url, carrito_a: CartPage):
    carrito_a.ir_al_checkout()

    paso_1 = CheckoutStepOnePage(page)
    expect(page).to_have_url(base_url + CheckoutStepOnePage.RUTA)
    expect(paso_1.titulo).to_have_text(TITULO_PASO_1)


def test_tc_checkout_004_continuar_con_datos_validos(page: Page, base_url, paso_1_carrito_a: CheckoutStepOnePage):
    paso_1_carrito_a.continuar(NOMBRE, APELLIDO, CODIGO_POSTAL)

    resumen = CheckoutStepTwoPage(page)
    expect(page).to_have_url(base_url + CheckoutStepTwoPage.RUTA)
    expect(resumen.titulo).to_have_text(TITULO_RESUMEN)


def test_tc_checkout_018_productos_del_resumen(page: Page, paso_1_carrito_a: CheckoutStepOnePage):
    paso_1_carrito_a.continuar(NOMBRE, APELLIDO, CODIGO_POSTAL)

    resumen = CheckoutStepTwoPage(page)
    expect(resumen.etiqueta_cantidad).to_have_text("QTY")
    expect(resumen.etiqueta_descripcion).to_have_text("Description")
    expect(resumen.nombres_productos).to_have_text([nombre for _id, nombre, _precio in CARRITO_A])
    expect(resumen.precios_productos).to_have_text([precio for _id, _nombre, precio in CARRITO_A])
    expect(resumen.cantidades_productos).to_have_text(["1"] * len(CARRITO_A))
    expect(resumen.botones_remove).to_have_count(0)


def test_tc_checkout_024_finalizar_el_pedido(page: Page, base_url, paso_2_carrito_a: CheckoutStepTwoPage):
    paso_2_carrito_a.finalizar()

    confirmacion = CheckoutCompletePage(page)
    expect(page).to_have_url(base_url + CheckoutCompletePage.RUTA)
    expect(confirmacion.titulo).to_have_text(TITULO_CONFIRMACION)


@pytest.mark.parametrize(
    "pantalla, contenido",
    [
        pytest.param(CheckoutStepOnePage, "formulario", id="TC-CHECKOUT-033_paso_1_sin_sesion"),
        pytest.param(CheckoutStepTwoPage, "resumen", id="TC-CHECKOUT-034_paso_2_sin_sesion"),
        pytest.param(CheckoutCompletePage, "confirmacion", id="TC-CHECKOUT-035_confirmacion_sin_sesion"),
    ],
)
def test_checkout_sin_sesion(page: Page, url_login, pantalla, contenido):
    # Precondición "Sesión cerrada": cada test abre un navegador nuevo, sin sesión
    pagina = pantalla(page)
    pagina.abrir()

    expect(page).to_have_url(url_login)
    expect(LoginPage(page).mensaje_error).to_have_text(ERROR_SIN_SESION.format(ruta=pantalla.RUTA))
    expect(getattr(pagina, contenido)).to_have_count(0)
