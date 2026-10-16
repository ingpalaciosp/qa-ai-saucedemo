# Carrito

URL: https://www.saucedemo.com · Usuario: `standard_user` / `secret_sauce`

## Listado de productos

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CART-001 | Añadir un producto desde el listado | 🔴 Alta | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Carrito vacío (icono sin número) | 1. Hacer clic en "Add to cart" de "Sauce Labs Backpack" | Debería cambiar el botón de "Sauce Labs Backpack" a "Remove" | ✅ El botón de "Sauce Labs Backpack" cambia a "Remove" | N/A |
| TC-CART-009 | Contador tras añadir un producto | 🔴 Alta | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Carrito vacío (icono sin número) | 1. Hacer clic en "Add to cart" de "Sauce Labs Backpack" | Debería mostrar `1` en el icono del carrito | ✅ El icono del carrito muestra `1` | N/A |
| TC-CART-002 | Contador con varios productos | 🔴 Alta | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Carrito vacío (icono sin número) | 1. Hacer clic en "Add to cart" de "Sauce Labs Backpack"<br>2. Hacer clic en "Add to cart" de "Sauce Labs Bike Light"<br>3. Hacer clic en "Add to cart" de "Sauce Labs Onesie" | Debería mostrar `3` en el icono del carrito | ✅ El icono del carrito muestra `3` | N/A |
| TC-CART-010 | Permanecer en el listado tras añadir | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Carrito vacío (icono sin número) | 1. Hacer clic en "Add to cart" de "Sauce Labs Backpack" | Debería seguir en `/inventory.html` | ✅ Sigue en `/inventory.html` | N/A |
| TC-CART-011 | Botones tras añadir varios productos | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Carrito vacío (icono sin número) | 1. Hacer clic en "Add to cart" de "Sauce Labs Backpack"<br>2. Hacer clic en "Add to cart" de "Sauce Labs Bike Light"<br>3. Hacer clic en "Add to cart" de "Sauce Labs Onesie" | Debería mostrar "Remove" en "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie" | ✅ Los tres productos muestran "Remove" | N/A |
| TC-CART-004 | Quitar un producto desde el listado | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. "Sauce Labs Backpack" y "Sauce Labs Bike Light" en el carrito (icono en `2`) | 1. Hacer clic en "Remove" de "Sauce Labs Backpack" | Debería cambiar el botón de "Sauce Labs Backpack" a "Add to cart" | ✅ El botón de "Sauce Labs Backpack" vuelve a "Add to cart" | N/A |
| TC-CART-012 | Contador al quitar desde el listado | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. "Sauce Labs Backpack" y "Sauce Labs Bike Light" en el carrito (icono en `2`) | 1. Hacer clic en "Remove" de "Sauce Labs Backpack" | Debería mostrar `1` en el icono del carrito | ✅ El icono del carrito pasa de `2` a `1` | N/A |
| TC-CART-013 | Quitar el último producto desde el listado | 🟢 Baja | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Solo "Sauce Labs Bike Light" en el carrito (icono en `1`) | 1. Hacer clic en "Remove" de "Sauce Labs Bike Light" | A confirmar | 🔍 El número desaparece del icono (no muestra `0`) y el botón vuelve a "Add to cart" | Comportamiento actual: el icono queda sin número. Duda: ¿sin número o `0`? |

## Página del carrito

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CART-003 | Ver los productos en el carrito | 🔴 Alta | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie" añadidos desde el listado | 1. Hacer clic en el icono del carrito | Debería navegar a `/cart.html` y listar "Sauce Labs Backpack" `$29.99`, "Sauce Labs Bike Light" `$9.99` y "Sauce Labs Onesie" `$7.99`, cada uno con QTY `1` | ✅ Navega a `/cart.html` y lista los tres productos con esos precios y QTY `1` | N/A |
| TC-CART-005 | Quitar un producto desde el carrito | 🔴 Alta | 1. Sesión iniciada con `standard_user`<br>2. "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie" en el carrito<br>3. Estar en `/cart.html` | 1. Hacer clic en "Remove" de "Sauce Labs Bike Light" | Debería quitar "Sauce Labs Bike Light" de la lista, mantener "Sauce Labs Backpack" `$29.99` y "Sauce Labs Onesie" `$7.99` con QTY `1` y seguir en `/cart.html` | ✅ Desaparece "Sauce Labs Bike Light"; quedan Backpack `$29.99` y Onesie `$7.99` con QTY `1`; sigue en `/cart.html` | N/A |
| TC-CART-016 | Contador al quitar desde el carrito | 🔴 Alta | 1. Sesión iniciada con `standard_user`<br>2. "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie" en el carrito<br>3. Estar en `/cart.html` | 1. Hacer clic en "Remove" de "Sauce Labs Bike Light" | Debería mostrar `2` en el icono del carrito | ✅ El icono del carrito muestra `2` | N/A |
| TC-CART-015 | Controles de la página del carrito | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie" añadidos desde el listado | 1. Hacer clic en el icono del carrito | Debería mostrar un botón "Remove" en cada producto y los botones "Continue Shopping" y "Checkout" | ✅ Cada producto tiene "Remove" y se ven "Continue Shopping" y "Checkout" | N/A |
| TC-CART-006 | "Continue Shopping" conserva el carrito | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. "Sauce Labs Backpack" y "Sauce Labs Onesie" añadidos desde el listado<br>3. Estar en `/cart.html` | 1. Hacer clic en "Continue Shopping" | Debería navegar a `/inventory.html` y mostrar `2` en el icono del carrito | ✅ Navega a `/inventory.html` y el icono muestra `2` | N/A |
| TC-CART-017 | Botones del listado tras quitar desde el carrito | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie" añadidos desde el listado<br>3. "Sauce Labs Bike Light" quitado desde `/cart.html`<br>4. Estar en `/cart.html` | 1. Hacer clic en "Continue Shopping" | Debería mostrar "Remove" en "Sauce Labs Backpack" y "Sauce Labs Onesie", y "Add to cart" en "Sauce Labs Bike Light" | ✅ Backpack y Onesie muestran "Remove"; Bike Light muestra "Add to cart" | N/A |
| TC-CART-007 | Abrir el carrito vacío | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Carrito vacío (icono sin número) | 1. Hacer clic en el icono del carrito | Debería navegar a `/cart.html` sin ningún producto listado | ✅ Navega a `/cart.html` sin productos | N/A |
| TC-CART-019 | Checkout con el carrito vacío | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Carrito vacío (icono sin número)<br>3. Estar en `/cart.html` | 1. Hacer clic en "Checkout" | A confirmar | 🔍 Navega a `/checkout-step-one.html` ("Checkout: Your Information") sin mensaje de error | Comportamiento actual: permite iniciar el checkout sin productos. Posible defecto si hay requisito que lo impida |
| TC-CART-014 | Cabecera de la página del carrito | 🟢 Baja | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. "Sauce Labs Backpack", "Sauce Labs Bike Light" y "Sauce Labs Onesie" añadidos desde el listado | 1. Hacer clic en el icono del carrito | Debería mostrar el título "Your Cart" y las columnas "QTY" y "Description" | ✅ Muestra "Your Cart", "QTY" y "Description" | N/A |
| TC-CART-018 | Mensaje de carrito vacío | 🟢 Baja | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. Carrito vacío (icono sin número) | ↳ igual que TC-CART-007 | A confirmar | 🔍 No aparece ningún mensaje; solo se ven las columnas "QTY" y "Description" y los botones "Continue Shopping" y "Checkout" | Comportamiento actual: sin mensaje de carrito vacío |

## Persistencia del carrito

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CART-008 | Carrito tras recargar la página | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. "Sauce Labs Backpack" y "Sauce Labs Onesie" en el carrito (icono en `2`) | 1. Recargar la página (F5) | Debería mostrar `2` en el icono del carrito y "Remove" en "Sauce Labs Backpack" y "Sauce Labs Onesie" | ✅ Tras recargar, el icono muestra `2` y ambos productos muestran "Remove" | Esperado tomado como comportamiento evidente (perder el carrito al recargar sería pérdida de datos); confirmar con el PO. Al terminar, vaciar el carrito |
| TC-CART-020 | Carrito tras cerrar sesión y volver a entrar | 🟡 Media | 1. Sesión iniciada con `standard_user`<br>2. Estar en `/inventory.html`<br>3. "Sauce Labs Backpack" y "Sauce Labs Onesie" en el carrito (icono en `2`) | 1. Hacer clic en "Open Menu"<br>2. Hacer clic en "Logout"<br>3. Escribir `standard_user` en "Username"<br>4. Escribir `secret_sauce` en "Password"<br>5. Hacer clic en "Login" | A confirmar | 🔍 Tras cerrar sesión vuelve a `/`; al entrar de nuevo el icono muestra `2` y ambos productos siguen con "Remove" | Comportamiento actual: el carrito se conserva tras cerrar sesión. Al terminar, vaciar el carrito |

## Resumen

- **Total:** 20 casos. 🔴 6 · 🟡 11 · 🟢 3.
- **Estados:** ✅ 16 · ❌ 0 · 🔍 4 · ⏸ 0 · sin ejecutar 0.
- Ejecutados el 14/10/2026 en www.saucedemo.com con `standard_user`.

## Orden de ejecución sugerido

1. 🔴 TC-CART-001, TC-CART-009, TC-CART-002, TC-CART-003, TC-CART-005, TC-CART-016
2. 🟡 TC-CART-010, TC-CART-011, TC-CART-004, TC-CART-012, TC-CART-015, TC-CART-006, TC-CART-017, TC-CART-007, TC-CART-019, TC-CART-008, TC-CART-020
3. 🟢 TC-CART-013, TC-CART-014, TC-CART-018

## Preguntas para el PO

- TC-CART-013: al quitar el último producto, ¿el icono debe quedar sin número o mostrar `0`?
- TC-CART-018: ¿el carrito vacío debe mostrar algún mensaje?
- TC-CART-019: ¿se debe impedir iniciar el checkout con el carrito vacío?
- TC-CART-020: ¿el carrito debe conservarse tras cerrar sesión? ¿Y entre usuarios distintos o en otro navegador?
- TC-CART-008: confirmar que el carrito debe conservarse al recargar.
- ¿Cuál es el método oficial para vaciar el carrito entre ejecuciones?

## Notas de ejecución

- Los clics de la ejecución del 14/10/2026 se lanzaron por código sobre el elemento (`dispatchEvent('click')`), no como los haría una persona: el clic de ratón simulado por Playwright no llegaba a la página porque la ventana del navegador no estaba visible.
- La sesión de SauceDemo caduca a los 10 minutos (cookie `session-username`).
- Al cargar `/inventory.html` directamente, el servidor responde 404 aunque la página se ve igual.
