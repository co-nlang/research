# The K₄/H² Maslov rung — opening at odd n (item A2, partial)

Paper XXII's $K_4/H^2$ rung: for a proper $K_4$ the nerve is $\partial\Delta^3\cong S^2$
(4 triangles), $\mu$ is a 2-cocycle, and the class is
$\langle\mu,[S^2]\rangle=\bigoplus_{\{a,b,c\}}\mu(a,b,c)$, with
$\mu(L_a,L_b,L_c)=1$ iff $\exists\,x\in L_a,y\in L_b$ with $x+y\in L_c$ and $\omega(x,y)=1$.

Rank-parity (Paper XX) makes it **rigid** ($=0$) at $n=3$ and even $n$ ($\mu$ uniform, so the
4 summands cancel). Paper XXII records the **opening** at odd $n\ge5$ as *computational*
("211 vs 189 of 400 sampled $K_4$"). This note upgrades that, partially.

## What is rigorous here

1. **Exact certified witnesses (n=5, n=7).** Explicit proper $K_4$ — written-down Lagrangian
   bases — with $\langle\mu,[S^2]\rangle=1$ and $=0$, $\mu$ recomputed *exactly* on the
   recorded Lagrangians. This is existence by certificate, not a sample statistic: the search
   is randomized, but each printed witness is an exact proof that both classes occur at that $n$.
2. **The flip reduction (structural).** Fixing $L_0,L_1,L_2$,
   $$\langle\mu,[S^2]\rangle=\mu(0,1,2)\;\oplus\;f(L_3),\qquad
     f(L_3)=\mu(0,1,3)\oplus\mu(0,2,3)\oplus\mu(1,2,3),$$
   because $L_3$ sits in exactly the three triangles that contain index 3. So surjectivity
   $\iff f(L_3)$ is non-constant over valid completions. We exhibit $L_3,L_3'$ with
   $f(L_3)\ne f(L_3')$ — a single Lagrangian swap toggles the class. ($f(L_3)$ has the clean
   reading $\big|\{\,ij\in\{01,02,12\}: L_3\cap A_{ij}\ne\varnothing\,\}\big|\bmod2$, where
   $A_{ij}=\{x+y:x\in L_i,y\in L_j,\omega(x,y)=1\}$ depends only on $L_i,L_j$.)

## The honest residue (why this is not yet the all-odd-n theorem)

A uniform statement for **all** odd $n\ge5$ is *not* obtained. Paper XXI's spread-stabilization
cannot transport a witness, for a structural (rank-parity) reason:
- to keep $n$ odd one appends an **even-$m$** spread, but even $m$ forces every appended triple's
  Maslov bit $\mu_m\equiv1$, so the stabilized $K_4$ becomes rigid ($\mu\equiv1$, sum $0$);
- the only μ-preserving spread has $m=3$ ($\mu_3\equiv0$), which **flips** $n$-parity.

So the dichotomy actively blocks transport. The all-odd-n case needs a per-$n$ construction or a
non-constancy lemma for $f(L_3)$ holding at every odd $n$. **Status: opening rigorous at $n=5,7$
(certificates) + the flip reduction; uniform all-odd-n open.**

## Files
- `k4_opening.py` — finds + exactly verifies witnesses (n=5,7) and demonstrates the flip.
  Pure Python, no deps. (μ as in `paper22/nerve_cochain.py`.)
