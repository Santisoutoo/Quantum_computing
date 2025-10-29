from pyquil import get_qc, Program
from pyquil.gates import I,X,CSWAP,MEASURE
from pyquil.quilbase import Declare

prog = Program(
	Declare("ro", "BIT", 3),
	X(0),X(1),X(2),
	MEASURE(0, ("ro", 0)),
	MEASURE(1, ("ro", 1)),
	MEASURE(2, ("ro", 2)))

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)

prog = Program(
        Declare("ro", "BIT", 3),
        X(0),X(1),X(2),
	CSWAP(0,1,2),
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1)),
	MEASURE(2, ("ro", 2)))

result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)
