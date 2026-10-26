from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Confirmación del pedido (Complete!): selectores y acciones, sin aserciones."""

    RUTA = "/checkout-complete.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.titulo = page.locator('[data-test="title"]')
        self.confirmacion = page.locator('[data-test="checkout-complete-container"]')
