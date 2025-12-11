from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare


def crear_programa_base(num_qubits, aplicar_hadamard=True):
    prog = Program(Declare("ro", "BIT", num_qubits))

    if aplicar_hadamard:
        for i in range(num_qubits):
            prog += H(i)

    return prog


def medir_qubits(program, qubits):
    for i, qubit in enumerate(qubits):
        program += MEASURE(qubit, ("ro", i))
    return program


def ejecutar_programa(program, num_shots=1, qvm_name='9q-square-qvm'):
    qvm = get_qc(qvm_name)
    program_wrapped = program.wrap_in_numshots_loop(num_shots)
    result = qvm.run(qvm.compile(program_wrapped))
    return result.get_register_map().get("ro")


def interpretar_resultado_binario(bits):
    resultado = 0
    for i, bit in enumerate(bits):
        resultado += bit * (2 ** (len(bits) - 1 - i))
    return resultado
