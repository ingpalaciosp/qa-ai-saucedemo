from playwright.sync_api import Page


class InventoryPage:
    """Pantalla de productos de SauceDemo: selectores y acciones, sin aserciones."""

    def __init__(self, page: Page):
        self.page = page
        self.imagenes_productos = page.locator("img.inventory_item_img")

    def obtener_src_imagenes(self) -> list[str]:
        return [imagen.get_attribute("src") for imagen in self.imagenes_productos.all()]
