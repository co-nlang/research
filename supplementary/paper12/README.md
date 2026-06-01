# Paper XII Supplementary Scripts

## Overview

Computational exploration of the Arf invariant and shifted quadratic forms for Mermin pentagrams in $W(5, \mathbb{F}_2)$.

## Scripts

| Script | Description | Runtime |
|--------|-------------|---------|
| `arf_candidate_search.py` | Enumerate q(u)=1 vectors, G₂(2) orbits, pentagram membership analysis | ~444s |
| `t_vector_analysis.py` | T-vector properties: q(T), ω(T,r), Lagrangian membership | ~437s |
| `g2_preserves_q.py` | Check if G₂(2) preserves q, orbit structure on F₂⁶ | ~30s |

## Key Results

### arf_candidate_search.py

- **28 vectors** with $q(u) = 1$ (not 36 as initially expected)
- **Single G₂(2) orbit**: $G_2(2)$ acts transitively on the 28 q=1 vectors
- **No fixed points**: no $G_2(2)$-distinguished choice of $u$
- **Coverage**: each q=1 vector belongs to 15 Lagrangians and covers 4,800/12,096 pentagrams (39.7%)
- **No universal u**: no single $u$ works for all pentagrams

### t_vector_analysis.py

- **T-vector theorem**: $\omega_{\text{int}}(T, r)$ is odd for ALL 10 rays, ALL 12,096 pentagrams (100%)
  - Algebraic proof: each ray has 3 disjoint neighbors (ω=1) and 6 sharing neighbors (ω=0), so $\omega(T, r) = 3 \equiv 1 \pmod{2}$
- **T ∉ ∪L_i**: $T$ is never in any Lagrangian of the pentagram (100%)
- **q(T) distribution**: 55.6% have $q(T) = 0$, 44.4% have $q(T) = 1$
- **T distinct values**: 63 distinct vectors (all non-zero vectors in $\mathbb{F}_2^6$), each appearing 192 times
- **Integer ω_int(T, r) values**: $\{-3: 1.3\%, -1: 48.7\%, +1: 48.7\%, +3: 1.3\%\}$

### g2_preserves_q.py

- **G₂(2) does NOT preserve q**: 376,320 violations out of 12,096 × 63 checks
- **G₂(2) acts transitively on all 63 non-zero vectors**: single orbit of size 63
- **Orbit composition**: each orbit contains 35 vectors with q=0 and 28 with q=1
- **Critical implication**: The standard quadratic form $q(v) = x_1 z_1 + x_2 z_2 + x_3 z_3$ is NOT a $G_2(2)$-invariant, invalidating the naive Arf invariant framework

## Requirements

- Python 3.8+
- NumPy

## Usage

```bash
python3 arf_candidate_search.py
python3 t_vector_analysis.py
```

## Mathematical Context

These scripts support Paper XII's investigation of whether the KS obstruction class $[f_3] \in H^1(K_5, \mathcal{F})$ can be identified with the Arf invariant of a shifted quadratic form $q' = q + \ell_u$.

**Key findings:**
1. The T-vector (sum of all 10 rays) satisfies $\omega(T, r) = 1$ for all rays — a clean algebraic theorem
2. However, $q(T) = 1$ only 44.4% of the time, so $T$ does not always give $\text{Arf}(q') = 1$
3. No universal $u$ exists; the correct $u$ must be pentagram-dependent
4. **G₂(2) does NOT preserve the standard quadratic form $q$**, acting transitively on all 63 non-zero vectors instead
5. The naive Arf invariant framework is **not G₂(2)-equivariant** and must be fundamentally revised

**Surviving results:**
- T-vector theorem (§2.5 of paper12_idea.md)
- β-formula and parity theorem (Paper XI)
- The obstruction $[f_3]$ requires a different cohomological interpretation

## License

Same as the main repository.
