"""
Ejemplo de uso del Entregable 1: Multithreading con PyQuil

Este script demuestra la ventaja de usar multithreading para ejecutar
múltiples circuitos cuánticos en paralelo.
"""

from moneda_cuantica import (
    competicion_cuatro_monedas_secuencial,
    competicion_cuatro_monedas_multithreading,
    analizar_resultados,
    imprimir_resultados
)


def comparar_metodos(num_tiradas: int = 50):
    """
    Compara la ejecución secuencial vs multithreading.

    Args:
        num_tiradas: Número de lanzamientos por moneda
    """
    print("\n" + "="*70)
    print("COMPARACIÓN: EJECUCIÓN SECUENCIAL VS MULTITHREADING")
    print("="*70 + "\n")

    # Ejecución secuencial
    print("1️⃣  MÉTODO SECUENCIAL")
    print("-" * 70)
    resultados_sec, tiempo_sec = competicion_cuatro_monedas_secuencial(num_tiradas)
    analisis_sec = analizar_resultados(resultados_sec)
    imprimir_resultados(analisis_sec, tiempo_sec)

    # Ejecución con multithreading
    print("\n2️⃣  MÉTODO MULTITHREADING")
    print("-" * 70)
    resultados_mt, tiempo_mt = competicion_cuatro_monedas_multithreading(num_tiradas)
    analisis_mt = analizar_resultados(resultados_mt)
    imprimir_resultados(analisis_mt, tiempo_mt)

    # Comparación de rendimiento
    print("\n" + "="*70)
    print("ANÁLISIS DE RENDIMIENTO")
    print("="*70)
    mejora = ((tiempo_sec - tiempo_mt) / tiempo_sec) * 100
    speedup = tiempo_sec / tiempo_mt

    print(f"\nTiempo secuencial:     {tiempo_sec:.3f}s")
    print(f"Tiempo multithreading: {tiempo_mt:.3f}s")
    print(f"Mejora:                {mejora:.1f}%")
    print(f"Speedup:               {speedup:.2f}x")

    if mejora > 0:
        print(f"\n✅ Multithreading es {mejora:.1f}% más rápido")
    else:
        print(f"\n⚠️  Multithreading no proporcionó mejora en este caso")

    print("\nNota: La mejora depende del número de cores disponibles y la")
    print("      carga del sistema. En sistemas con múltiples cores, el")
    print("      speedup debería acercarse al número de threads usados.")
    print("="*70 + "\n")


def demostrar_escalabilidad():
    """
    Demuestra cómo escala el multithreading con diferentes números de threads.
    """
    print("\n" + "="*70)
    print("DEMOSTRACIÓN DE ESCALABILIDAD")
    print("="*70 + "\n")

    from moneda_cuantica import ejecutar_moneda_single
    from concurrent.futures import ThreadPoolExecutor
    import time

    num_monedas = 8
    num_tiradas = 30

    print(f"Ejecutando {num_monedas} monedas con {num_tiradas} tiradas cada una\n")

    for num_threads in [1, 2, 4, 8]:
        inicio = time.time()

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [
                executor.submit(ejecutar_moneda_single, i+1, num_tiradas)
                for i in range(num_monedas)
            ]
            resultados = [f.result() for f in futures]

        tiempo = time.time() - inicio
        print(f"  {num_threads} thread(s): {tiempo:.3f}s")

    print("\nComo se puede observar, aumentar el número de threads")
    print("reduce el tiempo de ejecución hasta el límite de cores disponibles.")
    print("="*70 + "\n")


if __name__ == "__main__":
    # Comparar métodos
    comparar_metodos(num_tiradas=50)

    # Demostrar escalabilidad (comentado por defecto para no alargar la ejecución)
    # demostrar_escalabilidad()
