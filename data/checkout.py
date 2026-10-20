"""Datos de prueba del checkout de SauceDemo (ver "Datos y estados de partida" en casos/checkout.md)."""

# Datos válidos de referencia del comprador
NOMBRE = "Alicia"
APELLIDO = "Palacios"
CODIGO_POSTAL = "28001"

# Carrito A: id del producto (parte final del data-test "add-to-cart-..."), nombre y precio
CARRITO_A = [
    ("sauce-labs-backpack", "Sauce Labs Backpack", "$29.99"),
    ("sauce-labs-bike-light", "Sauce Labs Bike Light", "$9.99"),
]

TITULO_PASO_1 = "Checkout: Your Information"
TITULO_RESUMEN = "Checkout: Overview"
TITULO_CONFIRMACION = "Checkout: Complete!"

# Mensaje al abrir una página del checkout sin sesión; {ruta} es la página, por ejemplo "/cart.html"
ERROR_SIN_SESION = "Epic sadface: You can only access '{ruta}' when you are logged in."
