#!/usr/bin/env python3
"""
Paper XIX probe: n>=5 deformation vs symplectic invariants of the ray-span W.
Robustly confirms (multi-seed):
  - deterministic low-rank strata: rankG=0 => N_anti=0 ; rankG=4 => N_anti=6
  - whether rankG=2 ever occurs for a proper K5
  - radW (radical dim) as monotone order parameter for Sigma-uniformity / N_anti parity
Usage: python3 nge5_probe.py [n=5] [n_lag=3000] [max_k5=400] [seeds=3]
"""
import sys, time, random
from collections import Counter, defaultdict
from itertools import combinations

N      = int(sys.argv[1]) if len(sys.argv)>1 else 5
N_LAG  = int(sys.argv[2]) if len(sys.argv)>2 else 3000
MAX_K5 = int(sys.argv[3]) if len(sys.argv)>3 else 400
SEEDS  = int(sys.argv[4]) if len(sys.argv)>4 else 3

SZ=1<<(2*N); MSK=(1<<N)-1
PN=[bin(i).count('1')&1 for i in range(1<<N)]
XT=[[PN[i&j] for j in range(1<<N)] for i in range(1<<N)]
def symp(v,w): return XT[v&MSK][(w>>N)&MSK]^XT[(v>>N)&MSK][w&MSK]
def xspan(b):
    s={0}
    for x in b: s|={y^x for y in s}
    return s
def f2rank(vs):
    bs=[]
    for v in vs:
        x=v
        for b in bs: x=min(x,x^b)
        if x: bs.append(x); bs.sort(reverse=True)
    return len(bs)
def f2rank_rows(rows,ncols):
    rows=list(rows); rank=0
    for col in range(ncols):
        piv=None
        for i in range(rank,len(rows)):
            if (rows[i]>>col)&1: piv=i;break
        if piv is None: continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        for i in range(len(rows)):
            if i!=rank and (rows[i]>>col)&1: rows[i]^=rows[rank]
        rank+=1
    return rank

def gen(seed):
    ALL=list(range(1,SZ)); rng=random.Random(seed)
    def rl():
        b=[];sp={0}
        for _ in range(N):
            c=[v for v in ALL if v not in sp and all(symp(v,x)==0 for x in b)]
            if not c: return None
            v=rng.choice(c); b.append(v); sp=xspan(b)
        return frozenset(x for x in sp if x)
    lags=[];ls=set(); t=time.time()
    while len(lags)<N_LAG and time.time()-t<200:
        L=rl()
        if L and L not in ls: ls.add(L); lags.append(L)
    adj=[set() for _ in lags]
    for i in range(len(lags)):
        for j in range(i+1,len(lags)):
            if len(lags[i]&lags[j])==1: adj[i].add(j); adj[j].add(i)
    return lags,adj

def k5s(lags,adj,cap):
    n=len(lags); out=[]
    for i in range(n):
        if len(out)>=cap: break
        ai=adj[i]
        for j in ai:
            if j<=i: continue
            aij=ai&adj[j]
            for k in aij:
                if k<=j: continue
                aijk=aij&adj[k]
                for l in aijk:
                    if l<=k: continue
                    for m in (aijk&adj[l]):
                        if m<=l: continue
                        five=[lags[x] for x in (i,j,k,l,m)]; sh={}; ok=True
                        for a in range(5):
                            for b in range(a+1,5):
                                it=five[a]&five[b]
                                if len(it)!=1: ok=False;break
                                sh[(a,b)]=next(iter(it))
                            if not ok:break
                        if not ok or len(set(sh.values()))!=10: continue
                        out.append(sh)
                        if len(out)>=cap: return out
    return out

rankG_dist=Counter()
strat0=Counter(); strat4=Counter()
rad_suni=defaultdict(Counter); rad_par=defaultdict(Counter)
fix862=Counter()  # within (dimW,rankG,radW)=(8,6,2): N_anti parity
total=0
for s in range(SEEDS):
    lags,adj=gen(42+s)
    for sh in k5s(lags,adj,MAX_K5):
        def Rr(x,y): return sh[(min(x,y),max(x,y))]
        rays=[Rr(a,b) for a in range(5) for b in range(a+1,5)]
        nav=[]
        for mm in range(5):
            o=sorted(set(range(5))-{mm}); a,b,c,d=o
            prs=[((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]
            nav.append(sum(symp(Rr(*p1),Rr(*p2)) for p1,p2 in prs))
        Nanti=sum(nav); suni=len(set(x%2 for x in nav))==1
        dimW=f2rank(rays)
        G=[0]*10
        for x in range(10):
            for y in range(10):
                if x!=y and symp(rays[x],rays[y]): G[x]|=(1<<y)
        rankG=f2rank_rows(G,10); radW=dimW-rankG
        rankG_dist[rankG]+=1; total+=1
        if rankG==0: strat0[Nanti]+=1
        if rankG==4: strat4[Nanti]+=1
        rad_suni[radW][suni]+=1; rad_par[radW][Nanti%2]+=1
        if (dimW,rankG,radW)==(8,6,2): fix862[Nanti%2]+=1

print(f"n={N}  seeds={SEEDS}  K5 total={total}")
print(f"rankG dist: {dict(sorted(rankG_dist.items()))}   (rankG=2 present? {'YES' if rankG_dist.get(2,0) else 'NO'})")
print(f"rankG=0 -> N_anti: {dict(sorted(strat0.items()))}  (deterministic? {'YES' if len(strat0)<=1 else 'NO'})")
print(f"rankG=4 -> N_anti: {dict(sorted(strat4.items()))}  (deterministic? {'YES' if len(strat4)<=1 else 'NO'})")
print("radW -> Sigma-uniform / N_anti parity:")
for r in sorted(rad_suni):
    su=rad_suni[r]; pr=rad_par[r]; tot=sum(su.values())
    upct=100*su.get(True,0)/tot; epct=100*pr.get(0,0)/tot
    print(f"  radW={r}: n={tot:4d}  Sigma-uniform {upct:5.1f}%   N_anti-even {epct:5.1f}%")
print(f"fixed (8,6,2) N_anti parity: {dict(sorted(fix862.items()))}  (symplectic-invariant insufficiency: split={'YES' if len(fix862)>1 else 'NO'})")
