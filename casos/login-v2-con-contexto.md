# Login

Casos de prueba del login de SauceDemo, versión 2 (con contexto). Lección 2 del portafolio.

URL: https://www.saucedemo.com · Contraseña de todos los usuarios: `secret_sauce`

## Formulario de login

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-LOGIN-001 | Login con usuario válido | 🔴 Alta | Estar en la página de login (`/`) | 1. Escribir `standard_user` en "Username"<br>2. Escribir `secret_sauce` en "Password"<br>3. Hacer clic en "Login" | Debería redirigir a `/inventory.html` | ✅ Redirige a `/inventory.html` | Automatizado: tests/test_login.py |
| TC-LOGIN-002 | Login con usuario bloqueado | 🔴 Alta | Estar en la página de login (`/`) | 1. Escribir `locked_out_user` en "Username"<br>2. Escribir `secret_sauce` en "Password"<br>3. Hacer clic en "Login" | Debería mostrar "Epic sadface: Sorry, this user has been locked out." y seguir en la página de login (`/`), sin redirigir a `/inventory.html` | ✅ Muestra "Epic sadface: Sorry, this user has been locked out." y no redirige | Automatizado: tests/test_login.py |
| TC-LOGIN-006 | Contraseña incorrecta | 🔴 Alta | Estar en la página de login (`/`) | 1. Escribir `standard_user` en "Username"<br>2. Escribir `clave_incorrecta` en "Password"<br>3. Hacer clic en "Login" | Debería mostrar "Epic sadface: Username and password do not match any user in this service" y seguir en la página de login (`/`) | ✅ Muestra "Epic sadface: Username and password do not match any user in this service" | Automatizado: tests/test_login.py |
| TC-LOGIN-007 | Usuario inexistente | 🔴 Alta | Estar en la página de login (`/`) | 1. Escribir `usuario_inexistente` en "Username"<br>2. Escribir `secret_sauce` en "Password"<br>3. Hacer clic en "Login" | Debería mostrar "Epic sadface: Username and password do not match any user in this service" y seguir en la página de login (`/`) | ✅ Muestra "Epic sadface: Username and password do not match any user in this service" | Automatizado: tests/test_login.py |
| TC-LOGIN-003 | Login con `problem_user` | 🟡 Media | Estar en la página de login (`/`) | 1. Escribir `problem_user` en "Username"<br>2. Escribir `secret_sauce` en "Password"<br>3. Hacer clic en "Login" | Debería redirigir a `/inventory.html` | ✅ Redirige a `/inventory.html` | Automatizado: tests/test_login.py |
| TC-LOGIN-004 | Username vacío | 🟡 Media | Estar en la página de login (`/`) | 1. Dejar "Username" vacío<br>2. Escribir `secret_sauce` en "Password"<br>3. Hacer clic en "Login" | Debería mostrar "Epic sadface: Username is required" y seguir en la página de login (`/`) | ✅ Muestra "Epic sadface: Username is required" | Automatizado: tests/test_login.py |
| TC-LOGIN-005 | Password vacío | 🟡 Media | Estar en la página de login (`/`) | 1. Escribir `standard_user` en "Username"<br>2. Dejar "Password" vacío<br>3. Hacer clic en "Login" | Debería mostrar "Epic sadface: Password is required" y seguir en la página de login (`/`) | ✅ Muestra "Epic sadface: Password is required" | Automatizado: tests/test_login.py |
| TC-LOGIN-009 | Imágenes de los productos con `problem_user` | 🟡 Media | Estar en la página de login (`/`) | ↳ igual que TC-LOGIN-003 | Debería mostrar la foto de cada producto en los 6 productos de `/inventory.html`, no la misma imagen en todos | ❌ Los 6 productos muestran la misma imagen de un perro en lugar de la foto de cada producto | Bug: [issue #1](https://github.com/ingpalaciosp/qa-ai-saucedemo/issues/1). Automatizado: tests/test_login.py (marcado como xfail hasta que se corrija el bug) |
| TC-LOGIN-008 | Ambos campos vacíos | 🟢 Baja | Estar en la página de login (`/`) | 1. Dejar "Username" y "Password" vacíos<br>2. Hacer clic en "Login" | Deberia mostrar "Epic sadface: Username is required |  Muestra "Epic sadface: Username is required" | Automatizado: tests/test_login.py (comprueba el comportamiento actual) |

## Resumen

- **Total:** 9 casos. 🔴 4 · 🟡 4 · 🟢 1.
- **Estados:** ✅ 7 · ❌ 1 · ⏸ 0 · sin ejecutar 0.

## Orden de ejecución sugerido

1. 🔴 TC-LOGIN-001, TC-LOGIN-002, TC-LOGIN-006, TC-LOGIN-007
2. 🟡 TC-LOGIN-003, TC-LOGIN-004, TC-LOGIN-005, TC-LOGIN-009
3. 🟢 TC-LOGIN-008

## Preguntas para el PO

- TC-LOGIN-008: con los dos campos vacíos, ¿es correcto mostrar solo "Epic sadface: Username is required"?

> Validado manualmente en www.saucedemo.com el 05/10/2026.
>
> Reescrito el 16/10/2026 con la plantilla de casos de prueba, sin volver a ejecutar a mano: se añadieron Ids conservando el número de cada caso (caso 1 → TC-LOGIN-001…), prioridades y orden por prioridad. La observación de las imágenes del antiguo caso 3 pasó a su propio caso, TC-LOGIN-009.
