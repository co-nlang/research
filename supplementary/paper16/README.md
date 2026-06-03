# Paper XVI: Supplementary Computational Scripts

## Scripts

### `displacement_operator.py`

Weyl (Pauli-string) operator verification for all contexts and pentagrams.

**Steps:**
1. Enumerate 135 Lagrangians, 945 contexts, 12,096 pentagrams
2. Fano zero-sum: verify v₁⊕v₂⊕v₃⊕v₄ = 0 for all 945 contexts
3. Weyl product theorem: verify W_C = s(C)·I₈ for all 945 contexts
4. β-phase: verify (-i)^{β(C)} = s(C) for all 945 contexts
5. Pentagram product: verify ∏_C W_C = -I₈ for all 12,096 pentagrams
6. G₂(2) equivariance: Weyl sign distribution by k-type

**Runtime:** ~60 seconds

**Requirements:** Python 3, NumPy

## Key Results

| Step | Result | Status |
|------|--------|--------|
| Fano zero-sum | v₁⊕v₂⊕v₃⊕v₄ = 0 for all 945 contexts | 945/945 ✓ |
| Weyl Product Theorem | W_C = s(C)·I₈ for all 945 contexts | 945/945 ✓ |
| β-phase | (-i)^{β(C)} = s(C) for all 945 contexts | 945/945 ✓ |
| Pentagram Product | ∏_C W_C = -I₈ for all 12,096 pentagrams | 12,096/12,096 ✓ |

### Weyl Sign Distribution by k-type

| k-type | Total | s=-1 | s=+1 | % minus |
|--------|-------|------|------|---------|
| 0 | 448 | 176 | 272 | 39.3% |
| 1 | 392 | 128 | 264 | 32.7% |
| 3 | 98 | 20 | 78 | 20.4% |
| 7 | 7 | 0 | 7 | 0.0% |
| **Total** | **945** | **324** | **621** | **34.3%** |
