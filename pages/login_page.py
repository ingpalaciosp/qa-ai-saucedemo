from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Pantalla de login de SauceDemo: selectores y acciones, sin aserciones."""

    RUTA = "/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.campo_usuario = page.locator('[data-test="username"]')
        self.campo_password = page.locator('[data-test="password"]')
        self.boton_login = page.locator('[data-test="login-button"]')
        self.mensaje_error = page.locator('[data-test="error"]')

    def login(self, usuario: str, password: str):
        self.campo_usuario.fill(usuario)
        self.campo_password.fill(password)
        self.boton_login.click()
