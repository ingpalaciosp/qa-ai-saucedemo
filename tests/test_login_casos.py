import pytest
from playwright.sync_api import Page, expect

# Casos automatizados desde casos/login-v2-con-contexto.md

URL = "https://www.saucedemo.com"
URL_INVENTARIO = "https://www.saucedemo.com/inventory.html"
PASSWORD = "secret_sauce"


def login(page: Page, usuario: str, password: str):
    page.goto(URL)
    if usuario:
        page.fill("#user-name", usuario)
    if password:
        page.fill("#password", password)
    page.click("#login-button")


def mensaje_error(page: Page):
    return page.locator('[data-test="error"]')


def test_caso_1_login_usuario_valido(page: Page):
    login(page, "standard_user", PASSWORD)
    expect(page).to_have_url(URL_INVENTARIO)


def test_caso_2_usuario_bloqueado(page: Page):
    login(page, "locked_out_user", PASSWORD)
    expect(mensaje_error(page)).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )
    expect(page).to_have_url(URL + "/")


def test_caso_3_login_problem_user(page: Page):
    login(page, "problem_user", PASSWORD)
    expect(page).to_have_url(URL_INVENTARIO)


@pytest.mark.xfail(reason="Bug conocido: issue #1", strict=True)
def test_caso_3_problem_user_imagenes_distintas(page: Page):
    login(page, "problem_use", PASSWORD)
    expect(page).to_have_url(URL_INVENTARIO)

    imagenes = page.locator("img.inventory_item_img")
    expect(imagenes).to_have_count(6)

    direcciones_fotos = [imagenes.nth(i).get_attribute("src") for i in range(6)]
    assert len(set(direcciones_fotos)) > 1, f"Todas las imágenes son iguales: {direcciones_fotos[0]}"


def test_caso_4_username_vacio(page: Page):
    login(page, "", PASSWORD)
    expect(mensaje_error(page)).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url(URL + "/")


def test_caso_5_password_vacio(page: Page):
    login(page, "standard_user", "")
    expect(mensaje_error(page)).to_have_text("Epic sadface: Password is required")
    expect(page).to_have_url(URL + "/")

def test_caso_6_contrasena_incorrecta(page: Page):
    login(page, "standard_user", "clave_incorrecta")
    expect(mensaje_error(page)).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    expect(page).to_have_url(URL + "/")


def test_caso_7_usuario_inexistente(page: Page):
    login(page, "usuario_inexistente", PASSWORD)
    expect(mensaje_error(page)).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    expect(page).to_have_url(URL + "/")


def test_caso_8_ambos_campos_vacios(page: Page):
    login(page, "", "")
    expect(mensaje_error(page)).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url(URL + "/")
