from playwright.sync_api import Page


class BasePage:
    """Clase madre de todas las páginas: guarda la página del navegador y sabe abrirla."""

    RUTA = "/"

    def __init__(self, page: Page):
        self.page = page

    def abrir(self):
        self.page.goto(self.RUTA)
