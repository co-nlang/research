#!/usr/bin/env python3
"""
Verify the parity theorem algebraically on the standard pentagram.

Key identity:
  ∑h ≡ ∑q(r) + ∑ω_ns + ∑correction  (mod 2)

where:
  h(a,b) = ω_int(a,b)/2  (half-symplectic form)
  q(v) = x₁z₁ + x₂z₂ + x₃z₃  (quadratic form)
  ω_ns = sum of ω over non-sharing pairs
  correction = ∑_k a_xk·a_zk·b_xk·b_zk
"""

import numpy as np
from itertools import combinations

# Standard pentagram contexts (operator labels)
contexts = {
    'C1': ['XXX', 'XYY', 'YXY', 'YYX'],
    'C2': ['XXX', 'ZZX', 'ZXZ', 'XZZ'],
    'C3': ['YXY', 'ZXZ', 'ZYY', 'YYZ'],
    'C4': ['YYX', 'ZZX', 'ZYY', 'YZY'],
    'C5': ['XYY', 'XZZ', 'YYZ', 'YZY'],
}

# Pauli to (x,z) mapping
pauli_xz = {'I': (0,0), 'X': (1,0), 'Y': (1,1), 'Z': (0,1)}

def op_to_vec(op):
    """Convert 3-qubit operator to (x1,z1,x2,z2,x3,z3) in F_2^6."""
    v = []
    for ch in op:
        xi, zi = pauli_xz[ch]
        v.extend([xi, zi])
    return np.array(v, dtype=int)  # interleaved: x1,z1,x2,z2,x3,z3

def vec_from_interleaved(v):
    """Extract x=(x1,x2,x3) and z=(z1,z2,z3) from interleaved vector."""
    return v[0::2], v[1::2]

def omega_int(a, b):
    """Integer symplectic form: a_x · b_z - a_z · b_x."""
    ax, az = vec_from_interleaved(a)
    bx, bz = vec_from_interleaved(b)
    return int(np.dot(ax, bz) - np.dot(az, bx))

def q_form(v):
    """Standard quadratic form: x1*z1 + x2*z2 + x3*z3."""
    x, z = vec_from_interleaved(v)
    return int(np.dot(x, z))

def B_form(a, b):
    """Bilinear form B(a,b) = a_x · b_z."""
    ax, _ = vec_from_interleaved(a)
    _, bz = vec_from_interleaved(b)
    return int(np.dot(ax, bz))

def correction(a, b):
    """Quartic correction: sum_k a_xk * a_zk * b_xk * b_zk."""
    ax, az = vec_from_interleaved(a)
    bx, bz = vec_from_interleaved(b)
    return int(sum(ax[k]*az[k]*bx[k]*bz[k] for k in range(3)))

# Build ray vectors
ray_vecs = {}
for cname, ops in contexts.items():
    for op in ops:
        if op not in ray_vecs:
            ray_vecs[op] = op_to_vec(op)

rays = list(ray_vecs.keys())
print(f"Total rays: {len(rays)}")
for r in sorted(rays):
    v = ray_vecs[r]
    print(f"  {r}: {v.tolist()}, q={q_form(v)}")

# Build context-ray mapping
context_rays = {}
for cname, ops in contexts.items():
    context_rays[cname] = [ray_vecs[op] for op in ops]

# Identify sharing pairs (rays in same context)
sharing_pairs = []
non_sharing_pairs = []
ray_contexts = {r: [] for r in rays}
for cname, ops in contexts.items():
    for op in ops:
        ray_contexts[op].append(cname)

for i, r1 in enumerate(rays):
    for j, r2 in enumerate(rays):
        if i >= j:
            continue
        shared = set(ray_contexts[r1]) & set(ray_contexts[r2])
        if shared:
            sharing_pairs.append((r1, r2))
        else:
            non_sharing_pairs.append((r1, r2))

print(f"\nSharing pairs: {len(sharing_pairs)}")
print(f"Non-sharing pairs: {len(non_sharing_pairs)}")

# Compute all quantities
print("\n=== Sharing pairs ===")
sum_h = 0
sum_B_sharing = 0
sum_corr = 0
for r1, r2 in sharing_pairs:
    a, b = ray_vecs[r1], ray_vecs[r2]
    w = omega_int(a, b)
    h = w // 2
    B = B_form(a, b)
    c = correction(a, b)
    sum_h += h
    sum_B_sharing += B
    sum_corr += c
    print(f"  ({r1}, {r2}): ω={w}, h={h}, B={B}, corr={c}")

print(f"\n∑h (sharing) = {sum_h}, mod 2 = {sum_h % 2}")
print(f"∑B (sharing) = {sum_B_sharing}, mod 2 = {sum_B_sharing % 2}")
print(f"∑correction = {sum_corr}, mod 2 = {sum_corr % 2}")

print("\n=== Non-sharing pairs ===")
sum_omega_ns = 0
sum_B_ns = 0
for r1, r2 in non_sharing_pairs:
    a, b = ray_vecs[r1], ray_vecs[r2]
    w = omega_int(a, b)
    B = B_form(a, b)
    sum_omega_ns += w
    sum_B_ns += B
    print(f"  ({r1}, {r2}): ω={w}, B={B}")

print(f"\n∑ω (non-sharing) = {sum_omega_ns}, mod 2 = {sum_omega_ns % 2}")
print(f"∑B (non-sharing) = {sum_B_ns}, mod 2 = {sum_B_ns % 2}")

# Sum of q over all rays
sum_q = sum(q_form(ray_vecs[r]) for r in rays)
print(f"\n∑q(rays) = {sum_q}, mod 2 = {sum_q % 2}")

# Total omega
sum_omega_all = 0
for i, r1 in enumerate(rays):
    for j, r2 in enumerate(rays):
        if i < j:
            sum_omega_all += omega_int(ray_vecs[r1], ray_vecs[r2])
print(f"∑ω (all pairs) = {sum_omega_all}, mod 2 = {sum_omega_all % 2}")

# Verify identity: ∑h ≡ ∑q + ∑ω_ns + ∑corr (mod 2)
rhs = sum_q + sum_omega_ns + sum_corr
print(f"\n=== Identity verification ===")
print(f"∑h = {sum_h} ≡ {sum_h % 2} (mod 2)")
print(f"∑q + ∑ω_ns + ∑corr = {sum_q} + {sum_omega_ns} + {sum_corr} = {rhs} ≡ {rhs % 2} (mod 2)")
print(f"Match: {sum_h % 2 == rhs % 2}")

# Also verify: ∑B_sharing = ∑q + ∑B_ns (mod 2)
rhs2 = sum_q + sum_B_ns
print(f"\n∑B_sharing = {sum_B_sharing} ≡ {sum_B_sharing % 2} (mod 2)")
print(f"∑q + ∑B_ns = {sum_q} + {sum_B_ns} = {rhs2} ≡ {rhs2 % 2} (mod 2)")
print(f"Match: {sum_B_sharing % 2 == rhs2 % 2}")

# Per-context β
print("\n=== Per-context β ===")
beta_sum = 0
for cname in sorted(context_rays.keys()):
    crays = context_rays[cname]
    beta = 0
    for a, b in combinations(crays, 2):
        beta += omega_int(a, b)
    sign = (-1)**(beta // 2)
    beta_sum += beta
    print(f"  {cname}: β={beta}, β/2={beta//2}, sign={sign:+d}")

print(f"\nβ_sum = {beta_sum}, β_sum mod 4 = {beta_sum % 4}")
print(f"∏sign = {(-1)**(beta_sum // 2):+d}")
print(f"∑(β/2) = {beta_sum // 2}, odd = {(beta_sum // 2) % 2 == 1}")
