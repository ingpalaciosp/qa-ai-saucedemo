import pytest
from playwright.sync_api import Page, expect


def test_tc_sort_004_ordenar_por_nombre_a_z(page: Page, iniciar_sesion):
    inventario = iniciar_sesion()
    inventario.ordenar("Name (Z to A)")
    inventario.ordenar("Name (A to Z)")

    expect(inventario.nombres_productos.first).to_have_text("Sauce Labs Backpack")
    expect(inventario.nombres_productos.last).to_have_text("Test.allTheThings() T-Shirt (Red)")


@pytest.mark.parametrize(
    "opcion, primero, ultimo",
    [
        pytest.param("Name (Z to A)", "Test.allTheThings() T-Shirt (Red)", "Sauce Labs Backpack", id="TC-SORT-001_nombre_z_a"),
        pytest.param("Price (low to high)", "Sauce Labs Onesie", "Sauce Labs Fleece Jacket", id="TC-SORT-002_precio_menor_a_mayor"),
        pytest.param("Price (high to low)", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", id="TC-SORT-003_precio_mayor_a_menor"),
    ],
)
def test_ordenar_productos(page: Page, iniciar_sesion, opcion, primero, ultimo):
    inventario = iniciar_sesion()
    inventario.ordenar(opcion)

    expect(inventario.nombres_productos.first).to_have_text(primero)
    expect(inventario.nombres_productos.last).to_have_text(ultimo)
