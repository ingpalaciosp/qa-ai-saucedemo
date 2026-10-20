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
4. Escribe o actualiza la sección "Datos y estados de partida".
5. Elige los casos (ver "Cómo elegir los casos") y escríbelos con el formato de abajo.
6. Repasa la "Lista de comprobación final".
7. Guarda en `casos/<funcionalidad>.md`, salvo que te indiquen otra ruta. No modifiques otros archivos.

## Estructura del documento
1. `#` Funcionalidad. Ejemplo: `# Login`
2. `## Datos y estados de partida` (ver abajo)
3. `##` Una sección por pantalla o parte del flujo. Ejemplo: `## Formulario de login`. Debajo, una tabla con estas columnas:

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|

4. Las secciones finales (ver "Al final del archivo de casos").

Importante: una celda de tabla Markdown no admite saltos de línea (la tabla se rompe). Cuando haya varios pasos, sepáralos con `<br>` dentro de la misma celda:
`1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Hacer clic en "Login"`

## Datos y estados de partida
Al principio del archivo, antes de las tablas:
- **URL y usuario** de prueba.
- **Datos válidos de referencia**: un valor válido para cada campo. Son los que usan todos los casos salvo en el dato que se está probando.
- **Estados de partida con nombre** (por ejemplo "Carrito A: sesión iniciada y solo el producto X"), para que las precondiciones digan "Carrito A" en lugar de repetir todo.
- **Limpieza**: qué hay que deshacer antes de empezar si la aplicación guarda datos de una ejecución anterior.

## Qué va en cada columna
- **Id**: formato `TC-<MÓDULO>-<NNN>`. Módulo en mayúsculas y en una palabra corta (LOGIN, CART, CHECKOUT); número de 3 cifras. Un Id nunca cambia ni se reutiliza: si un caso deja de servir, se marca "Obsoleto" en Notas y se deja en la tabla.
- **Caso**: nombre corto que diga qué se prueba.
- **Prioridad**: 🔴 Alta, 🟡 Media o 🟢 Baja, siempre con su círculo, según los criterios de abajo.
- **Precondiciones**: estado inicial necesario (usuario, datos, página de partida). Si son varias, enuméralas con `<br>`. Escribe "N/A" si no hay ninguna.
- **Procedimiento**: acciones concretas, una por paso, enumeradas con `<br>` si hay más de una.
- **Esperado**: empieza por "Debería…" y se puede comprobar mirando: textos exactos, URL, números, y endpoint y método HTTP si aplica. Si no hay requisito, "A confirmar" (regla 1). Si solo una parte no tiene requisito: `Debería mostrar "Item total: $39.98". Tax y Total: A confirmar`.
- **Obtenido**: vacío al escribir el caso. Al ejecutarlo, el símbolo de estado y lo observado en presente: `✅ Redirige a /inicio`.
- **Notas**: información permanente del caso, en este orden y separada por `<br>`: `Req: <requisito>`, `Comportamiento actual: …`, `A confirmar: ¿…?`, `Bug: pendiente` o `Bug: #N`, `Automatizado: <archivo>`, `Obsoleto`. Escribe "N/A" si no hay nada.

Si un mismo procedimiento tiene varios resultados esperados, cada resultado va en su propia fila con su propio Id. En Procedimiento copia los pasos completos (no escribas "igual que otro caso") y repite las Precondiciones, para que cada fila se pueda ejecutar sola.

## Estilo
- Verbos de los pasos: "Hacer clic en", "Escribir … en", "Seleccionar … en", "Ir a la URL", "Pulsar Atrás en el navegador".
- Texto visible de la aplicación (botones, campos, mensajes, títulos) entre comillas dobles: "Continue", "Error: First Name is required".
- Valores que se escriben, URLs y código entre comillas invertidas: `28001`, `/cart.html`, `<b>1</b>`. Los caracteres `<` y `>` siempre entre comillas invertidas, o GitHub los oculta.
- Siempre el mismo nombre para lo mismo: si un campo se llama "Last Name" en la aplicación, no lo llames "apellido" en un caso y "Last Name" en otro.

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
- ❌ No coincide (describe exactamente qué pasó y pon `Bug: pendiente` o `Bug: #N` en Notas)
- 🔍 Era "A confirmar" y se completó observando la aplicación
- ⏸ Bloqueado (no se pudo ejecutar; explica por qué)

## Reglas
1. Si no hay requisito que diga cómo debe comportarse algo, no escribas lo observado como Esperado: escribe "A confirmar" en Esperado y "Comportamiento actual: <lo observado>" en Notas. Lo observado solo pasa a Esperado si coincide con un requisito o con un comportamiento evidente (por ejemplo, el aviso de campo obligatorio). Así los casos no dan por bueno un posible bug.
2. Nunca escribas en Esperado frases que no se pueden comprobar, como "funciona correctamente" o "se actualiza bien".
3. En casos negativos, incluye también lo que no debe pasar (por ejemplo: "y debería seguir en la página de login").
4. Cada caso se ejecuta partiendo solo de sus precondiciones, sin depender de que otro caso se haya ejecutado antes.
5. Si alguna acción no se pudo hacer como la haría una persona (por ejemplo, clics lanzados por código), indícalo en el "Registro de ejecuciones".
6. **Una variable por caso**: cada caso cambia un solo dato o acción respecto al camino feliz; el resto lleva los "Datos válidos de referencia". Si un caso mezcla varios datos inválidos y falla, no se sabe cuál lo causó.
7. **El resultado tiene que poder verse**: antes de escribir un Esperado, comprueba que la aplicación muestra el dato en algún sitio (pantalla, URL, mensaje, respuesta de la API, PDF). Si no se muestra en ningún lado, el caso pasaría siempre: dilo en Notas (`El dato no se muestra en ninguna pantalla; no se puede verificar en la interfaz`) y propón dónde observarlo.

## Cuando se resuelve algo
- **El PO responde un "A confirmar"**: escribe la respuesta como Esperado ("Debería…"), quita la pregunta de Notas, añade `Req: confirmado por PO el <fecha>`, borra la pregunta de "Preguntas para el PO" y actualiza el Resumen.
- **Se encuentra un bug**: Obtenido con ❌ y lo observado; en Notas `Bug: pendiente`. Cuando se reporte, cámbialo por `Bug: #N`.
- **Se ejecuta un caso**: rellena Obtenido, añade una fila al "Registro de ejecuciones" y actualiza el Resumen.

## Relación con la automatización
- Cuando un caso se automatice, el test debe llevar el Id en su nombre, por ejemplo `test_tc_login_001_login_valido`, para poder rastrear qué caso cubre cada test.
- Anota en Notas el archivo del test: `Automatizado: tests/test_login.py`.

## Al final del archivo de casos
1. **Resumen**: total de casos, cuántos de cada prioridad (🔴 🟡 🟢) y de cada estado (✅ ❌ 🔍 ⏸ sin ejecutar), y cuántos siguen "A confirmar". Los números tienen que cuadrar con las filas de las tablas.
2. **Orden de ejecución sugerido**: lista de Ids, primero todos los 🔴, luego los 🟡 y al final los 🟢.
3. **Preguntas para el PO**: una por cada duda que sigue "A confirmar", con los Ids afectados. Ni más ni menos.
4. **Fuera de alcance**: lo que no se probó y por qué (otros usuarios, navegadores, móvil, accesibilidad, rendimiento…). Escribe "N/A" si se probó todo.
5. **Registro de ejecuciones**: una fila por cada vez que se ejecutan casos, con estas columnas: `| Fecha | Entorno | Navegador | Usuario | Quién | Casos | Observaciones |`. En Observaciones va lo que no se hizo como una persona (regla 5).

## Lista de comprobación final
- [ ] Cada Id sigue `TC-<MÓDULO>-<NNN>` y ninguno se repite ni cambió.
- [ ] Está la sección "Datos y estados de partida" y los casos la usan.
- [ ] Cada caso cambia una sola variable respecto al camino feliz.
- [ ] Cada Esperado empieza por "Debería…" (o es "A confirmar") y se puede ver en la aplicación.
- [ ] Ningún texto, URL o dato es inventado.
- [ ] Lo que no tiene requisito está como "A confirmar" y tiene su pregunta para el PO; lo resuelto ya no tiene pregunta.
- [ ] Las filas de cada sección están ordenadas 🔴 → 🟡 → 🟢.
- [ ] Ninguna celda tiene saltos de línea reales (solo `<br>`).
- [ ] Se sigue la guía de "Estilo" (verbos, comillas, comillas invertidas).
- [ ] Las celdas vacías de Precondiciones y Notas dicen "N/A" (Obtenido queda vacío hasta ejecutar).
- [ ] Están las secciones finales y el Resumen cuadra con las tablas.

## Ejemplo
Ejemplo solo del formato: no copies sus textos, URL ni datos; usa siempre los del proyecto real.

# Login

## Datos y estados de partida

- URL: `https://ejemplo.com` · Usuario: `ana` / `Clave123`
- Datos válidos de referencia: usuario `ana`, contraseña `Clave123`
- **Sesión cerrada**: estar en `/login` sin sesión iniciada.
- Limpieza: N/A

## Formulario de login

| Id | Caso | Prioridad | Precondiciones | Procedimiento | Esperado | Obtenido | Notas |
|---|---|---|---|---|---|---|---|
| TC-LOGIN-001 | Login con credenciales válidas | 🔴 Alta | Sesión cerrada | 1. Escribir `ana` en "Usuario"<br>2. Escribir `Clave123` en "Contraseña"<br>3. Hacer clic en "Iniciar sesión" | Debería redirigir a `/inicio` | ✅ Redirige a `/inicio` | Req: HU-1 / CA-1<br>Automatizado: tests/test_login.py |
| TC-LOGIN-002 | Nombre de usuario visible tras el login | 🟡 Media | Sesión cerrada | 1. Escribir `ana` en "Usuario"<br>2. Escribir `Clave123` en "Contraseña"<br>3. Hacer clic en "Iniciar sesión" | Debería mostrar "ana" en la cabecera | | Req: HU-1 / CA-2 |
| TC-LOGIN-003 | Contraseña incorrecta | 🟡 Media | Sesión cerrada | 1. Escribir `ana` en "Usuario"<br>2. Escribir `Clave999` en "Contraseña"<br>3. Hacer clic en "Iniciar sesión" | Debería mostrar "Usuario o contraseña incorrectos" y seguir en `/login` | ❌ Muestra "Error" sin más texto y sigue en `/login` | Req: HU-1 / CA-3<br>Bug: pendiente |
| TC-LOGIN-004 | Usuario con espacios delante y detrás | 🟢 Baja | Sesión cerrada | 1. Escribir ` ana ` en "Usuario"<br>2. Escribir `Clave123` en "Contraseña"<br>3. Hacer clic en "Iniciar sesión" | A confirmar | | Comportamiento actual: rechaza el login con "Usuario o contraseña incorrectos"<br>A confirmar: ¿deben ignorarse los espacios? |

## Resumen

Total: 4 casos · 🔴 1 · 🟡 2 · 🟢 1 · ✅ 1 · ❌ 1 · sin ejecutar 2 · A confirmar 1

## Orden de ejecución sugerido

1. 🔴 TC-LOGIN-001
2. 🟡 TC-LOGIN-002, 003
3. 🟢 TC-LOGIN-004

## Preguntas para el PO

1. ¿Deben ignorarse los espacios delante y detrás del usuario? (TC-LOGIN-004)

## Fuera de alcance

- Navegadores distintos de Chrome y versión móvil: no hay requisitos.

## Registro de ejecuciones

| Fecha | Entorno | Navegador | Usuario | Quién | Casos | Observaciones |
|---|---|---|---|---|---|---|
| 01/01/2026 | ejemplo.com | Chrome | ana | Alicia | TC-LOGIN-001, 003 | N/A |
