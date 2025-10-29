from pyquil import get_qc, Program
from pyquil.gates import I,X,CZ,MEASURE
from pyquil.quilbase import Declare
from pyquil.api import WavefunctionSimulator

prog = Program(
	Declare("ro", "BIT", 2),
	X(0),I(1))

qvm = WavefunctionSimulator()
result = qvm.wavefunction(prog)

print(result)

prog.inst(CZ(0,1))

result = qvm.wavefunction(prog)

print(result)
