"""
Entregable 2: Implementación de Control Clásico en PyQuil
Protocolo de detección de trampas en juego de moneda cuántica
"""

from .juego_moneda_trampa import (
    juego_moneda_sin_control,
    juego_moneda_con_control_if,
    juego_moneda_con_control_while,
    protocolo_bb84_simplificado,
    analizar_deteccion_trampa
)

__all__ = [
    'juego_moneda_sin_control',
    'juego_moneda_con_control_if',
    'juego_moneda_con_control_while',
    'protocolo_bb84_simplificado',
    'analizar_deteccion_trampa'
]
