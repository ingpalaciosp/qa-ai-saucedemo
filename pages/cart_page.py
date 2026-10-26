from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    """Pantalla del carrito de SauceDemo: selectores y acciones, sin aserciones."""

    RUTA = "/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.boton_checkout = page.locator('[data-test="checkout"]')

    def ir_al_checkout(self):
        self.boton_checkout.click()
