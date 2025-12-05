#!/usr/bin/env python3
"""
Resumen Ejecutable - Práctica S14

Script de acceso rápido a todas las funcionalidades.
Para una experiencia completa, ejecuta: python main.py
"""

import sys
from pathlib import Path

# Añadir al path
sys.path.insert(0, str(Path(__file__).parent))


def resumen():
    """Muestra un resumen de la práctica."""
    print("""
TPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPW
Q                 PRÁCTICA S14 - CONCEPTOS AVANZADOS DE PYQUIL               Q
ZPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP]

=Ú CONTENIDO:

1ã  ENTREGABLE 1: Multithreading
   =Â entregable1_multithreading/
   ¡ Ejecución paralela de circuitos cuánticos
   <¯ Competición de 4 monedas con ThreadPoolExecutor
   =Ê Análisis de speedup y rendimiento

2ã  ENTREGABLE 2: Control Clásico
   =Â entregable2_control_clasico/
   <® Estructuras IF/WHILE en circuitos cuánticos
   = Detección de trampas con entrelazamiento
   = Protocolo BB84 simplificado

3ã  DOCUMENTACIÓN: Acceso a QPU Real
   =Â docs/guia_qpu_real.md
   =¥  Guía completa de solicitud de acceso
   ™  Configuración y mejores prácticas
   < Diferencias QVM vs QPU

PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP

=€ INICIO RÁPIDO:

   Opción 1 (Menú completo):
   $ python main.py

   Opción 2 (Entregable 1 directo):
   $ cd entregable1_multithreading && python ejemplo_uso.py

   Opción 3 (Entregable 2 directo):
   $ cd entregable2_control_clasico && python ejemplo_uso.py

PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP

=Ö DOCUMENTACIÓN:

   " README.md          - Documentación completa
   " GUIA_RAPIDA.md     - Guía de inicio rápido
   " docs/guia_qpu_real.md - Acceso a hardware real

PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP

=' INSTALACIÓN:

   $ pip install -r requirements.txt

   Dependencias:
   - pyquil >= 4.0.0
   - numpy >= 1.20.0
   - matplotlib >= 3.3.0

PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
""")


def demo_rapida_multithreading():
    """Demo rápida de multithreading."""
    print("\n" + "="*80)
    print("DEMO RÁPIDA: MULTITHREADING")
    print("="*80 + "\n")

    try:
        from entregable1_multithreading.moneda_cuantica import (
            competicion_cuatro_monedas_multithreading,
            analizar_resultados
        )

        print("Ejecutando competición con multithreading (10 tiradas por moneda)...\n")
        resultados, tiempo = competicion_cuatro_monedas_multithreading(num_tiradas=10)
        analisis = analizar_resultados(resultados)

        print(f"\nResultados:")
        print(f"  Total Caras:  {analisis['total_caras']}")
        print(f"  Total Cruces: {analisis['total_cruces']}")
        print(f"  Ganador:      {analisis['ganador']}")
        print(f"  Tiempo:       {tiempo:.3f}s")
        print("\n Demo completada. Para más detalles: python main.py")

    except Exception as e:
        print(f"L Error: {e}")
        print("Asegúrate de instalar las dependencias: pip install -r requirements.txt")


def demo_rapida_control_clasico():
    """Demo rápida de control clásico."""
    print("\n" + "="*80)
    print("DEMO RÁPIDA: CONTROL CLÁSICO")
    print("="*80 + "\n")

    try:
        from entregable2_control_clasico.juego_moneda_trampa import (
            juego_moneda_con_control_if
        )

        print("Circuito con control IF para detección de trampas:\n")
        prog = juego_moneda_con_control_if()
        print(prog)
        print("\n Demo completada. Para más detalles: python main.py")

    except Exception as e:
        print(f"L Error: {e}")
        print("Asegúrate de instalar las dependencias: pip install -r requirements.txt")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando in ['mt', 'multithreading', '1']:
            demo_rapida_multithreading()
        elif comando in ['cc', 'control', '2']:
            demo_rapida_control_clasico()
        elif comando in ['help', '-h', '--help']:
            resumen()
            print("\nUso: python pr.py [comando]")
            print("\nComandos:")
            print("  mt, multithreading, 1  - Demo de multithreading")
            print("  cc, control, 2         - Demo de control clásico")
            print("  help, -h, --help       - Mostrar esta ayuda")
            print("\nSin argumentos: mostrar resumen\n")
        else:
            print(f"Comando desconocido: {comando}")
            print("Usa 'python pr.py help' para ver comandos disponibles")
    else:
        resumen()
        print("\n=¡ Consejo: Ejecuta 'python main.py' para el menú completo interactivo\n")
