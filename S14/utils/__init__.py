"""
Utilidades comunes para las prácticas de computación cuántica
"""

from .quantum_utils import (
    crear_programa_base,
    ejecutar_programa,
    medir_qubits,
    interpretar_resultado_binario
)

__all__ = [
    'crear_programa_base',
    'ejecutar_programa',
    'medir_qubits',
    'interpretar_resultado_binario'
]
