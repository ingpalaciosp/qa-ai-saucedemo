# Normas del proyecto

Portafolio de QA sobre Sauce Demo: casos de prueba en Markdown y automatización con Python, pytest y Playwright (Page Object Model). Todo el código, los nombres y los comentarios van en español.

## Estructura

- `casos/`: casos de prueba. Se escriben y revisan con la skill `casos-de-prueba`.
- `pages/`: un Page Object por pantalla. Todos heredan de `BasePage` (CI).
- `data/`: datos de prueba (usuarios, textos esperados).
- `tests/`: los tests. Las fixtures compartidas están en `tests/conftest.py`.
- `scripts/revisar_reglas_qa.py`: linter que comprueba las normas marcadas con (CI). Se ejecuta en el CI antes de los tests. Una excepción justificada se marca al final de la línea con `# norma-ok: <motivo>`.
- `ruff.toml`: configuración de Ruff, el linter general de Python. Se ejecuta en el CI después de instalar las dependencias.

## Normas de la automatización

1. **Selectores solo en `pages/`** (CI). Nunca `locator`, `get_by_...` ni `data-test` dentro de un test.
2. **Orden de preferencia de selectores:** `data-test` > rol o etiqueta > texto > clase CSS. Nunca por posición ("el tercer botón") ni XPath. (CI: todo `locator` de `pages/` usa `data-test`, sin `nth-child`, `nth-of-type` ni XPath.)
3. **Un Page Object solo tiene selectores y acciones, sin aserciones** (CI). Los `expect` van en los tests.
4. **Nada de esperas fijas** (CI): ni `wait_for_timeout` ni `sleep`. Se espera algo concreto con `expect(...)` o `wait_for_url(...)`.
5. **Solo se automatizan casos con el esperado confirmado:** nunca un caso "A confirmar" ni uno con un bug abierto.
6. **Trazabilidad** (CI): el Id del caso va en el nombre del test (`test_tc_sort_004_...`) o en el `id` de cada fila de `pytest.param(..., id="TC-SORT-001_...")`. En el caso, Notas dice `Automatizado: tests/<archivo>.py`.
7. **Precondiciones = fixtures:** un estado de partida que usan varios tests es una fixture. Si solo la usa un archivo, va arriba de ese archivo; si la usan varios, en `conftest.py`.
8. **Mismo procedimiento con distintos datos = `parametrize`.**
9. **Cada test tiene al menos un `expect`** (CI) y tiene que poder fallar: si elige la opción que ya está puesta, pasa siempre.
10. **Ningún test saltado** (CI): ni `@pytest.mark.skip`, ni `skipif`, ni `pytest.skip(...)`. Si de verdad hace falta (por ejemplo, un bug que lo bloquea), se deja el motivo con `# norma-ok: <motivo>`.
11. **La contraseña nunca va en el código:** se lee de `SAUCE_PASSWORD` (en local, del `.env`; en el CI, del secret).

## Antes de dar algo por terminado

- `python scripts/revisar_reglas_qa.py` y `python -m ruff check .` sin problemas.
- `pytest` con los mismos resultados que antes del cambio, más los tests nuevos.
- Forzar el fallo de cada test nuevo cambiando su esperado, y después dejarlo como estaba.
- Actualizar la documentación afectada (`README.md`, `docs/estructura-del-proyecto.md`, Notas de los casos).
- Un PR = un tema. Los comandos de Git los ejecuta Alicia.
