#!/usr/bin/env python3
"""
Script Principal - Práctica S14: Conceptos Avanzados de PyQuil

Este script ejecuta demostraciones de los tres conceptos principales:
1. Multithreading en PyQuil
2. Control Clásico (IF/WHILE)
3. Información sobre acceso a QPU real

Autor: Práctica de Computación Cuántica
Fecha: Diciembre 2024
"""

import sys
from pathlib import Path

# Añadir directorios al path para imports
sys.path.insert(0, str(Path(__file__).parent))


def mostrar_banner():
    """Muestra el banner inicial del programa."""
    print("\n" + "="*80)
    print(" "*20 + "PRÁCTICA S14 - CONCEPTOS AVANZADOS DE PYQUIL")
    print("="*80)
    print("\nContenido:")
    print("  1. Multithreading - Ejecución paralela de circuitos cuánticos")
    print("  2. Control Clásico - Estructuras IF/WHILE en circuitos cuánticos")
    print("  3. Acceso a QPU - Guía para usar hardware cuántico real")
    print("\n" + "="*80 + "\n")


def ejecutar_entregable1():
    """Ejecuta la demostración del Entregable 1: Multithreading."""
    print("\n" + "█"*80)
    print("█" + " "*78 + "█")
    print("█" + " "*20 + "ENTREGABLE 1: MULTITHREADING EN PYQUIL" + " "*21 + "█")
    print("█" + " "*78 + "█")
    print("█"*80 + "\n")

    try:
        from entregable1_multithreading.moneda_cuantica import (
            competicion_cuatro_monedas_secuencial,
            competicion_cuatro_monedas_multithreading,
            analizar_resultados,
            imprimir_resultados
        )

        print("📖 DESCRIPCIÓN")
        print("-" * 80)
        print("Este entregable demuestra el uso de multithreading para paralelizar")
        print("la ejecución de múltiples circuitos cuánticos independientes.")
        print("\nEscenario: Competición de 4 monedas cuánticas")
        print("  - Cada moneda se lanza 50 veces")
        print("  - Jugador A gana con CARA (0)")
        print("  - Jugador B gana con CRUZ (1)")
        print("\nSe compara:")
        print("  • Ejecución SECUENCIAL: Una moneda tras otra")
        print("  • Ejecución PARALELA: Las 4 monedas simultáneamente")
        print("-" * 80 + "\n")

        input("Presiona Enter para ejecutar la comparación...")

        num_tiradas = 50

        # Ejecución secuencial
        print("\n🔄 Método 1: EJECUCIÓN SECUENCIAL")
        print("-" * 80)
        resultados_seq, tiempo_seq = competicion_cuatro_monedas_secuencial(num_tiradas)
        analisis_seq = analizar_resultados(resultados_seq)
        imprimir_resultados(analisis_seq, tiempo_seq)

        # Ejecución con multithreading
        print("\n⚡ Método 2: EJECUCIÓN CON MULTITHREADING")
        print("-" * 80)
        resultados_mt, tiempo_mt = competicion_cuatro_monedas_multithreading(num_tiradas)
        analisis_mt = analizar_resultados(resultados_mt)
        imprimir_resultados(analisis_mt, tiempo_mt)

        # Comparación
        print("\n📊 COMPARACIÓN DE RENDIMIENTO")
        print("=" * 80)
        mejora = ((tiempo_seq - tiempo_mt) / tiempo_seq) * 100
        speedup = tiempo_seq / tiempo_mt

        print(f"\n{'Método':<30} {'Tiempo':<15} {'Speedup':<15}")
        print("-" * 80)
        print(f"{'Secuencial':<30} {tiempo_seq:<15.3f}s {1.00:<15.2f}x")
        print(f"{'Multithreading (4 threads)':<30} {tiempo_mt:<15.3f}s {speedup:<15.2f}x")
        print("-" * 80)

        if mejora > 0:
            print(f"\n✅ Multithreading es {mejora:.1f}% más rápido ({speedup:.2f}x speedup)")
            print(f"   Tiempo ahorrado: {tiempo_seq - tiempo_mt:.3f} segundos")
        else:
            print(f"\n⚠️  En este caso, multithreading no proporcionó mejora")
            print(f"   (Puede deberse a overhead o limitaciones del sistema)")

        print("\n💡 CONCLUSIONES:")
        print("-" * 80)
        print("• El multithreading es efectivo para ejecutar múltiples circuitos")
        print("  cuánticos independientes en paralelo")
        print("• El speedup depende del número de cores disponibles")
        print("• Los objetos QVM de PyQuil son thread-safe")
        print("• Ideal para escenarios con múltiples experimentos o variaciones")
        print("=" * 80)

    except ImportError as e:
        print(f"❌ Error al importar el módulo: {e}")
        print("   Asegúrate de que todos los archivos estén en su lugar.")
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")


def ejecutar_entregable2():
    """Ejecuta la demostración del Entregable 2: Control Clásico."""
    print("\n" + "█"*80)
    print("█" + " "*78 + "█")
    print("█" + " "*18 + "ENTREGABLE 2: CONTROL CLÁSICO EN PYQUIL" + " "*21 + "█")
    print("█" + " "*78 + "█")
    print("█"*80 + "\n")

    try:
        from entregable2_control_clasico.juego_moneda_trampa import (
            juego_moneda_sin_control,
            juego_moneda_con_control_if,
            protocolo_bb84_simplificado,
            demostrar_control_clasico,
            ejecutar_analisis_completo
        )

        print("📖 DESCRIPCIÓN")
        print("-" * 80)
        print("Este entregable demuestra el uso de control clásico (IF/WHILE)")
        print("dentro de circuitos cuánticos para implementar protocolos de")
        print("verificación y detección de trampas.")
        print("\nConceptos implementados:")
        print("  • Control IF-THEN-ELSE basado en mediciones")
        print("  • Detección de trampas mediante entrelazamiento")
        print("  • Protocolo BB84 simplificado")
        print("  • Verificación de integridad cuántica")
        print("-" * 80 + "\n")

        input("Presiona Enter para ver los circuitos con control clásico...")

        # Demostrar estructuras de control
        demostrar_control_clasico()

        input("\nPresiona Enter para ejecutar el análisis de detección de trampas...")

        # Ejecutar análisis completo
        ejecutar_analisis_completo()

        print("\n💡 CONCLUSIONES:")
        print("-" * 80)
        print("• El control clásico permite tomar decisiones en tiempo de ejecución")
        print("• Las instrucciones IF-THEN permiten algoritmos adaptativos")
        print("• El entrelazamiento cuántico es útil para verificación")
        print("• Los protocolos como BB84 usan control clásico para seguridad")
        print("• PyQuil soporta control de flujo directamente en Quil")
        print("=" * 80)

    except ImportError as e:
        print(f"❌ Error al importar el módulo: {e}")
        print("   Asegúrate de que todos los archivos estén en su lugar.")
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")


def mostrar_info_qpu():
    """Muestra información sobre el acceso a QPU real."""
    print("\n" + "█"*80)
    print("█" + " "*78 + "█")
    print("█" + " "*15 + "INFORMACIÓN: ACCESO A COMPUTADORES CUÁNTICOS REALES" + " "*13 + "█")
    print("█" + " "*78 + "█")
    print("█"*80 + "\n")

    print("📖 GUÍA COMPLETA DE ACCESO A QPU")
    print("-" * 80)
    print("\nLa documentación completa sobre cómo solicitar acceso y usar")
    print("hardware cuántico real (QPU) está disponible en:\n")
    print("  📄 docs/guia_qpu_real.md")
    print("\nEsta guía incluye:")
    print("  • Proceso de solicitud de acceso a Rigetti QCS")
    print("  • Configuración de credenciales y entorno")
    print("  • Diferencias entre QVM (simulador) y QPU (hardware real)")
    print("  • Mejores prácticas para ejecución en QPU")
    print("  • Gestión de cuotas y optimización de circuitos")
    print("  • Ejemplos de código completos")
    print("-" * 80 + "\n")

    print("🔑 RESUMEN RÁPIDO")
    print("-" * 80)
    print("\n1. SOLICITAR ACCESO:")
    print("   • Visita: https://qcs.rigetti.com/")
    print("   • Programa académico: partnerships@rigetti.com")
    print("   • Incluir afiliación institucional y descripción del proyecto")
    print("\n2. CONFIGURAR:")
    print("   • pip install qcs-sdk-python")
    print("   • qcs auth login")
    print("\n3. EJECUTAR:")
    print("   • qpu = get_qc('Aspen-M-3', as_qvm=False)")
    print("   • result = qpu.run(executable)")
    print("-" * 80 + "\n")

    print("⚠️  CONSIDERACIONES IMPORTANTES")
    print("-" * 80)
    print("• El acceso a QPU real está sujeto a aprobación")
    print("• Tiempo de espera típico: 2-4 semanas")
    print("• Requiere justificación académica o de investigación")
    print("• El uso consume cuota asignada")
    print("• Siempre probar primero en QVM (as_qvm=True)")
    print("-" * 80 + "\n")

    print("📚 DIFERENCIAS: QVM vs QPU")
    print("-" * 80)
    print(f"{'Aspecto':<25} {'QVM (Simulador)':<25} {'QPU (Hardware Real)':<25}")
    print("-" * 80)
    print(f"{'Velocidad':<25} {'Rápido':<25} {'Latencia de red':<25}")
    print(f"{'Ruido':<25} {'Opcional/ideal':<25} {'Real e inevitable':<25}")
    print(f"{'Costo':<25} {'Gratuito':<25} {'Consume cuota':<25}")
    print(f"{'Disponibilidad':<25} {'24/7':<25} {'Horarios limitados':<25}")
    print(f"{'Acceso':<25} {'Libre':<25} {'Requiere aprobación':<25}")
    print("-" * 80 + "\n")

    print("🌐 RECURSOS")
    print("-" * 80)
    print("• PyQuil Docs:  https://pyquil-docs.rigetti.com/")
    print("• QCS Guide:    https://docs.rigetti.com/qcs/")
    print("• Slack:        rigetti-forest.slack.com")
    print("• GitHub:       https://github.com/rigetti/pyquil")
    print("=" * 80 + "\n")


def menu_principal():
    """Muestra el menú principal y maneja la navegación."""
    while True:
        print("\n" + "="*80)
        print(" "*30 + "MENÚ PRINCIPAL")
        print("="*80)
        print("\n1. 🧵 Ejecutar Entregable 1: Multithreading")
        print("2. 🎮 Ejecutar Entregable 2: Control Clásico")
        print("3. 🖥️  Ver Información sobre QPU Real")
        print("4. 📚 Ejecutar TODO (completo)")
        print("0. 🚪 Salir")
        print("\n" + "="*80)

        try:
            opcion = input("\nSelecciona una opción (0-4): ").strip()

            if opcion == "0":
                print("\n" + "="*80)
                print(" "*25 + "¡Gracias por usar el programa!")
                print("="*80 + "\n")
                break

            elif opcion == "1":
                ejecutar_entregable1()
                input("\n✅ Entregable 1 completado. Presiona Enter para volver al menú...")

            elif opcion == "2":
                ejecutar_entregable2()
                input("\n✅ Entregable 2 completado. Presiona Enter para volver al menú...")

            elif opcion == "3":
                mostrar_info_qpu()
                input("\n✅ Información mostrada. Presiona Enter para volver al menú...")

            elif opcion == "4":
                print("\n" + "="*80)
                print(" "*25 + "EJECUCIÓN COMPLETA")
                print("="*80 + "\n")
                ejecutar_entregable1()
                input("\n⏸️  Presiona Enter para continuar con el Entregable 2...")
                ejecutar_entregable2()
                input("\n⏸️  Presiona Enter para ver la información sobre QPU...")
                mostrar_info_qpu()
                print("\n✅ Ejecución completa finalizada.")
                input("\nPresiona Enter para volver al menú...")

            else:
                print("\n⚠️  Opción no válida. Por favor, elige una opción entre 0 y 4.")
                input("Presiona Enter para continuar...")

        except KeyboardInterrupt:
            print("\n\n" + "="*80)
            print(" "*25 + "Programa interrumpido por el usuario")
            print("="*80 + "\n")
            break

        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            import traceback
            traceback.print_exc()
            input("\nPresiona Enter para continuar...")


def main():
    """Función principal del programa."""
    mostrar_banner()

    # Verificar dependencias
    try:
        import pyquil
        import numpy
        print("✅ Dependencias verificadas correctamente")
        print(f"   PyQuil versión: {pyquil.__version__}")
        print(f"   NumPy versión:  {numpy.__version__}")
    except ImportError as e:
        print(f"❌ Error: Falta una dependencia: {e}")
        print("\n   Instala las dependencias con:")
        print("   pip install -r requirements.txt\n")
        return

    # Mostrar menú
    menu_principal()


if __name__ == "__main__":
    main()
