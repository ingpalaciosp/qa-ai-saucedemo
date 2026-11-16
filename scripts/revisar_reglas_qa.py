"""Linter de las reglas de QA del framework (las marcadas con (CI) en CLAUDE.md).

Lee el código sin ejecutarlo y avisa de lo que no cumple las normas.
Se ejecuta en el CI antes de los tests y también en local:
    python scripts/revisar_reglas_qa.py

Usa el módulo ast de Python, que convierte el código en un árbol (archivo -> funciones ->
llamadas). Así sabe qué hay dentro de cada test y no confunde el código con los comentarios.

Excepción justificada: si una línea lleva el comentario "# norma-ok: <motivo>", no se marca.
"""

import ast
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
EXCEPCION = "# norma-ok:"
ID_EN_NOMBRE = re.compile(r"^test_tc_[a-z]+_\d{3}_")  # test_tc_sort_004_...
ID_DE_FILA = re.compile(r"^TC-[A-Z]+-\d{3}")  # id="TC-SORT-001_..."
POSICION_O_XPATH = re.compile(r"nth-child|nth-of-type|xpath|^//")


def nombre_de_la_llamada(llamada: ast.Call) -> str:
    """expect(...) -> "expect"; page.locator(...) -> "locator"."""
    if isinstance(llamada.func, ast.Name):
        return llamada.func.id
    if isinstance(llamada.func, ast.Attribute):
        return llamada.func.attr
    return ""


def texto_del_selector(llamada: ast.Call) -> str | None:
    """El texto del primer argumento si es un texto fijo o un f-string; si no, None."""
    if not llamada.args:
        return None
    argumento = llamada.args[0]
    if isinstance(argumento, ast.Constant) and isinstance(argumento.value, str):
        return argumento.value
    if isinstance(argumento, ast.JoinedStr):  # f'[data-test="add-to-cart-{producto_id}"]'
        return "".join(p.value for p in argumento.values if isinstance(p, ast.Constant))
    return None


def tiene_aserción(test: ast.FunctionDef) -> bool:
    """¿Hay algún expect(...) o assert en cualquier parte de la función?"""
    for nodo in ast.walk(test):
        if isinstance(nodo, ast.Assert):
            return True
        if isinstance(nodo, ast.Call) and nombre_de_la_llamada(nodo) == "expect":
            return True
    return False


def tiene_id_de_caso(test: ast.FunctionDef) -> bool:
    """El Id va en el nombre, o en el id= de TODAS las filas de su parametrize."""
    if ID_EN_NOMBRE.match(test.name):
        return True
    for decorador in test.decorator_list:
        if isinstance(decorador, ast.Call) and nombre_de_la_llamada(decorador) == "parametrize":
            tiene_tabla = len(decorador.args) > 1 and isinstance(decorador.args[1], ast.List)
            filas = decorador.args[1].elts if tiene_tabla else []
            ids = []
            for fila in filas:
                if isinstance(fila, ast.Call) and nombre_de_la_llamada(fila) == "param":
                    ids += [k.value.value for k in fila.keywords
                            if k.arg == "id" and isinstance(k.value, ast.Constant)]
            if filas and len(ids) == len(filas) and all(ID_DE_FILA.match(i) for i in ids):
                return True
    return False


def revisar_archivo(archivo: Path) -> list[tuple[int, str, str]]:
    """Devuelve (línea, qué pasa, cómo arreglarlo) por cada problema del archivo."""
    carpeta = archivo.relative_to(RAIZ).parts[0]  # "tests" o "pages"
    arbol = ast.parse(archivo.read_text(encoding="utf-8"))
    problemas = []

    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.Call):
            llamada = nombre_de_la_llamada(nodo)

            # Esperas fijas (tests y pages)
            if llamada in ("wait_for_timeout", "sleep"):
                problemas.append((nodo.lineno, "Espera fija",
                                  "espera algo concreto: expect(...) o wait_for_url(...), nunca un tiempo fijo"))

            if carpeta == "tests":
                # Selectores en los tests: locator(...), get_by_...(...) o un texto con data-test
                usa_data_test = any(
                    isinstance(a, ast.Constant) and isinstance(a.value, str) and "data-test" in a.value
                    for a in nodo.args
                )
                if llamada == "locator" or llamada.startswith("get_by_") or usa_data_test:
                    problemas.append((nodo.lineno, "Selector dentro de un test",
                                      "los selectores van en el Page Object de su pantalla (pages/)"))

            if carpeta == "pages":
                # Aserciones en los Page Objects
                if llamada == "expect":
                    problemas.append((nodo.lineno, "Aserción dentro de un Page Object",
                                      "las aserciones (expect) van en los tests; "
                                      "el Page Object solo tiene selectores y acciones"))
                # Selectores frágiles
                if llamada == "locator":
                    selector = texto_del_selector(nodo)
                    if selector is not None and "data-test" not in selector:
                        problemas.append((nodo.lineno, "Selector frágil (sin data-test)",
                                          "usa data-test; si el elemento no lo tiene, get_by_role o get_by_label"))
                    elif selector is not None and POSICION_O_XPATH.search(selector):
                        problemas.append((nodo.lineno, "Selector frágil (posición o XPath)",
                                          "no dependas de la posición ni de XPath: "
                                          "apunta al elemento por su data-test"))

        # Tests saltados: @pytest.mark.skip, @pytest.mark.skipif o pytest.skip(...)
        if carpeta == "tests" and isinstance(nodo, ast.Attribute) and nodo.attr in ("skip", "skipif"):
            problemas.append((nodo.lineno, "Test saltado (skip)",
                              "un test saltado no se ejecuta y nadie se entera; si de verdad hace falta, "
                              "deja el motivo con # norma-ok: <motivo> (por ejemplo, el bug que lo bloquea)"))

        # Todo Page Object hereda de BasePage
        if carpeta == "pages" and isinstance(nodo, ast.ClassDef) and nodo.name != "BasePage":
            if not any(isinstance(base, ast.Name) and base.id == "BasePage" for base in nodo.bases):
                problemas.append((nodo.lineno, "Page Object sin BasePage",
                                  f"{nodo.name} tiene que heredar de BasePage: class {nodo.name}(BasePage)"))

        # Reglas de cada test
        if carpeta == "tests" and isinstance(nodo, ast.FunctionDef) and nodo.name.startswith("test_"):
            if not tiene_aserción(nodo):
                problemas.append((nodo.lineno, "Test sin aserción",
                                  f"{nodo.name} no tiene ningún expect ni assert: pasaría siempre"))
            if not tiene_id_de_caso(nodo):
                problemas.append((nodo.lineno, "Test sin Id de caso",
                                  f"{nodo.name}: pon el Id en el nombre (test_tc_sort_001_...) "
                                  f"o en el id= de cada fila (id=\"TC-SORT-001_...\")"))

    # Quitar las líneas con excepción justificada
    lineas = archivo.read_text(encoding="utf-8").splitlines()
    return [p for p in problemas if EXCEPCION not in lineas[p[0] - 1]]


def revisar() -> list[str]:
    mensajes = []
    for carpeta in ("tests", "pages"):
        for archivo in sorted((RAIZ / carpeta).rglob("*.py")):
            ruta = archivo.relative_to(RAIZ).as_posix()
            lineas = archivo.read_text(encoding="utf-8").splitlines()
            for linea, que_pasa, como_arreglar in sorted(set(revisar_archivo(archivo))):
                mensajes.append(f"{ruta}:{linea}: {que_pasa} -> {como_arreglar}\n    {lineas[linea - 1].strip()}")
    return mensajes


if __name__ == "__main__":
    problemas = revisar()
    if problemas:
        print(f"Reglas de QA: {len(problemas)} problema(s)\n")
        print("\n".join(problemas))
        sys.exit(1)
    print("Reglas de QA: todo en orden")
