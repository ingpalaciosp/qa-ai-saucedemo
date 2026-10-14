# Casos de prueba – Carrito SauceDemo (diseñados por el agente)

URL: https://www.saucedemo.com

Usuario: `standard_user` / `secret_sauce`

Precondición común: sesión iniciada en `/inventory.html` con el carrito vacío (icono del carrito sin número y todos los productos con botón "Add to cart"). Ojo: el carrito no se vacía al cerrar sesión (ver caso 8), así que hay que quitar a mano lo que haya quedado de una ejecución anterior.

| # | Caso | Pasos | Resultado esperado | Resultado real | ¿Coincide? |
|---|------|-------|--------------------|----------------|------------|
| 1 | Añadir un producto desde el listado | 1. En `/inventory.html`, clic en "Add to cart" de "Sauce Labs Backpack" | 1. El botón del producto deberia de cambiar a "Remove". 2.  El icono del carrito deberia muestrar el número `1`. Debe de permanecer en `/inventory.html` |  El botón del producto  cambia a "Remove". 2.  El icono del carrito muestra el número `1`. Permanece en `/inventory.html` | ✅ Sí |
| 2 | El número del carrito cuenta varios productos | 1. Clic en "Add to cart" de "Sauce Labs Backpack"<br>2. Clic en "Add to cart" de "Sauce Labs Bike Light"<br>3. Clic en "Add to cart" de "Sauce Labs Onesie" | 1. El icono del carrito debe de mostrar `3`. 2. Los tres productos deben mostrar "Remove" | 1. El icono del carrito muestra `3`. 2. Los tres productos muestran "Remove" | ✅ Sí |
| 3 | Ver el contenido del carrito | 1. Añadir "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie"<br>2. Clic en el icono del carrito | 1. Debe Navegar a `/cart.html` con el título "Your Cart" y las columnas "QTY" y "Description". 2. Debe Listar 3 productos, cada uno con QTY `1` y botón "Remove": "Sauce Labs Backpack" `$29.99`, "Sauce Labs Bike Light" `$9.99`, "Sauce Labs Onesie" `$7.99`. 3. Deben mostrarse los botones "Continue Shopping" y "Checkout". 4. El icono del carrito debe mostrar `3` | | |
| 4 | Quitar un producto desde el listado | 1. Añadir "Sauce Labs Backpack" y "Sauce Labs Bike Light" (icono en `2`)<br>2. Clic en "Remove" de "Sauce Labs Backpack"<br>3. Clic en "Remove" de "Sauce Labs Bike Light" | Tras el paso 2: el botón de Backpack vuelve a "Add to cart" y el icono muestra `1`. Tras el paso 3: el botón de Bike Light vuelve a "Add to cart" y el número desaparece del icono (no muestra `0`) | | |
| 5 | Quitar un producto desde el carrito | 1. Añadir "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie"<br>2. Clic en el icono del carrito<br>3. Clic en "Remove" de "Sauce Labs Bike Light" | "Sauce Labs Bike Light" desaparece de la lista. Quedan "Sauce Labs Backpack" `$29.99` y "Sauce Labs Onesie" `$7.99`, ambos con QTY `1`. El icono pasa de `3` a `2`. Se permanece en `/cart.html` | | |
| 6 | "Continue Shopping" vuelve al listado conservando el carrito | 1. Dejar el carrito como al final del caso 5 (Backpack y Onesie)<br>2. En `/cart.html`, clic en "Continue Shopping" | Navega a `/inventory.html`. El icono sigue mostrando `2`. "Sauce Labs Backpack" y "Sauce Labs Onesie" muestran "Remove"; "Sauce Labs Bike Light" (quitado desde el carrito) muestra "Add to cart" | | |
| 7 | Carrito vacío | 1. Con el carrito vacío, clic en el icono del carrito | Navega a `/cart.html` con el título "Your Cart", las columnas "QTY" y "Description" y ningún producto listado. El icono no muestra número. Siguen visibles "Continue Shopping" y "Checkout". No aparece ningún mensaje de "carrito vacío". Qué ocurre al pulsar "Checkout" con el carrito vacío: A confirmar | | |
| 8 | El carrito se conserva al recargar y al cerrar sesión | 1. Añadir "Sauce Labs Backpack" y "Sauce Labs Onesie" (icono en `2`)<br>2. Recargar `/inventory.html`<br>3. Abrir el menú ("Open Menu") y cerrar sesión<br>4. Iniciar sesión de nuevo con `standard_user` / `secret_sauce` | Tras el paso 2 y tras el paso 4: el icono sigue mostrando `2` y ambos productos siguen con "Remove". Si el carrito se conserva también con otro usuario o en otro navegador: A confirmar | | |

## Otras observaciones de la exploración

- Desde la página de detalle de "Sauce Labs Bolt T-Shirt" (`/inventory-item.html?id=1`, precio `$15.99`), "Add to cart" también sube el número del icono y el botón cambia a "Remove". No está incluido en los 8 casos.
- No se vio en el carrito ningún control para cambiar la cantidad: QTY aparece como texto `1`. Si se puede tener más de una unidad del mismo producto: A confirmar.
- No se exploró el flujo de "Checkout" ni el total del pedido: A confirmar.

> Explorado por el agente con el navegador en www.saucedemo.com el 11/10/2026. Pendiente de validación manual.
