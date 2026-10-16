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
from pages.login_page import LoginPage

# Casos automatizados desde casos/login-v2-con-contexto.md


@pytest.mark.parametrize(
    "usuario",
    [
        pytest.param(USUARIO_ESTANDAR, id="TC-LOGIN-001_usuario_valido"),
        pytest.param(USUARIO_PROBLEMA, id="TC-LOGIN-003_problem_user"),
    ],
)
def test_login_correcto(page: Page, login_page: LoginPage, url_inventario, usuario):
    login_page.login(usuario, PASSWORD)
    expect(page).to_have_url(url_inventario)


def test_tc_login_009_problem_user_imagenes_distintas(page: Page, iniciar_sesion, url_inventario):
    inventario = iniciar_sesion(USUARIO_PROBLEMA)
    # Precondiciones: si fallan, el test sale en rojo (no las tapa el xfail)
    expect(page).to_have_url(url_inventario)
    expect(inventario.imagenes_productos).to_have_count(6)

    direcciones_fotos = inventario.obtener_src_imagenes()
    if len(set(direcciones_fotos)) == 1:
        pytest.xfail(f"Bug conocido: issue #1. Todas las imágenes son iguales: {direcciones_fotos[0]}")


@pytest.mark.parametrize(
    "usuario, password, mensaje",
    [
        pytest.param(USUARIO_BLOQUEADO, PASSWORD, ERROR_USUARIO_BLOQUEADO, id="TC-LOGIN-002_usuario_bloqueado"),
        pytest.param("", PASSWORD, ERROR_USUARIO_REQUERIDO, id="TC-LOGIN-004_username_vacio"),
        pytest.param(USUARIO_ESTANDAR, "", ERROR_PASSWORD_REQUERIDO, id="TC-LOGIN-005_password_vacio"),
        pytest.param(
            USUARIO_ESTANDAR, PASSWORD_INCORRECTA, ERROR_CREDENCIALES_INVALIDAS,
            id="TC-LOGIN-006_contrasena_incorrecta",
        ),
        pytest.param(
            USUARIO_INEXISTENTE, PASSWORD, ERROR_CREDENCIALES_INVALIDAS,
            id="TC-LOGIN-007_usuario_inexistente",
        ),
        pytest.param("", "", ERROR_USUARIO_REQUERIDO, id="TC-LOGIN-008_ambos_campos_vacios"),
    ],
)
def test_login_con_error(page: Page, login_page: LoginPage, url_login, usuario, password, mensaje):
    login_page.login(usuario, password)
    expect(login_page.mensaje_error).to_have_text(mensaje)
    expect(page).to_have_url(url_login)
