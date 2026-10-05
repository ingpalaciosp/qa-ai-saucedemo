# Revisión de casos de login generados por IA — saucedemo.com

| # | Caso | Esperado según IA | Resultado real | ¿Acertó? | Corrección |
|---|---|---|---|---|---|
| 1 | `standard_user` / `secret_sauce` | Entra a la página de productos (`/inventory.html`) | Igual que lo esperado | ✅ Sí | — |
| 2 | Usuario y contraseña vacíos | "Epic sadface: Username is required" | Igual que lo esperado | ✅ Sí | — |
| 3 | `standard_user` / contraseña vacía | "Epic sadface: Password is required" | Igual que lo esperado | ✅ Sí | — |
| 4 | `standard_user` / `abc123` | "Epic sadface: Username and password do not match any user in this service" | Igual que lo esperado | ✅ Sí | — |
| 5 | `usuario_falso` / `secret_sauce` | Mismo error que el caso 4 (no revela si falla el usuario o la contraseña) | Igual que lo esperado | ✅ Sí | — |
| 6 | `locked_out_user` / `secret_sauce` | "Epic sadface: Sorry, this user has been locked out." | Igual que lo esperado | ✅ Sí | — |
| 7 | `Standard_User` / `secret_sauce` | No entra; error "el usuario distingue mayúsculas" | No entra; error "Epic sadface: Username and password do not match any user in this service" | ❌ No | La IA inventó el texto del mensaje. Usar el texto real en el assert |
| 8 | Abrir `/inventory.html` sin sesión | Vuelve al login con "Epic sadface: You can only access '/inventory.html' when you are logged in." | Igual que lo esperado | ✅ Sí | — |

## Resumen

- **Casos generados por IA:** 8
- **Correctos:** 7 (87,5%)
- **Error encontrado:** la IA inventó el texto del mensaje de error.

### Lecciones
1. La IA no conoce lo que no ha visto.
2. Siempre validar contra la app real.
3. Comparar palabra por palabra para evitar falsos positivos.
