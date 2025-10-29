from pyquil import get_qc, Program
from pyquil.gates import I,X,CNOT,MEASURE
from pyquil.quilbase import Declare
import numpy as np

prog = Program(
	Declare("ro", "BIT", 2),
	X(0),I(1),
	MEASURE(0, ("ro", 0)),
	MEASURE(1, ("ro", 1)))

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)

prog = Program(
        Declare("ro", "BIT", 2),
        X(0),I(1),
	    CNOT(0,1),
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1)))

result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)

