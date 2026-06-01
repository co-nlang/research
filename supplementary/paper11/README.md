# Paper XI: Quadratic Refinement and the Parity Theorem

Python scripts proving Conjecture 9.1 (equiangular → odd parity) via quadratic refinement and geometric decomposition of the symplectic form.

## Scripts

### Core Results

- **`quadratic_refinement_v2.py`**: Discovers the β-formula: s(C) = (-1)^{β(C)/2} where β(C) = ∑ ω_int(vⱼ,vₖ) (integer symplectic form). Verifies: (1) 0/945 mismatches; (2) β_sum ≡ 2 (mod 4) for all 12,096 pentagrams; (3) ω_total always odd. Runtime: ~437s.

- **`decompose_omega.py`**: Decomposes ω_total into 30 sharing pairs + 15 disjoint pairs. Proves: ω_sharing ≡ 0 (100%), ω_disjoint ≡ 1 (100%), and each vertex contributes ω_v ≡ 1 (100%). Runtime: ~440s.

- **`prove_disjoint_omega.py`**: Geometric proof that ω(r_{ij}, r_{kl}) = 1 for disjoint pairs. Verifies: (1) dim(L_k ∩ (L_i + L_j)) = 2 for all 30,000 triples; (2) r_{kl} ∉ L_i + L_j for all 15,000 disjoint pairs. Runtime: ~440s.

- **`verify_quadratic_identity.py`**: Verifies the quadratic form identity Q(T) ≡ ∑Q(r) + ω_total (mod 2) for all 12,096 pentagrams (100%). Runtime: ~440s.

### Supporting Analysis

- **`omega_integer_values.py`**: Analyzes integer ω_int values for disjoint pairs. Result: ω ∈ {-3, -1, +1, +3} (all odd), with 97.3% being ±1. Sum ranges from -19 to +27 (always odd). Runtime: ~440s.

- **`analyze_T_structure.py`**: Analyzes T = ∑r (sum of all 10 rays). Verifies: T ≠ 0 (100%), T ∉ L_i for any Lagrangian, 63 distinct T values. Runtime: ~440s.

- **`check_T.py`**: Verifies T ≠ 0 for all 12,096 pentagrams. Runtime: ~440s.

- **`check_full_identity.py`**: Verifies ω_ns ≡ 1 (100%) and ω_sharing ≡ 0 (100%). Tests decomposition ∑h ≡ ∑Q + ω_ns + c_sharing (fails 50.9% — decomposition incorrect). Runtime: ~440s.

- **`check_sum_q_plus_c.py`**: Tests ∑Q + c_sharing parity (varies 49.1%/50.9% — not invariant). Runtime: ~440s.

- **`verify_conditions.py`**: Checks individual conditions ∑Q(r) and c_sharing (both vary — not individually invariant). Runtime: ~440s.

### Orbit Analysis

- **`class2_characterization.py`**: k-profile and parity analysis per G₂(2) orbit. Computes Lagrangian V-intersection profiles, parity distributions, and Q-sum invariants. Result: Class I and Class II have distinct k-profile distributions; Q-sum is G₂(2)-invariant (55.6% Q=1, 44.4% Q=0). Runtime: ~458s.

### Standard Pentagram

- **`verify_identity.py`**: Verifies algebraic decomposition on the standard Mermin pentagram: ∑h=15, ∑B=57, ∑correction=12, ∑ω_ns=15, ∑Q=12, β_sum=30 ≡ 2 (mod 4). Runtime: <1s.

### Failed Approaches

- **`quadratic_refinement.py`**: Tests naive S-formula (S = ∑B(vⱼ,vₖ)): 464/945 mismatches. Discovers key identity S_sum ≡ ∑Q + ∑ω_all (mod 2) (1000/1000 match). Runtime: ~437s.

## Key Results

- **β-formula**: s(C) = (-1)^{β(C)/2} with 0/945 mismatches
- **Parity theorem**: β_sum ≡ 2 (mod 4) for all 12,096 pentagrams → KS contradiction
- **Geometric proof**: ω_disjoint ≡ 1 via cap property and dim(L_k ∩ (L_i+L_j))=2
- **Quadratic identity**: Q(T) + ∑Q(r) ≡ 1 (mod 2) for all pentagrams
- **Integer ω values**: ω_int ∈ {-3, -1, +1, +3} for disjoint pairs (all odd)

## Proof Structure

1. **β-formula** (computational): s(C) = (-1)^{β(C)/2}
2. **ω decomposition**: 45 pairs = 30 sharing (ω=0) + 15 disjoint (ω≡1)
3. **Geometric lemma** (computational): dim(L_k ∩ (L_i+L_j)) = 2
4. **Cap argument**: r_{kl} ∉ span(r_{ik}, r_{jk}) → r_{kl} ∉ r_{ij}^⊥ → ω=1
5. **Parity**: ω_total = 15 × (odd) ≡ 1 → β_sum ≡ 2 (mod 4)

## Requirements

- Python 3.9+
- NumPy

## Usage

Scripts are independent. Most complete in 7-8 minutes; `class2_characterization.py` takes ~8 minutes.

```bash
python quadratic_refinement_v2.py  # β-formula discovery
python decompose_omega.py          # ω decomposition
python prove_disjoint_omega.py     # geometric proof
```

## Data

- **Pentagrams**: 12,096 Mermin pentagrams (from `g2_orbits.py` in `paper10/`)
- **Contexts**: 945 proper contexts (135 Lagrangians × 7 Fano lines)
- **Rays**: 10 shared operators per pentagram (K₅ edges)

## References

- Paper X: *The Equiangular Characterization of Mermin Pentagrams*
- Paper IX: *The Obstruction Ladder*
- `g2_orbits.py` in `../paper10/` for G₂(2) generators and pentagram enumeration
