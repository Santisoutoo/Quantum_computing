# Guía de Estilo de Código - PyQuil

Este documento describe el estilo de código utilizado en esta práctica, siguiendo tus convenciones personales de programación cuántica.

## 📝 Convenciones Principales

### 1. Creación de Programas

**✅ CORRECTO - Estilo compacto en el constructor:**

```python
from pyquil import Program, get_qc
from pyquil.gates import H, X, MEASURE
from pyquil.quilbase import Declare

prog = Program(
    Declare("ro", "BIT", 2),
    X(0),
    H(1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1))
)
```

**❌ EVITAR - Estilo con operador +=:**

```python
# Este estilo funciona pero no es el preferido
prog = Program()
prog += Declare("ro", "BIT", 2)
prog += X(0)
prog += H(1)
# ...
```

### 2. Ejecución de Programas

**✅ CORRECTO - Usar wrap_in_numshots_loop y get_register_map:**

```python
# Para un solo shot
prog = Program(
    Declare("ro", "BIT", 1),
    H(0),
    MEASURE(0, ("ro", 0))
)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")

# Para múltiples shots
prog = Program(
    Declare("ro", "BIT", 1),
    H(0),
    MEASURE(0, ("ro", 0))
).wrap_in_numshots_loop(50)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")
```

**❌ EVITAR - Compilar por separado:**

```python
# Este estilo funciona pero no es el preferido
qvm = get_qc('9q-square-qvm')
executable = qvm.compile(prog)
result = qvm.run(executable)
measurements = result.readout_data['ro']
```

### 3. Acceso a Resultados

**✅ CORRECTO - Usar get_register_map().get("ro"):**

```python
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")
```

**❌ EVITAR - Usar readout_data directamente:**

```python
# Este estilo funciona pero no es el preferido
result = qvm.run(executable)
measurements = result.readout_data['ro']
```

## 📚 Ejemplos Completos

### Ejemplo 1: Moneda Cuántica Simple

```python
from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare

# Crear programa
prog = Program(
    Declare("ro", "BIT", 1),
    H(0),
    MEASURE(0, ("ro", 0))
).wrap_in_numshots_loop(1)

# Ejecutar
qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")

# Interpretar
if measurements[0][0] == 0:
    print("CARA")
else:
    print("CRUZ")
```

### Ejemplo 2: Múltiples Qubits con SWAP

```python
from pyquil import Program, get_qc
from pyquil.gates import X, I, SWAP, MEASURE
from pyquil.quilbase import Declare

# Programa sin SWAP
prog1 = Program(
    Declare("ro", "BIT", 2),
    X(0),
    I(1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1))
)

qvm = get_qc('9q-square-qvm')
result1 = qvm.run(qvm.compile(prog1))
print(result1.get_register_map().get("ro"))  # [[1 0]]

# Programa con SWAP
prog2 = Program(
    Declare("ro", "BIT", 2),
    X(0),
    I(1),
    SWAP(0, 1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1))
)

result2 = qvm.run(qvm.compile(prog2))
print(result2.get_register_map().get("ro"))  # [[0 1]]
```

### Ejemplo 3: Competición de Monedas

```python
from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare
import numpy as np

# 4 monedas, 50 tiradas cada una
prog = Program(
    Declare("ro", "BIT", 4),
    H(0),
    H(1),
    H(2),
    H(3),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
    MEASURE(2, ("ro", 2)),
    MEASURE(3, ("ro", 3))
).wrap_in_numshots_loop(50)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")

# Contar resultados
caras_por_moneda = [
    np.sum(measurements[:, i] == 0)
    for i in range(4)
]

print(f"Caras por moneda: {caras_por_moneda}")
total_caras = sum(caras_por_moneda)
total_cruces = 200 - total_caras

if total_caras > total_cruces:
    print("Ganador: CARAS")
else:
    print("Ganador: CRUCES")
```

### Ejemplo 4: Control Clásico con IF

```python
from pyquil import Program, get_qc
from pyquil.gates import H, X, CNOT, MEASURE
from pyquil.quilbase import Declare

# Crear estado entrelazado con control IF
prog = Program()

# Declarar memoria
prog += Declare("ro", "BIT", 2)
prog += Declare("control", "BIT", 1)

# Preparar estado Bell
prog += H(0)
prog += CNOT(0, 1)

# Medir qubit de control
prog += H(2)
prog += MEASURE(2, ("control", 0))

# Control IF: aplicar X condicionalmente
prog.if_then(
    ("control", 0),
    Program(X(1)),  # Si control==1, aplicar X
    Program()       # Si no, no hacer nada
)

# Mediciones finales
prog += MEASURE(0, ("ro", 0))
prog += MEASURE(1, ("ro", 1))

# Ejecutar
qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
print(result.get_register_map().get("ro"))
```

## 🔧 Funciones Utilitarias

Las funciones utilitarias también siguen este estilo:

```python
def ejecutar_programa(program: Program, num_shots: int = 1,
                     qvm_name: str = '9q-square-qvm'):
    """Ejecuta un programa cuántico."""
    qvm = get_qc(qvm_name)
    program_wrapped = program.wrap_in_numshots_loop(num_shots)
    result = qvm.run(qvm.compile(program_wrapped))

    return result.get_register_map().get("ro")
```

## ✨ Ventajas de Este Estilo

1. **Compacto**: Programas más concisos y fáciles de leer
2. **Declarativo**: El programa se define todo de una vez
3. **Consistente**: Mismo patrón en todos los scripts
4. **Eficiente**: Menos líneas de código para la misma funcionalidad

## 📖 Referencia Rápida

```python
# Patrón básico
prog = Program(
    Declare("ro", "BIT", n),
    # ... puertas cuánticas ...
    MEASURE(qubit, ("ro", index))
).wrap_in_numshots_loop(shots)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")
```

---

**Nota**: Todos los módulos de esta práctica (entregable1, entregable2, utils) siguen este estilo de código de forma consistente.
