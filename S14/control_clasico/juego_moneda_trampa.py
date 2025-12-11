from pyquil import Program, get_qc
from pyquil.gates import H, X, MEASURE
from pyquil.quilbase import Declare


def control_simple():
    prog = Program(
        Declare("ro", "BIT", 2),
        H(0),
        MEASURE(0, ("ro", 0))
    )
    prog.if_then(("ro", 0), Program(X(1)))
    prog += MEASURE(1, ("ro", 1))
    return prog


def copiar_bit():
    prog = Program(
        Declare("ro", "BIT", 2),
        H(0),
        MEASURE(0, ("ro", 0))
    )
    prog.if_then(("ro", 0), Program(X(1)))
    prog += MEASURE(1, ("ro", 1))
    return prog


def correccion_error():
    prog = Program(
        Declare("ro", "BIT", 2),
        X(0),
        MEASURE(0, ("ro", 0))
    )
    prog.if_then(("ro", 0), Program(X(0)))
    prog += MEASURE(0, ("ro", 1))
    return prog


def ejecutar_programa(program, num_intentos=10):
    qvm = get_qc('9q-square-qvm')
    resultados = []

    for _ in range(num_intentos):
        result = qvm.run(qvm.compile(program))
        resultados.append(result.get_register_map().get("ro")[0])

    return resultados


def analizar_trampas(resultados):
    total = len(resultados)
    trampas = sum(1 for r in resultados if len(r) >= 2 and r[0] != r[1])

    return {
        'total': total,
        'trampas': trampas,
        'tasa': (trampas / total) * 100
    }


def imprimir_analisis(analisis):
    print(f"\nTotal: {analisis['total']}")
    print(f"Trampas: {analisis['trampas']}")
    print(f"Tasa: {analisis['tasa']:.1f}%\n")
