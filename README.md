# QA con IA sobre Sauce Demo

Proyecto de portafolio de QA sobre [Sauce Demo](https://www.saucedemo.com), una tienda online de práctica.
Uso IA para generar casos de prueba y después los valido uno a uno contra la aplicación real,
para medir cuánto acierta y documentar dónde se equivoca.

## Resultados

| Funcionalidad | Casos generados por IA | Correctos | Acierto | Revisión |
|---|---|---|---|---|
| Login | 8 | 7 | 87,5% | [casos/login-revision-ia.md](casos/login-revision-ia.md) |

## Próximamente

- Automatización de los casos validados con Playwright.
- Agente explorador con IA que navega la web y reporta bugs.
- Playwright Agents (planner, generator, healer) para generar y reparar tests.
