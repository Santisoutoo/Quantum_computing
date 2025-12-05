# Práctica S14 - Conceptos Avanzados de PyQuil

Esta práctica cubre tres conceptos avanzados de programación cuántica con PyQuil:

1. **Multithreading** - Ejecución paralela de circuitos cuánticos
2. **Control Clásico** - Estructuras if/while dentro de circuitos cuánticos
3. **Acceso a QPU Real** - Guía para usar hardware cuántico real

## 📁 Estructura del Proyecto

```
S14/
├── README.md                          # Este archivo
├── GUIA_RAPIDA.md                    # Guía de inicio rápido
├── ESTILO_CODIGO.md                  # Guía de estilo de código
├── requirements.txt                   # Dependencias
├── main.py                           # Script principal
├── pr.py                             # Acceso rápido a demos
├── test_rapido.py                    # Tests de verificación
│
├── utils/                            # Utilidades comunes
│   ├── __init__.py
│   └── quantum_utils.py              # Funciones utilitarias
│
├── entregable1_multithreading/       # Entregable 1
│   ├── __init__.py
│   ├── moneda_cuantica.py           # Implementación multithreading
│   └── ejemplo_uso.py               # Ejemplos de uso
│
├── entregable2_control_clasico/      # Entregable 2
│   ├── __init__.py
│   ├── juego_moneda_trampa.py       # Control clásico IF/WHILE
│   └── ejemplo_uso.py               # Ejemplos de uso
│
└── docs/                             # Documentación
    └── guia_qpu_real.md             # Guía completa de acceso a QPU
```

## 💻 Estilo de Código

Esta práctica sigue tu estilo personal de programación cuántica. Los programas se crean de forma compacta y se ejecutan usando `.get_register_map().get("ro")`.

**Ejemplo básico:**
```python
from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare

prog = Program(
    Declare("ro", "BIT", 1),
    H(0),
    MEASURE(0, ("ro", 0))
).wrap_in_numshots_loop(10)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")
```

📖 **Ver [ESTILO_CODIGO.md](ESTILO_CODIGO.md) para más detalles y ejemplos completos**

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip instalado

### Instalar Dependencias

```bash
# Desde el directorio S14
pip install -r requirements.txt
```

El archivo `requirements.txt` incluye:
```
pyquil>=4.0.0
numpy>=1.20.0
matplotlib>=3.3.0
```

### Verificar Instalación

```bash
python -c "from pyquil import get_qc; print('PyQuil instalado correctamente')"
```

## 📖 Uso

### Opción 1: Script Principal (Recomendado)

Ejecuta el script principal para ver todos los ejemplos:

```bash
python main.py
```

Este script ejecutará:
1. Demostración de multithreading
2. Demostración de control clásico
3. Información sobre acceso a QPU real

### Opción 2: Entregables Individuales

#### Entregable 1: Multithreading

```bash
cd entregable1_multithreading
python ejemplo_uso.py
```

**Características:**
- Competición de 4 monedas cuánticas
- Comparación secuencial vs paralelo
- Análisis de rendimiento (speedup)
- Demostración de escalabilidad

**Uso programático:**

```python
from entregable1_multithreading import (
    competicion_cuatro_monedas_multithreading,
    analizar_resultados,
    imprimir_resultados
)

# Ejecutar competición con multithreading
resultados, tiempo = competicion_cuatro_monedas_multithreading(num_tiradas=50)

# Analizar resultados
analisis = analizar_resultados(resultados)
imprimir_resultados(analisis, tiempo)
```

#### Entregable 2: Control Clásico

```bash
cd entregable2_control_clasico
python ejemplo_uso.py
```

**Características:**
- Control IF para detección de trampas
- Control WHILE para verificación iterativa
- Protocolo BB84 simplificado
- Análisis de entrelazamiento

**Uso programático:**

```python
from entregable2_control_clasico import (
    juego_moneda_con_control_if,
    protocolo_bb84_simplificado,
    ejecutar_analisis_completo
)

# Ejecutar juego con control IF
prog = juego_moneda_con_control_if()
print(prog)

# Ejecutar análisis completo
ejecutar_analisis_completo()
```

## 📚 Contenido de los Entregables

### Entregable 1: Multithreading

**Objetivo**: Implementar multithreading para ejecutar múltiples circuitos cuánticos en paralelo.

**Conceptos cubiertos:**
- Thread-safety de objetos QVM
- `concurrent.futures.ThreadPoolExecutor`
- Paralelización de ejecuciones cuánticas
- Análisis de rendimiento y speedup

**Ejercicio implementado:**
Competición de monedas cuánticas donde 4 monedas se lanzan 50 veces cada una. Se compara la ejecución secuencial vs paralela.

**Resultados esperados:**
- Reducción del tiempo de ejecución con multithreading
- Speedup cercano al número de threads (en sistemas con múltiples cores)
- Ventajas claras en escenarios con múltiples circuitos independientes

**Referencias:**
- [PyQuil Multithreading Guide](https://pyquil-docs.rigetti.com/en/latest/advanced_usage.html#multithreading)

---

### Entregable 2: Control Clásico

**Objetivo**: Implementar estructuras de control clásico (IF/WHILE) dentro de circuitos cuánticos.

**Conceptos cubiertos:**
- Instrucciones IF-THEN-ELSE en Quil
- Control de flujo basado en mediciones
- Protocolos de verificación cuántica
- Detección de anomalías mediante entrelazamiento

**Ejercicios implementados:**

1. **Juego sin control**: Baseline sin verificación
2. **Juego con IF**: Detección condicional de trampas
3. **Juego con WHILE**: Verificación iterativa
4. **Protocolo BB84**: Distribución de claves cuánticas

**Caso de uso: Detección de Trampas**

El escenario implementa un protocolo donde Alice prepara qubits entrelazados y envía uno a Bob. Si Bob intenta medirlo prematuramente (hacer trampa), se rompe el entrelazamiento y Alice lo detecta usando control clásico IF.

**Referencias:**
- [PyQuil Classical Control Flow](https://pyquil-docs.rigetti.com/en/latest/advanced_usage.html#classical-control-flow)
- [BB84 Protocol](https://en.wikipedia.org/wiki/BB84)

---

### Documentación: Acceso a QPU Real

**Objetivo**: Proporcionar una guía completa para solicitar acceso y usar computadores cuánticos reales.

**Contenido:**
- Proceso de solicitud de acceso a Rigetti QCS
- Diferencias entre QVM (simulador) y QPU (hardware real)
- Configuración de credenciales y entorno
- Mejores prácticas para ejecución en QPU
- Gestión de cuotas y optimización de circuitos
- Consideraciones de topología y calibración

**Archivo**: [`docs/guia_qpu_real.md`](docs/guia_qpu_real.md)

## 🔬 Conceptos Técnicos

### Multithreading en PyQuil

PyQuil garantiza que los objetos relacionados con QVM (Quantum Virtual Machine) son **thread-safe**:

```python
from concurrent.futures import ThreadPoolExecutor

# Los objetos QVM se pueden usar de forma segura desde múltiples threads
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(ejecutar_circuito, i) for i in range(4)]
    resultados = [f.result() for f in futures]
```

**Ventajas:**
- Reducción del tiempo de ejecución en sistemas multi-core
- Paralelización natural de experimentos independientes
- Mejor utilización de recursos computacionales

### Control Clásico en Quil

Quil soporta instrucciones de control clásico que permiten tomar decisiones basadas en resultados de mediciones:

```
MEASURE 0 ro[0]
JUMP-WHEN @then ro[0]
H 1
JUMP @end
LABEL @then
X 1
LABEL @end
```

En PyQuil, esto se simplifica con:

```python
prog.if_then(("ro", 0), Program(X(1)), Program(H(1)))
```

**Aplicaciones:**
- Algoritmos adaptativos
- Corrección de errores
- Protocolos de verificación
- Criptografía cuántica

### QPU vs QVM

| Característica | QVM | QPU |
|---------------|-----|-----|
| Tipo | Simulador clásico | Hardware cuántico real |
| Velocidad | Rápida (pocos qubits) | Latencia de red + ejecución |
| Ruido | Opcional/ideal | Real e inevitable |
| Acceso | Libre 24/7 | Requiere cuota y aprobación |
| Costo | Gratuito | Pago o cuota limitada |

## 🎯 Objetivos de Aprendizaje

Al completar esta práctica, deberías ser capaz de:

- ✅ Implementar ejecución paralela de circuitos cuánticos usando multithreading
- ✅ Analizar mejoras de rendimiento y calcular speedup
- ✅ Usar estructuras de control clásico (IF/WHILE) en circuitos cuánticos
- ✅ Implementar protocolos de verificación cuántica
- ✅ Comprender las diferencias entre simuladores y hardware real
- ✅ Solicitar y configurar acceso a QPUs reales
- ✅ Optimizar circuitos para ejecución en hardware real

## 📊 Resultados Esperados

### Multithreading

Ejecutando con 4 threads en un sistema con 4+ cores:

```
Tiempo secuencial:     ~2.5s
Tiempo multithreading: ~0.8s
Speedup:               ~3x
Mejora:                ~68%
```

### Control Clásico

El protocolo de detección de trampas debería mostrar:

```
Sin trampa:     Correlación ~100% en qubits entrelazados
Con trampa:     Correlación ~50% (decorrelación observable)
Detección:      >90% de precisión
```

## 🐛 Solución de Problemas

### Error: "No module named 'pyquil'"

```bash
pip install --upgrade pyquil
```

### Error: "Connection refused" al conectar a QVM

```bash
# Instalar y ejecutar quilc y qvm localmente
# Ver: https://pyquil-docs.rigetti.com/en/latest/start.html#downloading-the-qvm-and-compiler
```

### Multithreading no mejora el rendimiento

- Verifica que tu sistema tenga múltiples cores
- El QVM simula operaciones cuánticas, el speedup depende de la carga computacional
- Para circuitos muy simples, el overhead de threads puede dominar

### Control clásico no funciona como esperado

- Verifica la versión de PyQuil (requiere >=4.0)
- Algunos backends no soportan todas las instrucciones de control
- Usa `print(prog)` para inspeccionar el código Quil generado

## 📖 Referencias

### Documentación Oficial

- [PyQuil Documentation](https://pyquil-docs.rigetti.com/)
- [Quil Specification](https://github.com/quil-lang/quil)
- [Rigetti QCS](https://qcs.rigetti.com/)

### Artículos y Tutoriales

- [Multithreading Guide](https://pyquil-docs.rigetti.com/en/latest/advanced_usage.html#multithreading)
- [Classical Control Flow](https://pyquil-docs.rigetti.com/en/latest/advanced_usage.html#classical-control-flow)
- [QPU Execution](https://pyquil-docs.rigetti.com/en/latest/the_quantum_computer.html#the-quantum-processing-unit-qpu)

### Papers

- BB84 Protocol: Bennett & Brassard (1984)
- Quantum Entanglement and Verification: Ekert (1991)
- Rigetti QPU Architecture: [arXiv:2001.00054](https://arxiv.org/abs/2001.00054)

## 👨‍🎓 Autor

Práctica desarrollada para la asignatura de Computación Cuántica.

## 📝 Licencia

Este proyecto es material educativo para uso académico.

---

**Nota**: Los ejemplos están diseñados para ejecutarse en QVM (simulador). Para ejecutar en QPU real, necesitarás solicitar acceso siguiendo la guía en [`docs/guia_qpu_real.md`](docs/guia_qpu_real.md).
