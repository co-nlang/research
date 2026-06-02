# Paper XIV Supplementary Materials

## Scripts

### `stabilizer_algebra.py`

**Purpose:** Computes stabilizer algebras for all 4 G₂(2) orbits and verifies k-profile exhaustiveness.

**Key results:**
- O₁: Z₂ (order 2, abelian)
- O₂: S₃ (order 6, non-abelian, 3 order-2, 2 order-3)
- O₃: S₃ (same)
- O₄: S₃ (same)
- k-Profile: 7 types, 12,096/12,096 odd parity (100%)
- Runtime: 57s

**k-Profile distribution:**
| k-profile | Count | % |
|-----------|-------|------|
| (1,1,1,0,0) | 3,584 | 29.6% |
| (1,0,0,0,0) | 2,688 | 22.2% |
| (3,1,1,0,0) | 2,688 | 22.2% |
| (3,3,3,0,0) | 896 | 7.4% |
| (1,1,1,1,1) | 896 | 7.4% |
| (3,0,0,0,0) | 896 | 7.4% |
| (7,1,1,1,1) | 448 | 3.7% |

**Requirements:** Python 3, numpy

**Usage:** `python3 stabilizer_algebra.py`

### `beta_distribution.py`

**Purpose:** Computes β_sum distribution and h-patterns per k-profile for all 12,096 pentagrams.

**Key results:**
- β_sum range: [-34, 30]
- β_sum mod 4 = 2 (100%)
- β_sum/2 range: [-17, 15]
- Only 3 distinct h-patterns: (0,0,0,0,1), (0,0,1,1,1), (1,1,1,1,1)
- (3,3,3,0,0) and (7,1,1,1,1) have NO 5-minus pentagrams
- Runtime: 49s

**Requirements:** Python 3, numpy

**Usage:** `python3 beta_distribution.py`

## Key Findings

1. All three order-6 stabilizers are S₃ (not Z₆). The Orbit 4 parity anomaly is NOT explained by stabilizer algebra type.

2. Only 3 h-patterns exist across all 12,096 pentagrams — a striking structural constraint.

3. β_sum is tightly concentrated: median = -2 for ALL k-profiles, range [-34, 30].
