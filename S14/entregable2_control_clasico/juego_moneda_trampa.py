"""
Implementación de control clásico en PyQuil para detección de trampas.

Basado en la guía de PyQuil:
https://pyquil-docs.rigetti.com/en/latest/advanced_usage.html#classical-control-flow

Este módulo implementa un juego de moneda cuántica donde un jugador (Alicia)
quiere verificar si otro jugador (Bob) está haciendo trampa. Se usan
estructuras de control clásico (if/while) dentro del circuito cuántico.

Escenarios implementados:
1. Juego sin control: medición directa
2. Juego con control IF: verificación condicional de trampa
3. Juego con control WHILE: repetición hasta condición de honestidad
4. Protocolo BB84 simplificado: intercambio cuántico seguro
"""

from pyquil import Program, get_qc
from pyquil.gates import H, X, Z, CNOT, MEASURE
from pyquil.quilbase import Declare
from pyquil.quil import address_qubits
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class ResultadoJuego:
    """Almacena los resultados de un juego"""
    intento: int
    resultado_qubit: int
    deteccion_trampa: bool
    medicion_verificacion: int


def juego_moneda_sin_control() -> Program:
    """
    Implementa un juego de moneda simple sin control de trampas.

    Alice prepara una moneda cuántica en superposición y Bob la mide.
    No hay verificación de trampa.

    Returns:
        Programa cuántico sin control clásico
    """
    prog = Program(
        Declare("ro", "BIT", 1),
        H(0),
        MEASURE(0, ("ro", 0))
    )

    return prog


def juego_moneda_con_control_if() -> Program:
    """
    Implementa un juego de moneda con verificación condicional de trampa usando IF.

    Alice prepara dos qubits:
    - Qubit 0: la moneda cuántica
    - Qubit 1: qubit de verificación (entrelazado con el primero)

    Si Bob mide el qubit de verificación primero (haciendo trampa),
    el entrelazamiento se rompe y Alice lo detecta.

    El control IF permite tomar decisiones basadas en mediciones previas:
    IF ro[1] == 1 THEN
        aplicar corrección
    END

    Returns:
        Programa cuántico con control IF
    """
    prog = Program()

    # Declarar memoria para dos qubits
    prog += Declare("ro", "BIT", 2)
    prog += Declare("trampa_detectada", "BIT", 1)

    # Alice prepara un estado entrelazado (Bell state)
    # |Ψ⟩ = (|00⟩ + |11⟩)/√2
    prog += H(0)
    prog += CNOT(0, 1)

    # Bob podría intentar medir el qubit de verificación (trampa)
    # Simulamos un 50% de probabilidad de trampa
    prog += H(2)  # Qubit auxiliar para decidir si Bob hace trampa
    prog += MEASURE(2, ("trampa_detectada", 0))

    # Control clásico IF: Si se detecta intento de trampa
    # Aplicamos una transformación para "marcar" el resultado
    prog.if_then(
        ("trampa_detectada", 0),
        Program(X(1)),  # Marcar el qubit de verificación
        Program()  # No hacer nada si no hay trampa
    )

    # Alice mide el qubit de verificación para detectar trampa
    prog += MEASURE(1, ("ro", 1))

    # Bob mide el qubit de la moneda
    prog += MEASURE(0, ("ro", 0))

    return prog


def juego_moneda_con_control_while() -> Program:
    """
    Implementa un protocolo de verificación repetitiva usando WHILE.

    Alice prepara múltiples pares de qubits entrelazados y verifica
    repetidamente hasta que detecta un patrón consistente (sin trampa)
    o un máximo de intentos.

    El control WHILE permite repetir operaciones:
    WHILE ro[contador] < max_intentos:
        preparar estado
        medir
        verificar
        incrementar contador
    END

    Nota: PyQuil soporta WHILE pero con limitaciones. Esta es una
    demostración conceptual usando control clásico.

    Returns:
        Programa cuántico con control WHILE (simplificado)
    """
    prog = Program()

    # Declarar memoria
    prog += Declare("ro", "BIT", 3)
    prog += Declare("contador", "BIT", 1)
    prog += Declare("verificado", "BIT", 1)

    # Inicializar contador
    # En PyQuil real, el WHILE loop está limitado, así que usamos
    # una aproximación con IF anidados para simular iteraciones

    # Iteración 1
    prog += H(0)
    prog += CNOT(0, 1)
    prog += MEASURE(0, ("ro", 0))
    prog += MEASURE(1, ("ro", 1))

    # Verificar si hay correlación (no trampa)
    # Si ro[0] == ro[1], entonces verificado = 1
    # Esto se simula con operaciones cuánticas auxiliares

    prog += H(2)  # Qubit auxiliar para segunda verificación
    prog += MEASURE(2, ("ro", 2))

    return prog


def protocolo_bb84_simplificado() -> Program:
    """
    Implementa una versión simplificada del protocolo BB84 con control clásico.

    BB84 es un protocolo de distribución de claves cuánticas donde:
    1. Alice prepara qubits en bases aleatorias (Z o X)
    2. Bob mide en bases aleatorias
    3. Alice y Bob comparan bases (control clásico)
    4. Si las bases coinciden, el bit es válido

    Este protocolo usa control clásico IF para decidir qué base usar.

    Returns:
        Programa cuántico del protocolo BB84 simplificado
    """
    prog = Program()

    # Declarar memoria
    prog += Declare("ro", "BIT", 4)
    prog += Declare("base_alice", "BIT", 1)
    prog += Declare("base_bob", "BIT", 1)
    prog += Declare("bit_alice", "BIT", 1)

    # Alice elige una base aleatoria (0=Z, 1=X)
    prog += H(0)
    prog += MEASURE(0, ("base_alice", 0))

    # Alice elige un bit aleatorio
    prog += H(1)
    prog += MEASURE(1, ("bit_alice", 0))

    # Control IF: Alice prepara el qubit según su base elegida
    # Si base_alice == 1 (base X), aplica H al qubit de datos
    prog.if_then(
        ("bit_alice", 0),
        Program(X(2))  # Si el bit es 1, aplicar X
    )

    prog.if_then(
        ("base_alice", 0),
        Program(H(2))  # Si la base es X, aplicar H
    )

    # Bob elige una base aleatoria
    prog += H(3)
    prog += MEASURE(3, ("base_bob", 0))

    # Control IF: Bob mide según su base elegida
    prog.if_then(
        ("base_bob", 0),
        Program(H(2))  # Si la base es X, aplicar H antes de medir
    )

    # Bob mide
    prog += MEASURE(2, ("ro", 0))

    # Guardar las bases para comparación
    prog += MEASURE(0, ("ro", 1))  # base_alice
    prog += MEASURE(3, ("ro", 2))  # base_bob
    prog += MEASURE(1, ("ro", 3))  # bit_alice

    return prog


def ejecutar_juego(program: Program, num_intentos: int = 10) -> List[np.ndarray]:
    """
    Ejecuta un programa de juego múltiples veces.

    Args:
        program: Programa cuántico a ejecutar
        num_intentos: Número de veces a ejecutar

    Returns:
        Lista con los resultados de cada intento
    """
    qvm = get_qc('9q-square-qvm')
    resultados = []

    for _ in range(num_intentos):
        result = qvm.run(qvm.compile(program))
        resultados.append(result.get_register_map().get("ro")[0])

    return resultados


def analizar_deteccion_trampa(resultados: List[np.ndarray]) -> Dict[str, any]:
    """
    Analiza los resultados para detectar patrones de trampa.

    Args:
        resultados: Lista de resultados de mediciones

    Returns:
        Diccionario con el análisis
    """
    total_intentos = len(resultados)
    trampas_detectadas = 0
    resultados_validos = 0

    for resultado in resultados:
        # En un juego con verificación, si los qubits entrelazados
        # no están correlacionados, se detecta trampa
        if len(resultado) >= 2:
            if resultado[0] != resultado[1]:
                trampas_detectadas += 1
            else:
                resultados_validos += 1

    return {
        'total_intentos': total_intentos,
        'trampas_detectadas': trampas_detectadas,
        'resultados_validos': resultados_validos,
        'tasa_trampa': (trampas_detectadas / total_intentos) * 100,
        'tasa_validos': (resultados_validos / total_intentos) * 100
    }


def demostrar_control_clasico():
    """
    Función de demostración de las capacidades de control clásico.
    """
    print("\n" + "="*70)
    print("DEMOSTRACIÓN DE CONTROL CLÁSICO EN PYQUIL")
    print("="*70 + "\n")

    # 1. Juego sin control
    print("1️⃣  JUEGO SIN CONTROL DE TRAMPAS")
    print("-" * 70)
    prog_sin_control = juego_moneda_sin_control()
    print(prog_sin_control)
    print("\nEste programa no tiene control clásico. Bob puede medir directamente")
    print("sin que Alice pueda verificar si hubo trampa.\n")

    # 2. Juego con IF
    print("2️⃣  JUEGO CON CONTROL IF")
    print("-" * 70)
    prog_con_if = juego_moneda_con_control_if()
    print(prog_con_if)
    print("\nEste programa usa IF para tomar decisiones basadas en mediciones.")
    print("Alice puede detectar si Bob intenta medir el qubit de verificación.\n")

    # 3. Protocolo BB84
    print("3️⃣  PROTOCOLO BB84 SIMPLIFICADO")
    print("-" * 70)
    prog_bb84 = protocolo_bb84_simplificado()
    print(prog_bb84)
    print("\nEste programa usa IF para implementar el protocolo BB84 de")
    print("distribución de claves cuánticas con verificación de bases.\n")

    print("="*70)


def ejecutar_analisis_completo():
    """
    Ejecuta un análisis completo de detección de trampas.
    """
    print("\n" + "="*70)
    print("ANÁLISIS DE DETECCIÓN DE TRAMPAS CON CONTROL CLÁSICO")
    print("="*70 + "\n")

    num_intentos = 20

    # Ejecutar juego con control IF
    print("Ejecutando juego con control IF...")
    prog_if = juego_moneda_con_control_if()
    resultados_if = ejecutar_juego(prog_if, num_intentos)

    print(f"\nResultados de {num_intentos} intentos:")
    for i, res in enumerate(resultados_if[:5], 1):
        print(f"  Intento {i}: {res}")
    if num_intentos > 5:
        print(f"  ... ({num_intentos - 5} intentos más)")

    # Analizar resultados
    analisis = analizar_deteccion_trampa(resultados_if)

    print("\n" + "-"*70)
    print("RESULTADOS DEL ANÁLISIS")
    print("-"*70)
    print(f"Total de intentos:      {analisis['total_intentos']}")
    print(f"Trampas detectadas:     {analisis['trampas_detectadas']} ({analisis['tasa_trampa']:.1f}%)")
    print(f"Resultados válidos:     {analisis['resultados_validos']} ({analisis['tasa_validos']:.1f}%)")

    print("\nInterpretación:")
    if analisis['tasa_trampa'] > 30:
        print("  ⚠️  Alta tasa de detección de anomalías")
        print("     Posible intento de interferencia en el sistema")
    else:
        print("  ✅ Tasa normal de decorrelación")
        print("     Sistema funcionando correctamente")

    print("\n" + "="*70 + "\n")
