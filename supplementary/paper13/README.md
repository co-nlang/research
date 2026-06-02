# Paper XIII Supplementary Scripts

Scripts for "The Maslov Index and the Kochen–Specker Obstruction: Negative Results, the k-Profile Theorem, and Orbit 4 Anomaly"

## Scripts

| Script | Description | Runtime |
|--------|-------------|---------|
| `maslov_index.py` | Kashiwara triple index computation for Mermin pentagrams | ~15min (full), ~5min (500 sample) |
| `maslov_candidates.py` | Tests 8 alternative Maslov-like quantities against β_sum/2 | ~5min (500 sample) |
| `path_a_half_symplectic_sample.py` | **Key result**: verifies Σhᵢ mod 2 is determined by k-profile (7 profiles, all → odd) | ~5min |
| `analyze_h_structure.py` | Analyzes h(C) mod 2 distribution by k-type and V-point count | ~2min |
| `analyze_h_correlation.py` | Analyzes h-pattern correlation within pentagrams by k-profile | ~5min |
| `class2_full.py` | Full enumeration of G₂(2)-equivariant invariants across 4 orbits (Class I/II comparison) | ~7min |

## Key Results

1. **Kashiwara index refuted**: Standard Kashiwara Maslov index does NOT equal β_sum/2 (match rate <11%)
2. **β_sum ordering dependence**: β_sum depends on point ordering, but β_sum mod 4 = 2 is ordering-invariant
3. **k-profile theorem**: Σhᵢ mod 2 is 100% determined by k-profile (7 profiles, all give odd parity)
4. **h-pattern structure**: Individual h_i mod 2 varies within k-type, but sum is constrained
5. **G₂(2)-equivariant invariants fail**: k-profile, q(T), triple intersections cannot distinguish Class I/II
6. **Orbit 4 anomaly**: O₄ has 60.6% 1-minus vs 65-68% for O₁/O₂/O₃

## Requirements

- Python 3.8+
- NumPy

## Usage

```bash
python3 path_a_half_symplectic_sample.py
```

## Data

- 135 Lagrangians in W(5, F₂)
- 945 proper contexts (complement of Fano line)
- 12,096 Mermin pentagrams (4 G₂(2) orbits)
- 7 k-profiles: (0,0,0,0,1), (0,0,0,0,3), (0,0,1,1,1), (0,0,1,1,3), (0,0,3,3,3), (1,1,1,1,1), (1,1,1,1,7)
