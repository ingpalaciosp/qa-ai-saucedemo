from playwright.sync_api import Page


class InventoryPage:
    """Pantalla de productos de SauceDemo: selectores y acciones, sin aserciones."""

    RUTA = "/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        # Cada imagen tiene un data-test que termina en "-img" (ej. "inventory-item-sauce-labs-backpack-img")
        self.imagenes_productos = page.locator('img[data-test$="-img"]')

    def obtener_src_imagenes(self) -> list[str]:
        # .all() no espera: primero se espera a que aparezca al menos una imagen
        self.imagenes_productos.first.wait_for()
        return [imagen.get_attribute("src") for imagen in self.imagenes_productos.all()]
