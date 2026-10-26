---
name: reportar-bug
description: Reglas de Alicia para redactar y publicar bugs como issues de GitHub a partir de casos de prueba fallidos (❌). Úsala siempre que se pida reportar, redactar, crear o revisar un bug o un issue, pasar a GitHub los casos que no coinciden, o cambiar "Bug: pendiente" por "Bug: #N". Prepara un borrador para que Alicia lo revise y solo publica cuando ella lo aprueba.
---

# Reportar bugs: de caso fallido a issue

Objetivo: que quien lea el issue reproduzca el bug a la primera, sin conocer los casos ni preguntar nada, y que se pueda seguir el hilo caso → issue → caso.

Quien decide es Alicia: la skill redacta, ella revisa y aprueba. Nunca se publica un issue sin su "sí" explícito a ese borrador concreto.

## Flujo de trabajo
1. **Reúne los casos.** Alicia da los Ids (`TC-CHECKOUT-012`) o pide "los bugs pendientes" de un archivo. Busca cada Id en todos los archivos de `casos/` y lee las filas completas, incluida la sección "Datos y estados de partida" de su archivo. Lee también la guía de bugs del repo si existe (`docs/flujo-de-bugs.md`) y la plantilla (`.github/ISSUE_TEMPLATE/bug.md`): si dicen algo distinto de esta skill, mandan ellas.
   Lee las etiquetas del repo con sus descripciones (`gh label list` o `https://api.github.com/repos/<dueño>/<repo>/labels`) y los tableros (`gh project list --owner <dueño>`). Son la fuente para elegir etiquetas y proyecto.
2. **Agrupa por causa.** Un issue por bug, no por caso: si varios casos ❌ se arreglarían con el mismo cambio, van en un solo issue (por ejemplo, "solo espacios" en tres campos). Si dudas, propón la agrupación y pregunta.
3. **Busca duplicados.** Lista los issues abiertos (`gh issue list --state all --search "TC-CHECKOUT-012"` o, sin gh, `https://api.github.com/repos/<dueño>/<repo>/issues?state=all`). Si un caso ya tiene issue, dilo y no lo redactes otra vez.
4. **Pregunta por la reproducción.** Antes de redactar, pide a Alicia para cada bug: si lo reprodujo a mano, en qué navegador, en qué fecha y con qué datos exactos. Los casos ejecutados por un agente (clics o campos por script, ver "Registro de ejecuciones" del archivo de casos) no cuentan como reproducción. Si no lo ha reproducido, puedes redactar el borrador, pero márcalo `⚠️ Pendiente de reproducir` y no lo publiques.
5. **Redacta el borrador** con el formato de abajo y muéstralo en el chat: título, etiquetas y descripción en bloques de código para copiar. Nombra cada borrador por los Ids de sus casos (`TC-CHECKOUT-013 + 037`), nunca con letras o números inventados ("Bug A"), y usa ese mismo nombre en las decisiones y en los mensajes siguientes. Debajo, una lista corta de **decisiones a revisar** (agrupación, severidad, prioridad y cualquier dato que hayas supuesto).
6. **Aplica sus correcciones** y vuelve a mostrar solo lo que cambió.
7. **Publica** cuando Alicia lo apruebe (ver "Publicar").
8. **Cierra el hilo** en el archivo de casos (ver "Después de publicar").

## Formato del issue
Sigue la plantilla del repo si existe. Encabezados en inglés (Steps, Observed, Expected) y el resto en español.

**Título:** `Bug Fixing - [Flujo] - [Módulo] - [Pantalla] - Descripción`
- Exactamente 4 bloques antes de la descripción, con los nombres que muestra la aplicación. Ejemplo: `Checkout - Checkout Step One - Your Information`. En una API, la pantalla es el endpoint: `Reservas - Booking - PUT /booking/{id}`.
- Descripción corta en presente, que diga el fallo y no el caso: "Los campos aceptan solo espacios". Máximo unos 100 caracteres en total para que GitHub no lo corte.

**Descripción, en este orden:**
1. `Casos: TC-XXX-NNN, TC-XXX-NNN (casos/<archivo>.md)`: siempre la primera línea, seguida de una línea en blanco.
2. `Precondiciones:` solo si el bug necesita un estado especial. Nunca uses los nombres de "Datos y estados de partida" ("Carrito A"): escribe lo que significan (usuario, contraseña, productos).
3. `Steps:` desde cero, empezando por la URL y el login. Un paso por acción, numerados. Incluye el paso que provoca el bug. En una API: método, URL, cabeceras y cuerpo de la petición, en un bloque de código.
4. **Variantes:** si varios casos solo cambian un dato, escribe los pasos una vez con un paso "Rellenar los campos según la variante de la tabla" y añade una tabla con una fila por caso. Deja una línea en blanco encima de la tabla.
5. `Observed:` lo que pasa, en presente. Si hay variantes, di si pasa en todas. Deja un hueco `(captura)` donde Alicia pegará la imagen.
6. `Expected:` copia el Esperado del caso ("Debería…"). Si una parte es "A confirmar", no la inventes: va en Notas.
7. `Notas:` en este orden: origen del Esperado (`Resultado esperado por criterio QA, pendiente de validar con el PO`, `Requisito: …` o `Comportamiento estándar de la web`), cada "A confirmar" pendiente, casos relacionados que no son del bug y `Entorno: <web> · <navegador> · <DD/MM/AAAA>` de la reproducción de Alicia.

## Etiquetas
Usa solo etiquetas que existan en el repo. Si falta una que el formato necesita, no la inventes en el issue: avisa a Alicia para que la cree con el formato `Categoría: valor` y el mismo color que las de su categoría.
- **Siempre** `bug`.
- **Componente:** según dónde está el fallo. Se ve en la interfaz y no hay API de por medio → `Componente: frontend`. Falla una respuesta de API o un servidor → `Componente: backend`. Si no lo sabes, propón uno y ponlo en "decisiones a revisar".
- **Modulo:** sale del Id (`TC-<MÓDULO>-NNN`), pero el nombre de la etiqueta puede estar en otro idioma: busca entre las etiquetas `Modulo:` del repo la que corresponde (`TC-INVENTORY` → `Modulo: inventario`). Si no hay ninguna, propón el nombre en minúscula y sin tilde, en el idioma de las demás.
- **Severidad** (cuánto daño hace; la propone QA). Usa las descripciones de las etiquetas del repo. Si no tienen descripción: alta = bloquea una funcionalidad principal; media = afecta al uso; baja = detalle visual o menor.
- **Prioridad** (cuándo arreglarlo; la decide negocio). Propónla según las descripciones del repo y márcala en "decisiones a revisar".
- Si Alicia elige algo distinto de tu propuesta, respétalo y pregunta solo si quiere dejar el motivo en Notas.
- **Proyecto:** si el repo tiene un solo tablero, úsalo. Si tiene varios o ninguno, pregunta la primera vez.

## Reglas
1. **Nada que no se haya observado.** No escribas efectos, mensajes ni datos que no estén en el caso o en lo que Alicia vio. Si algo te parece probable, va como pregunta en "decisiones a revisar", no en el issue.
2. **Los datos de los pasos son los que se usaron de verdad.** Si Alicia reprodujo con `46021` y el caso dice `28001`, el issue dice `46021`. Los datos tienen que coincidir con las capturas.
3. **Nombres exactos de la aplicación** entre comillas dobles ("Checkout", "Zip/Postal Code"); valores, URLs y código entre comillas invertidas fuera de los bloques de código.
4. **Revisa la ortografía**: tildes ("vacío"), encabezados ("Expected"), números de pasos seguidos y sin dobles espacios.
5. **Una captura por estado relevante** (antes y después) basta. Las capturas solo se pueden añadir en la web: recuérdale a Alicia dónde pegarlas.

## Publicar
- **Con GitHub CLI** (`gh` instalado y con sesión iniciada; compruébalo con `gh auth status`): guarda la descripción en un archivo temporal y ejecuta
  `gh issue create --title "<título>" --body-file <archivo> --label "bug" --label "<Componente>" --label "<Modulo>" --label "<Severidad>" --label "<Prioridad>" --project "<tablero>"` (sin `--project` si no hay tablero).
  Si falla `--project` por permisos, publica sin él y dile a Alicia que ejecute `gh auth refresh -s project`.
  Después dale el enlace del issue y recuérdale que entre con **Edit** a pegar las capturas.
- **Sin GitHub CLI**: deja el borrador listo para copiar y dile que lo cree en Issues → New issue → **Bug**.
- Publica de uno en uno y en el orden de los borradores, para que los números (#N) sean predecibles.

## Después de publicar
Cuando tengas el número de cada issue:
- En `casos/<funcionalidad>.md`, en las Notas de cada caso del issue, cambia `Bug: pendiente` por `Bug: [issue #N](https://github.com/<dueño>/<repo>/issues/N)`. El enlace va completo porque en un archivo `.md` del repo `#N` no se convierte en enlace.
- Actualiza la frase de bugs del Resumen (por ejemplo, "8 bugs pendientes de reportar") para que cuadre.
- No toques ningún otro archivo. Alicia hace el commit y el PR.

## Lista de comprobación antes de mostrar el borrador
- [ ] Un issue por causa; ningún caso está ya en otro issue.
- [ ] Título con 4 bloques y una descripción corta del fallo.
- [ ] Primera línea `Casos:` con todos los Ids y el archivo.
- [ ] Pasos desde cero, sin nombres internos de los casos y con los datos que usó Alicia.
- [ ] Variantes en tabla si solo cambia un dato.
- [ ] Expected copiado del caso; lo "A confirmar" está en Notas.
- [ ] Notas con el origen del Esperado y el Entorno de la reproducción.
- [ ] Etiquetas: `bug`, Componente, Modulo, Severidad y Prioridad.
- [ ] Nada inventado; las dudas están en "decisiones a revisar".
- [ ] Si no está reproducido a mano: `⚠️ Pendiente de reproducir` y sin publicar.
