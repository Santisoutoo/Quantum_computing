# Guía de Acceso a Computadores Cuánticos Reales (QPU)

Esta guía explica cómo solicitar acceso a los sistemas reales de Rigetti Computing (QCS - Quantum Cloud Services) y ejecutar circuitos en hardware cuántico real.

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Solicitud de Acceso a QCS](#solicitud-de-acceso-a-qcs)
4. [Configuración del Entorno](#configuración-del-entorno)
5. [Diferencias entre QVM y QPU](#diferencias-entre-qvm-y-qpu)
6. [Ejecución en QPU Real](#ejecución-en-qpu-real)
7. [Consideraciones Importantes](#consideraciones-importantes)
8. [Recursos Adicionales](#recursos-adicionales)

---

## Introducción

Un **Quantum Processing Unit (QPU)** es un procesador cuántico físico, en contraposición al **Quantum Virtual Machine (QVM)**, que es un simulador clásico.

**Ventajas de usar QPU real:**
- Experiencia con hardware cuántico real
- Observación de efectos de ruido real
- Validación de algoritmos en condiciones realistas

**Desventajas:**
- Tiempo de ejecución limitado (cuotas)
- Mayor latencia que el simulador
- Resultados afectados por ruido y decoherencia
- Disponibilidad limitada

---

## Requisitos Previos

Antes de solicitar acceso, asegúrate de tener:

- ✅ Cuenta de PyQuil configurada
- ✅ Conocimientos básicos de programación cuántica
- ✅ Experiencia previa con QVM
- ✅ Circuitos optimizados y probados en simulador
- ✅ Justificación académica o de investigación

---

## Solicitud de Acceso a QCS

### Paso 1: Crear una Cuenta

1. Visita [Rigetti QCS](https://qcs.rigetti.com/)
2. Haz clic en "Sign Up" o "Get Started"
3. Completa el formulario de registro

### Paso 2: Solicitar Acceso

Rigetti ofrece diferentes programas de acceso:

#### a) **Programa Académico**
- Para estudiantes e investigadores
- Requiere afiliación institucional verificada
- Puede incluir créditos gratuitos

**Cómo solicitar:**
```
- Email: partnerships@rigetti.com
- Asunto: "Academic Access Request - [Tu Universidad]"
- Incluir:
  * Carta de presentación
  * Afiliación institucional
  * Descripción del proyecto
  * Publicaciones previas (si las hay)
```

#### b) **Programa Quantum Advantage Prize**
- Competición para investigadores
- Acceso gratuito al QPU
- Más información: https://www.rigetti.com/

#### c) **Acceso Comercial**
- Pago por uso
- Sin periodo de espera
- Soporte prioritario

### Paso 3: Esperar Aprobación

- Tiempo de respuesta: 2-4 semanas
- Recibirás credenciales de acceso
- Se te asignará una cuota de tiempo de QPU

---

## Configuración del Entorno

Una vez aprobado el acceso:

### 1. Instalar QCS CLI

```bash
# Instalar el cliente de línea de comandos
pip install qcs-sdk-python

# Verificar instalación
qcs --version
```

### 2. Configurar Credenciales

```bash
# Iniciar sesión
qcs auth login

# Verificar conexión
qcs quantum-processors list
```

### 3. Configurar PyQuil

```python
from pyquil import get_qc
from pyquil.api import QCSClient

# Conectar al servicio QCS
client = QCSClient()

# Listar QPUs disponibles
qpus = client.list_quantum_processors()
print("QPUs disponibles:", qpus)
```

---

## Diferencias entre QVM y QPU

| Aspecto | QVM (Simulador) | QPU (Hardware Real) |
|---------|----------------|---------------------|
| **Velocidad** | Rápido para pocos qubits | Más lento (latencia de red) |
| **Ruido** | Configurable/ideal | Ruido real inevitable |
| **Costo** | Gratuito | Consume cuota |
| **Disponibilidad** | 24/7 | Horarios limitados |
| **Número de qubits** | Limitado por RAM | Limitado por hardware |
| **Resultados** | Deterministas (sin ruido) | Estocásticos (con ruido) |

---

## Ejecución en QPU Real

### Código de Ejemplo

```python
from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE
from pyquil.quilbase import Declare

def ejecutar_en_qpu():
    """
    Ejecuta un circuito simple en un QPU real.
    """
    # Crear el circuito
    prog = Program(
        Declare("ro", "BIT", 2),
        H(0),
        CNOT(0, 1),
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1))
    )

    # IMPORTANTE: Especificar un QPU real
    # Ejemplo: 'Aspen-M-3' (verificar disponibilidad)
    qpu = get_qc('Aspen-M-3', as_qvm=False)  # as_qvm=False para usar hardware real

    # Compilar para el QPU específico
    executable = qpu.compile(prog)

    # Ejecutar (esto consumirá cuota)
    num_shots = 1000
    result = qpu.run(executable.wrap_in_numshots_loop(num_shots))

    return result.readout_data['ro']

# Para probar sin consumir cuota, usar modo simulado:
def ejecutar_en_simulador_realista():
    """
    Simula un QPU real incluyendo ruido.
    """
    # as_qvm=True simula el QPU sin consumir cuota
    qpu = get_qc('Aspen-M-3', as_qvm=True)
    # ... resto del código igual
```

### Optimización para QPU

Antes de ejecutar en hardware real, optimiza tu circuito:

```python
from pyquil.api import QPUCompiler

# 1. Minimizar profundidad del circuito
# 2. Reducir número de puertas
# 3. Usar puertas nativas del QPU
# 4. Considerar la topología del chip

# Compilar con optimización
compiler = QPUCompiler(quantum_processor_id='Aspen-M-3')
native_quil = compiler.quil_to_native_quil(prog)
executable = compiler.native_quil_to_executable(native_quil)
```

---

## Consideraciones Importantes

### 1. **Gestión de Cuota**

- Cada ejecución consume tiempo de tu cuota asignada
- Usa `as_qvm=True` para probar sin consumir cuota
- Optimiza circuitos antes de ejecutar en hardware real

```python
# BUENA PRÁCTICA: Probar primero en simulador
qvm = get_qc('Aspen-M-3', as_qvm=True)  # No consume cuota
resultado_prueba = qvm.run(executable)

# Solo después ejecutar en hardware real
qpu = get_qc('Aspen-M-3', as_qvm=False)  # Consume cuota
resultado_real = qpu.run(executable)
```

### 2. **Topología del Chip**

Los QPUs tienen conectividad limitada entre qubits:

```python
# Verificar topología
from pyquil.api import get_qc

qpu = get_qc('Aspen-M-3')
topology = qpu.quantum_processor.qubits()
edges = qpu.quantum_processor.edges()

print(f"Qubits disponibles: {topology}")
print(f"Conexiones: {edges}")
```

### 3. **Calibración**

Los QPUs se calibran regularmente:

```python
# Obtener datos de calibración actuales
specs = qpu.quantum_processor.get_specs()

# T1, T2, fidelidad de puertas, etc.
for qubit in specs.qubits:
    print(f"Qubit {qubit}: T1={specs.t1[qubit]}μs, T2={specs.t2[qubit]}μs")
```

### 4. **Manejo de Errores**

```python
import time
from pyquil.api import QCSClient

def ejecutar_con_reintentos(qpu, executable, max_intentos=3):
    """
    Ejecuta en QPU con manejo de errores.
    """
    for intento in range(max_intentos):
        try:
            resultado = qpu.run(executable)
            return resultado
        except Exception as e:
            print(f"Intento {intento + 1} falló: {e}")
            if intento < max_intentos - 1:
                time.sleep(5)  # Esperar antes de reintentar
            else:
                raise
```

---

## Recursos Adicionales

### Documentación Oficial

- **PyQuil Documentation**: https://pyquil-docs.rigetti.com/
- **QCS User Guide**: https://docs.rigetti.com/qcs/
- **Quil Specification**: https://github.com/quil-lang/quil

### Tutoriales

1. **Getting Started with QCS**: https://pyquil-docs.rigetti.com/en/latest/getting_started.html
2. **The Quantum Computer**: https://pyquil-docs.rigetti.com/en/latest/the_quantum_computer.html
3. **QPU Execution**: https://pyquil-docs.rigetti.com/en/latest/advanced_usage.html#the-quantum-processing-unit-qpu

### Comunidad

- **Rigetti Slack Community**: https://rigetti-forest.slack.com/
- **GitHub Issues**: https://github.com/rigetti/pyquil/issues
- **Stack Overflow**: Tag `[pyquil]`

### Papers y Publicaciones

- Rigetti's QPU Architecture: https://arxiv.org/abs/2001.00054
- Quantum Advantage Prize papers: https://www.rigetti.com/research

---

## Ejemplo Completo: Ejecutar en QPU

```python
#!/usr/bin/env python3
"""
Script completo para ejecutar en QPU real de Rigetti.
"""

from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare
import numpy as np

def main():
    # Definir el circuito
    prog = Program(
        Declare("ro", "BIT", 1),
        H(0),
        MEASURE(0, ("ro", 0))
    )

    print("Circuito a ejecutar:")
    print(prog)
    print("\n" + "="*60)

    # 1. Probar en simulador
    print("\n1. Probando en simulador (QVM)...")
    qvm = get_qc('Aspen-M-3', as_qvm=True)
    executable = qvm.compile(prog)
    result_qvm = qvm.run(executable.wrap_in_numshots_loop(100))
    print(f"Resultado QVM: {np.mean(result_qvm.readout_data['ro']):.2f}")

    # 2. Ejecutar en QPU real (descomentar cuando tengas acceso)
    # print("\n2. Ejecutando en QPU real...")
    # qpu = get_qc('Aspen-M-3', as_qvm=False)
    # executable = qpu.compile(prog)
    # result_qpu = qpu.run(executable.wrap_in_numshots_loop(100))
    # print(f"Resultado QPU: {np.mean(result_qpu.readout_data['ro']):.2f}")

    print("\n" + "="*60)
    print("¡Completado!")

if __name__ == "__main__":
    main()
```

---

## Contacto y Soporte

**Para problemas técnicos:**
- support@rigetti.com

**Para solicitudes académicas:**
- partnerships@rigetti.com

**Para preguntas de la comunidad:**
- Slack: rigetti-forest.slack.com

---

**Última actualización**: Diciembre 2024

**Nota**: El acceso a QPUs reales está sujeto a disponibilidad y aprobación de Rigetti. Los tiempos de espera y procesos pueden variar.
