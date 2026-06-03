# Paper XV Supplementary Materials

## Scripts

### `metaplectic_lift.py`

**Purpose:** Computes the Weil representation of Sp(6, F₂) restricted to G₂(2) on C⁸, then analyzes how the three S₃ stabilizer subgroups lift to the metaplectic group.

**Weil representation construction:**
- Three generator types: GL(n), symmetric (B), Fourier
- LDU decomposition for arbitrary symplectic matrices
- q=2 case: Gauss sum degenerates, use direct matrix construction

**Key results (60s runtime, full 12,096 G₂(2) elements):**

| Orbit | Group | Lift Type | c(st,st)=+1 | s² cocycles | t³ cocycles |
|-------|-------|-----------|-------------|-------------|-------------|
| O₁ | Z₂ | — | — | — | — |
| O₂ | S₃ | NON-SPLIT | 4/6 | [1, 1, -1] | [-1, -1] |
| O₃ | S₃ | SPLIT | 6/6 | [1, 1, 1] | [1, 1] |
| O₄ | S₃ | NON-SPLIT | 4/6 | [1, 1, -1] | [-1, 1] |

**Findings:**
1. O₃ is the ONLY split S₃ — all cocycles = +1. Correlates with O₃'s unique 25%/25%/25% k-profile uniformity (Paper XIV).
2. O₂ and O₄ are both non-split, but differ in t³ cocycles: O₂ = [-1,-1], O₄ = [-1,+1].
3. The O₄ mixed t³ cocycle is a candidate explanation for the Orbit 4 parity anomaly (60.6% vs 65-68%).
4. Split/non-split distinction cuts across Class I/II boundary.

**Requirements:** Python 3, numpy

**Usage:** `python3 metaplectic_lift.py`

### `weil_cocycle.py`

**Purpose:** Tests the conjecture β(C)/2 mod 2 = c(g_C, g_C^{-1}) mod 2, where g_C ∈ G₂(2) maps V → L_C.

**Result (50s, NEGATIVE):** 48.8% match rate — conjecture is FALSE.

**Structural diagnosis:** 81/135 Lagrangians have varying h values across their contexts, so a Lagrangian-level g_C cannot determine h(C). The β-cocycle identification must be at the context level, not the Lagrangian level.

**Additional finding:** G₂(2) acts on 135 Lagrangians with two orbits: 72 + 63 = 135.
- Orbit A (72): orbit of V, Stab ≅ GL(3, F₂) (order 168)
- Orbit B (63): complementary orbit, Stab order 192 = 2⁶×3

**Requirements:** Python 3, numpy

**Usage:** `python3 weil_cocycle.py`
