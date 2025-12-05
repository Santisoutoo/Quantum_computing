#!/usr/bin/env python3
"""
Script de prueba rápida para verificar que los módulos funcionan correctamente
con el estilo de código actualizado.
"""

from pyquil import get_qc, Program
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare

print("="*70)
print("TEST RÁPIDO - Verificación del estilo de código")
print("="*70 + "\n")

# Test 1: Programa simple con el nuevo estilo
print("1. Test de programa simple:")
print("-" * 70)

prog = Program(
    Declare("ro", "BIT", 1),
    H(0),
    MEASURE(0, ("ro", 0))
).wrap_in_numshots_loop(10)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.get_register_map().get("ro")

print(f"Resultados de 10 lanzamientos: {measurements.flatten()}")
print(f"Promedio (esperado ~0.5): {measurements.mean():.2f}")
print("✅ Test 1 completado\n")

# Test 2: Importar y usar módulo de multithreading
print("2. Test de módulo multithreading:")
print("-" * 70)

try:
    from entregable1_multithreading.moneda_cuantica import (
        crear_programa_moneda,
        ejecutar_moneda_single
    )

    # Crear programa de moneda
    prog_moneda = crear_programa_moneda(0)
    print(f"Programa de moneda creado:\n{prog_moneda}")

    # Ejecutar una moneda
    resultado = ejecutar_moneda_single(1, num_tiradas=10)
    print(f"\nResultado: Moneda {resultado.moneda_id}")
    print(f"  Caras: {resultado.caras}, Cruces: {resultado.cruces}")
    print(f"  Tiempo: {resultado.tiempo_ejecucion:.3f}s")
    print("✅ Test 2 completado\n")

except Exception as e:
    print(f"❌ Error en test 2: {e}\n")

# Test 3: Importar y usar módulo de control clásico
print("3. Test de módulo control clásico:")
print("-" * 70)

try:
    from entregable2_control_clasico.juego_moneda_trampa import (
        juego_moneda_sin_control,
        ejecutar_juego
    )

    # Crear programa sin control
    prog_sin_control = juego_moneda_sin_control()
    print(f"Programa sin control:\n{prog_sin_control}")

    # Ejecutar juego
    resultados = ejecutar_juego(prog_sin_control, num_intentos=5)
    print(f"\nResultados de 5 intentos: {resultados}")
    print("✅ Test 3 completado\n")

except Exception as e:
    print(f"❌ Error en test 3: {e}\n")

print("="*70)
print("TODOS LOS TESTS COMPLETADOS")
print("="*70)
print("\nAhora puedes ejecutar:")
print("  • python main.py          - Para el menú completo")
print("  • python pr.py           - Para ver el resumen")
print("="*70 + "\n")
