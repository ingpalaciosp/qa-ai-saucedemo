import pytest
from playwright.sync_api import Page, expect

from data.usuarios import (
    ERROR_CREDENCIALES_INVALIDAS,
    ERROR_PASSWORD_REQUERIDO,
    ERROR_USUARIO_BLOQUEADO,
    ERROR_USUARIO_REQUERIDO,
    PASSWORD,
    PASSWORD_INCORRECTA,
    USUARIO_BLOQUEADO,
    USUARIO_ESTANDAR,
    USUARIO_INEXISTENTE,
    USUARIO_PROBLEMA,
)
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# Casos automatizados desde casos/login-v2-con-contexto.md


@pytest.mark.parametrize(
    "usuario",
    [
        pytest.param(USUARIO_ESTANDAR, id="caso_1_usuario_valido"),
        pytest.param(USUARIO_PROBLEMA, id="caso_3_problem_user"),
    ],
)
def test_login_correcto(page: Page, login_page: LoginPage, url_inventario, usuario):
    login_page.login(usuario, PASSWORD)
    expect(page).to_have_url(url_inventario)


@pytest.mark.xfail(reason="Bug conocido: issue #1", strict=True)
def test_caso_3_problem_user_imagenes_distintas(page: Page, login_page: LoginPage, url_inventario):
    login_page.login(USUARIO_PROBLEMA, PASSWORD)
    expect(page).to_have_url(url_inventario)

    inventario = InventoryPage(page)
    expect(inventario.imagenes_productos).to_have_count(6)

    direcciones_fotos = inventario.obtener_src_imagenes()
    assert len(set(direcciones_fotos)) > 1, f"Todas las imágenes son iguales: {direcciones_fotos[0]}"


@pytest.mark.parametrize(
    "usuario, password, mensaje",
    [
        pytest.param(USUARIO_BLOQUEADO, PASSWORD, ERROR_USUARIO_BLOQUEADO, id="caso_2_usuario_bloqueado"),
        pytest.param("", PASSWORD, ERROR_USUARIO_REQUERIDO, id="caso_4_username_vacio"),
        pytest.param(USUARIO_ESTANDAR, "", ERROR_PASSWORD_REQUERIDO, id="caso_5_password_vacio"),
        pytest.param(
            USUARIO_ESTANDAR, PASSWORD_INCORRECTA, ERROR_CREDENCIALES_INVALIDAS,
            id="caso_6_contrasena_incorrecta",
        ),
        pytest.param(
            USUARIO_INEXISTENTE, PASSWORD, ERROR_CREDENCIALES_INVALIDAS,
            id="caso_7_usuario_inexistente",
        ),
        pytest.param("", "", ERROR_USUARIO_REQUERIDO, id="caso_8_ambos_campos_vacios"),
    ],
)
def test_login_con_error(page: Page, login_page: LoginPage, url_login, usuario, password, mensaje):
    login_page.login(usuario, password)
    expect(login_page.mensaje_error).to_have_text(mensaje)
    expect(page).to_have_url(url_login)
