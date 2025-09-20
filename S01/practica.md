# Computación Cuántica y Natural
## Práctica 1: Introducción a PyQuil

## 1. Objetivo

El objetivo de esta práctica es preparar el entorno de desarrollo para PyQuil y crear los primeros programas funcionales.

## 2. Resultados de Aprendizaje

- RA01: Conocer los fundamentos de los sistemas cuánticos y sus aplicaciones
- RA06: Identificar aplicaciones futuras de la computación cuántica y natural en empresas
- RA07: Utilizar herramientas de software específicas del campo

## 3. Descripción del Entorno

### 3.1 Componentes del Quil SDK

El SDK de Quil incluye:
- **pyQuil**: Librería para construcción y ejecución de programas
- **quilc**: Compilador
- **QVM**: Simulador cuántico

### 3.2 Instalación

Opciones disponibles:

1. **Docker con Forest SDK completo**:
```bash
docker run --rm -it rigetti/forest
```

2. **Docker con componentes separados**:
```bash
docker run --rm -it -p 5555:5555 rigetti/quilc -P -S
docker run --rm -it -p 5000:5000 rigetti/qvm -S
```

3. **Instalación local**: 
    - Descargar SDK desde [qcs.rigetti.com/sdk-downloads](https://qcs.rigetti.com/sdk-downloads)

### 3.3 Configuración del Entorno Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install pyquil
```

### 3.4 Estados de Bell

Los estados de Bell son estados cuánticos de dos qubits que representan el máximo entrelazamiento cuántico.

Se presentan cuatro circuitos diferentes para generar los estados de Bell, comenzando con el más básico que utiliza:
- Una puerta Hadamard
- Una puerta CNOT
- Estado inicial |0⟩

**Nota**: Se recomienda verificar la inicialización correcta de los qubits en los programas de ejemplo.

