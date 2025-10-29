from pyquil import get_qc, Program
from pyquil.gates import I,X,SWAP,MEASURE
from pyquil.quilbase import Declare
import numpy as np

prog = Program(
	Declare("ro", "BIT", 2),
	I(0),X(1),
	MEASURE(0, ("ro", 0)),
	MEASURE(1, ("ro", 1)))

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)

prog = Program(
        Declare("ro", "BIT", 2),
        I(0),X(1),
	    SWAP(0,1),
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1)))

result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")

print(result)

matr = [[0],[0],[1],[0]]
swap = [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]

print(np.dot(swap,matr))
