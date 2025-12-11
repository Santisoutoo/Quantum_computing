"""
Ejemplo: Multithreading con PyQuil
"""

from moneda_cuantica import (
    competicion_secuencial,
    competicion_multithreading,
    analizar_resultados,
    imprimir_resultados
)


def comparar_metodos():
    num_tiradas = 50

    print("\n" + "="*60)
    print("COMPARACIÓN: SECUENCIAL VS MULTITHREADING")
    print("="*60 + "\n")

    # Secuencial
    resultados_sec, tiempo_sec = competicion_secuencial(num_tiradas)
    analisis_sec = analizar_resultados(resultados_sec)
    imprimir_resultados(analisis_sec, tiempo_sec)

    # Multithreading
    resultados_mt, tiempo_mt = competicion_multithreading(num_tiradas)
    analisis_mt = analizar_resultados(resultados_mt)
    imprimir_resultados(analisis_mt, tiempo_mt)

    # Comparación
    mejora = ((tiempo_sec - tiempo_mt) / tiempo_sec) * 100
    speedup = tiempo_sec / tiempo_mt

    print("="*60)
    print("ANÁLISIS DE RENDIMIENTO")
    print("="*60)
    print(f"Tiempo secuencial:     {tiempo_sec:.3f}s")
    print(f"Tiempo multithreading: {tiempo_mt:.3f}s")
    print(f"Speedup:               {speedup:.2f}x")
    print(f"Mejora:                {mejora:.1f}%")
    print("="*60 + "\n")


if __name__ == "__main__":
    comparar_metodos()
