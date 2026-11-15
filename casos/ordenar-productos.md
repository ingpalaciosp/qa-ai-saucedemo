# Ordenar productos

Casos de prueba del desplegable de orden del listado de productos de SauceDemo (`/inventory.html`).

## Datos y estados de partida

- URL: `https://www.saucedemo.com` · Usuario: `standard_user` (contraseña en `.env`)
- Datos válidos de referencia: N/A (no hay campos para escribir; solo se elige una opción del desplegable)
- Opciones del desplegable: "Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"
- Productos del listado (6): "Sauce Labs Backpack" ($29.99), "Sauce Labs Bike Light" ($9.99), "Sauce Labs Bolt T-Shirt" ($15.99), "Sauce Labs Fleece Jacket" ($49.99), "Sauce Labs Onesie" ($7.99), "Test.allTheThings() T-Shirt (Red)" ($15.99)
- **Sesión cerrada**: estar en la página de login (`/`) sin sesión iniciada.
- **Listado sin ordenar**: sesión iniciada con `standard_user`, estar en `/inventory.html` y no haber cambiado la opción del desplegable.
- **Listado Z-A**: Listado sin ordenar y después seleccionar "Name (Z to A)" en el desplegable de orden.
- Limpieza: N/A (el orden elegido no se guarda; la página no guarda nada del orden en el navegador)

## Desplegable de orden

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-SORT-001 | Ordenar por nombre de la Z a la A | 🟡 Media | Listado sin ordenar | 1. Seleccionar "Name (Z to A)" en el desplegable de orden | Debería mostrar los 6 productos ordenados por nombre de la Z a la A: primero "Test.allTheThings() T-Shirt (Red)" y último "Sauce Labs Backpack" | ✅ Primero "Test.allTheThings() T-Shirt (Red)" y último "Sauce Labs Backpack"; los 6 en orden de la Z a la A | Req: texto de la opción "Name (Z to A)"<br>Automatizado: tests/test_ordenar_productos.py |
| TC-SORT-002 | Ordenar por precio de menor a mayor | 🟡 Media | Listado sin ordenar | 1. Seleccionar "Price (low to high)" en el desplegable de orden | Debería mostrar los 6 productos con cada precio igual o mayor que el anterior: primero "Sauce Labs Onesie" ("$7.99") y último "Sauce Labs Fleece Jacket" ("$49.99") | ✅ Primero "Sauce Labs Onesie" ("$7.99") y último "Sauce Labs Fleece Jacket" ("$49.99"); cada precio es igual o mayor que el anterior | Req: texto de la opción "Price (low to high)"<br>Automatizado: tests/test_ordenar_productos.py |
| TC-SORT-003 | Ordenar por precio de mayor a menor | 🟡 Media | Listado sin ordenar | 1. Seleccionar "Price (high to low)" en el desplegable de orden | Debería mostrar los 6 productos con cada precio igual o menor que el anterior: primero "Sauce Labs Fleece Jacket" ("$49.99") y último "Sauce Labs Onesie" ("$7.99") | ✅ Primero "Sauce Labs Fleece Jacket" ("$49.99") y último "Sauce Labs Onesie" ("$7.99"); cada precio es igual o menor que el anterior | Req: texto de la opción "Price (high to low)"<br>Automatizado: tests/test_ordenar_productos.py |
| TC-SORT-004 | Volver a ordenar por nombre de la A a la Z | 🟡 Media | Listado Z-A | 1. Seleccionar "Name (A to Z)" en el desplegable de orden | Debería mostrar los 6 productos ordenados por nombre de la A a la Z: primero "Sauce Labs Backpack" y último "Test.allTheThings() T-Shirt (Red)" | ✅ Primero "Sauce Labs Backpack" y último "Test.allTheThings() T-Shirt (Red)"; los 6 en orden de la A a la Z | Req: texto de la opción "Name (A to Z)"<br>Parte de Listado Z-A porque al entrar ya sale "Name (A to Z)": seleccionarla desde el inicio no cambiaría nada y el caso pasaría siempre<br>Automatizado: tests/test_ordenar_productos.py |
| TC-SORT-005 | Orden del listado al entrar | 🟢 Baja | Sesión cerrada | 1. Escribir `standard_user` en "Username"<br>2. Escribir la contraseña en "Password"<br>3. Hacer clic en "Login" | Debería mostrar los productos en el orden que indica la opción visible en el desplegable. Qué opción sale por defecto: A confirmar | ✅ El desplegable muestra "Name (A to Z)" y la lista está en ese orden (primero "Sauce Labs Backpack") | Comportamiento actual: el desplegable muestra "Name (A to Z)" y el primer producto es "Sauce Labs Backpack"<br>A confirmar: ¿qué orden debe salir por defecto? |
| TC-SORT-006 | Empate de precio al ordenar de menor a mayor | 🟢 Baja | Listado sin ordenar | 1. Seleccionar "Price (low to high)" en el desplegable de orden | A confirmar | 🔍 Sale "Sauce Labs Bolt T-Shirt" antes que "Test.allTheThings() T-Shirt (Red)", los dos a "$15.99" | Comportamiento actual: "Sauce Labs Bolt T-Shirt" y "Test.allTheThings() T-Shirt (Red)" cuestan los dos "$15.99" y sale primero "Sauce Labs Bolt T-Shirt"<br>A confirmar: ¿en qué orden deben salir dos productos con el mismo precio? |
| TC-SORT-007 | Empate de precio al ordenar de mayor a menor | 🟢 Baja | Listado sin ordenar | 1. Seleccionar "Price (high to low)" en el desplegable de orden | A confirmar | 🔍 Sale "Sauce Labs Bolt T-Shirt" antes que "Test.allTheThings() T-Shirt (Red)", los dos a "$15.99" | Comportamiento actual: sale primero "Sauce Labs Bolt T-Shirt" y después "Test.allTheThings() T-Shirt (Red)", igual que en TC-SORT-006 (el empate no se invierte al cambiar de dirección)<br>A confirmar: ¿en qué orden deben salir dos productos con el mismo precio? |

## Mantener el orden al navegar

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-SORT-008 | Orden tras recargar la página | 🟢 Baja | Listado sin ordenar | 1. Seleccionar "Price (high to low)" en el desplegable de orden<br>2. Pulsar F5 en el navegador | A confirmar | 🔍 Vuelve a "Name (A to Z)" y el primer producto es "Sauce Labs Backpack" | Comportamiento actual: vuelve a "Name (A to Z)" y el primer producto es "Sauce Labs Backpack"<br>A confirmar: ¿debe mantenerse el orden elegido? |
| TC-SORT-009 | Orden tras ir al carrito y volver | 🟢 Baja | Listado sin ordenar | 1. Seleccionar "Price (high to low)" en el desplegable de orden<br>2. Hacer clic en el icono del carrito<br>3. Hacer clic en "Continue Shopping" | A confirmar | 🔍 Vuelve a "Name (A to Z)" y el primer producto es "Sauce Labs Backpack" | Comportamiento actual: vuelve a "Name (A to Z)" y el primer producto es "Sauce Labs Backpack"<br>A confirmar: ¿debe mantenerse el orden elegido? |

## Resumen

Total: 9 casos · 🔴 0 · 🟡 4 · 🟢 5 · ✅ 5 · ❌ 0 · 🔍 4 · ⏸ 0 · sin ejecutar 0 · A confirmar 5 (TC-SORT-005 solo en parte)

## Orden de ejecución sugerido

1. 🟡 TC-SORT-001, 002, 003, 004
2. 🟢 TC-SORT-005, 006, 007, 008, 009

## Preguntas para el PO

1. ¿Qué orden debe salir por defecto al entrar al listado de productos? (TC-SORT-005)
2. Cuando dos productos tienen el mismo precio, ¿en qué orden deben salir? Hoy "Sauce Labs Bolt T-Shirt" sale antes que "Test.allTheThings() T-Shirt (Red)" en las dos direcciones. (TC-SORT-006, 007)
3. ¿El orden elegido debe mantenerse al recargar la página o al volver del carrito? (TC-SORT-008, 009)

## Fuera de alcance

- Otros usuarios (`problem_user`, `error_user`…): estos casos usan solo `standard_user`.
- Nombres y descripciones de los productos: no son parte del orden.
- Navegadores distintos de Chrome, versión móvil y uso con teclado: no hay requisitos.

## Registro de ejecuciones

| Fecha | Entorno | Navegador | Usuario | Quién | Casos | Observaciones |
|---|---|---|---|---|---|---|
| 12/11/2026 | www.saucedemo.com | Chrome | `standard_user` | Alicia | TC-SORT-001, 002, 003, 005, 006, 007, 008, 009 | Observación a mano antes de escribir los casos (fase de exploración). TC-SORT-004 no se ejecutó a mano |
| 12/11/2026 | www.saucedemo.com | Chromium (Playwright) | `standard_user` | Claude | TC-SORT-001 a 009 | Ejecutado con un script temporal de Playwright, cada caso con un navegador nuevo. La opción se eligió con `select_option` por código, no con un clic de persona en el desplegable |
