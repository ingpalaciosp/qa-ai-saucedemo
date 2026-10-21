from playwright.sync_api import Page


class CheckoutStepOnePage:
    """Paso 1 del checkout (Your Information): selectores y acciones, sin aserciones."""

    RUTA = "/checkout-step-one.html"

    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator('[data-test="title"]')
        self.formulario = page.locator('[data-test="checkout-info-container"]')
        self.campo_nombre = page.locator('[data-test="firstName"]')
        self.campo_apellido = page.locator('[data-test="lastName"]')
        self.campo_codigo_postal = page.locator('[data-test="postalCode"]')
        self.boton_continuar = page.locator('[data-test="continue"]')

    def abrir(self):
        self.page.goto(self.RUTA)

    def continuar(self, nombre: str, apellido: str, codigo_postal: str):
        self.campo_nombre.fill(nombre)
        self.campo_apellido.fill(apellido)
        self.campo_codigo_postal.fill(codigo_postal)
        self.boton_continuar.click()
