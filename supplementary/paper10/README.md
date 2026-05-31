# Paper X: Equiangular Characterization of Mermin Pentagrams

Python scripts verifying the equiangular Lagrangian characterization of Mermin pentagrams in the 3-qubit Pauli group.

## Scripts

- **`paper10_conjecture25.py`**: Original Conjecture 2.5 testing (collinearity-obstruction dictionary). Enumerates 135 Lagrangians, 945 proper contexts, and searches for Mermin pentagrams. Result: Conjecture 2.5 fails; collinearity is not the obstruction.

- **`p0_standard_pentagram.py`**: Verifies the standard Mermin pentagram has odd parity (all 5 contexts multiply to -I).

- **`p1_orbit_check.py`**: Analyzes the 12,096 Mermin pentagrams and their relation to the G₂(2) group action.

- **`p2_type_b_analysis.py`**: Type B analysis (4 distinct Fano points). Collinearity vs sign pattern correlation.

- **`p3_sign_patterns.py`**: Sign pattern analysis for Type B and Type F2 pentagrams (collinear vs non-collinear subsets).

- **`p3_corrected.py`**: Corrected full sign pattern analysis for Type B and Type F2.

- **`p3_verify_f2.py`**: Verification script for Type F2 (3 Fano points + 2 transverse).

- **`p4_type_f4.py`**: Type F4 analysis (1 Fano point + 4 transverse). Identifies 25% with zero Fano points (pure transverse).

- **`p5_lagrangian_intersection.py`**: Analyzes Lagrangian intersection patterns and Ghost Pentagon Rigidity.

- **`p6_equiangular_check.py`**: Verifies Theorem 1.8 (necessity): all 12,096 Mermin pentagrams have equiangular Lagrangian configuration dim(Lᵢ ∩ Lⱼ) = 1.

- **`p7_ray_configuration.py`**: Verifies Theorem 1.9 (10-Ray Cap): 10 intersection rays form a cap in PG(5,F₂) with 0 collinear triples, spanning full F₂⁶.

- **`p8_sufficiency_check.py`**: Verifies Theorem 1.8 (sufficiency): all equiangular K₅ have odd parity. Confirms three-way equivalence: K₅ ⟺ equiangular ⟺ Mermin. Output: parity distribution 7,884 / 4,104 / 108. Note: reports 5× overcount (60,480) due to root vertex loop; true count is 12,096.

- **`g2_orbits.py`**: Computes the G₂(2) orbit decomposition of all 12,096 Mermin pentagrams. Uses G₂(2) generators extracted from GAP AtlasRep, transformed to standard symplectic basis. Result: 4 orbits of sizes 6,048 + 2,016 + 2,016 + 2,016.

- **`orbit_type_lagrangian.py`**: Classifies each pentagram by Lagrangian V-intersection profile (Type B/F2/F4) and reports distribution per G₂(2) orbit. Result: 2-class structure (Class I: orbits 1+2, Class II: orbits 3+4), Type B ratio constant at 1/9 across all orbits.

## Key Results

- **Type A exclusion**: 0 pentagrams with 5 distinct Fano points
- **Theorem 1.8**: K₅ ⟺ equiangular Lagrangian configuration (geometric proof + computational verification)
- **10-Ray Cap**: 10 shared operators form a cap in PG(5,F₂)
- **Parity**: 100% odd (1-minus: 65.2%, 3-minus: 33.9%, 5-minus: 0.9%)
- **G₂(2) orbits**: 12,096 pentagrams in 4 orbits (6,048 + 3 × 2,016)
- **2-class structure**: Orbits split into Class I (orbits 1+2, 8,064 pentagrams, 61.1% F2, 27.8% F4) and Class II (orbits 3+4, 4,032 pentagrams, 55.6% F2, 33.3% F4). Standard pentagram in Class I.
- **Type B invariance**: Type B ratio = 1/9 across all 4 orbits (G₂(2)-invariant)

## Requirements

- Python 3.9+
- NumPy

## Usage

Scripts are independent. Most complete in 5-10 minutes; `p8_sufficiency_check.py` takes ~10 minutes; `g2_orbits.py` takes ~7 minutes.

```bash
python paper10_conjecture25.py
python p0_standard_pentagram.py
python p8_sufficiency_check.py
```

## License

MIT (see LICENSE).
