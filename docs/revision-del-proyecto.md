# Revisión del proyecto de automatización (SauceDemo)

Revisión hecha con la mirada de un SDET senior (un ingeniero de pruebas que también programa).
Stack del proyecto: **Python + Pytest + Playwright** (con el plugin `pytest-playwright`).

> 💡 Este documento está pensado para aprender. Cada vez que aparece un término técnico,
> se explica con palabras sencillas en un recuadro como este.

---

## Estado a 26/10/2026

De los 12 problemas de la revisión, 9 están resueltos, 1 está a medias y 2 siguen pendientes.
El resto del documento se deja como estaba: es la foto del proyecto el día de la revisión.

| Id | Problema | Estado | Cómo quedó |
|---|---|---|---|
| 🔴 A1 | Error de escritura `problem_use` | ✅ Resuelto | El test usa `USUARIO_PROBLEMA` de `data/usuarios.py` |
| 🟡 M1 | Localizador dentro del test | ✅ Resuelto | `pages/inventory_page.py`, con localizadores `data-test` |
| 🟡 M2 | Tests casi idénticos | ✅ Resuelto | `test_login_con_error` con `parametrize` (6 casos) |
| 🟡 M3 | Datos de prueba dentro del test | ⚠️ A medias | Datos en `data/` y secret `SAUCE_PASSWORD` creado en GitHub. Falta pasarlo en `tests.yml` y quitar el valor por defecto de `os.getenv` |
| 🟡 M4 | Fixtures de URL en el archivo de tests | ✅ Resuelto | En `tests/conftest.py` |
| 🟡 M5 | `.gitignore` incompleto | ✅ Resuelto | Incluye `test-results/` e `informe.html` |
| 🟢 B1 | Numeración duplicada | ✅ Resuelto | Ids `TC-LOGIN-001` a `TC-LOGIN-009` |
| 🟢 B2 | `if` innecesarios en `login()` | ✅ Resuelto | `login()` sin `if` |
| 🟢 B3 | Localizadores alternativos | ⏳ Pendiente | Tarjeta F1-10 de la ruta |
| 🟢 B4 | Casos 7 y 8 sin automatizar | ⏳ Pendiente | `Standard_User` con mayúsculas y `/inventory.html` sin sesión |
| 🟢 B5 | MCP con `@latest` | ✅ Resuelto | `.mcp.json` fija `@playwright/mcp@0.0.83` |
| 🟢 B6 | README desactualizado | ✅ Resuelto | La automatización está en resultados |

Del apartado 7: la fixture `usuario_logueado` existe con el nombre `iniciar_sesion`. La `BasePage` del apartado 6 está pendiente (tarjeta F1-06).

---

## Índice

1. [Glosario rápido](#1-glosario-rápido)
2. [Estructura actual del proyecto](#2-estructura-actual-del-proyecto)
3. [¿Apliqué bien el Page Object Model?](#3-apliqué-bien-el-page-object-model)
4. [Lo que está bien hecho](#4-lo-que-está-bien-hecho-)
5. [Problemas encontrados](#5-problemas-encontrados)
6. [¿Cuándo crear una BasePage?](#6-cuándo-crear-una-basepage)
7. [Estructura de carpetas propuesta](#7-estructura-de-carpetas-propuesta)
8. [Plan de trabajo recomendado](#8-plan-de-trabajo-recomendado)

---

## 1. Glosario rápido

Antes de empezar, estas son las palabras que vas a ver a lo largo del documento:

| Término | Explicación sencilla |
|---|---|
| **Test automático** | Un programa que hace lo que haría una persona probando la web (escribir, hacer clic) y comprueba que el resultado es el correcto. |
| **Pytest** | La herramienta de Python que encuentra tus tests, los ejecuta y te dice cuáles pasan y cuáles fallan. |
| **Playwright** | La herramienta que controla el navegador (Chrome, Firefox…) desde el código. |
| **Page Object Model (POM)** | Una forma de organizar el código: creas una clase por cada pantalla de la web. La clase sabe *dónde* están los elementos y *cómo* usarlos; el test solo dice *qué* hacer y *qué* comprobar. |
| **Clase** | En Python, un "molde" que agrupa datos y funciones relacionadas. Por ejemplo, `LoginPage` agrupa todo lo del login. |
| **Método** | Una función que pertenece a una clase. Por ejemplo, `login()` dentro de `LoginPage`. |
| **Localizador (locator / selector)** | La "dirección" de un elemento en la página para que Playwright lo encuentre. Ejemplo: `[data-test="username"]`. |
| **`data-test`** | Un atributo que los desarrolladores añaden al HTML *especialmente para los tests*. Es el localizador más estable porque nadie lo cambia por motivos de diseño. |
| **Assert / `expect`** | La comprobación del test: "espero que la URL sea X", "espero que aparezca este mensaje". Si no se cumple, el test falla. |
| **Fixture** | Una función que prepara algo antes del test (abrir el navegador, ir a una página) y se lo entrega listo. Así no repites ese código en cada test. |
| **`conftest.py`** | Archivo especial donde pytest busca fixtures compartidas. Todo lo que pongas ahí lo pueden usar todos los tests sin importarlo. |
| **CI (Integración Continua)** | Un servidor (en tu caso, GitHub Actions) que ejecuta tus tests automáticamente cada vez que subes código. |
| **`xfail`** | Marca de pytest que significa "sé que este test falla por un bug conocido". El test falla, pero pytest no lo cuenta como error. |
| **Falso positivo** | Un test que dice "todo bien" (o "fallo esperado") pero en realidad no está probando lo que debería. Es peligroso porque da una falsa sensación de seguridad. |
| **Herencia / clase base** | Una clase "madre" con código común. Las clases "hijas" heredan ese código y no tienen que repetirlo. |
| **Variable de entorno** | Un valor que se guarda en el sistema (o en el CI) y no en el código. Se usa para contraseñas y datos sensibles. |

---

## 2. Estructura actual del proyecto

```
saucedemo/
├── .github/workflows/tests.yml   → CI: ejecuta los tests en GitHub en cada push o pull request
├── .claude/                       → configuración de Claude Code y tu skill "casos-de-prueba"
├── .mcp.json                      → conecta el servidor MCP de Playwright (para que la IA use el navegador)
├── .playwright-mcp/               → capturas y logs de la IA explorando la web (ignorado en git ✔)
├── casos/                         → casos de prueba manuales en Markdown (login, carrito, checkout)
├── docs/flujo-de-bugs.md          → diagrama del ciclo de vida de un bug
├── pages/
│   ├── __init__.py                → convierte la carpeta en "paquete" para poder importar desde ella
│   └── login_page.py              → Page Object del login
├── tests/
│   ├── conftest.py                → fixtures compartidas (la fixture login_page)
│   └── test_login_casos.py        → 9 tests de login
├── pytest.ini                     → configuración de pytest: URL base, navegador, trazas y capturas
├── requirements.txt               → lista de librerías necesarias, con su versión fija
└── README.md                      → presentación del portafolio y resultados
```

> 💡 **¿Qué es un "paquete" en Python?** Una carpeta con un archivo `__init__.py` dentro.
> Gracias a eso puedes escribir `from pages.login_page import LoginPage` en tus tests.

---

## 3. ¿Apliqué bien el Page Object Model?

> 💡 **Recordatorio:** el POM sirve para que, si mañana cambia un botón de la web,
> lo arregles en **un solo lugar** (la clase de la página) y no en todos los tests.

| Pregunta | Respuesta |
|---|---|
| ¿Cada página tiene su clase en `pages/`? | ⚠️ **Parcial.** Existe `LoginPage`, pero uno de los tests usa la página de productos (inventario) y esa página todavía no tiene clase. |
| ¿Los localizadores están solo en las páginas? | ⚠️ **Casi siempre.** Hay una excepción en `tests/test_login_casos.py:44` (`"img.inventory_item_img"`). |
| ¿Los métodos son acciones del usuario? | ✅ **Sí.** `abrir()` y `login()` describen lo que hace una persona. |
| ¿Los asserts están en los tests y no en las páginas? | ✅ **Sí.** `LoginPage` no comprueba nada, y además lo dejaste escrito en el comentario de la clase. ¡Muy bien! |
| ¿Hay código repetido que debería ir en una BasePage? | **Todavía no.** Con una sola página no hay nada repetido. Tendrá sentido al crear la segunda o tercera página (ver sección 6). |

---

## 4. Lo que está bien hecho ✅

1. **Localizadores `data-test`** (`pages/login_page.py:9-12`).
   Es el tipo de selector más estable. Mejoraste respecto a tu primer test, que usaba `#user-name`.

2. **Uso de `expect()` de Playwright** en lugar de `assert` normal.
   > 💡 `expect` **reintenta** la comprobación durante unos segundos (5 por defecto) hasta que se cumpla.
   > Por eso no necesitas poner esperas a mano.

3. **Ningún `time.sleep()`** en todo el proyecto.
   > 💡 `time.sleep(3)` significa "espera 3 segundos sí o sí". Es mala práctica: si la web tarda 4, el test falla;
   > si tarda 1, pierdes 2 segundos. Playwright ya espera automáticamente a que los elementos estén listos.

4. **`base_url` en `pytest.ini`.** La dirección de la web está en un solo sitio y `page.goto("/")` la completa sola.

5. **Fixture `login_page` en `conftest.py`.** Evita repetir "crear la página y abrirla" en cada test.

6. **Tests independientes.**
   > 💡 Significa que cada test funciona por sí solo, sin necesitar que otro se ejecute antes.
   > pytest-playwright abre un navegador "limpio" para cada test, así que ninguno ensucia al siguiente.

7. **Trazas y capturas solo cuando un test falla** (`--tracing retain-on-failure --screenshot only-on-failure`), y además se guardan en el CI.
   > 💡 Una **traza** es como una grabación paso a paso de lo que hizo el test. Se abre con
   > `playwright show-trace` y te ayuda a entender por qué falló.

8. **Versiones fijas en `requirements.txt`** (por ejemplo `pytest==9.1.1`). Así el CI no se rompe de repente porque salga una versión nueva de una librería.

9. **Uso de `xfail` con `strict=True`** para documentar un bug conocido y enlazarlo al issue #1. Es una idea excelente (aunque ahora mismo tiene un fallo, ver problema A1).
   > 💡 `strict=True` significa: "si este test empieza a pasar, avísame". Así te enteras cuando arreglan el bug.

10. **Trazabilidad.** Cada test corresponde a un caso documentado en `casos/login-v2-con-contexto.md`.
    > 💡 **Trazabilidad** = poder seguir el hilo entre el caso escrito y el test automático.

---

## 5. Problemas encontrados

Ordenados por prioridad:

- 🔴 **Alta:** el test da un resultado falso. Hay que corregirlo cuanto antes.
- 🟡 **Media:** funciona, pero te va a dar problemas cuando el proyecto crezca.
- 🟢 **Baja:** detalles para mejorar la calidad.

---

### 🔴 A1. Error de escritura que invalida el test del bug

📍 `tests/test_login_casos.py:41`

```python
login_page.login("problem_use", PASSWORD)   # ← falta la "r" de "problem_user"
```

**¿Por qué es un problema?**
Con `problem_use` el login falla, y el test se cae en la línea 42 porque la URL no cambia.
Como el test está marcado con `xfail`, pytest lo cuenta como "fallo esperado" y lo da por bueno.
Pero falla **por el motivo equivocado**: nunca llega a revisar las imágenes.

Si algún día arreglan el bug de las imágenes, el test seguirá fallando por el error de escritura,
y `strict=True` **nunca te avisará**. Es un **falso positivo**.

**Cómo corregirlo:**

```python
login_page.login("problem_user", PASSWORD)
```

**Lección para el futuro:** un `xfail` debe fallar *justo en la línea del bug*.
Puedes ver el motivo de cada xfail ejecutando:

```bash
pytest -rxX
```

---

### 🟡 M1. Localizador dentro del test y falta la página de inventario

📍 `tests/test_login_casos.py:44-47`

```python
imagenes = page.locator("img.inventory_item_img")   # ← localizador dentro del test
```

**¿Por qué es un problema?**
Rompe la regla del POM. Si cambia la clase CSS `inventory_item_img`, tendrás que buscarla en todos los tests.
Además, un selector por clase CSS es más frágil que uno `data-test`, porque los diseñadores cambian las clases a menudo.

**Cómo corregirlo:** crea el archivo `pages/inventory_page.py`:

```python
from playwright.sync_api import Page


class InventoryPage:
    """Pantalla de productos (inventario) de SauceDemo."""

    def __init__(self, page: Page):
        self.page = page
        self.imagenes_productos = page.locator("img.inventory_item_img")

    def obtener_src_imagenes(self) -> list[str]:
        return [img.get_attribute("src") for img in self.imagenes_productos.all()]
```

Y en el test:

```python
inventario = InventoryPage(page)
expect(inventario.imagenes_productos).to_have_count(6)
direcciones_fotos = inventario.obtener_src_imagenes()
```

---

### 🟡 M2. Tests casi idénticos que podrían usar `parametrize`

📍 `tests/test_login_casos.py:26-82`

**¿Por qué es un problema?**
Los casos 2, 4, 5, 6, 7 y 8 hacen exactamente lo mismo: login, comprobar el mensaje de error y comprobar la URL.
Solo cambian los datos. Eso es código repetido.

> 💡 **`parametrize`** le da a pytest una "tabla de datos" y ejecuta el mismo test una vez por cada fila.
> Es como una plantilla de test que se rellena con datos distintos.

**Cómo corregirlo:**

```python
@pytest.mark.parametrize(
    "usuario, password, mensaje",
    [
        ("locked_out_user", PASSWORD, "Epic sadface: Sorry, this user has been locked out."),
        ("", PASSWORD, "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        # ... resto de casos
    ],
    ids=["bloqueado", "usuario_vacio", "password_vacio"],
)
def test_login_con_error(page, login_page, url_login, usuario, password, mensaje):
    login_page.login(usuario, password)
    expect(login_page.mensaje_error).to_have_text(mensaje)
    expect(page).to_have_url(url_login)
```

> 💡 `ids` le pone un nombre a cada fila, para que en el informe veas `test_login_con_error[bloqueado]`
> en lugar de `test_login_con_error[0]`.

**Nota:** esto es **opcional**. Tener tests separados también es válido y a veces se leen mejor.
Pero si vas a añadir muchos casos de error, `parametrize` escala mejor.

---

### 🟡 M3. Datos de prueba escritos dentro del test

📍 `tests/test_login_casos.py:8` y todas las llamadas a `login(...)`

**¿Por qué es un problema?**
La contraseña `"secret_sauce"`, los usuarios y los mensajes de error están escritos dentro del archivo de tests.
Si cambian, tienes que editar muchos sitios.

En una aplicación real, una contraseña **nunca** debe ir en el código, porque queda guardada en el historial de git para siempre.
En SauceDemo la contraseña es pública, así que aquí el riesgo es bajo, pero conviene aprender el buen hábito desde ya.

**Cómo corregirlo:**

1. Crea un archivo `data/usuarios.py` con los usuarios y los mensajes:

   ```python
   USUARIO_ESTANDAR = "standard_user"
   USUARIO_BLOQUEADO = "locked_out_user"
   MENSAJE_USUARIO_BLOQUEADO = "Epic sadface: Sorry, this user has been locked out."
   ```

2. Lee la contraseña desde una **variable de entorno**:

   ```python
   import os

   PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
   ```

   > 💡 `os.getenv("SAUCE_PASSWORD", "secret_sauce")` significa: "busca la variable `SAUCE_PASSWORD`;
   > si no existe, usa `secret_sauce`".

3. En GitHub, guarda la contraseña como **secret**.
   > 💡 Un **secret** de GitHub es una variable cifrada: el CI la puede usar, pero nadie la ve en el código.

---

### 🟡 M4. Fixtures de URL definidas en el archivo de tests

📍 `tests/test_login_casos.py:11-18`

**¿Por qué es un problema?**
Las fixtures `url_login` y `url_inventario` también las van a necesitar los futuros tests de carrito y checkout.
Si se quedan en este archivo, acabarás copiándolas en cada archivo nuevo.

**Cómo corregirlo:** muévelas a `tests/conftest.py`:

```python
@pytest.fixture
def url_login(base_url: str) -> str:
    return base_url + "/"


@pytest.fixture
def url_inventario(base_url: str) -> str:
    return base_url + "/inventory.html"
```

---

### 🟡 M5. `.gitignore` incompleto

📍 `.gitignore`

> 💡 **`.gitignore`** es la lista de archivos que git debe ignorar (no subir al repositorio).

**¿Por qué es un problema?**
Faltan `test-results/` (la carpeta donde Playwright guarda trazas y capturas) e `informe.html`
(el informe que genera pytest-html). Si ejecutas los tests en tu ordenador, acabarás subiendo
esos archivos generados a git sin querer.

**Cómo corregirlo:** añade estas líneas al `.gitignore`:

```
test-results/
informe.html
```

---

### 🟢 B1. Nombres de test con numeración duplicada

📍 `tests/test_login_casos.py:34` y `tests/test_login_casos.py:40`

Hay dos tests que empiezan por `test_caso_3_...`. Además, un número solo no dice nada cuando el test falla.

Tu skill de casos de prueba usa IDs del tipo `TC-LOGIN-001`. Puedes usar el mismo formato en los nombres de los tests:

```python
def test_tc_login_003_problem_user_imagenes_distintas(...):
```

Así, cuando un test falla en el informe, sabes al instante a qué caso documentado corresponde.

---

### 🟢 B2. `if` innecesarios en `login()`

📍 `pages/login_page.py:18-21`

`fill("")` funciona perfectamente en Playwright (deja el campo vacío), así que no hacen falta los `if`.
El código queda más simple y, además, te aseguras de que el campo quede vacío aunque tuviera texto antes:

```python
def login(self, usuario: str, password: str):
    self.campo_usuario.fill(usuario)
    self.campo_password.fill(password)
    self.boton_login.click()
```

---

### 🟢 B3. Localizadores alternativos de Playwright

Tu forma actual (`page.locator('[data-test="username"]')`) ya es buena. Playwright ofrece dos atajos que conviene conocer:

- **`get_by_test_id`:** un atajo para `data-test`. Primero hay que decirle a Playwright que tu atributo se llama `data-test`
  (por defecto busca `data-testid`):

  ```python
  playwright.selectors.set_test_id_attribute("data-test")
  page.get_by_test_id("username")
  ```

- **`get_by_role`:** busca los elementos como los vería una persona (o un lector de pantalla):

  ```python
  page.get_by_role("button", name="Login")
  ```

  > 💡 Un **rol** es el "tipo" de elemento: botón, enlace, casilla, título… Usarlo hace los tests más
  > parecidos a cómo un usuario real usa la web.

---

### 🟢 B4. Casos documentados que todavía no están automatizados

📍 `casos/login-revision-ia.md`

Los casos **7** (`Standard_User` con mayúsculas) y **8** (abrir `/inventory.html` sin haber iniciado sesión) no tienen test automático.
El caso 8 es especialmente valioso porque prueba **seguridad**: que nadie pueda saltarse el login.

---

### 🟢 B5. `.mcp.json` usa `@playwright/mcp@latest`

📍 `.mcp.json:9`

`@latest` descarga siempre la última versión, así que un día puede cambiar el comportamiento sin que te des cuenta.
Fija una versión concreta, igual que hiciste en `requirements.txt`.

---

### 🟢 B6. README desactualizado

📍 `README.md:40`

En la sección "Próximamente" pone "Automatización de los casos validados con Playwright", ¡pero eso ya lo tienes hecho!
Muévelo a la sección de resultados y lúcelo en tu portafolio.

---

## 6. ¿Cuándo crear una BasePage?

Cuando tengas `LoginPage`, `InventoryPage` y `CartPage`, verás que repites `self.page = page` en todas
y quizás algunas acciones comunes (abrir una ruta, usar el menú lateral).

Una **BasePage** es una clase "madre" con ese código común. Las demás páginas **heredan** de ella y no lo repiten:

```python
# pages/base_page.py
from playwright.sync_api import Page


class BasePage:
    RUTA = "/"

    def __init__(self, page: Page):
        self.page = page

    def abrir(self):
        self.page.goto(self.RUTA)
```

```python
# pages/inventory_page.py
from pages.base_page import BasePage


class InventoryPage(BasePage):     # ← "hereda" de BasePage
    RUTA = "/inventory.html"
    # ya tiene self.page y abrir() sin escribirlos otra vez
```

> 💡 `class InventoryPage(BasePage)` se lee: "InventoryPage es un tipo de BasePage".
> Recibe automáticamente todo lo que tiene la madre.

También puedes crear **componentes** para las partes que aparecen en varias páginas, como la cabecera
con el icono del carrito o el menú hamburguesa. Así no los duplicas en cada página.

---

## 7. Estructura de carpetas propuesta

```
saucedemo/
├── .github/workflows/tests.yml
├── pages/
│   ├── __init__.py
│   ├── base_page.py            ← clase madre con el código común
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── components/
│       └── header.py           ← icono del carrito y menú (aparecen en varias páginas)
├── data/
│   └── usuarios.py             ← usuarios, mensajes de error, datos del comprador
├── tests/
│   ├── conftest.py             ← fixtures comunes: urls, login_page, usuario_logueado
│   ├── login/
│   │   └── test_login.py
│   ├── carrito/
│   │   └── test_carrito.py
│   └── checkout/
│       └── test_checkout.py
├── casos/                      ← documentación de casos manuales (ya la tienes muy bien)
├── docs/
├── pytest.ini
├── requirements.txt
└── README.md
```

### Consejo para cuando hagas el carrito

Crea una fixture `usuario_logueado` en `conftest.py` que haga el login y te deje directamente en el inventario:

```python
@pytest.fixture
def usuario_logueado(login_page: LoginPage, page: Page) -> InventoryPage:
    login_page.login("standard_user", PASSWORD)
    return InventoryPage(page)
```

Así los tests del carrito empiezan ya con la sesión iniciada y no repiten el login.

> 💡 **Sobre el carrito que "no se vacía al cerrar sesión":** en `casos/carrito-casos-agente.md` anotaste
> que hay que vaciarlo a mano. Eso pasa en las pruebas **manuales**. En los tests **automáticos** no te afecta,
> porque cada test empieza con un navegador limpio (sin cookies ni datos guardados).

---

## 8. Plan de trabajo recomendado

Tu base es muy buena: aplicas POM, usas buenos selectores, fixtures, `expect` sin esperas fijas
y tienes un CI con trazas que muchos proyectos profesionales no tienen.

Orden sugerido para seguir mejorando:

- [ ] **A1:** corregir el error de escritura `problem_use` → `problem_user`.
- [ ] **M1:** crear `pages/inventory_page.py` y sacar el localizador del test.
- [ ] **M4:** mover las fixtures de URL a `tests/conftest.py`.
- [ ] **M5:** añadir `test-results/` e `informe.html` al `.gitignore`.
- [ ] **M3:** separar los datos de prueba en `data/` y leer la contraseña de una variable de entorno.
- [ ] **M2:** (opcional) agrupar los casos de error con `parametrize`.
- [ ] **Bajas:** renombrar tests con IDs `TC-LOGIN-NNN`, simplificar `login()`, automatizar los casos 7 y 8, fijar la versión del MCP y actualizar el README.
- [ ] **Al empezar el carrito:** crear `BasePage` y la fixture `usuario_logueado`.
