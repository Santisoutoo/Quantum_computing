"""
Entregable 1: Multithreading en PyQuil
"""

from .moneda_cuantica import (
    ejecutar_moneda,
    competicion_secuencial,
    competicion_multithreading,
    analizar_resultados,
    imprimir_resultados
)

__all__ = [
    'ejecutar_moneda',
    'competicion_secuencial',
    'competicion_multithreading',
    'analizar_resultados',
    'imprimir_resultados'
]
