# Checkout

URL: https://www.saucedemo.com

Usuario: `standard_user` / `secret_sauce`

Datos de comprador usados en los casos: First Name `Alicia`, Last Name `Palacios`, Zip/Postal Code `28001`.

Estados de partida a los que remiten las precondiciones:

- **Carrito A**: sesión iniciada y carrito con solo "Sauce Labs Backpack" (`$29.99`) y "Sauce Labs Bike Light" (`$9.99`); el icono del carrito muestra `2`.
- **Carrito B**: sesión iniciada y carrito con solo "Sauce Labs Onesie" (`$7.99`); el icono del carrito muestra `1`.
- **Carrito vacío**: sesión iniciada y ningún producto en el carrito; el icono no muestra número.

El carrito no se vacía al cerrar sesión, así que hay que quitar a mano lo que haya quedado de una ejecución anterior.

## Acceso al checkout

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CHECKOUT-001 | Entrar al checkout con productos | 🔴 Alta | Carrito A. Estar en "/cart.html" | Click "Checkout" | Debería redirigir a "/checkout-step-one.html" y mostrar el título "Checkout: Your Information" | | N/A |
| TC-CHECKOUT-002 | Entrar al checkout con el carrito vacío | 🔴 Alta | Carrito vacío. Estar en "/cart.html" | Click "Checkout" | Debería mostrar el botón Checkout deshabilitado. No debería redirigir a /checkout-step-one.html | | Criterio QA, validar con PO. Comportamiento actual: el botón está habilitado y redirige sin mensaje. Relacionado con TC-CHECKOUT-030 |

## Paso 1: Your Information

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CHECKOUT-004 | Continuar con datos válidos | 🔴 Alta | Carrito A. Estar en "/checkout-step-one.html" | Escribir `Alicia`, `Palacios` y `28001` y click "Continue" | Debería redirigir a "/checkout-step-two.html" y mostrar el título "Checkout: Overview" | | N/A |
| TC-CHECKOUT-005 | Continuar con todo vacío | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" con los tres campos vacíos | Click "Continue" | Debería mostrar a la vez los mensajes "Error: First Name is required", "Error: Last Name is required" y "Error: Postal Code is required", y seguir en "/checkout-step-one.html", sin pasar a "/checkout-step-two.html" | | Criterio QA, validar con PO. Comportamiento actual: solo muestra "Error: First Name is required"; los errores aparecen de uno en uno. |
| TC-CHECKOUT-007 | Falta First Name | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | Dejar First Name vacío, escribir `Palacios` y `28001` y click "Continue" | Debería mostrar "Error: First Name is required" y seguir en "/checkout-step-one.html" con `Palacios` y `28001` aún escritos | | N/A |
| TC-CHECKOUT-008 | Falta Last Name | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | Escribir `Alicia`, dejar Last Name vacío, escribir `28001` y click "Continue" | Debería mostrar "Error: Last Name is required" y seguir en "/checkout-step-one.html" con `Alicia` y `28001` aún escritos | | N/A |
| TC-CHECKOUT-009 | Falta Zip/Postal Code | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | Escribir `Alicia` y `Palacios`, dejar Zip/Postal Code vacío y click "Continue" | Debería mostrar "Error: Postal Code is required" y seguir en "/checkout-step-one.html" con `Alicia` y `Palacios` aún escritos | | N/A |
| TC-CHECKOUT-012 | Solo espacios en los tres campos | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | Escribir un espacio en cada campo y click "Continue" | A confirmar | | Comportamiento actual: redirige a "/checkout-step-two.html" sin mostrar error. A confirmar: ¿los espacios deben contar como campo vacío? |
| TC-CHECKOUT-013 | Zip con letras y símbolos | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | Escribir `Alicia`, `Palacios` y `abc!@#` y click "Continue" | A confirmar | | Comportamiento actual: redirige a "/checkout-step-two.html" sin mostrar error. A confirmar: ¿qué formato debe tener el código postal? |
| TC-CHECKOUT-015 | Texto muy largo y con etiquetas HTML | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | Escribir `<b>1</b>` en First Name, 300 veces la letra `x` en Last Name y `1` en Zip/Postal Code y click "Continue" | A confirmar | | Comportamiento actual: redirige a "/checkout-step-two.html" sin mostrar error ni ejecutar el HTML escrito; los campos no tienen longitud máxima. A confirmar: ¿cuáles son las longitudes mínima y máxima? |
| TC-CHECKOUT-016 | Cancel en el paso 1 | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | Click "Cancel" | Debería redirigir a "/cart.html" con "Sauce Labs Backpack" y "Sauce Labs Bike Light" en la lista y el icono del carrito con `2` | | N/A |
| TC-CHECKOUT-003 | Elementos del formulario | 🟢 Baja | Carrito A. Estar en "/cart.html" | Click "Checkout" | Debería mostrar tres campos vacíos con los textos de ayuda "First Name", "Last Name" y "Zip/Postal Code", los botones "Cancel" y "Continue", y el icono del carrito con `2` | | N/A |
| TC-CHECKOUT-006 | Campos marcados al fallar la validación | 🟢 Baja | Carrito A. Estar en "/checkout-step-one.html" con los tres campos vacíos | ↳ igual que TC-CHECKOUT-005 | A confirmar | | Comportamiento actual: marca en error los tres campos, cada uno con su icono de error; se marcan los tres aunque falte solo uno. A confirmar: ¿debe marcarse solo el campo que falta? |
| TC-CHECKOUT-010 | Orden de validación con varios campos vacíos | 🟢 Baja | Carrito A. Estar en "/checkout-step-one.html" | Escribir solo `28001` en Zip/Postal Code y click "Continue" | A confirmar | | Comportamiento actual: muestra únicamente "Error: First Name is required" (no el de Last Name) y sigue en "/checkout-step-one.html". A confirmar: con varios campos vacíos, ¿debe avisarse solo del primero o de todos? |
| TC-CHECKOUT-011 | Cerrar el mensaje de error | 🟢 Baja | Carrito A. Estar en "/checkout-step-one.html" con el mensaje "Error: First Name is required" visible y `Palacios` y `28001` escritos | Click en la ✕ del mensaje de error | Debería desaparecer el mensaje y las marcas de error de los tres campos, conservar `Palacios` y `28001` y seguir en "/checkout-step-one.html" | | N/A |
| TC-CHECKOUT-014 | Nombre y apellido numéricos | 🟢 Baja | Carrito A. Estar en "/checkout-step-one.html" | Escribir `123`, `456` y `28001` y click "Continue" | A confirmar | | Comportamiento actual: redirige a "/checkout-step-two.html" sin mostrar error. A confirmar: ¿qué caracteres se admiten en nombre y apellido? |
| TC-CHECKOUT-017 | Volver atrás desde el paso 2 | 🟢 Baja | Carrito A. Estar en "/checkout-step-two.html" tras rellenar `Alicia`, `Palacios` y `28001` | Pulsar "Atrás" en el navegador | A confirmar | | Comportamiento actual: vuelve a "/checkout-step-one.html" con los tres campos vacíos y sin mensaje de error. A confirmar: ¿deben conservarse los datos ya escritos? |

## Paso 2: Overview

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CHECKOUT-018 | Productos del resumen | 🔴 Alta | Carrito A. Estar en "/checkout-step-one.html" | Escribir `Alicia`, `Palacios` y `28001` y click "Continue" | Debería mostrar las columnas "QTY" y "Description" y dos productos con QTY `1`: "Sauce Labs Backpack" `$29.99` y "Sauce Labs Bike Light" `$9.99`, ninguno con botón "Remove" | | N/A |
| TC-CHECKOUT-020 | Totales con dos productos | 🔴 Alta | Carrito A. Estar en "/checkout-step-one.html" | ↳ igual que TC-CHECKOUT-018 | Debería mostrar "Price Total" e "Item total: $39.98" (suma de `$29.99` y `$9.99`). Tax y Total: A confirmar | | Comportamiento actual: muestra "Tax: $3.20" y "Total: $43.18"; equivale a un 8 % redondeado a dos decimales. A confirmar: regla del impuesto y de su redondeo |
| TC-CHECKOUT-021 | Totales con un producto | 🔴 Alta | Carrito B. Estar en "/checkout-step-one.html" | Escribir `Alicia`, `Palacios` y `28001` y click "Continue" | Debería mostrar un solo producto, "Sauce Labs Onesie" `$7.99` con QTY `1`, e "Item total: $7.99". Tax y Total: A confirmar | | Comportamiento actual: muestra "Tax: $0.64" y "Total: $8.63". A confirmar: regla del impuesto (ver TC-CHECKOUT-020) |
| TC-CHECKOUT-024 | Finalizar el pedido | 🔴 Alta | Carrito A. Estar en "/checkout-step-two.html" | Click "Finish" | Debería redirigir a "/checkout-complete.html" y mostrar el título "Checkout: Complete!" | | N/A |
| TC-CHECKOUT-019 | Información de pago y envío | 🟡 Media | Carrito A. Estar en "/checkout-step-one.html" | ↳ igual que TC-CHECKOUT-018 | Debería mostrar "Payment Information:" con "SauceCard #31337" y "Shipping Information:" con "Free Pony Express Delivery!" | | N/A |
| TC-CHECKOUT-023 | Cancel en el paso 2 | 🟡 Media | Carrito A. Estar en "/checkout-step-two.html" | Click "Cancel" | A confirmar | | Comportamiento actual: redirige a "/inventory.html" (no a "/cart.html") con el icono del carrito en `2` y los botones de "Sauce Labs Backpack" y "Sauce Labs Bike Light" en "Remove". A confirmar: ¿"Cancel" en el resumen debe llevar al inventario o al carrito, como en el paso 1? |
| TC-CHECKOUT-025 | Resumen con el carrito vacío | 🟡 Media | Carrito vacío. Estar en "/checkout-step-one.html" | Escribir `Alicia`, `Palacios` y `28001` y click "Continue" | A confirmar | | Comportamiento actual: redirige a "/checkout-step-two.html" sin productos listados y muestra "Item total: $0", "Tax: $0.00" y "Total: $0.00", con "Finish" habilitado. "Item total" sale como `$0` y no `$0.00`. A confirmar: ¿debe poder llegarse al resumen sin productos? |
| TC-CHECKOUT-022 | Enlace del nombre del producto | 🟢 Baja | Carrito A. Estar en "/checkout-step-two.html" | Click en el nombre "Sauce Labs Backpack" | Debería redirigir a "/inventory-item.html?id=4", mostrar "Sauce Labs Backpack" y el botón "Remove" | | N/A |

## Confirmación del pedido

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CHECKOUT-027 | El carrito se vacía al finalizar | 🔴 Alta | Carrito A. Estar en "/checkout-step-two.html" | ↳ igual que TC-CHECKOUT-024 | Debería quedar el icono del carrito sin número (no `0` ni `2`) | | N/A |
| TC-CHECKOUT-030 | Finalizar un pedido sin productos | 🔴 Alta | Carrito vacío. Estar en "/checkout-step-two.html" | Click "Finish" | A confirmar | | Comportamiento actual: redirige a "/checkout-complete.html" y muestra "Thank you for your order!". A confirmar: ¿debe poder confirmarse un pedido de `$0.00` sin productos? |
| TC-CHECKOUT-026 | Contenido de la confirmación | 🟡 Media | Carrito A. Estar en "/checkout-step-two.html" | ↳ igual que TC-CHECKOUT-024 | Debería mostrar "Thank you for your order!", el texto "Your order has been dispatched, and will arrive just as fast as the pony can get there!", la imagen "Pony Express" y los botones "Back Home" y "Generate PDF order" | | N/A |
| TC-CHECKOUT-028 | Back Home | 🟡 Media | Estar en "/checkout-complete.html" tras finalizar un pedido con el Carrito A | Click "Back Home" | Debería redirigir a "/inventory.html" con los seis productos en "Add to cart" y el icono del carrito sin número | | N/A |
| TC-CHECKOUT-029 | Generate PDF order | 🟡 Media | Estar en "/checkout-complete.html" tras finalizar un pedido con el Carrito A | Click "Generate PDF order" | A confirmar | | Comportamiento actual: sin observar, el botón no se exploró. A confirmar: si el PDF se descarga o se abre, el nombre del archivo y qué datos contiene |

## Acceso directo por URL

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-CHECKOUT-033 | Paso 1 sin sesión | 🔴 Alta | Sesión cerrada | Ingresar en la URL "/checkout-step-one.html" | Debería redirigir a "/" y mostrar "Epic sadface: You can only access '/checkout-step-one.html' when you are logged in.", sin mostrar el formulario | | N/A |
| TC-CHECKOUT-034 | Paso 2 sin sesión | 🔴 Alta | Sesión cerrada | Ingresar en la URL "/checkout-step-two.html" | Debería redirigir a "/" y mostrar "Epic sadface: You can only access '/checkout-step-two.html' when you are logged in.", sin mostrar el resumen | | N/A |
| TC-CHECKOUT-035 | Confirmación sin sesión | 🔴 Alta | Sesión cerrada | Ingresar en la URL "/checkout-complete.html" | Debería redirigir a "/" y mostrar "Epic sadface: You can only access '/checkout-complete.html' when you are logged in.", sin mostrar la confirmación | | N/A |
| TC-CHECKOUT-031 | Saltarse el paso 1 con sesión | 🟡 Media | Carrito B. No haber rellenado el paso 1 | Ingresar en la URL "/checkout-step-two.html" | A confirmar | | Comportamiento actual: muestra "Checkout: Overview" con "Sauce Labs Onesie" `$7.99` y "Total: $8.63", sin pedir los datos del comprador. A confirmar: ¿debe exigirse haber completado el paso 1? |
| TC-CHECKOUT-032 | Abrir la confirmación sin finalizar | 🟡 Media | Carrito B. No haber pulsado "Finish" | Ingresar en la URL "/checkout-complete.html" | A confirmar | | Comportamiento actual: muestra "Thank you for your order!" y el icono del carrito sigue en `1`. A confirmar: ¿debe poder verse la confirmación sin haber finalizado un pedido? |

## Resumen

Total: 35 casos.

| Prioridad | Casos |
|---|---|
| 🔴 Alta | 12 |
| 🟡 Media | 16 |
| 🟢 Baja | 7 |

| Estado | Casos |
|---|---|
| ✅ Coincide | 0 |
| ❌ No coincide | 0 |
| 🔍 Confirmado observando | 0 |
| ⏸ Bloqueado | 0 |
| Sin ejecutar | 35 |

15 casos tienen el Esperado "A confirmar": 13 por completo y 2 solo en el impuesto y el total (TC-CHECKOUT-020 y 021).

## Orden de ejecución sugerido

1. 🔴 **Alta (smoke test)**, siguiendo el flujo de compra: TC-CHECKOUT-001, 004, 018, 020, 024, 027, 021, 002, 030, 033, 034, 035.
2. 🟡 **Media**: TC-CHECKOUT-005, 007, 008, 009, 012, 013, 015, 016, 019, 023, 025, 026, 028, 029, 031, 032.
3. 🟢 **Baja**: TC-CHECKOUT-003, 006, 010, 011, 014, 017, 022.

## Preguntas para el PO

1. ¿Debe permitirse iniciar el checkout, llegar al resumen y confirmar un pedido con el carrito vacío? Hoy se puede completar un pedido de `$0.00`. (TC-CHECKOUT-002, 025, 030)
2. En el resumen con el carrito vacío, "Item total" sale como `$0` y los otros importes como `$0.00`. ¿Cuál es el formato correcto? (TC-CHECKOUT-025)
3. Cuando falta un campo, hoy se marcan en error los tres. ¿Debe marcarse solo el que falta? (TC-CHECKOUT-006)
4. Con varios campos vacíos, hoy solo se avisa del primero. ¿Debe avisarse de todos? (TC-CHECKOUT-010)
5. ¿Los campos con solo espacios deben tratarse como vacíos? Hoy se aceptan. (TC-CHECKOUT-012)
6. ¿Qué formato debe tener Zip/Postal Code? Hoy acepta letras y símbolos. (TC-CHECKOUT-013)
7. ¿Qué caracteres y qué longitudes mínima y máxima se admiten en First Name y Last Name? Hoy aceptan números, etiquetas HTML y 300 caracteres. (TC-CHECKOUT-014, 015)
8. Al volver atrás desde el resumen, ¿deben conservarse los datos del comprador? Hoy el formulario aparece vacío. (TC-CHECKOUT-017)
9. ¿Cuál es la regla del impuesto y de su redondeo? Lo observado equivale a un 8 %. (TC-CHECKOUT-020, 021)
10. "Cancel" en el resumen lleva hoy a "/inventory.html", mientras que en el paso 1 lleva a "/cart.html". ¿Es lo deseado? (TC-CHECKOUT-023)
11. ¿Qué debe hacer "Generate PDF order": descargar o abrir, con qué nombre de archivo y con qué datos? (TC-CHECKOUT-029)
12. ¿Debe poder abrirse "/checkout-step-two.html" sin haber rellenado el paso 1? (TC-CHECKOUT-031)
13. ¿Debe poder abrirse "/checkout-complete.html" sin haber finalizado un pedido? Hoy muestra el agradecimiento y el carrito no se vacía. (TC-CHECKOUT-032)
14. ¿El checkout debe comportarse igual con los demás usuarios de prueba (`problem_user`, `error_user`, `performance_glitch_user`, `visual_user`)? Solo se exploró `standard_user`.

> Explorado por el agente con el navegador en www.saucedemo.com el 11/10/2026 con `standard_user`. Los botones se pulsaron desde el DOM porque los clics de ratón del navegador automatizado no llegaban a la página; los campos se rellenaron por script. No se exploró el envío del formulario con la tecla Enter, el botón "Generate PDF order" ni otros usuarios. Pendiente de validación manual.
>
> Reescrito el 11/10/2026 con la versión actual de la plantilla, sin volver a explorar la web: prioridades con su círculo de color, filas de cada sección ordenadas por prioridad (🔴, 🟡, 🟢) sin renumerar los IDs, y esperados sin requisito en "A confirmar".
