from pyquil import get_qc, Program
from pyquil.gates import CNOT, X, MEASURE
from pyquil.quilbase import Declare

prog = Program(
    Declare("ro", "BIT", 2),
    X(0),
    X(1),
    CNOT(1, 0),               
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(100)

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog))

measurements = result.readout_data['ro']

for i, measurement in enumerate(measurements):
    print(f"Shot {i}: {measurement}")