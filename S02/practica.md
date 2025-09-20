# Computación Cuántica y Natural
## Actividad Práctica - Unidad I: Introducción a la Computación Cuántica y Natural
### Sesión 01: La moneda perfecta


## 1. Objetivo de la actividad

El objetivo de la presente actividad es explicar el funcionamiento de la puerta de Hadamard, una de las puertas claves de la computación cuántica, y cómo se puede usar con PyQuil.

## 2. Resultados de aprendizaje relacionados

- Conocer los fundamentos de los sistemas cuánticos y sus aplicaciones (RA01)
- Identificar las posibles aplicaciones futuras de la computación cuántica y natural en las empresas (RA06)
- Utilizar herramientas de software en el ámbito de la asignatura (RA07)

## 3. Descripción de la actividad

La puerta de Hadamard, o puerta H, es una puerta de cúbit único (aunque en lecciones posteriores veremos que puede verse amplificada para n-cúbits mediante operaciones matriciales) fundamental en computación cuántica de cara a garantizar la generación de programas realmente cuánticos. Su importancia está basada en su capacidad para generar estados de superposición, es decir, partiendo de un estado |0⟩ en una puerta cuántica, podremos pasar a un estado |0⟩ y |1⟩, y viceversa con el estado |1⟩.

### Fases del proyecto

El objetivo es construir un sistema de moneda perfecta cuántica en tres fases:

1. **Sistema Simple:**
    - Construir sistema con un solo cúbit aplicando puerta Hadamard
    - Realizar una medida y obtener cara/cruz aleatoriamente
    - Requisitos específicos:
      - Una sola ejecución
      - Usar funciones `declare` y `measure`
      - Imprimir resultado (0=cara, 1=cruz)

2. **Competición entre dos usuarios:**
    - Usuario A (gana cara) vs Usuario B (gana cruz)
    - 50 lanzamientos
    - Determinar ganador
    - Analizar diferencias entre iteraciones y múltiples ejecuciones

3. **Sistema con cuatro monedas:**
    - Mismos competidores
    - 50 lanzamientos por moneda
    - Implementar usando dos técnicas:
      - Modificación del registro para valores separados
      - Uso de función `measure_all`
