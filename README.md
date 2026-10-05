# QA con IA sobre Sauce Demo

Proyecto de portafolio de QA sobre [Sauce Demo](https://www.saucedemo.com), una tienda online de práctica.
Uso IA para generar casos de prueba y después los valido uno a uno contra la aplicación real,
para medir cuánto acierta y documentar dónde se equivoca.

## Resultados

| Funcionalidad | Casos generados por IA | Correctos | Acierto | Revisión |
|---|---|---|---|---|
| Login | 8 | 7 | 87,5% | [casos/login-revision-ia.md](casos/login-revision-ia.md) |

### Comparativa: sin contexto vs. con contexto (Login)

| Lección | Enfoque | Acierto | Textos inventados | Casos "A confirmar" | Casos |
|---|---|---|---|---|---|
| Lección 1 | Sin contexto | 87,5% | 1 | — | [casos/login-revision-ia.md](casos/login-revision-ia.md) |
| Lección 2 | Con contexto real (campos, usuarios y mensajes exactos) | 100% de los casos definidos | 0 | 1 (completado después por observación) | [casos/login-v2-con-contexto.md](casos/login-v2-con-contexto.md) |

**Lección aprendida:** más contexto = menos inventos. Cuando la IA recibe los datos reales de la
aplicación y la regla de escribir "A confirmar" si no sabe algo, deja de inventar textos y marca
las dudas para que se validen contra la aplicación.

### Resumen de la Lección 2: login con contexto

Casos: [casos/login-v2-con-contexto.md](casos/login-v2-con-contexto.md)

- **Casos que coincidieron:** 7 de 7 definidos (100%). Cubren los tres usuarios (`standard_user`,
  `locked_out_user`, `problem_user`), Username vacío, Password vacío, contraseña incorrecta y
  usuario inexistente.
- **Caso 8 (ambos campos vacíos):** la IA puso "A confirmar" porque no sabía el resultado. Lo ejecuté
  y lo completé con lo que observé: "Epic sadface: Username is required".
- **Lección aprendida:** si le doy a la IA el contexto real, no inventa, y si le pido que no suponga,
  admite lo que no sabe.

## Próximamente

- Automatización de los casos validados con Playwright.
- Agente explorador con IA que navega la web y reporta bugs.
- Playwright Agents (planner, generator, healer) para generar y reparar tests.
