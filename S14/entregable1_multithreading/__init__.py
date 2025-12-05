"""
Entregable 1: Implementación de Multithreading en PyQuil
Competición de monedas cuánticas usando múltiples threads
"""

from .moneda_cuantica import (
    crear_programa_moneda,
    ejecutar_moneda_single,
    competicion_cuatro_monedas_secuencial,
    competicion_cuatro_monedas_multithreading,
    analizar_resultados
)

__all__ = [
    'crear_programa_moneda',
    'ejecutar_moneda_single',
    'competicion_cuatro_monedas_secuencial',
    'competicion_cuatro_monedas_multithreading',
    'analizar_resultados'
]
