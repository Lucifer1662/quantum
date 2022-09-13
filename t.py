import numpy as np

import qiskit as qk

from qiskit import QuantumCircuit, transpile, Aer, IBMQ, QuantumRegister, ClassicalRegister
import qiskit as qk
from qiskit.quantum_info.operators import Operator


def Q1(a, b):
    qc = QuantumCircuit(2, 2)
    qc.initialize([a,b], 0)
    qc.cx(0,1)
    qc.s(1)
    # qc.barrier()
    # cx = Operator([
    #     [1, 0],
    #     [0, 0]
    # ])
    # qc.unitary(cx, 0, label='A')
    qc.measure(0,0)
    qc.z(1).c_if(0, 0)
    

    
    return qc

def foo():
    pass

