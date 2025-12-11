from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare
from concurrent.futures import ThreadPoolExecutor
import time


def ejecutar_moneda(num_tiradas):
    prog = Program(
        Declare("ro", "BIT", 1),
        H(0),
        MEASURE(0, ("ro", 0))
    )
    qvm = get_qc('9q-square-qvm')
    prog = prog.wrap_in_numshots_loop(num_tiradas)
    result = qvm.run(qvm.compile(prog))
    return result.get_register_map().get("ro")


def competicion_secuencial(num_tiradas=50):
    inicio = time.time()
    resultados = [ejecutar_moneda(num_tiradas) for _ in range(4)]
    return resultados, time.time() - inicio


def competicion_multithreading(num_tiradas=50):
    inicio = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for _ in range(4):
            future = executor.submit(ejecutar_moneda, num_tiradas)
            futures.append(future)

        resultados = []
        for f in futures:
            resultado = f.result()
            resultados.append(resultado)

    tiempo_total = time.time() - inicio
    return resultados, tiempo_total


def analizar_resultados(resultados):
    caras = sum((r == 0).sum() for r in resultados)
    cruces = sum((r == 1).sum() for r in resultados)

    if caras > cruces:
        ganador = "CARAS"
    elif cruces > caras:
        ganador = "CRUCES"
    else:
        ganador = "EMPATE"

    return {'caras': caras, 'cruces': cruces, 'ganador': ganador}


def imprimir_resultados(analisis, tiempo):
    print(f"\nCaras: {analisis['caras']}")
    print(f"Cruces: {analisis['cruces']}")
    print(f"Ganador: {analisis['ganador']}")
    print(f"Tiempo: {tiempo:.3f}s\n")
