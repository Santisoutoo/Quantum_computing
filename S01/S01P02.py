from pyquil import get_qc, Program
from pyquil.gates import CNOT, H, MEASURE
from pyquil.quilbase import Declare


prog = Program(
    Declare("ro", "BIT", 2),
    H(0),
    CNOT(0, 1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(100)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))
measurements = result.readout_data['ro']

for res in measurements:
    print(res)
