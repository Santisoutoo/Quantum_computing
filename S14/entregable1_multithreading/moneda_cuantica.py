"""
Implementación de competición de monedas cuánticas con multithreading.

Basado en la guía de PyQuil:
https://pyquil-docs.rigetti.com/en/latest/advanced_usage.html#multithreading

Este módulo implementa una competición entre dos jugadores (A y B) que lanzan
4 monedas cuánticas 50 veces cada una. El jugador A gana con CARA (0) y el
jugador B con CRUZ (1).
"""

from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare
import numpy as np
from typing import List, Tuple, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from dataclasses import dataclass


@dataclass
class ResultadoMoneda:
    """Almacena los resultados de una moneda cuántica"""
    moneda_id: int
    caras: int
    cruces: int
    tiempo_ejecucion: float

    @property
    def total_lanzamientos(self) -> int:
        return self.caras + self.cruces


def crear_programa_moneda(qubit: int = 0) -> Program:
    """
    Crea un programa para una moneda cuántica.

    Args:
        qubit: Índice del qubit a usar

    Returns:
        Programa cuántico para lanzar una moneda
    """
    prog = Program(
        Declare("ro", "BIT", 1),
        H(qubit),
        MEASURE(qubit, ("ro", 0))
    )

    return prog


def ejecutar_moneda_single(moneda_id: int, num_tiradas: int = 50,
                          qvm_name: str = '9q-square-qvm') -> ResultadoMoneda:
    """
    Ejecuta una única moneda cuántica con múltiples tiradas.

    Args:
        moneda_id: Identificador de la moneda
        num_tiradas: Número de lanzamientos
        qvm_name: Nombre del simulador cuántico

    Returns:
        Resultados de la moneda
    """
    inicio = time.time()

    # Crear el programa y el QC
    prog = crear_programa_moneda(0).wrap_in_numshots_loop(num_tiradas)
    qvm = get_qc(qvm_name)

    # Ejecutar y obtener resultados
    result = qvm.run(qvm.compile(prog))
    mediciones = result.get_register_map().get("ro").flatten()

    caras = np.sum(mediciones == 0)
    cruces = num_tiradas - caras

    tiempo = time.time() - inicio

    return ResultadoMoneda(
        moneda_id=moneda_id,
        caras=int(caras),
        cruces=int(cruces),
        tiempo_ejecucion=tiempo
    )


def competicion_cuatro_monedas_secuencial(num_tiradas: int = 50) -> Tuple[List[ResultadoMoneda], float]:
    """
    Ejecuta la competición de 4 monedas de forma secuencial.

    Args:
        num_tiradas: Número de lanzamientos por moneda

    Returns:
        Tupla con (lista de resultados, tiempo total)
    """
    print("Ejecutando competición SECUENCIAL...")
    inicio = time.time()

    resultados = []
    for i in range(4):
        print(f"  Lanzando moneda {i+1}...")
        resultado = ejecutar_moneda_single(i+1, num_tiradas)
        resultados.append(resultado)

    tiempo_total = time.time() - inicio

    return resultados, tiempo_total


def competicion_cuatro_monedas_multithreading(num_tiradas: int = 50,
                                              max_workers: int = 4) -> Tuple[List[ResultadoMoneda], float]:
    """
    Ejecuta la competición de 4 monedas usando multithreading.

    Según la guía de PyQuil, los objetos QVM son thread-safe y se pueden
    usar desde múltiples threads de forma segura. Esto permite paralelizar
    la ejecución de múltiples circuitos.

    Args:
        num_tiradas: Número de lanzamientos por moneda
        max_workers: Número máximo de threads

    Returns:
        Tupla con (lista de resultados, tiempo total)
    """
    print(f"Ejecutando competición con MULTITHREADING ({max_workers} threads)...")
    inicio = time.time()

    resultados = []

    # Usar ThreadPoolExecutor para ejecutar en paralelo
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Crear futures para cada moneda
        futures = {
            executor.submit(ejecutar_moneda_single, i+1, num_tiradas): i+1
            for i in range(4)
        }

        # Obtener resultados conforme se completan
        for future in as_completed(futures):
            moneda_id = futures[future]
            try:
                resultado = future.result()
                resultados.append(resultado)
                print(f"  Moneda {moneda_id} completada en {resultado.tiempo_ejecucion:.3f}s")
            except Exception as e:
                print(f"  Error en moneda {moneda_id}: {e}")

    # Ordenar resultados por ID de moneda
    resultados.sort(key=lambda x: x.moneda_id)

    tiempo_total = time.time() - inicio

    return resultados, tiempo_total


def analizar_resultados(resultados: List[ResultadoMoneda]) -> Dict[str, any]:
    """
    Analiza los resultados de la competición y determina el ganador.

    Args:
        resultados: Lista de resultados de las monedas

    Returns:
        Diccionario con el análisis completo
    """
    total_caras = sum(r.caras for r in resultados)
    total_cruces = sum(r.cruces for r in resultados)
    total_lanzamientos = sum(r.total_lanzamientos for r in resultados)

    if total_caras > total_cruces:
        ganador = "Jugador A (CARAS)"
    elif total_cruces > total_caras:
        ganador = "Jugador B (CRUCES)"
    else:
        ganador = "EMPATE"

    return {
        'resultados_por_moneda': resultados,
        'total_caras': total_caras,
        'total_cruces': total_cruces,
        'total_lanzamientos': total_lanzamientos,
        'ganador': ganador,
        'porcentaje_caras': (total_caras / total_lanzamientos) * 100,
        'porcentaje_cruces': (total_cruces / total_lanzamientos) * 100
    }


def imprimir_resultados(analisis: Dict[str, any], tiempo_total: float):
    """
    Imprime los resultados de forma formateada.

    Args:
        analisis: Diccionario con el análisis de resultados
        tiempo_total: Tiempo total de ejecución
    """
    print("\n" + "="*60)
    print("RESULTADOS DE LA COMPETICIÓN")
    print("="*60)

    print("\nResultados por moneda:")
    for resultado in analisis['resultados_por_moneda']:
        print(f"  Moneda {resultado.moneda_id}: "
              f"Caras={resultado.caras}, Cruces={resultado.cruces} "
              f"(Tiempo: {resultado.tiempo_ejecucion:.3f}s)")

    print(f"\nTotales:")
    print(f"  Total Caras (A): {analisis['total_caras']} ({analisis['porcentaje_caras']:.1f}%)")
    print(f"  Total Cruces (B): {analisis['total_cruces']} ({analisis['porcentaje_cruces']:.1f}%)")
    print(f"\n🏆 GANADOR: {analisis['ganador']}")
    print(f"\n⏱️  Tiempo total de ejecución: {tiempo_total:.3f}s")
    print("="*60 + "\n")
