"""Datos de prueba de SauceDemo: usuarios, contraseña y mensajes de error."""

import os

# La contraseña se lee de la variable de entorno SAUCE_PASSWORD.
# Si no existe, se usa la contraseña pública de SauceDemo.
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
PASSWORD_INCORRECTA = "clave_incorrecta"

USUARIO_ESTANDAR = "standard_user"
USUARIO_BLOQUEADO = "locked_out_user"
USUARIO_PROBLEMA = "problem_user"
USUARIO_INEXISTENTE = "usuario_inexistente"

ERROR_USUARIO_BLOQUEADO = "Epic sadface: Sorry, this user has been locked out."
ERROR_USUARIO_REQUERIDO = "Epic sadface: Username is required"
ERROR_PASSWORD_REQUERIDO = "Epic sadface: Password is required"
ERROR_CREDENCIALES_INVALIDAS = "Epic sadface: Username and password do not match any user in this service"
