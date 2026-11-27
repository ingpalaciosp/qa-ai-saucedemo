from typing import Callable

from playwright.sync_api import Page, expect

from data.checkout import TITULO_CONFIRMACION
from data.usuarios import (
    ERROR_CREDENCIALES_INVALIDAS,
    ERROR_USUARIO_BLOQUEADO,
    ERROR_USUARIO_REQUERIDO,
    PASSWORD,
    PASSWORD_INCORRECTA,
    USUARIO_BLOQUEADO,
    USUARIO_ESTANDAR,
)
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_carrito(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    page.wait_for_timeout(2000)

    page.locator(".inventory_item:nth-child(1) button").click()
    insignia = page.locator(".shopping_cart_badge")

    page.locator('[data-test="product-sort-container"]').select_option("az")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    insignia.is_visible()


def test_e_login_clave_incorrecta(page: Page, login_page: LoginPage, url_login: str):
    # Objetivo: con la contraseña incorrecta, se muestra un mensaje de error
    login_page.login(USUARIO_ESTANDAR, PASSWORD_INCORRECTA)
    expect(login_page.mensaje_error).to_have_text(ERROR_CREDENCIALES_INVALIDAS)
    expect(page).to_have_url(url_login)


def test_f_login_valido(page: Page, iniciar_sesion: Callable[..., InventoryPage], url_inventario: str):
    # Objetivo: con usuario y contraseña correctos, entras al inventario
    iniciar_sesion()
    expect(page).to_have_url(url_inventario)


def test_g_resumen_muestra_productos(page: Page, paso_2_carrito_a: CheckoutStepTwoPage):
    # Objetivo: el resumen del pedido muestra los 2 productos del carrito A
    expect(paso_2_carrito_a.nombres_productos.first).to_have_text("Sauce Labs Backpack")
    expect(paso_2_carrito_a.nombres_productos.last).to_have_text("Sauce Labs Bike Light")


def test_h_resumen_item_total(page: Page, paso_2_carrito_a):
    # Objetivo: el resumen muestra "Item total: $39.98"
    expect(paso_2_carrito_a.resumen).to_be_visible()
    expect(paso_2_carrito_a.resumen).to_contain_text("Item total: $39.98")


def test_1_usuario_bloqueado(page: Page, login_page: LoginPage, url_login: str):
    # Objetivo: el usuario bloqueado ve "Epic sadface: Sorry, this user has been locked out."
    login_page.login(USUARIO_BLOQUEADO, PASSWORD)
    expect(login_page.mensaje_error).to_have_text(ERROR_USUARIO_BLOQUEADO)
    expect(page).to_have_url(url_login)


def test_2_ordenar_precio_menor_a_mayor(page: Page, iniciar_sesion: Callable[..., InventoryPage]):
    # Objetivo: al ordenar por precio de menor a mayor, el primero es "Sauce Labs Onesie"
    inventario = iniciar_sesion()
    inventario.ordenar("Price (low to high)")
    expect(inventario.nombres_productos.first).to_have_text("Sauce Labs Onesie")


def test_3_compra_terminada(page: Page, paso_2_carrito_a: CheckoutStepTwoPage):
    # Objetivo: al terminar la compra, el título es "Checkout: Complete!"
    paso_2_carrito_a.finalizar()
    expect(paso_2_carrito_a.titulo).to_have_text(TITULO_CONFIRMACION)


def test_4_login_sin_usuario(page: Page, login_page: LoginPage):
    # Objetivo: sin usuario, aparece "Epic sadface: Username is required"
    login_page.login("", PASSWORD)
    expect(login_page.mensaje_error).to_have_text(ERROR_USUARIO_REQUERIDO)


def test_5_resumen_tiene_2_productos(page: Page, paso_2_carrito_a: CheckoutStepTwoPage):
    # Objetivo: el resumen del carrito A muestra 2 productos
    expect(paso_2_carrito_a.nombres_productos).to_have_count(2)


def test_tc_cart_009_contador_tras_anadir_un_producto(page: Page, iniciar_sesion): 
    inventario = iniciar_sesion()
    inventario.agregar_al_carrito("sauce-labs-backpack")

    expect(inventario.contador_carrito).to_have_text("1")
    
def test_tc_cart_002_contador_varios_productos(page: Page, iniciar_sesion):
    inventario = iniciar_sesion()
    inventario.agregar_al_carrito("sauce-labs-backpack")
    inventario.agregar_al_carrito("sauce-labs-bike-light")
    inventario.agregar_al_carrito("sauce-labs-onesie")

    expect(inventario.contador_carrito).to_have_text("3")

def test_tc_sort_005_ordenar_por_nombre_a_z(page: Page, iniciar_sesion):
    inventario = iniciar_sesion()
    inventario.ordenar("Name (Z to A)")
    inventario.ordenar("Name (A to Z)")

    expect(inventario.nombres_productos).to_have_text([
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"])

def test_tc_cart_012_quitar_producto_del_listado(page: Page, iniciar_sesion):
    inventario = iniciar_sesion()
    inventario.agregar_al_carrito("sauce-labs-backpack")
    inventario.agregar_al_carrito("sauce-labs-bike-light")
    inventario.remover_producto_listado("sauce-labs-backpack")

    expect(inventario.contador_carrito).to_have_text("1")

def test_tc_cart_016_contador_quitar_desde_el_carrito(page: Page, carrito_a):
    carrito_a.remover_carrito("sauce-labs-bike-lightD")     

    expect(carrito_a.contador_carrito).to_have_text("1")

   
def test_tc_sort_005_ordenar_a_z_sin_lista(page: Page, iniciar_sesion):
    inventario = iniciar_sesion()
    inventario.ordenar("Name (Z to A)")
    inventario.ordenar("Name (A to Z)")

    # 1. Leo los nombres que hay en pantalla (sean 6 o 6.000)
    nombres_en_pantalla = inventario.nombres_productos.all_text_contents()

    # 2. Hago una copia y la ordeno yo de la A a la Z
    copia_ordenada = sorted(nombres_en_pantalla)

    # 3. Si la pantalla ya estaba ordenada, las dos listas son iguales
    assert nombres_en_pantalla == copia_ordenada

def test_tc_cart_002_contador_varios_productos(page: Page, iniciar_sesion):
    inventario = iniciar_sesion()
    inventario.agregar_al_carrito("sauce-labs-backpack")
    inventario.agregar_al_carrito("sauce-labs-bike-light")
    inventario.agregar_al_carrito("sauce-labs-onesie")

    expect(inventario.contador_carrito).to_have_text("3")


def test_tct_cart_010_permanecer_en_el_listado_al_añadir(page: Page, iniciar_sesion, url_inventario):
    inventario = iniciar_sesion()
    inventario.agregar_al_carrito("sauce-labs-backpack")

    expect(page).to_have_url(url_inventario)
    