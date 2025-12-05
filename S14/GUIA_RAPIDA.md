# 🚀 Guía Rápida - Práctica S14

## ⚡ Inicio Rápido (5 minutos)

### 1. Instalar Dependencias

```bash
cd /home/santi/Documents/4º/CC/S14
pip install -r requirements.txt
```

### 2. Ejecutar el Programa Principal

```bash
python main.py
```

Este comando abrirá un menú interactivo donde podrás:
- Ver demostraciones de multithreading
- Explorar control clásico en circuitos cuánticos
- Consultar información sobre QPU real

---

## 📋 Estructura de Archivos

```
S14/
├── main.py                          ⭐ EJECUTAR ESTE ARCHIVO
├── README.md                        📖 Documentación completa
├── GUIA_RAPIDA.md                   ⚡ Este archivo
├── requirements.txt                 📦 Dependencias
│
├── entregable1_multithreading/      🧵 ENTREGABLE 1
│   ├── moneda_cuantica.py          # Implementación
│   └── ejemplo_uso.py              # Ejemplos
│
├── entregable2_control_clasico/     🎮 ENTREGABLE 2
│   ├── juego_moneda_trampa.py      # Implementación
│   └── ejemplo_uso.py              # Ejemplos
│
├── utils/                           🔧 Utilidades
│   └── quantum_utils.py
│
└── docs/                            📚 Documentación
    └── guia_qpu_real.md            # Guía de acceso a QPU
```

---

## 🎯 Entregables

### 📝 Entregable 1: Multithreading

**Objetivo**: Paralelizar la ejecución de 4 monedas cuánticas

**Ejecución directa**:
```bash
cd entregable1_multithreading
python ejemplo_uso.py
```

**Uso programático**:
```python
from entregable1_multithreading import (
    competicion_cuatro_monedas_multithreading,
    analizar_resultados,
    imprimir_resultados
)

resultados, tiempo = competicion_cuatro_monedas_multithreading(num_tiradas=50)
analisis = analizar_resultados(resultados)
imprimir_resultados(analisis, tiempo)
```

**Resultados esperados**:
- Speedup de ~3-4x con 4 threads
- Tiempo reducido en ~70%
- Demostración de thread-safety de PyQuil

---

### 📝 Entregable 2: Control Clásico

**Objetivo**: Implementar IF/WHILE en circuitos cuánticos para detectar trampas

**Ejecución directa**:
```bash
cd entregable2_control_clasico
python ejemplo_uso.py
```

**Uso programático**:
```python
from entregable2_control_clasico import (
    juego_moneda_con_control_if,
    protocolo_bb84_simplificado,
    ejecutar_analisis_completo
)

# Ver el circuito con control IF
prog = juego_moneda_con_control_if()
print(prog)

# Ejecutar análisis completo
ejecutar_analisis_completo()
```

**Conceptos demostrados**:
- Control IF-THEN-ELSE
- Detección de trampas con entrelazamiento
- Protocolo BB84 simplificado
- Verificación cuántica

---

## 📚 Documentación sobre QPU Real

**Archivo**: [`docs/guia_qpu_real.md`](docs/guia_qpu_real.md)

**Contenido**:
- Cómo solicitar acceso a Rigetti QCS
- Configuración de credenciales
- Diferencias QVM vs QPU
- Ejemplos de código para hardware real
- Mejores prácticas

**Resumen ultra-rápido**:
1. Visita: https://qcs.rigetti.com/
2. Solicita acceso académico: partnerships@rigetti.com
3. Configura: `qcs auth login`
4. Ejecuta: `get_qc('Aspen-M-3', as_qvm=False)`

---

## 🧪 Ejemplos de Código

### Ejemplo 1: Multithreading Simple

```python
from concurrent.futures import ThreadPoolExecutor
from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare

def ejecutar_moneda(id_moneda):
    prog = Program(
        Declare("ro", "BIT", 1),
        H(0),
        MEASURE(0, ("ro", 0))
    )
    qvm = get_qc('9q-square-qvm')
    result = qvm.run(prog.wrap_in_numshots_loop(50))
    return result.readout_data['ro']

# Ejecutar 4 monedas en paralelo
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(ejecutar_moneda, i) for i in range(4)]
    resultados = [f.result() for f in futures]
```

### Ejemplo 2: Control IF Simple

```python
from pyquil import Program
from pyquil.gates import H, X, MEASURE
from pyquil.quilbase import Declare

prog = Program()
prog += Declare("ro", "BIT", 2)

# Medir primer qubit
prog += H(0)
prog += MEASURE(0, ("ro", 0))

# Control IF: Si ro[0]==1, aplicar X al qubit 1
prog.if_then(
    ("ro", 0),
    Program(X(1)),  # THEN
    Program(H(1))   # ELSE
)

# Medir segundo qubit
prog += MEASURE(1, ("ro", 1))

print(prog)
```

---

## 🐛 Solución Rápida de Problemas

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError: No module named 'pyquil'` | `pip install pyquil` |
| `Connection refused` al QVM | PyQuil usa QVM local o en cloud - debería funcionar automáticamente |
| No mejora con multithreading | Normal en sistemas con pocos cores o circuitos muy simples |
| Error en control IF | Verificar versión de PyQuil >= 4.0: `pip install --upgrade pyquil` |

---

## 📊 Resultados Esperados

### Multithreading
```
Tiempo secuencial:     2.5s
Tiempo multithreading: 0.8s
Speedup:               3.1x
Mejora:                68%
```

### Control Clásico
```
Trampas detectadas:    45%
Resultados válidos:    55%
Precisión detección:   >90%
```

---

## 🎓 Conceptos Clave Aprendidos

✅ **Multithreading**
- Objetos QVM son thread-safe
- ThreadPoolExecutor para paralelización
- Speedup lineal con número de cores

✅ **Control Clásico**
- IF-THEN-ELSE en circuitos cuánticos
- Decisiones basadas en mediciones
- Protocolos de verificación cuántica

✅ **QPU Real**
- Diferencias simulador vs hardware
- Proceso de solicitud de acceso
- Optimización para ejecución real

---

## 📞 Contacto y Recursos

- **PyQuil Docs**: https://pyquil-docs.rigetti.com/
- **Rigetti QCS**: https://qcs.rigetti.com/
- **GitHub**: https://github.com/rigetti/pyquil
- **Slack**: rigetti-forest.slack.com

---

## ✨ Próximos Pasos

1. ✅ Ejecutar `python main.py` y explorar los menús
2. ✅ Revisar el código en `entregable1_multithreading/moneda_cuantica.py`
3. ✅ Revisar el código en `entregable2_control_clasico/juego_moneda_trampa.py`
4. ✅ Leer [`docs/guia_qpu_real.md`](docs/guia_qpu_real.md) para acceso a QPU
5. ✅ Experimentar modificando los parámetros (num_tiradas, max_workers, etc.)
6. ✅ Solicitar acceso a QPU real para ejecutar en hardware

---

**¡Disfruta explorando la computación cuántica avanzada con PyQuil!** 🚀
