#!/usr/bin/env python3
"""
item-24 test, part 2: does degree-3 need the H^3 pentagram, or does adaptive
composition of H^2 (GHZ) gates already reach it?

Part 1 (mbqc_degree.py): non-adaptive l2-MBQC on ANY stabilizer resource caps at
sigma-degree 2. So degree-3 must come from ADAPTIVITY (temporal composition + linear
classical control).

In l2-MBQC the classical control is LINEAR (it may only route/XOR bits). A measured
deterministic outcome may be fed as a setting bit to a later measurement -- that routing
is linear; the nonlinearity lives in each quantum gate. The Anders-Browne gate (a single
GHZ = an H^2 resource) deterministically computes AND(a,b) (degree 2, verified in part 1).

So we may compose AB/GHZ gates with linear wiring -- still valid adaptive l2-MBQC -- and
ask what degree we reach using ONLY H^2 resources (no pentagram).
"""
from itertools import product

def anf_degree(f, n):
    """Algebraic (ANF) degree of Boolean f: {0,1}^n -> {0,1}."""
    tt = [f(x) for x in product((0, 1), repeat=n)]  # index = sum x_i 2^(n-1-i)
    a = tt[:]
    # Mobius transform in this index convention
    for i in range(n):
        step = 1 << (n - 1 - i)
        for base in range(0, 1 << n, step << 1):
            for k in range(base, base + step):
                a[k + step] ^= a[k]
    deg = 0
    for idx, c in enumerate(a):
        if c:
            deg = max(deg, bin(idx).count("1"))
    return deg

# The H^2 gate (one GHZ, Anders-Browne), verified deterministic in part 1:
def AND(a, b):     # the genuinely nonlinear, degree-2 primitive from a single GHZ
    return a & b

# Adaptive composition with LINEAR control only (routing measured bits forward):
def deg3(x):       # two GHZ gates: AND(AND(q1,q2), q3)
    q1, q2, q3 = x
    return AND(AND(q1, q2), q3)

def deg4(x):       # three GHZ gates
    q1, q2, q3, q4 = x
    return AND(AND(AND(q1, q2), q3), q4)

print("=== degree reachable by adaptive composition of H^2 (GHZ) gates only ===")
print(f"  single GHZ gate  AND(q1,q2)            : degree {anf_degree(lambda x: AND(*x), 2)}")
print(f"  two GHZ gates    AND(AND(q1,q2),q3)    : degree {anf_degree(deg3, 3)}")
print(f"  three GHZ gates  AND(AND(AND..),q4)    : degree {anf_degree(deg4, 4)}")

print(f"""
=> Degree 3 (and any degree) is reached using ONLY H^2 (GHZ / Mermin-square) resources,
   composed with linear classical control. The H^3 PENTAGRAM IS NOT NEEDED for degree 3.

   This is expected: Anders-Browne already shows a single H^2 resource makes l2-MBQC
   universal (parity control + one AND = all Boolean functions). There is no room above
   it for H^3 to add computational power.

VERDICT on the conjecture 'cohomological degree = computational degree' (in l2-MBQC):
   REFUTED. Computational function-degree is governed by ADAPTIVE DEPTH (composition),
   not by the cohomological rung of the resource:
     - non-adaptively, every stabilizer resource (square or pentagram) = degree 2;
     - adaptively, H^2 alone already reaches every degree.
   The H^3 pentagram provides NO computational-degree separation over the H^2 square.
""")
