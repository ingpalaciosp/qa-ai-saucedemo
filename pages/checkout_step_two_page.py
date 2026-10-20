from playwright.sync_api import Page


class CheckoutStepTwoPage:
    """Paso 2 del checkout (Overview): selectores y acciones, sin aserciones."""

    RUTA = "/checkout-step-two.html"

    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator('[data-test="title"]')
        self.resumen = page.locator('[data-test="checkout-summary-container"]')
        self.etiqueta_cantidad = page.locator('[data-test="cart-quantity-label"]')
        self.etiqueta_descripcion = page.locator('[data-test="cart-desc-label"]')
        self.nombres_productos = page.locator('[data-test="inventory-item-name"]')
        self.precios_productos = page.locator('[data-test="inventory-item-price"]')
        self.cantidades_productos = page.locator('[data-test="item-quantity"]')
        self.botones_remove = page.locator('[data-test="cart-list"] [data-test^="remove-"]')
        self.boton_finish = page.locator('[data-test="finish"]')

    def abrir(self):
        self.page.goto(self.RUTA)

    def finalizar(self):
        self.boton_finish.click()
