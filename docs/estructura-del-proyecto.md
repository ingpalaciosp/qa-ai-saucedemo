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
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   └── checkout_complete_page.py
│
├── tests/                      🔍 Los inspectores (los tests)
│   ├── conftest.py
│   ├── test_login.py
│   └── test_checkout.py
│
├── data/                       🥫 La despensa (datos de prueba)
│   ├── __init__.py
│   ├── usuarios.py
│   └── checkout.py
│
├── casos/                      📖 Casos de prueba escritos a mano
├── docs/                       📖 Documentación
│
├── .github/
│   ├── workflows/tests.yml     🤖 El inspector automático (CI)
│   └── ISSUE_TEMPLATE/bug.md   🐞 Plantilla para reportar bugs
│
├── pytest.ini                  ⚙️ Configuración de pytest
├── requirements.txt            📦 Lista de "compras" (librerías)
├── README.md                   🪪 La portada del proyecto
├── .gitignore                  🚫 Lo que git no debe guardar
├── .env.example                🔑 Plantilla de las variables de entorno (sin valores)
├── .gitattributes              ↩️ Finales de línea LF para todos
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
| `base_page.py` | La clase "madre" de todas las páginas. Guarda la página del navegador (`self.page`) y tiene la acción `abrir()`, que va a la `RUTA` de cada página. Las demás páginas **heredan** de ella y no repiten ese código. |
| `login_page.py` | La pantalla de login. Sabe dónde están el usuario, la contraseña, el botón y el mensaje de error. Tiene la acción `login()`. |
| `inventory_page.py` | La pantalla de productos. Sabe dónde están las imágenes, los botones "Add to cart" y el icono del carrito. Tiene las acciones `agregar_al_carrito()`, `ir_al_carrito()` y `obtener_src_imagenes()`, que devuelve la dirección de cada foto. |
| `cart_page.py` | La pantalla del carrito. Sabe dónde está el botón "Checkout" y tiene la acción `ir_al_checkout()`. |
| `checkout_step_one_page.py` | El paso 1 del checkout (*Your Information*). Sabe dónde están el título, los tres campos y el botón "Continue". Tiene la acción `continuar()`, que rellena los campos y pulsa "Continue". |
| `checkout_step_two_page.py` | El paso 2 del checkout (*Overview*). Sabe dónde están el resumen, los productos con su nombre, precio y cantidad, y el botón "Finish". Tiene la acción `finalizar()`. |
| `checkout_complete_page.py` | La confirmación del pedido (*Complete!*). Sabe dónde están el título y el mensaje de confirmación. |
| `__init__.py` | Un archivo vacío. Le dice a Python "esta carpeta es un **paquete**", y gracias a eso puedes escribir `from pages.login_page import LoginPage`. |

> 💡 **¿Qué es heredar?** `class CartPage(BasePage):` significa que `CartPage` recibe todo lo de `BasePage` sin escribirlo. Por eso todas las páginas tienen `abrir()` aunque no aparezca en su archivo.

> 💡 **¿Qué es `RUTA`?** Cada página guarda su dirección dentro de la web, por ejemplo `RUTA = "/cart.html"`.
> Los tests la usan para comprobar a qué página llegaron (`base_url + CartPage.RUTA`) y `abrir()` la usa para ir directo.
> Si la dirección cambia, se corrige en un solo sitio.

> 💡 **Regla de oro:** en `pages/` **no se comprueba nada**. Las páginas solo *hacen* cosas;
> quienes *verifican* son los tests.

---

## 🔍 `tests/`: los tests

**Para qué existe:** aquí están las pruebas automáticas. Pytest busca en esta carpeta todos los archivos que empiezan por `test_` y los ejecuta.

| Archivo | Qué hace |
|---|---|
| `test_login.py` | Los 9 tests de login. Cada uno usa las páginas para actuar y `expect()` para comprobar el resultado. |
| `test_checkout.py` | Los 7 tests del checkout: entrar con productos, continuar con datos válidos, revisar el resumen, finalizar el pedido y abrir las 3 pantallas del checkout sin haber iniciado sesión. |
| `conftest.py` | Un archivo **especial** de pytest. Contiene las **fixtures** compartidas. |

> 💡 **¿Qué es una fixture?** Es un "ayudante" que prepara algo antes del test y se lo entrega listo.
> Tu `conftest.py` tiene seis:
>
> - `url_login`: la dirección de la página de login.
> - `url_inventario`: la dirección de la página de productos.
> - `login_page`: crea la página de login y la abre, así el test empieza ya en el login.
> - `iniciar_sesion`: inicia sesión (con el usuario estándar si no se indica otro) y deja al test en el inventario.
> - `carrito_a`: inicia sesión, añade "Sauce Labs Backpack" y "Sauce Labs Bike Light" y deja al test en el carrito.
> - `paso_1_carrito_a` y `paso_2_carrito_a`: avanzan desde el Carrito A hasta el paso 1 o el paso 2 del checkout.
>
> Lo que pongas en `conftest.py` lo pueden usar **todos** los tests sin importarlo. Pytest lo encuentra solo.

> 💡 **Fixtures encadenadas:** `paso_2_carrito_a` usa `paso_1_carrito_a`, que usa `carrito_a`, que usa `iniciar_sesion`.
> Cada una da un paso más, como las precondiciones de `casos/checkout.md`.
> Así un test que necesita estar en el paso 2 solo pide `paso_2_carrito_a`, y pytest prepara todo lo anterior.

---

## 🥫 `data/`: los datos de prueba

**Para qué existe:** separa los **datos** (usuarios, contraseñas, mensajes) del **código** de los tests.

| Archivo | Qué hace |
|---|---|
| `usuarios.py` | Los usuarios de SauceDemo, la contraseña y los mensajes de error, cada uno con un nombre claro como `ERROR_USUARIO_BLOQUEADO`. |
| `checkout.py` | Los datos del checkout: el comprador de referencia (`Alicia`, `Palacios`, `28001`), los productos del Carrito A con su precio, los títulos de cada paso y el mensaje de error al entrar sin sesión. |
| `__init__.py` | Igual que en `pages/`: convierte la carpeta en paquete para poder importarla. |

> 💡 **¿Por qué separarlo?** Si mañana cambia un mensaje de error, lo cambias **en un solo lugar**
> y todos los tests se actualizan.

> 💡 **Variable de entorno:** la contraseña se lee con `os.getenv("SAUCE_PASSWORD")` y no está escrita en ningún archivo del repositorio.
> En tu PC viene del archivo `.env` (que carga `load_dotenv()` y no se sube a GitHub); en el CI, del secret de GitHub.
> Si no existe, los tests se detienen con un mensaje que explica qué hacer. En proyectos reales así se evita escribir contraseñas en el código.

---

## 📖 `casos/` y `docs/`: la documentación

**Para qué existen:** guardan lo que escribes **para personas**, no para la computadora. No se ejecutan.

| Carpeta | Qué contiene |
|---|---|
| `casos/` | Tus casos de prueba **manuales** en tablas: login, carrito y checkout, más la comparación de lo que acertó la IA. Los tests automáticos nacen de aquí. |
| `docs/` | El diagrama del flujo de bugs (`flujo-de-bugs.md`), la revisión del proyecto (`revision-del-proyecto.md`) y este documento (`estructura-del-proyecto.md`). |

> 💡 Esto se llama **trazabilidad**: cada test automático corresponde a un caso escrito aquí.
> Por eso los tests llevan el Id del caso en el nombre, como `TC-LOGIN-004_username_vacio`
> o `test_tc_checkout_024_finalizar_el_pedido`, y el caso dice `Automatizado: tests/test_checkout.py`.

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

## 🐞 `.github/ISSUE_TEMPLATE/bug.md`: la plantilla de bugs

**Para qué existe:** cuando creas un issue en GitHub y eliges **Bug**, la plantilla rellena el issue con la estructura de siempre: el título `Bug Fixing - [Flujo] - [Módulo] - [Pantalla] - ` y las etiquetas `bug` y `Componente: frontend`.

Severidad, Prioridad y Módulo se añaden a mano. El flujo completo está en `docs/flujo-de-bugs.md`.

> 💡 GitHub solo lee las plantillas que están en la rama `main`.

---

## ⚙️ Archivos sueltos de la raíz

| Archivo | Para qué sirve |
|---|---|
| `pytest.ini` | La **configuración de pytest**. Dice dónde están los tests (`tests`), la dirección de la web (`base_url`), qué navegador usar y que guarde trazas y capturas **solo cuando un test falla**. |
| `requirements.txt` | La **lista de compras**: las librerías que necesita el proyecto, con su versión exacta. Se instalan con `pip install -r requirements.txt`. |
| `README.md` | La **portada** del proyecto en GitHub. Explica qué es y muestra tus resultados. |
| `.gitignore` | La lista de cosas que **git no debe guardar**, porque se generan solas o son privadas. |
| `.env.example` | La **plantilla** de las variables de entorno: tiene el nombre `SAUCE_PASSWORD` sin su valor. Se copia como `.env` (privado, en `.gitignore`) y ahí se escribe la contraseña. |
| `.gitattributes` | Obliga a guardar todos los archivos de texto con finales de línea **LF**, igual que el CI en Linux. Así Windows no cambia los finales de línea y no aparecen cambios "fantasma". |

> 💡 **¿Qué es una traza?** Una "grabación" paso a paso de lo que hizo el test.
> Si falla, la abres con `playwright show-trace` y ves exactamente qué pasó.

---

## 🤝 Configuración para trabajar con IA

| Archivo / carpeta | Para qué sirve |
|---|---|
| `.claude/` | La configuración de Claude Code y tus dos skills: `casos-de-prueba`, tu plantilla para escribir casos, y `reportar-bug`, que convierte un caso ❌ en el borrador de un issue y solo lo publica cuando tú lo apruebas. |
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
2. pytest abre tests/            → encuentra test_login.py y test_checkout.py
3. pytest lee conftest.py        → prepara las fixtures (abre el login, o llega hasta el paso 2 del checkout)
4. El test toma datos de data/   → usuario y contraseña, o los datos del comprador
5. El test usa pages/            → login_page.login(usuario, password) / paso_1.continuar(nombre, apellido, código)
6. El test comprueba con expect  → "¿llegué al inventario?" / "¿salió el mensaje correcto?"
7. Si falla → se guarda una traza en test-results/
```

**En una frase:** `tests/` decide *qué* probar, `pages/` sabe *cómo* hacerlo,
`data/` aporta *con qué* datos, y `pytest.ini` y `conftest.py` lo preparan todo.

Cuando automatices otra pantalla (por ejemplo, el ordenamiento de productos), la idea será la misma: una página nueva en `pages/`, sus datos en `data/` y sus tests en `tests/`.
