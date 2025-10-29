from pyquil import get_qc, Program
from pyquil.gates import I,X,SWAP,MEASURE
from pyquil.quilbase import Declare

prog = Program(
	Declare("ro", "BIT", 2),
	I(0),I(1),
	MEASURE(0, ("ro", 0)),
	MEASURE(1, ("ro", 1)))

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)

prog = Program(
        Declare("ro", "BIT", 2),
        I(0),I(1),
	    SWAP(0,1),
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1)))

result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)
