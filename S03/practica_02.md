# Computación Cuántica y Natural
## Práctica: Las Puertas de Pauli
### Unidad II: Fundamentos de los sistemas cuánticos - Sesión 03

## 1. Objetivo de la actividad
Comprender el funcionamiento de las puertas de Pauli y su implementación usando PyQuil.

## 2. Resultados de aprendizaje
- RA01: Conocer los fundamentos de los sistemas cuánticos y sus aplicaciones
- RA06: Identificar las posibles aplicaciones futuras de la computación cuántica y natural en las empresas
- RA07: Utilizar herramientas de software en el ámbito de la asignatura

## 3. Descripción teórica
Las puertas de Pauli son tres puertas fundamentales de la mecánica cuántica que operan sobre 1 cúbit. Nombradas por Wolfgang Pauli, son esenciales en la corrección de errores cuánticos.

### Puertas X, Y, Z
- **Puerta X**: Equivalente a la puerta NOT clásica. Realiza una inversión de 180º en el eje X.
- **Puerta Z**: Rota los valores en el eje Z, modificando la fase para el estado |1> y manteniéndola para |0>.
- **Puerta Y**: Ejecuta una rotación en el eje Y, combinando cambios de estado y fase.

## 4. Ejercicios prácticos
1. Utilizar el wavesimulator para todas las pruebas
2. Para las puertas Z e Y:
    - Crear dos programas con estados iniciales |0> y |1>
    
### Estructura de cada programa:
1. Definir programa con memoria y estado inicial
2. Ejecutar wavesimulator e imprimir función de onda
3. Añadir puerta lógica usando `prog.inst(X)`
4. Re-ejecutar wavesimulator e imprimir nueva función de onda

### Ejercicio adicional:
Implementar la puerta Y mediante combinación de otras puertas y el número imaginario (1j) en Python. Desarrollar dos programas demostrativos para ambos estados iniciales.
