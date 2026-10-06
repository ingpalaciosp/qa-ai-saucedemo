# Casos de prueba – Login SauceDemo (v2, con contexto)

URL: https://www.saucedemo.com

| # | Caso | Resultado esperado | Resultado real | ¿Coincide? |
|---|------|--------------------|----------------|------------|
| 1 | Login con usuario válido: Username `standard_user`, Password `secret_sauce`, clic en Login | Redirige a `/inventory.html` | Igual que lo esperado | ✅ Sí |
| 2 | Login con usuario bloqueado: Username `locked_out_user`, Password `secret_sauce`, clic en Login | Se muestra "Epic sadface: Sorry, this user has been locked out." y no redirige | Igual que lo esperado | ✅ Sí |
| 3 | Login con `problem_user`: Username `problem_user`, Password `secret_sauce`, clic en Login | Redirige a `/inventory.html` | Redirige a `/inventory.html`. Observación: los 6 productos muestran la misma imagen de un perro en lugar de la foto de cada producto. | ✅ Sí (login). ⚠️ Bug encontrado: [issue #1](https://github.com/ingpalaciosp/qa-ai-saucedemo/issues/1) |
| 4 | Username vacío: Password `secret_sauce`, clic en Login | Se muestra "Epic sadface: Username is required" | Igual que lo esperado | ✅ Sí |
| 5 | Password vacío: Username `standard_user`, clic en Login | Se muestra "Epic sadface: Password is required" | Igual que lo esperado | ✅ Sí |
| 6 | Contraseña incorrecta: Username `standard_user`, Password `clave_incorrecta`, clic en Login | Se muestra "Epic sadface: Username and password do not match any user in this service" | Igual que lo esperado | ✅ Sí |
| 7 | Usuario inexistente: Username `usuario_inexistente`, Password `secret_sauce`, clic en Login | Se muestra "Epic sadface: Username and password do not match any user in this service" | Igual que lo esperado | ✅ Sí |
| 8 | Ambos campos vacíos: clic en Login sin completar Username ni Password | A confirmar (la IA no lo sabía) | Epic sadface: Username is required | 🔍 Completado por observación |

> Validado manualmente en www.saucedemo.com el 05/10/2026
