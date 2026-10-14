from playwright.sync_api import Page


class LoginPage:
    """Pantalla de login de SauceDemo: selectores y acciones, sin aserciones."""

    def __init__(self, page: Page):
        self.page = page
        self.campo_usuario = page.locator('[data-test="username"]')
        self.campo_password = page.locator('[data-test="password"]')
        self.boton_login = page.locator('[data-test="login-button"]')
        self.mensaje_error = page.locator('[data-test="error"]')

    def abrir(self):
        self.page.goto("/")

    def login(self, usuario: str, password: str):
        if usuario:
            self.campo_usuario.fill(usuario)
        if password:
            self.campo_password.fill(password)
        self.boton_login.click()
