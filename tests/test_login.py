from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com"


def test_login_correcto(page: Page):
    # 1. PREPARAR: abrir la página
    page.goto(URL)

    # 2. ACTUAR: escribir usuario y contraseña, y hacer clic
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # 3. COMPROBAR: ¿llegué a la página de productos?
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_sin_usuario(page: Page):
    page.goto(URL)
    page.click("#login-button")

    # comprobar mensaje de error exacto
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Username is required"
    )