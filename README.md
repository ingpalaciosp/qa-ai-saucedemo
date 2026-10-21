# QA con IA sobre Sauce Demo
[![Tests de QA](https://github.com/ingpalaciosp/qa-ai-saucedemo/actions/workflows/tests.yml/badge.svg)](https://github.com/ingpalaciosp/qa-ai-saucedemo/actions/workflows/tests.yml)

Proyecto de portafolio de QA sobre [Sauce Demo](https://www.saucedemo.com), una tienda online de práctica.
Uso IA para diseñar y ejecutar casos de prueba, los valido contra la aplicación real para medir cuánto
acierta y dónde se equivoca, y automatizo solo los casos cuyo resultado esperado está confirmado.

## Qué hay en el proyecto

| Carpeta | Contenido |
|---|---|
| [`casos/`](casos/) | Casos de prueba escritos en Markdown con una plantilla única |
| [`.claude/skills/casos-de-prueba/`](.claude/skills/casos-de-prueba/SKILL.md) | La plantilla y las reglas que sigue la IA para escribir los casos |
| [`pages/`](pages/) · [`data/`](data/) · [`tests/`](tests/) | Automatización con Page Object Model, datos de prueba y tests |
| [`.github/workflows/`](.github/workflows/tests.yml) | CI: los tests se ejecutan en cada push y PR |
| [`docs/`](docs/) | Estructura del proyecto, flujo de bugs y revisiones |

## Resultados

### Login: ¿cuánto acierta la IA?

| Lección | Enfoque | Acierto | Textos inventados | Casos "A confirmar" | Casos |
|---|---|---|---|---|---|
| Lección 1 | Sin contexto | 87,5% (7 de 8) | 1 | — | [casos/login-revision-ia.md](casos/login-revision-ia.md) |
| Lección 2 | Con contexto real (campos, usuarios y mensajes exactos) | 100% de los casos definidos | 0 | 1 (completado después por observación) | [casos/login-v2-con-contexto.md](casos/login-v2-con-contexto.md) |

**Lección aprendida:** más contexto = menos inventos. Cuando la IA recibe los datos reales de la
aplicación y la regla de escribir "A confirmar" si no sabe algo, deja de inventar textos y marca
las dudas para que se validen contra la aplicación.

- **Casos que coincidieron (Lección 2):** 7 de 7 definidos. Cubren los tres usuarios (`standard_user`,
  `locked_out_user`, `problem_user`), Username vacío, Password vacío, contraseña incorrecta y
  usuario inexistente.
- **Caso 8 (ambos campos vacíos):** la IA puso "A confirmar" porque no sabía el resultado. Lo ejecuté
  y lo completé con lo que observé: "Epic sadface: Username is required".

### Checkout: casos diseñados y ejecutados con un agente de IA

Casos: [casos/checkout.md](casos/checkout.md)

Un agente de IA con navegador (Playwright) diseñó los casos siguiendo la skill, los ejecutó en
saucedemo con `standard_user` y anotó lo observado. Después revisé y corregí los casos y ejecuté
a mano el que el agente no pudo hacer.

| Total | 🔴 Alta | 🟡 Media | 🟢 Baja |
|---|---|---|---|
| 48 casos | 14 | 22 | 12 |

| Estado | Casos | Qué significa |
|---|---|---|
| ✅ Coincide | 24 | El resultado es el esperado |
| ❌ No coincide | 8 | Bugs pendientes de reportar |
| 🔍 Observado | 16 | No hay requisito: se anotó lo observado y la duda quedó como pregunta para el PO |

**Bugs encontrados:**
- Con el carrito vacío se puede entrar al checkout (TC-CHECKOUT-002).
- El paso 1 acepta campos con solo espacios (TC-CHECKOUT-012, 038, 039).
- El paso 1 acepta un código postal con letras y símbolos o de 1 carácter (TC-CHECKOUT-013, 037).
- No se quitan los espacios delante y detrás del nombre: el PDF del pedido muestra "Alicia  Palacios" (TC-CHECKOUT-041).
- Enviar el paso 1 con la tecla Enter redirige a `/cart.html` (TC-CHECKOUT-044, ejecutado a mano).

**Lecciones aprendidas:**
- **Una variable por caso:** un caso que probaba tres campos a la vez se dividió en tres, para saber qué falla.
- **El resultado tiene que poder verse:** el nombre del comprador no aparece en ninguna pantalla, pero sí
  en el PDF del pedido. Ahí se pudo comprobar la inyección de HTML (`<b>1</b>` se muestra como texto)
  y apareció el bug de los espacios.
- **Revisar a la IA:** la IA escribió como resultado esperado detalles que solo había observado (por ejemplo,
  cómo se ve el icono del carrito vacío). Esos casos pasaron a "criterio QA, validar con PO", y la regla
  se añadió a una nueva versión de la skill.

## Cómo se escriben los casos

La [skill `casos-de-prueba`](.claude/skills/casos-de-prueba/SKILL.md) es el estándar que siguen tanto
las personas como la IA. Sus reglas principales:

- **"A confirmar" si no hay requisito:** lo observado no se escribe como resultado esperado, para no dar por bueno un bug.
- **Una variable por caso** y **valores límite** en cada campo.
- **Ids que nunca cambian** (`TC-<MÓDULO>-<NNN>`) para mantener la trazabilidad caso → test → bug.
- **Datos y estados de partida** con nombre (por ejemplo "Carrito A"), para que cada caso sea independiente.
- Al final de cada archivo: resumen, orden de ejecución, preguntas para el PO, fuera de alcance y registro de ejecuciones.

## Automatización

Python + pytest + Playwright, con Page Object Model (una clase por pantalla en `pages/`), datos separados
(`data/`) y las precondiciones de los casos como fixtures de pytest (`tests/conftest.py`).
Se ejecutan en GitHub Actions en cada push y PR, con informe HTML y trazas de los fallos.

| Archivo | Casos automatizados |
|---|---|
| [`tests/test_login.py`](tests/test_login.py) | TC-LOGIN-001 a 009 (el 009 marcado como fallo esperado por un bug conocido, issue #1) |
| [`tests/test_checkout.py`](tests/test_checkout.py) | TC-CHECKOUT-001, 004, 018, 024, 033, 034 y 035 |

**Qué se automatiza:** en checkout, solo los casos 🔴 cuyo resultado esperado está confirmado, es decir,
sin bug, sin "A confirmar" y sin preguntas al PO. Automatizar un resultado que nadie confirmó lo
convertiría en "lo correcto".

**Trazabilidad:** cada test lleva el Id de su caso en el nombre (`test_tc_checkout_018_productos_del_resumen`)
y el caso indica en Notas qué archivo lo automatiza.

```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

## Próximamente

- Automatización de los casos de carrito.
- Evaluación automática de la skill con [Promptfoo](https://www.promptfoo.dev/), para medir si cada cambio la mejora.
- Pruebas de API.
- Agente explorador con IA que navega la web y reporta bugs.
- Playwright Agents (planner, generator, healer) para generar y reparar tests.
