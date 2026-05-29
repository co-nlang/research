# Paper VII: Conjecture 4.2 Verification Scripts

Two Python scripts verifying the Peres-Mermin obstruction class for the twistor googly resolution:

- **`paper7_conj42.py`**: Group cohomology computation of the two obstruction classes:
  1. Peres-Mermin square `[f] ≠ 0 ∈ H²(G_PM, Z/2)` — Paper III central extension
  2. Full 2-qubit Pauli group `P₂̄`: mod-2 reduction splits, but full Z/4 cocycle does not

- **`paper7_conj42_layer2.py`**: Čech/cellular verification of Conjecture 4.2:
  - `Φ*([f]) = c₁(O(1)) mod 2 ≠ 0 ∈ H²(CP³, Z/2)`
  - Uses transgression `π₁(SO(3)) ≅ Z/2 → H²(S², Z/2)` for the local consistency check

## Requirements

- Python 3.9+
- NumPy

## Usage

```bash
python paper7_conj42.py
python paper7_conj42_layer2.py
```

Scripts are self-contained and produce structured output.

## License

MIT (see LICENSE).
