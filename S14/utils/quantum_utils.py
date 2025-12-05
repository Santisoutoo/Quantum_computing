"""
Funciones utilitarias para programas cuánticos con PyQuil
"""

from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare
from typing import List, Tuple
import numpy as np


def crear_programa_base(num_qubits: int, aplicar_hadamard: bool = True) -> Program:
    """
    Crea un programa cuántico base con declaración de memoria y puertas Hadamard opcionales.

    Args:
        num_qubits: Número de qubits a usar
        aplicar_hadamard: Si se debe aplicar Hadamard a todos los qubits

    Returns:
        Programa cuántico inicializado
    """
    prog = Program()
    prog += Declare("ro", "BIT", num_qubits)

    if aplicar_hadamard:
        for i in range(num_qubits):
            prog += H(i)

    return prog


def medir_qubits(program: Program, qubits: List[int]) -> Program:
    """
    Añade mediciones de qubits al programa.

    Args:
        program: Programa cuántico
        qubits: Lista de índices de qubits a medir

    Returns:
        Programa con mediciones añadidas
    """
    for i, qubit in enumerate(qubits):
        program += MEASURE(qubit, ("ro", i))

    return program


def ejecutar_programa(program: Program, num_shots: int = 1,
                     qvm_name: str = '9q-square-qvm') -> np.ndarray:
    """
    Ejecuta un programa cuántico en el simulador.

    Args:
        program: Programa cuántico a ejecutar
        num_shots: Número de ejecuciones
        qvm_name: Nombre del simulador cuántico

    Returns:
        Array con los resultados de medición
    """
    qvm = get_qc(qvm_name)
    program_wrapped = program.wrap_in_numshots_loop(num_shots)
    result = qvm.run(qvm.compile(program_wrapped))

    return result.get_register_map().get("ro")


def interpretar_resultado_binario(bits: np.ndarray) -> int:
    """
    Convierte un array de bits en un entero decimal.

    Args:
        bits: Array de bits (0s y 1s)

    Returns:
        Valor entero correspondiente
    """
    resultado = 0
    for i, bit in enumerate(bits):
        resultado += bit * (2 ** (len(bits) - 1 - i))

    return resultado
