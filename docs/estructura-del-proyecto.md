# Estructura del proyecto

Explicación sencilla de cada carpeta y archivo del proyecto: para qué existe, qué significa y cuál es su función.

> 💡 Los recuadros como este explican los términos técnicos con palabras sencillas.

---

## Una forma fácil de entenderlo

Imagina que el proyecto es **un restaurante**:

- **`pages/`** es la **cocina**: ahí se sabe *cómo* se hace cada cosa.
- **`tests/`** son los **inspectores de calidad**: piden algo y comprueban que salga bien.
- **`data/`** es la **despensa**: los ingredientes (datos) que se usan.
- **`casos/`** y **`docs/`** son el **libro de recetas** escrito a mano.
- **`.github/`** es un **inspector automático** que revisa todo cada vez que alguien cambia algo.

```
saucedemo/
│
├── pages/                      🍳 La cocina (Page Objects)
│   ├── __init__.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/                      🔍 Los inspectores (los tests)
│   ├── conftest.py
│   └── test_login.py
│
├── data/                       🥫 La despensa (datos de prueba)
│   ├── __init__.py
│   └── usuarios.py
│
├── casos/                      📖 Casos de prueba escritos a mano
├── docs/                       📖 Documentación
│
├── .github/workflows/tests.yml 🤖 El inspector automático (CI)
│
├── pytest.ini                  ⚙️ Configuración de pytest
├── requirements.txt            📦 Lista de "compras" (librerías)
├── README.md                   🪪 La portada del proyecto
├── .gitignore                  🚫 Lo que git no debe guardar
│
├── .claude/  .mcp.json         🤝 Configuración para trabajar con IA
│
└── (carpetas automáticas: .venv, __pycache__, .pytest_cache, test-results, .playwright-mcp)
```

---

## 🍳 `pages/`: las páginas de la web

**Para qué existe:** guarda una clase por cada pantalla de SauceDemo. Es la base del **Page Object Model (POM)**.

**Qué significa:** un *Page Object* es un "objeto" de código que representa una página. Sabe dos cosas:

1. **Dónde** está cada elemento (el campo de usuario, el botón, el mensaje de error). Son los **localizadores**.
2. **Qué puede hacer** el usuario ahí (escribir, hacer clic, iniciar sesión). Son los **métodos**.

| Archivo | Qué hace |
|---|---|
| `login_page.py` | La pantalla de login. Sabe dónde están el usuario, la contraseña, el botón y el mensaje de error. Tiene las acciones `abrir()` y `login()`. |
| `inventory_page.py` | La pantalla de productos. Sabe dónde están las imágenes y tiene la acción `obtener_src_imagenes()`, que devuelve la dirección de cada foto. |
| `__init__.py` | Un archivo vacío. Le dice a Python "esta carpeta es un **paquete**", y gracias a eso puedes escribir `from pages.login_page import LoginPage`. |

> 💡 **Regla de oro:** en `pages/` **no se comprueba nada**. Las páginas solo *hacen* cosas;
> quienes *verifican* son los tests.

---

## 🔍 `tests/`: los tests

**Para qué existe:** aquí están las pruebas automáticas. Pytest busca en esta carpeta todos los archivos que empiezan por `test_` y los ejecuta.

| Archivo | Qué hace |
|---|---|
| `test_login.py` | Los 9 tests de login. Cada uno usa las páginas para actuar y `expect()` para comprobar el resultado. |
| `conftest.py` | Un archivo **especial** de pytest. Contiene las **fixtures** compartidas. |

> 💡 **¿Qué es una fixture?** Es un "ayudante" que prepara algo antes del test y se lo entrega listo.
> Tu `conftest.py` tiene tres:
>
> - `login_page`: crea la página de login y la abre, así el test empieza ya en el login.
> - `url_login`: la dirección de la página de login.
> - `url_inventario`: la dirección de la página de productos.
>
> Lo que pongas en `conftest.py` lo pueden usar **todos** los tests sin importarlo. Pytest lo encuentra solo.

---

## 🥫 `data/`: los datos de prueba

**Para qué existe:** separa los **datos** (usuarios, contraseñas, mensajes) del **código** de los tests.

| Archivo | Qué hace |
|---|---|
| `usuarios.py` | Los usuarios de SauceDemo, la contraseña y los mensajes de error, cada uno con un nombre claro como `ERROR_USUARIO_BLOQUEADO`. |
| `__init__.py` | Igual que en `pages/`: convierte la carpeta en paquete para poder importarla. |

> 💡 **¿Por qué separarlo?** Si mañana cambia un mensaje de error, lo cambias **en un solo lugar**
> y todos los tests se actualizan.

> 💡 **Variable de entorno:** la contraseña se lee con `os.getenv("SAUCE_PASSWORD", "secret_sauce")`.
> Significa "busca la contraseña en el sistema; si no está, usa `secret_sauce`".
> En proyectos reales así se evita escribir contraseñas en el código.

---

## 📖 `casos/` y `docs/`: la documentación

**Para qué existen:** guardan lo que escribes **para personas**, no para la computadora. No se ejecutan.

| Carpeta | Qué contiene |
|---|---|
| `casos/` | Tus casos de prueba **manuales** en tablas: login, carrito y checkout, más la comparación de lo que acertó la IA. Los tests automáticos nacen de aquí. |
| `docs/` | El diagrama del flujo de bugs (`flujo-de-bugs.md`), la revisión del proyecto (`revision-del-proyecto.md`) y este documento (`estructura-del-proyecto.md`). |

> 💡 Esto se llama **trazabilidad**: cada test automático corresponde a un caso escrito aquí.
> Por eso los tests tienen nombres como `caso_4_username_vacio`.

---

## 🤖 `.github/workflows/tests.yml`: el CI

**Para qué existe:** le dice a **GitHub Actions** que ejecute tus tests automáticamente cada vez que subes código o abres un *pull request*.

> 💡 **CI (Integración Continua)** es como tener un compañero que, cada vez que alguien cambia algo,
> prueba todo y avisa si se rompió.

El archivo indica los pasos:

1. Descargar el código.
2. Instalar Python.
3. Instalar las librerías (`requirements.txt`).
4. Instalar el navegador Chromium.
5. Ejecutar los tests.
6. Guardar el informe, y las trazas y capturas si algo falló.

> 💡 El punto al inicio de `.github` significa que es una carpeta **oculta**.
> Es normal en carpetas de configuración.

---

## ⚙️ Archivos sueltos de la raíz

| Archivo | Para qué sirve |
|---|---|
| `pytest.ini` | La **configuración de pytest**. Dice dónde están los tests (`tests`), la dirección de la web (`base_url`), qué navegador usar y que guarde trazas y capturas **solo cuando un test falla**. |
| `requirements.txt` | La **lista de compras**: las librerías que necesita el proyecto, con su versión exacta. Se instalan con `pip install -r requirements.txt`. |
| `README.md` | La **portada** del proyecto en GitHub. Explica qué es y muestra tus resultados. |
| `.gitignore` | La lista de cosas que **git no debe guardar**, porque se generan solas o son privadas. |

> 💡 **¿Qué es una traza?** Una "grabación" paso a paso de lo que hizo el test.
> Si falla, la abres con `playwright show-trace` y ves exactamente qué pasó.

---

## 🤝 Configuración para trabajar con IA

| Archivo / carpeta | Para qué sirve |
|---|---|
| `.claude/` | La configuración de Claude Code y tu skill `casos-de-prueba`, que es tu plantilla para escribir casos. |
| `.mcp.json` | Conecta el **servidor MCP de Playwright**. |

> 💡 Un **MCP** es un "enchufe" que permite a la IA usar herramientas; en este caso,
> abrir y controlar un navegador.

---

## 🗑️ Carpetas que se crean solas (no las toques)

Las genera la computadora y están en `.gitignore`, así que no se suben a GitHub:

| Carpeta | Quién la crea y para qué |
|---|---|
| `.venv/` | El **entorno virtual**: una "caja" aislada donde se instalan las librerías de *este* proyecto, para no mezclarlas con otros. |
| `__pycache__/` | La crea Python. Guarda versiones "pre-traducidas" de tu código para que arranque más rápido. |
| `.pytest_cache/` | La crea pytest. Recuerda, por ejemplo, qué tests fallaron la última vez. |
| `test-results/` | La crea Playwright cuando un test falla. Ahí quedan las trazas y capturas. |
| `.playwright-mcp/` | La crea el MCP cuando la IA navega: capturas y registros de esa exploración. |

---

## 🔄 Cómo trabajan juntas las piezas

Cuando escribes `pytest`, pasa esto:

```
1. pytest lee pytest.ini         → "los tests están en tests/, la web es saucedemo.com"
2. pytest abre tests/            → encuentra test_login.py
3. pytest lee conftest.py        → prepara las fixtures (abre la página de login)
4. El test toma datos de data/   → usuario y contraseña
5. El test usa pages/            → login_page.login(usuario, password)
6. El test comprueba con expect  → "¿llegué al inventario?" / "¿salió el mensaje correcto?"
7. Si falla → se guarda una traza en test-results/
```

**En una frase:** `tests/` decide *qué* probar, `pages/` sabe *cómo* hacerlo,
`data/` aporta *con qué* datos, y `pytest.ini` y `conftest.py` lo preparan todo.

Cuando empieces con el carrito, aparecerán `pages/cart_page.py` y nuevos tests, pero la idea será la misma.
