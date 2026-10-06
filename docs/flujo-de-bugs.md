# Flujo de gestión de bugs

```mermaid
stateDiagram-v2
    direction LR
    state "Por hacer" as PorHacer
    state "En progreso" as EnProgreso
    state "Ready for QA" as ReadyQA
    state "Reabierto" as Reabierto
    state "Finalizada" as Finalizada
    state "Cerrada" as Cerrada
    [*] --> PorHacer: QA reporta el bug
    PorHacer --> EnProgreso: Dev lo toma
    PorHacer --> Cerrada: Duplicado / no es bug
    EnProgreso --> ReadyQA: Dev lo corrige
    ReadyQA --> Finalizada: QA verifica OK
    ReadyQA --> Reabierto: QA verifica y sigue fallando
    Reabierto --> EnProgreso: Dev lo retoma
    Finalizada --> [*]
    Cerrada --> [*]
```

## Estados

| Estado | Significado | Responsable |
|---|---|---|
| **Por hacer** | Bug reportado, pendiente de asignar | QA reporta |
| **En progreso** | El desarrollador lo está corrigiendo | Dev |
| **Ready for QA** | Corregido, pendiente de verificación | QA |
| **Reabierto** | QA lo verificó y sigue fallando; vuelve a desarrollo | Dev |
| **Finalizada** | QA lo verificó y funciona correctamente | QA cierra |
| **Cerrada** | Cerrado sin corrección: duplicado o no es un bug | QA / PO |

## Reglas
- Un bug solo pasa a **Finalizada** cuando el QA lo verifica, no cuando el desarrollador dice que está arreglado.
- Al pasar a **Cerrada**, se deja un comentario con el motivo (por ejemplo: "Duplicado de #3").
- Cada bug lleva etiquetas de **Severidad**, **Prioridad**, **Componente** y **Módulo**.

## Convención de títulos
`Bug Fixing - [Flujo] - [Módulo] - [Pantalla] - Descripción del problema`

Ejemplo: `Bug Fixing - Login - Inventory - Products - Todas las imágenes de productos muestran la misma foto de un perro`
