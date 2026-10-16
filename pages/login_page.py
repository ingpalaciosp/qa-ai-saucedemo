from playwright.sync_api import Page


class LoginPage:
    """Pantalla de login de SauceDemo: selectores y acciones, sin aserciones."""

    RUTA = "/"

    def __init__(self, page: Page):
        self.page = page
        self.campo_usuario = page.locator('[data-test="username"]')
        self.campo_password = page.locator('[data-test="password"]')
        self.boton_login = page.locator('[data-test="login-button"]')
        self.mensaje_error = page.locator('[data-test="error"]')

    def abrir(self):
        self.page.goto(self.RUTA)

    def login(self, usuario: str, password: str):
        self.campo_usuario.fill(usuario)
        self.campo_password.fill(password)
        self.boton_login.click()
