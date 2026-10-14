---
name: casos-de-prueba
description: Plantilla única de Alicia para diseñar, escribir o revisar casos de prueba en cualquier proyecto. Úsala siempre que pidan casos de prueba, test cases, una matriz de pruebas o validar casos.
---

# Casos de prueba: plantilla única

## Estructura del documento
- `#` Funcionalidad. Ejemplo: `# Login`
- `##` Pantalla o sección. Ejemplo: `## Formulario de login`
- Debajo de cada sección, una tabla con estas columnas:

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|

## Qué va en cada columna
- **Id**: formato `TC-<MÓDULO>-<NNN>`. El módulo va en mayúsculas, en una palabra corta (LOGIN, CART, CHECKOUT). El número tiene 3 cifras. Un ID nunca cambia ni se reutiliza: si un caso deja de servir, se marca "Obsoleto" en Notas.
- **Caso**: nombre corto que diga qué se prueba.
- **Prioridad**: 🔴 Alta, 🟡 Media o 🟢 Baja, siempre con su círculo de color, según los criterios de abajo.
- **Precondiciones**: estado inicial necesario (usuario, datos, página). Escribe "—" si no aplica.
- **Procedimiento**: la acción concreta que se realiza.
- **Esperado**: empieza por "Debería…". Debe poder comprobarse mirando: textos exactos entre comillas, URL, números, endpoints y método HTTP si aplica.
- **Obtenido**: vacío al escribir el caso. Al ejecutarlo, empieza con un símbolo y describe en presente lo observado: "✅ Redirige a la página principal".
- **Notas**: bug relacionado (issue #N), dudas, "Comportamiento actual: …", "A confirmar" u "Obsoleto". Escribe "—" si no hay nada.

Si un mismo procedimiento tiene varios resultados esperados, cada uno va en su propia fila con su propio Id, y en Procedimiento se escribe "↳ igual que <Id>".

## Criterios de prioridad
- 🔴 **Alta**: camino principal del negocio, dinero o cálculos, seguridad o pérdida de datos. Si falla, el usuario no puede hacer lo importante. Forman el smoke test y se ejecutan primero.
- 🟡 **Media**: validaciones, mensajes de error y funciones secundarias que tienen alternativa.
- 🟢 **Baja**: detalles visuales, textos y casos de borde poco probables.

## Orden de las filas
- Dentro de cada sección, las filas van ordenadas por prioridad: primero 🔴 Alta, después 🟡 Media y al final 🟢 Baja.
- En un archivo nuevo, numera los IDs siguiendo ese orden.
- Si el archivo ya existe, los casos nuevos reciben el siguiente número libre del módulo y se colocan en el bloque de su prioridad. Nunca renumeres los existentes.

## Símbolos para Obtenido
- ✅ Coincide con lo esperado
- ❌ No coincide (describir exactamente qué pasó)
- 🔍 Era "A confirmar" y se completó observando la aplicación
- ⏸ Bloqueado (no se pudo ejecutar; explicar por qué)

## Reglas
1. Si puedes ver la aplicación (navegador u otra herramienta), explórala antes de escribir. Usa solo textos, valores y comportamientos que hayas visto; nunca inventes.
2. Si no hay requisito que diga cómo debe comportarse algo, NO escribas lo observado como Esperado. Escribe en Esperado "A confirmar" y en Notas "Comportamiento actual: <lo que observaste>". Lo observado solo es Esperado cuando coincide con un requisito o con un comportamiento evidente (por ejemplo, un mensaje de error de campo obligatorio).
3. Prohibido en Esperado: "funciona correctamente", "se actualiza bien" o similares.
4. En casos negativos, incluye también lo que NO debe pasar (por ejemplo: "Debería seguir en la página de login").
5. Cada caso debe poder ejecutarse partiendo de sus precondiciones, sin depender de otro caso.
6. Mezcla casos positivos, negativos y de borde.
7. Si el archivo ya existe, conserva todos los IDs existentes.
8. Si alguna acción no se pudo hacer como lo haría una persona (por ejemplo, clics lanzados por código), indícalo al final del archivo.
9. Guarda el archivo en `casos/<funcionalidad>.md` del proyecto, salvo que te indiquen otra ruta. No modifiques otros archivos.

## Ejemplo
Ejemplo ilustrativo del formato: no copies sus textos, URL ni datos. Usa siempre los del proyecto real.

# Login

## Formulario de login

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-LOGIN-001 | Login con credenciales válidas | 🔴 Alta | Usuario registrado y activo. Estar en la página de login | Escribir usuario y contraseña válidos y click en el botón de iniciar sesión | Debería redirigir a la página principal | | — |
| TC-LOGIN-002 | Usuario visible tras el login | 🟡 Media | Usuario registrado y activo. Estar en la página de login | ↳ igual que TC-LOGIN-001 | Debería mostrar el nombre del usuario en la cabecera | | — |
| TC-LOGIN-003 | Contraseña incorrecta | 🟡 Media | Usuario registrado y activo. Estar en la página de login | Escribir el usuario y una contraseña incorrecta y hacer click en el botón de iniciar sesión | Debería mostrar un mensaje de error de credenciales y seguir en la página de login | | A confirmar: texto exacto del mensaje |
| TC-LOGIN-004 | Espacios alrededor del usuario | 🟢 Baja | Estar en la página de login | Escribir el usuario con espacios delante y detrás, y la contraseña correcta | A confirmar | | Comportamiento actual: rechaza el login con error de credenciales |

## Cierre de sesión

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-LOGIN-005 | Cerrar sesión | 🔴 Alta | Sesión iniciada | Hacer click en la opción de cerrar sesión | Debería redirigir a la página de login | | — |

## Al final del archivo
1. **Resumen**: total de casos, cuántos hay de cada prioridad (🔴 🟡 🟢) y de cada estado (✅ ❌ 🔍 ⏸ sin ejecutar).
2. **Orden de ejecución sugerido**: lista de IDs, primero todos los 🔴, luego los 🟡 y al final los 🟢.
3. **Preguntas para el PO**: todo lo que quedó "A confirmar".