---
name: casos-de-prueba
description: Plantilla y reglas de Alicia para diseñar, escribir, ampliar o revisar casos de prueba (test cases) en cualquier proyecto. Úsala siempre que se pidan casos de prueba, escenarios de prueba, una matriz de pruebas, un smoke test, casos para una historia de usuario o validar casos existentes, y antes de automatizar pruebas a partir de casos. Genera o actualiza casos/<funcionalidad>.md.
---

# Casos de prueba: plantilla única

Objetivo: que cualquier persona, o un script de automatización, pueda ejecutar cada caso sin preguntar nada y decidir si pasó o falló solo mirando la aplicación.

## Flujo de trabajo
1. Reúne las fuentes: requisitos, historia de usuario, criterios de aceptación, diseños o la propia aplicación. Si no hay ninguna fuente y no puedes ver la aplicación, pide al menos una antes de escribir.
2. Si puedes ver la aplicación (navegador u otra herramienta), explórala antes de escribir. Usa solo textos, valores y comportamientos que hayas visto o que estén en los requisitos; nunca inventes.
3. Si ya existe `casos/<funcionalidad>.md`, léelo completo. Para numerar casos nuevos, busca el número más alto de ese módulo en todos los archivos de `casos/`.
4. Elige los casos (ver "Cómo elegir los casos") y escríbelos con el formato de abajo.
5. Repasa la "Lista de comprobación final".
6. Guarda en `casos/<funcionalidad>.md`, salvo que te indiquen otra ruta. No modifiques otros archivos.

## Estructura del documento
- `#` Funcionalidad. Ejemplo: `# Login`
- `##` Pantalla o sección. Ejemplo: `## Formulario de login`
- Debajo de cada sección, una tabla con estas columnas:

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|

Importante: una celda de tabla Markdown no admite saltos de línea (la tabla se rompe). Cuando haya varios pasos, sepáralos con `<br>` dentro de la misma celda:
`1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Hacer clic en "Login"`

## Qué va en cada columna
- **Id**: formato `TC-<MÓDULO>-<NNN>`. Módulo en mayúsculas y en una palabra corta (LOGIN, CART, CHECKOUT); número de 3 cifras. Un Id nunca cambia ni se reutiliza: si un caso deja de servir, se marca "Obsoleto" en Notas y se deja en la tabla.
- **Caso**: nombre corto que diga qué se prueba.
- **Prioridad**: 🔴 Alta, 🟡 Media o 🟢 Baja, siempre con su círculo, según los criterios de abajo.
- **Precondiciones**: estado inicial necesario (usuario, datos, página de partida). Si son varias, enuméralas con `<br>`. Escribe "N/A" si no hay ninguna.
- **Procedimiento**: acciones concretas, una por paso, enumeradas con `<br>` si hay más de una. Nombra los botones y campos con su texto visible entre comillas.
- **Esperado**: siempre empieza por "Debería…" y se puede comprobar mirando: textos exactos entre comillas, URL, números, y endpoint y método HTTP si aplica. Ejemplo: `Debería mostrar "Pedido confirmado" y la URL debería ser /checkout-complete`.
- **Obtenido**: vacío al escribir el caso. Al ejecutarlo, empieza por el símbolo de estado y describe en presente lo observado: `✅ Redirige a la página principal`.
- **Notas**: bug relacionado (issue #N), dudas, "Comportamiento actual: …", "A confirmar", "Obsoleto" o el test automatizado que lo cubre. Escribe "N/A" si no hay nada.

Si un mismo procedimiento tiene varios resultados esperados, cada resultado va en su propia fila con su propio Id, y en Procedimiento se escribe "↳ igual que <Id>". Esa fila repite sus Precondiciones, para que siga pudiendo ejecutarse sola.

## Criterios de prioridad
- 🔴 **Alta**: camino principal del negocio, dinero o cálculos, seguridad o pérdida de datos. Si falla, el usuario no puede hacer lo importante. Forman el smoke test (la prueba rápida que se ejecuta primero para saber si vale la pena seguir probando).
- 🟡 **Media**: validaciones, mensajes de error y funciones secundarias que tienen alternativa.
- 🟢 **Baja**: detalles visuales, textos y casos de borde poco probables.

## Cómo elegir los casos
- Empieza por el camino feliz (el uso normal que sale bien) y después los caminos de error.
- Por cada campo de entrada: un valor válido, vacío, formato inválido y, si hay límites, los valores en el límite y justo por fuera (mínimo, máximo, mínimo − 1, máximo + 1).
- Por cada flujo: completar, cancelar o volver atrás, y repetir la acción (doble clic, recargar).
- Si dos casos comprobarían exactamente lo mismo, deja solo uno.
- Mezcla casos positivos, negativos y de borde.

## Orden de las filas y numeración
- Dentro de cada sección, las filas van por prioridad: primero 🔴, después 🟡 y al final 🟢.
- En un archivo nuevo, numera de arriba abajo, sección por sección, siguiendo ese orden.
- En un archivo que ya existe, los casos nuevos reciben el siguiente número libre del módulo y se colocan en el bloque de su prioridad. Nunca renumeres ni borres los existentes.

## Símbolos para Obtenido
- ✅ Coincide con lo esperado
- ❌ No coincide (describe exactamente qué pasó y enlaza el bug en Notas si existe)
- 🔍 Era "A confirmar" y se completó observando la aplicación
- ⏸ Bloqueado (no se pudo ejecutar; explica por qué)

## Reglas
1. Si no hay requisito que diga cómo debe comportarse algo, no escribas lo observado como Esperado: escribe "A confirmar" en Esperado y "Comportamiento actual: <lo observado>" en Notas. Lo observado solo pasa a Esperado si coincide con un requisito o con un comportamiento evidente (por ejemplo, el aviso de campo obligatorio). Así los casos no dan por bueno un posible bug.
2. Nunca escribas en Esperado frases que no se pueden comprobar, como "funciona correctamente" o "se actualiza bien".
3. En casos negativos, incluye también lo que no debe pasar (por ejemplo: "y debería seguir en la página de login").
4. Cada caso se ejecuta partiendo solo de sus precondiciones, sin depender de que otro caso se haya ejecutado antes.
5. Si alguna acción no se pudo hacer como la haría una persona (por ejemplo, clics lanzados por código), indícalo al final del archivo.

## Relación con la automatización
- Cuando un caso se automatice, el test debe llevar el Id en su nombre, por ejemplo `test_tc_login_001_login_valido`, para poder rastrear qué caso cubre cada test.
- Anota en Notas el archivo del test: `Automatizado: tests/test_login.py`.

## Al final del archivo de casos
1. **Resumen**: total de casos, cuántos de cada prioridad (🔴 🟡 🟢) y de cada estado (✅ ❌ 🔍 ⏸ sin ejecutar).
2. **Orden de ejecución sugerido**: lista de Ids, primero todos los 🔴, luego los 🟡 y al final los 🟢.
3. **Preguntas para el PO**: todo lo que quedó "A confirmar".

## Lista de comprobación final
- [ ] Cada Id sigue `TC-<MÓDULO>-<NNN>` y ninguno se repite ni cambió.
- [ ] Cada Esperado empieza por "Debería…" y se puede comprobar mirando.
- [ ] Ningún texto, URL o dato es inventado.
- [ ] Lo que no tiene requisito está como "A confirmar".
- [ ] Las filas de cada sección están ordenadas 🔴 → 🟡 → 🟢.
- [ ] Ninguna celda tiene saltos de línea reales (solo `<br>`).
- [ ] Las celdas vacías de Precondiciones y Notas dicen "N/A" (Obtenido queda vacío hasta ejecutar).
- [ ] Está el resumen final.

## Ejemplo
Ejemplo solo del formato: no copies sus textos, URL ni datos; usa siempre los del proyecto real.

# Login

## Formulario de login

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-LOGIN-001 | Login con credenciales válidas | 🔴 Alta | 1. Usuario registrado y activo<br>2. Estar en la página de login | 1. Escribir el usuario<br>2. Escribir la contraseña válida<br>3. Hacer clic en "Iniciar sesión" | Debería redirigir a la página principal (/inicio) | ✅ Redirige a la página principal (/inicio) | Automatizado: tests/test_login.py |
| TC-LOGIN-002 | Nombre de usuario visible tras el login | 🟡 Media | 1. Usuario registrado y activo<br>2. Estar en la página de login | 1. Escribir el usuario<br>2. Escribir la contraseña válida<br>3. Hacer clic en "Iniciar sesión" | Debería mostrar el nombre del usuario en la cabecera | | N/A |
| TC-LOGIN-003 | Contraseña incorrecta | 🟡 Media | 1. Usuario registrado y activo<br>2. Estar en la página de login | 1. Escribir el usuario<br>2. Escribir una contraseña incorrecta<br>3. Hacer clic en "Iniciar sesión" | Debería mostrar "Usuario o contraseña incorrectos" y seguir en la página de login | | N/A |
| TC-LOGIN-004 | Usuario con espacios delante y detrás | 🟢 Baja | 1. Usuario registrado y activo<br>2. Estar en la página de login | 1. Escribir el usuario con espacios delante y detrás<br>2. Escribir la contraseña válida<br>3. Hacer clic en "Iniciar sesión" | A confirmar | | Comportamiento actual: rechaza el login con "Usuario o contraseña incorrectos" |

## Cierre de sesión

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-LOGIN-005 | Cerrar sesión | 🔴 Alta | Sesión iniciada | 1. Abrir el menú de usuario<br>2. Hacer clic en "Cerrar sesión" | Debería redirigir a la página de login y no permitir volver a /inicio con el botón Atrás | | N/A |