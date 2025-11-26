#!/usr/bin/env python3
"""
Dado Cuántico con Simulación de Ruido en PyQuil

Este script implementa un dado cuántico de 8 caras usando 3 qubits y estudia
cómo diferentes tipos de ruido cuántico afectan su comportamiento.

Autor: Proyecto Educativo de Computación Cuántica
Fecha: 2025
"""

import os
from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.noise import add_decoherence_noise, define_noisy_readout
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from scipy.stats import chisquare

# Configuración de matplotlib
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10


def crear_directorio_resultados():
    """Crea el directorio para guardar resultados si no existe."""
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
        print("✓ Directorio 'resultados/' creado")


def binario_a_dado(resultado_binario):
    """
    Convierte un resultado binario de 3 bits a un número del dado (1-8).

    Args:
        resultado_binario: Array de 3 bits [b2, b1, b0]

    Returns:
        int: Número del dado (1-8)

    Ejemplo:
        [1, 0, 1] → 101₂ → 5₁₀ → 6
    """
    decimal = resultado_binario[0] * 4 + resultado_binario[1] * 2 + resultado_binario[2] * 1
    return decimal + 1


def ejecutar_dado_sin_ruido(shots=10000):
    """
    Ejecuta el dado cuántico sin ruido.

    Args:
        shots: Número de lanzamientos del dado

    Returns:
        list: Resultados del dado (números del 1 al 8)
    """
    print(f"→ Ejecutando dado sin ruido ({shots} lanzamientos)...")

    qc = get_qc('3q-qvm')

    # Crear el programa cuántico
    program = Program()

    # Aplicar puerta Hadamard a cada qubit (crea superposición)
    program += H(0)
    program += H(1)
    program += H(2)

    # Declarar memoria clásica
    ro = program.declare('ro', 'BIT', 3)

    # Medir los qubits
    program += MEASURE(0, ro[0])
    program += MEASURE(1, ro[1])
    program += MEASURE(2, ro[2])

    # Ejecutar múltiples veces
    program = program.wrap_in_numshots_loop(shots)

    # Compilar y ejecutar
    executable = qc.compile(program)
    result = qc.run(executable)
    resultados_bits = result.get_register_map()['ro']

    # Convertir a números del dado
    resultados_dado = [binario_a_dado(bits) for bits in resultados_bits]

    print("  ✓ Completado")
    return resultados_dado


def ejecutar_dado_con_decoherencia(T1, T2, gate_time=200e-9, shots=10000):
    """
    Ejecuta el dado cuántico con ruido de decoherencia.

    Args:
        T1: Tiempo de relajación (segundos)
        T2: Tiempo de coherencia (segundos)
        gate_time: Duración de las puertas (segundos)
        shots: Número de lanzamientos

    Returns:
        list: Resultados del dado
    """
    qc = get_qc('3q-qvm')

    program = Program()
    program += H(0)
    program += H(1)
    program += H(2)

    ro = program.declare('ro', 'BIT', 3)
    program += MEASURE(0, ro[0])
    program += MEASURE(1, ro[1])
    program += MEASURE(2, ro[2])

    # Añadir ruido de decoherencia
    noisy_program = add_decoherence_noise(program, T1=T1, T2=T2, gate_time=gate_time)
    noisy_program = noisy_program.wrap_in_numshots_loop(shots)

    executable = qc.compile(noisy_program)
    result = qc.run(executable)
    resultados_bits = result.get_register_map()['ro']

    resultados_dado = [binario_a_dado(bits) for bits in resultados_bits]

    return resultados_dado


def ejecutar_dado_con_ruido_lectura(p00, p11, shots=10000):
    """
    Ejecuta el dado cuántico con ruido de lectura.

    Args:
        p00: Probabilidad de medir correctamente |0⟩
        p11: Probabilidad de medir correctamente |1⟩
        shots: Número de lanzamientos

    Returns:
        list: Resultados del dado
    """
    qc = get_qc('3q-qvm')

    program = Program()
    program += H(0)
    program += H(1)
    program += H(2)

    ro = program.declare('ro', 'BIT', 3)

    # Añadir ruido de lectura a cada qubit
    for qubit in [0, 1, 2]:
        program += define_noisy_readout(qubit, p00=p00, p11=p11)

    program += MEASURE(0, ro[0])
    program += MEASURE(1, ro[1])
    program += MEASURE(2, ro[2])

    program = program.wrap_in_numshots_loop(shots)

    executable = qc.compile(program)
    result = qc.run(executable)
    resultados_bits = result.get_register_map()['ro']

    resultados_dado = [binario_a_dado(bits) for bits in resultados_bits]

    return resultados_dado


def ejecutar_dado_con_ambos_ruidos(T1, T2, p00, p11, gate_time=200e-9, shots=10000):
    """
    Ejecuta el dado cuántico con ambos tipos de ruido.

    Args:
        T1: Tiempo de relajación
        T2: Tiempo de coherencia
        p00: Probabilidad de lectura correcta de |0⟩
        p11: Probabilidad de lectura correcta de |1⟩
        gate_time: Duración de las puertas
        shots: Número de lanzamientos

    Returns:
        list: Resultados del dado
    """
    qc = get_qc('3q-qvm')

    program = Program()
    program += H(0)
    program += H(1)
    program += H(2)

    ro = program.declare('ro', 'BIT', 3)

    # Ruido de lectura
    for qubit in [0, 1, 2]:
        program += define_noisy_readout(qubit, p00=p00, p11=p11)

    program += MEASURE(0, ro[0])
    program += MEASURE(1, ro[1])
    program += MEASURE(2, ro[2])

    # Ruido de decoherencia
    noisy_program = add_decoherence_noise(program, T1=T1, T2=T2, gate_time=gate_time)
    noisy_program = noisy_program.wrap_in_numshots_loop(shots)

    executable = qc.compile(noisy_program)
    result = qc.run(executable)
    resultados_bits = result.get_register_map()['ro']

    resultados_dado = [binario_a_dado(bits) for bits in resultados_bits]

    return resultados_dado


def calcular_frecuencias(resultados):
    """
    Calcula las frecuencias de cada cara del dado.

    Args:
        resultados: Lista de resultados del dado

    Returns:
        dict: Frecuencias en porcentaje para cada cara (1-8)
    """
    contador = Counter(resultados)
    total = len(resultados)

    # Asegurar que todas las caras estén representadas
    frecuencias = {i: (contador.get(i, 0) / total) * 100 for i in range(1, 9)}

    return frecuencias


def graficar_resultados_dado(resultados, titulo="Dado Cuántico", ax=None):
    """
    Grafica un histograma de los resultados del dado.

    Args:
        resultados: Lista de resultados
        titulo: Título del gráfico
        ax: Eje de matplotlib (opcional)

    Returns:
        matplotlib.axes: El eje con el gráfico
    """
    frecuencias = calcular_frecuencias(resultados)
    caras = list(frecuencias.keys())
    porcentajes = list(frecuencias.values())

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    # Barras
    bars = ax.bar(caras, porcentajes, color='skyblue', edgecolor='navy', alpha=0.7)

    # Línea del valor teórico
    ax.axhline(y=12.5, color='red', linestyle='--', linewidth=2, label='Teórico (12.5%)')

    # Configuración
    ax.set_xlabel('Cara del Dado', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frecuencia (%)', fontsize=12, fontweight='bold')
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_xticks(caras)
    ax.set_ylim([0, 20])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Valores sobre las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=9)

    return ax


def calcular_metricas(resultados, nombre):
    """
    Calcula métricas estadísticas para evaluar la calidad del dado.

    Args:
        resultados: Lista de resultados
        nombre: Nombre de la condición

    Returns:
        dict: Diccionario con métricas
    """
    frecuencias = calcular_frecuencias(resultados)
    valores = list(frecuencias.values())

    # Desviación estándar
    desv_std = np.std(valores)

    # Máxima desviación del valor teórico
    max_desv = max([abs(v - 12.5) for v in valores])

    # Test chi-cuadrado
    contadores = Counter(resultados)
    observados = [contadores.get(i, 0) for i in range(1, 9)]
    esperados = [len(resultados) / 8] * 8
    chi2, p_value = chisquare(observados, esperados)

    return {
        'Condición': nombre,
        'Desviación Estándar (%)': f"{desv_std:.3f}",
        'Max Desviación del 12.5% (%)': f"{max_desv:.3f}",
        'Chi-cuadrado': f"{chi2:.2f}",
        'p-value': f"{p_value:.4f}"
    }


def main():
    """Función principal que ejecuta todas las simulaciones."""

    print("="*70)
    print(" DADO CUÁNTICO CON SIMULACIÓN DE RUIDO EN PYQUIL")
    print("="*70)
    print()

    # Crear directorio para resultados
    crear_directorio_resultados()
    print()

    # Número de lanzamientos
    shots = 10000

    # =========================================================================
    # 1. DADO SIN RUIDO
    # =========================================================================
    print("[1/6] Ejecutando dado sin ruido...")
    resultados_sin_ruido = ejecutar_dado_sin_ruido(shots)
    print()

    # =========================================================================
    # 2. DADO CON DECOHERENCIA (3 niveles)
    # =========================================================================
    print("[2/6] Ejecutando dado con ruido de decoherencia...")

    niveles_decoherencia = {
        'Ruido Bajo (QPU actual)': {'T1': 30e-6, 'T2': 15e-6},
        'Ruido Medio': {'T1': 10e-6, 'T2': 5e-6},
        'Ruido Alto': {'T1': 1e-6, 'T2': 0.5e-6}
    }

    resultados_decoherencia = {}
    for nivel, params in niveles_decoherencia.items():
        print(f"  → {nivel}: T1={params['T1']*1e6:.1f}μs, T2={params['T2']*1e6:.1f}μs")
        resultados = ejecutar_dado_con_decoherencia(params['T1'], params['T2'], shots=shots)
        resultados_decoherencia[nivel] = resultados
        print("    ✓ Completado")
    print()

    # =========================================================================
    # 3. DADO CON RUIDO DE LECTURA (3 niveles)
    # =========================================================================
    print("[3/6] Ejecutando dado con ruido de lectura...")

    niveles_lectura = {
        'Alta Fidelidad (99%)': {'p00': 0.99, 'p11': 0.99},
        'Media Fidelidad (95%)': {'p00': 0.95, 'p11': 0.95},
        'Baja Fidelidad (85%)': {'p00': 0.85, 'p11': 0.85}
    }

    resultados_lectura = {}
    for nivel, params in niveles_lectura.items():
        print(f"  → {nivel}: p(0|0)={params['p00']}, p(1|1)={params['p11']}")
        resultados = ejecutar_dado_con_ruido_lectura(params['p00'], params['p11'], shots=shots)
        resultados_lectura[nivel] = resultados
        print("    ✓ Completado")
    print()

    # =========================================================================
    # 4. DADO CON AMBOS RUIDOS
    # =========================================================================
    print("[4/6] Ejecutando dado con ambos tipos de ruido...")
    resultados_ambos = ejecutar_dado_con_ambos_ruidos(
        T1=10e-6, T2=5e-6,
        p00=0.95, p11=0.95,
        shots=shots
    )
    print("  ✓ Completado")
    print()

    # =========================================================================
    # 5. GENERAR GRÁFICOS
    # =========================================================================
    print("[5/6] Generando gráficos...")

    # Gráfico 1: Sin ruido
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    graficar_resultados_dado(resultados_sin_ruido, "Dado Cuántico - Sin Ruido", ax=ax1)
    plt.tight_layout()
    plt.savefig('resultados/1_sin_ruido.png', dpi=150, bbox_inches='tight')
    print("  ✓ Guardado: resultados/1_sin_ruido.png")
    plt.close()

    # Gráfico 2: Comparativa de decoherencia
    fig2, axes2 = plt.subplots(1, 3, figsize=(18, 5))
    for idx, (nivel, resultados) in enumerate(resultados_decoherencia.items()):
        graficar_resultados_dado(resultados, f"Dado Cuántico - {nivel}", ax=axes2[idx])
    plt.tight_layout()
    plt.savefig('resultados/2_decoherencia.png', dpi=150, bbox_inches='tight')
    print("  ✓ Guardado: resultados/2_decoherencia.png")
    plt.close()

    # Gráfico 3: Comparativa de ruido de lectura
    fig3, axes3 = plt.subplots(1, 3, figsize=(18, 5))
    for idx, (nivel, resultados) in enumerate(resultados_lectura.items()):
        graficar_resultados_dado(resultados, f"Dado Cuántico - {nivel}", ax=axes3[idx])
    plt.tight_layout()
    plt.savefig('resultados/3_ruido_lectura.png', dpi=150, bbox_inches='tight')
    print("  ✓ Guardado: resultados/3_ruido_lectura.png")
    plt.close()

    # Gráfico 4: Comparativa final 2x2
    fig4, axes4 = plt.subplots(2, 2, figsize=(16, 12))
    axes4 = axes4.flatten()

    graficar_resultados_dado(resultados_sin_ruido, "Sin Ruido (Ideal)", ax=axes4[0])
    graficar_resultados_dado(
        resultados_decoherencia['Ruido Medio'],
        "Con Ruido de Decoherencia (T1=10μs, T2=5μs)",
        ax=axes4[1]
    )
    graficar_resultados_dado(
        resultados_lectura['Media Fidelidad (95%)'],
        "Con Ruido de Lectura (95% fidelidad)",
        ax=axes4[2]
    )
    graficar_resultados_dado(resultados_ambos, "Con Ambos Tipos de Ruido", ax=axes4[3])

    plt.suptitle('Comparativa Completa: Efectos del Ruido en el Dado Cuántico',
                 fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('resultados/4_comparativa_final.png', dpi=150, bbox_inches='tight')
    print("  ✓ Guardado: resultados/4_comparativa_final.png")
    plt.close()

    print()

    # =========================================================================
    # 6. TABLA DE MÉTRICAS
    # =========================================================================
    print("[6/6] Calculando métricas estadísticas...")

    metricas = [
        calcular_metricas(resultados_sin_ruido, "Sin Ruido"),
        calcular_metricas(resultados_decoherencia['Ruido Medio'], "Decoherencia Media"),
        calcular_metricas(resultados_lectura['Media Fidelidad (95%)'], "Lectura Media (95%)"),
        calcular_metricas(resultados_ambos, "Ambos Ruidos")
    ]

    df_metricas = pd.DataFrame(metricas)

    print()
    print("="*80)
    print(" TABLA RESUMEN DE MÉTRICAS")
    print("="*80)
    print()
    print(df_metricas.to_string(index=False))
    print()
    print("="*80)

    # Guardar tabla como CSV
    df_metricas.to_csv('resultados/metricas.csv', index=False)
    print()
    print("✓ Tabla guardada en: resultados/metricas.csv")
    print()

    # =========================================================================
    # RESUMEN FINAL
    # =========================================================================
    print("="*70)
    print(" SIMULACIÓN COMPLETADA")
    print("="*70)
    print()
    print("Archivos generados:")
    print("  - resultados/1_sin_ruido.png")
    print("  - resultados/2_decoherencia.png")
    print("  - resultados/3_ruido_lectura.png")
    print("  - resultados/4_comparativa_final.png")
    print("  - resultados/metricas.csv")
    print()
    print("Para más detalles, consulta el notebook: dado_cuantico_ruido.ipynb")
    print("="*70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Simulación interrumpida por el usuario")
    except Exception as e:
        print(f"\n\n❌ Error durante la ejecución: {e}")
        import traceback
        traceback.print_exc()
