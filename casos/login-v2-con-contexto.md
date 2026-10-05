# Casos de prueba – Login SauceDemo (v2, con contexto)

URL: https://www.saucedemo.com

| # | Caso | Resultado esperado | Resultado real | ¿Coincide? |
|---|------|--------------------|----------------|------------|
| 1 | Login con usuario válido: Username `standard_user`, Password `secret_sauce`, clic en Login | Redirige a `/inventory.html` | | |
| 2 | Login con usuario bloqueado: Username `locked_out_user`, Password `secret_sauce`, clic en Login | Se muestra "Epic sadface: Sorry, this user has been locked out." y no redirige | | |
| 3 | Login con `problem_user`: Username `problem_user`, Password `secret_sauce`, clic en Login | Redirige a `/inventory.html` | | |
| 4 | Username vacío: Password `secret_sauce`, clic en Login | Se muestra "Epic sadface: Username is required" | | |
| 5 | Password vacío: Username `standard_user`, clic en Login | Se muestra "Epic sadface: Password is required" | | |
| 6 | Contraseña incorrecta: Username `standard_user`, Password `clave_incorrecta`, clic en Login | Se muestra "Epic sadface: Username and password do not match any user in this service" | | |
| 7 | Usuario inexistente: Username `usuario_inexistente`, Password `secret_sauce`, clic en Login | Se muestra "Epic sadface: Username and password do not match any user in this service" | | |
| 8 | Ambos campos vacíos: clic en Login sin completar Username ni Password | Epic sadface: Username is required | | |
