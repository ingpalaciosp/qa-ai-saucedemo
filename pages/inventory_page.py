from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Pantalla de productos de SauceDemo: selectores y acciones, sin aserciones."""

    RUTA = "/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # Cada imagen tiene un data-test que termina en "-img" (ej. "inventory-item-sauce-labs-backpack-img")
        self.imagenes_productos = page.locator('img[data-test$="-img"]')
        self.enlace_carrito = page.locator('[data-test="shopping-cart-link"]')

    def agregar_al_carrito(self, producto_id: str):
        # producto_id es la parte final del data-test, por ejemplo "sauce-labs-backpack"
        self.page.locator(f'[data-test="add-to-cart-{producto_id}"]').click()

    def ir_al_carrito(self):
        self.enlace_carrito.click()

    def obtener_src_imagenes(self) -> list[str]:
        # .all() no espera: primero se espera a que aparezca al menos una imagen
        self.imagenes_productos.first.wait_for()
        return [imagen.get_attribute("src") for imagen in self.imagenes_productos.all()]
