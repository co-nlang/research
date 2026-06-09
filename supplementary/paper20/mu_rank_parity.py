import sys, time, random
from itertools import combinations
from collections import Counter
def build(N):
    SZ=1<<(2*N); MSK=(1<<N)-1
    PN=[bin(i).count('1')&1 for i in range(1<<N)]
    XT=[[PN[i&j] for j in range(1<<N)] for i in range(1<<N)]
    def symp(v,w): return XT[v&MSK][(w>>N)&MSK]^XT[(v>>N)&MSK][w&MSK]
    def xspan(b):
        s={0}
        for x in b: s|={y^x for y in s}
        return s
    def rand_lag(rng,ALL):
        b=[];sp={0}
        for _ in range(N):
            c=[v for v in ALL if v not in sp and all(symp(v,x)==0 for x in b)]
            if not c: return None
            v=rng.choice(c); b.append(v); sp=xspan(b)
        return frozenset(x for x in sp if x)
    def mu_triple(La,Lb,Lc):
        for x in La:
            for y in Lb:
                if (x^y) in Lc and symp(x,y): return 1
        return 0
    return SZ,symp,rand_lag,mu_triple
def run(N,target,seed):
    SZ,symp,rand_lag,mu_triple=build(N)
    ALL=list(range(1,SZ)); rng=random.Random(seed)
    # generate proper K3: 3 Lagrangians pairwise meeting in 1 ray, 3 distinct rays
    muc=Counter(); found=0; t=time.time()
    pool=[]
    while found<target and time.time()-t<300:
        # build a fresh triple
        La=rand_lag(rng,ALL); Lb=rand_lag(rng,ALL)
        if not La or not Lb: continue
        iab=La&Lb
        if len(iab)!=1: continue
        Lc=rand_lag(rng,ALL)
        if not Lc: continue
        iac=La&Lc; ibc=Lb&Lc
        if len(iac)!=1 or len(ibc)!=1: continue
        vab=next(iter(iab)); vac=next(iter(iac)); vbc=next(iter(ibc))
        if len({vab,vac,vbc})!=3: continue
        muc[mu_triple(La,Lb,Lc)]+=1; found+=1
    print(f"  n={N}: proper K3 sampled={found}  mu dist={dict(muc)}   (predict: n even -> all 1)")
print("=== mu by n: testing mu==1 <=> n even (rank sigma = n-3) ===")
run(4,300,11)
run(5,300,11)
run(6,200,11)
