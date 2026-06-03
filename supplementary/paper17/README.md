# Paper XVII: Supplementary Computational Scripts

## Scripts

### `pentagram_holonomy.py`

K₅ structure analysis and Weyl holonomy computation for all 12,096 pentagrams.

**Steps:**
1. Enumerate 135 Lagrangians, 945 contexts, 12,096 pentagrams
2. Build K₅ shared-ray matrix for each pentagram (vᵢⱼ = Cᵢ ∩ Cⱼ)
3. Count anticommuting cross-context pairs N for each pentagram
4. Verify N = 15 for all 12,096 pentagrams (100%)
5. Compare β_sum vs N (both ≡ 2 mod 4, but not equal)
6. Verify β_sum vs cross-context ω_int sum

**Runtime:** ~60 seconds

**Requirements:** Python 3, NumPy

### `check_all_k5.py`

Exhaustive search for even-parity K₅ configurations (parity +1).

**Steps:**
1. Enumerate all 5-cliques of Lagrangians with pairwise dim(Lᵢ ∩ Lⱼ) = 1
2. Compute parity for each K₅ configuration
3. Verify: zero even-parity K₅s exist

**Runtime:** ~30 seconds

**Requirements:** Python 3, NumPy

### `t_vector_holonomy.py`

T-vector analysis: for each pentagram, find T ∈ F₂⁶ with ω(T, v) = 1 for all 10 rays, and explore relationships between T and β_sum.

**Steps:**
1. Enumerate pentagrams
2. Solve ω(T, v) = 1 for all 10 rays (F₂ linear system)
3. Test candidate identities: β_sum ≡ Σ ω_int(T,v)² (mod 4), β_sum ≡ Σ ω_int(T,v) (mod 4)
4. Context-level analysis: s(C) vs Σ_{v∈C} ω_int(T,v)

**Runtime:** ~60 seconds

**Requirements:** Python 3, NumPy

## Key Results

| Script | Result | Status |
|--------|--------|--------|
| `pentagram_holonomy.py` | N = 15 anticommuting cross-context pairs for all pentagrams | 12,096/12,096 ✓ |
| `pentagram_holonomy.py` | ∏_C W_C = (-1)^{15} I₈ = -I₈ | 12,096/12,096 ✓ |
| `check_all_k5.py` | Zero even-parity K₅ configurations exist | 0 found ✓ |
| `t_vector_holonomy.py` | T-vector exists for all pentagrams (unique solution) | 12,096/12,096 ✓ |

### Cross-Context Anticommutation (Theorem 17.1)

For any K₅ configuration of Lagrangians (L₁,...,L₅) in Sp(6,F₂), all 15 cross-context ray pairs {vᵢⱼ, vₖₗ} (with {i,j} ∩ {k,l} = ∅) satisfy ω(vᵢⱼ, vₖₗ) = 1.

**Proof sketch:** Fano zero-sum forces uniformity within each row; ω mod 2 symmetry propagates to global constant c; size argument (10 > 7) forces c = 1.

**Corollary:** ∏_C W_C = (-1)^{15} I₈ = -I₈ algebraically, with no enumeration needed.
