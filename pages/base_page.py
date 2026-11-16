from playwright.sync_api import Page


class BasePage:
    """Clase madre de todas las páginas: guarda la página, sabe abrirla
    y localiza el título de arriba (el login no tiene)"""

    RUTA = "/"

    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator('[data-test="title"]')

    def abrir(self):
        self.page.goto(self.RUTA)
