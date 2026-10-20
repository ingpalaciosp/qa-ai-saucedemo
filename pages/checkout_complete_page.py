from playwright.sync_api import Page


class CheckoutCompletePage:
    """Confirmación del pedido (Complete!): selectores y acciones, sin aserciones."""

    RUTA = "/checkout-complete.html"

    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator('[data-test="title"]')
        self.confirmacion = page.locator('[data-test="checkout-complete-container"]')

    def abrir(self):
        self.page.goto(self.RUTA)
