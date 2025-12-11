#!/usr/bin/env python3
"""
Práctica S14: Multithreading y Control Clásico en PyQuil
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def ejecutar_entregable1():
    print("\n" + "="*60)
    print("ENTREGABLE 1: MULTITHREADING")
    print("="*60 + "\n")

    from multithreading.moneda_cuantica import (
        competicion_secuencial,
        competicion_multithreading,
        analizar_resultados,
        imprimir_resultados
    )

    num_tiradas = 50

    # Secuencial
    print("Ejecutando secuencial...")
    resultados_sec, tiempo_sec = competicion_secuencial(num_tiradas)
    analisis_sec = analizar_resultados(resultados_sec)
    imprimir_resultados(analisis_sec, tiempo_sec)

    # Multithreading
    print("Ejecutando multithreading...")
    resultados_mt, tiempo_mt = competicion_multithreading(num_tiradas)
    analisis_mt = analizar_resultados(resultados_mt)
    imprimir_resultados(analisis_mt, tiempo_mt)

    # Comparación
    mejora = ((tiempo_sec - tiempo_mt) / tiempo_sec) * 100
    speedup = tiempo_sec / tiempo_mt

    print("="*60)
    print("COMPARACIÓN")
    print("="*60)
    print(f"Tiempo secuencial:     {tiempo_sec:.3f}s")
    print(f"Tiempo multithreading: {tiempo_mt:.3f}s")
    print(f"Speedup:               {speedup:.2f}x")
    print(f"Mejora:                {mejora:.1f}%")
    print("="*60 + "\n")


def ejecutar_entregable2():
    print("\n" + "="*60)
    print("ENTREGABLE 2: CONTROL CLÁSICO")
    print("="*60 + "\n")

    from control_clasico.juego_moneda_trampa import (
        control_simple,
        copiar_bit,
        correccion_error
    )

    print("Ejemplo 1: Control simple con IF")
    print("-"*60)
    prog1 = control_simple()
    print(prog1)
    print("→ Mide q0, si es 1 aplica X a q1")
    print("→ JUMP-WHEN = salto condicional (IF clásico)")

    print("\nEjemplo 2: Copiar bit")
    print("-"*60)
    prog2 = copiar_bit()
    print(prog2)
    print("→ Copia el resultado de q0 a q1")
    print("→ Control clásico: lee ro[0] y decide si aplicar X(1)")

    print("\nEjemplo 3: Corrección de error")
    print("-"*60)
    prog3 = correccion_error()
    print(prog3)
    print("→ Aplica X(0), mide, y corrige si está en |1⟩")
    print("→ Control clásico: invierte de nuevo para volver a |0⟩")
    print()


def mostrar_info_qpu():
    print("\n" + "="*60)
    print("INFORMACIÓN: ACCESO A QPU REAL")
    print("="*60 + "\n")

    print("  No implementado, acceso no disponible\n")

    print("Pasos para solicitar acceso:")
    print("1. Registrarse en: https://qcs.rigetti.com/")
    print("2. Solicitar acceso académico: partnerships@rigetti.com")
    print("3. Esperar aprobación (puede tardar varios días)")
    print("\n" + "="*60 + "\n")


def menu():
    while True:
        print("\n" + "="*60)
        print("PRÁCTICA S14 - PYQUIL")
        print("="*60)
        print("\n1. Entregable 1: Multithreading")
        print("2. Entregable 2: Control Clásico")
        print("3. Info QPU Real")
        print("0. Salir")
        print("\n" + "="*60)

        opcion = input("\nOpción: ").strip()

        if opcion == "0":
            break
        elif opcion == "1":
            ejecutar_entregable1()
        elif opcion == "2":
            ejecutar_entregable2()
        elif opcion == "3":
            mostrar_info_qpu()
        else:
            print("Opción no válida")


if __name__ == "__main__":
    try:
        import pyquil
        print(f"PyQuil {pyquil.__version__}")
        menu()
    except ImportError:
        print("Error: Instala pyquil (pip install -r requirements.txt)")
