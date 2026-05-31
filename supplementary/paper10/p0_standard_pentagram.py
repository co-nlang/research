#!/usr/bin/env python3
"""P0: Verify standard pentagram parity with corrected Pauli format."""

import numpy as np

I2 = np.array([[1, 0], [0, 1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}

def pauli_to_vector(s):
    """Convert Pauli string to symplectic vector (x1,x2,x3,z1,z2,z3)."""
    x = [0, 0, 0]
    z = [0, 0, 0]
    for q, c in enumerate(s):
        if c == 'X':
            x[q] = 1
        elif c == 'Y':
            x[q] = 1
            z[q] = 1
        elif c == 'Z':
            z[q] = 1
    return tuple(x + z)

def vector_to_pauli_string(v):
    """Corrected: v = (x1,x2,x3,z1,z2,z3)."""
    chars = []
    for q in range(3):
        x, z = v[q], v[q + 3]
        if x == 0 and z == 0:
            chars.append('I')
        elif x == 1 and z == 0:
            chars.append('X')
        elif x == 1 and z == 1:
            chars.append('Y')
        elif x == 0 and z == 1:
            chars.append('Z')
    return ''.join(chars)

def get_pauli3(v):
    s = vector_to_pauli_string(v)
    M = PAULI[s[0]]
    for c in s[1:]:
        M = np.kron(M, PAULI[c])
    return M

def context_product_sign(ops):
    P = np.eye(8, dtype=complex)
    for v in ops:
        P = P @ get_pauli3(v)
    return int(round(P[0, 0].real))

# Standard pentagram from Paper IX
contexts = {
    'C1': ['XXX', 'XYY', 'YXY', 'YYX'],
    'C2': ['XXX', 'ZZX', 'ZXZ', 'XZZ'],
    'C3': ['YXY', 'ZXZ', 'ZYY', 'YYZ'],
    'C4': ['YYX', 'ZZX', 'ZYY', 'YZY'],
    'C5': ['XYY', 'XZZ', 'YYZ', 'YZY'],
}

print("Standard Pentagram Parity Check (corrected Pauli format)")
print("=" * 60)

minus_count = 0
for name, ops in contexts.items():
    vecs = [pauli_to_vector(op) for op in ops]
    sign = context_product_sign(vecs)
    pauli_check = [vector_to_pauli_string(v) for v in vecs]
    status = "-I" if sign == -1 else "+I"
    if sign == -1:
        minus_count += 1
    print(f"  {name}: {ops} -> {pauli_check} -> {sign} ({status})")

print(f"\nTotal -I contexts: {minus_count}/5")
print(f"Parity: {'ODD (Mermin)' if minus_count % 2 == 1 else 'EVEN (NOT Mermin)'}")
