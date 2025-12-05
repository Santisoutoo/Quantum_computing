"""
Ejemplo de uso del Entregable 2: Control Clásico en PyQuil

Este script demuestra el uso de estructuras de control clásico (IF/WHILE)
dentro de circuitos cuánticos para implementar protocolos de verificación
y detección de trampas.
"""

from juego_moneda_trampa import (
    demostrar_control_clasico,
    ejecutar_analisis_completo,
    protocolo_bb84_simplificado,
    ejecutar_juego
)


def ejemplo_basico_control_if():
    """
    Ejemplo básico del uso de control IF en PyQuil.
    """
    print("\n" + "="*70)
    print("EJEMPLO BÁSICO: CONTROL IF EN PYQUIL")
    print("="*70 + "\n")

    print("El control clásico IF permite tomar decisiones dentro del")
    print("circuito cuántico basadas en resultados de mediciones previas.\n")

    print("Sintaxis básica:")
    print("-" * 70)
    print("""
    # Medir un qubit
    prog += MEASURE(0, ("ro", 0))

    # Tomar decisión basada en el resultado
    prog.if_then(
        ("ro", 0),              # Condición: si ro[0] == 1
        Program(X(1)),          # THEN: aplicar X al qubit 1
        Program(H(1))           # ELSE: aplicar H al qubit 1
    )
    """)

    print("\nEsto permite implementar algoritmos adaptativos donde las")
    print("operaciones futuras dependen de mediciones intermedias.")
    print("="*70 + "\n")


def ejemplo_protocolo_bb84():
    """
    Ejemplo del protocolo BB84 simplificado.
    """
    print("\n" + "="*70)
    print("EJEMPLO: PROTOCOLO BB84 SIMPLIFICADO")
    print("="*70 + "\n")

    print("El protocolo BB84 es fundamental en criptografía cuántica.")
    print("Permite a dos partes compartir una clave secreta detectando")
    print("cualquier intento de espionaje.\n")

    print("Pasos del protocolo:")
    print("-" * 70)
    print("1. Alice elige aleatoriamente:")
    print("   - Una base de medición (Z o X)")
    print("   - Un bit clásico (0 o 1)")
    print("\n2. Alice prepara el qubit según su elección:")
    print("   - Base Z: |0⟩ o |1⟩")
    print("   - Base X: |+⟩ o |-⟩")
    print("\n3. Bob elige aleatoriamente una base y mide")
    print("\n4. Alice y Bob comparan bases (usando control clásico IF):")
    print("   - Si coinciden: el bit es válido")
    print("   - Si no coinciden: descartan el bit")
    print("\n5. Verifican una muestra para detectar espías")

    print("\n" + "-"*70)
    print("Ejecutando simulación del protocolo...")
    print("-"*70 + "\n")

    prog = protocolo_bb84_simplificado()
    resultados = ejecutar_juego(prog, num_intentos=10)

    print("Resultados de 10 ejecuciones:")
    print("\nFormato: [bit_medido, base_alice, base_bob, bit_alice]")
    for i, res in enumerate(resultados, 1):
        bases_coinciden = res[1] == res[2]
        marca = "✅" if bases_coinciden else "❌"
        print(f"  {i:2d}. {res} {marca} {'(bases coinciden)' if bases_coinciden else '(bases diferentes - descartar)'}")

    coincidencias = sum(1 for res in resultados if res[1] == res[2])
    print(f"\nBits válidos: {coincidencias}/{len(resultados)} ({(coincidencias/len(resultados))*100:.1f}%)")
    print("(Teóricamente esperamos ~50% de coincidencia)")

    print("\n" + "="*70 + "\n")


def ejemplo_deteccion_trampa():
    """
    Ejemplo de detección de trampas usando entrelazamiento.
    """
    print("\n" + "="*70)
    print("EJEMPLO: DETECCIÓN DE TRAMPAS CON ENTRELAZAMIENTO")
    print("="*70 + "\n")

    print("Escenario:")
    print("-" * 70)
    print("Alice y Bob juegan con una moneda cuántica.")
    print("Alice quiere asegurarse de que Bob no haga trampa.")
    print("\nMétodo de Alice:")
    print("1. Prepara dos qubits entrelazados (Bell state)")
    print("2. Envía uno a Bob, mantiene el otro")
    print("3. Si Bob intenta medir antes de tiempo, rompe el entrelazamiento")
    print("4. Alice detecta la trampa al medir su qubit")

    print("\n" + "-"*70)
    print("Principio cuántico:")
    print("-"*70)
    print("Estado entrelazado: |Ψ⟩ = (|00⟩ + |11⟩)/√2")
    print("\nPropiedades:")
    print("  • Si ambos qubits se miden en la misma base,")
    print("    los resultados están perfectamente correlacionados")
    print("  • Cualquier medición intermedia destruye la correlación")
    print("  • Alice puede detectar esta decorrelación")

    print("\n" + "="*70 + "\n")


def menu_ejemplos():
    """
    Menú interactivo para ejecutar diferentes ejemplos.
    """
    while True:
        print("\n" + "="*70)
        print("EJEMPLOS DE CONTROL CLÁSICO EN PYQUIL")
        print("="*70)
        print("\n1. Demostración completa de control clásico")
        print("2. Ejemplo básico de control IF")
        print("3. Protocolo BB84 simplificado")
        print("4. Detección de trampas con entrelazamiento")
        print("5. Análisis completo de detección")
        print("0. Salir")
        print("\n" + "="*70)

        try:
            opcion = input("\nSelecciona una opción (0-5): ").strip()

            if opcion == "0":
                print("\n¡Hasta luego!\n")
                break
            elif opcion == "1":
                demostrar_control_clasico()
            elif opcion == "2":
                ejemplo_basico_control_if()
            elif opcion == "3":
                ejemplo_protocolo_bb84()
            elif opcion == "4":
                ejemplo_deteccion_trampa()
            elif opcion == "5":
                ejecutar_analisis_completo()
            else:
                print("\n⚠️  Opción no válida. Por favor, elige 0-5.")

            input("\nPresiona Enter para continuar...")

        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!\n")
            break
        except Exception as e:
            print(f"\n⚠️  Error: {e}")
            input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    print("\n🔬 Bienvenido a los ejemplos de Control Clásico en PyQuil")

    # Ejecutar el menú interactivo
    # menu_ejemplos()

    # O ejecutar todos los ejemplos directamente
    ejemplo_basico_control_if()
    ejemplo_protocolo_bb84()
    ejemplo_deteccion_trampa()
    demostrar_control_clasico()
    ejecutar_analisis_completo()
