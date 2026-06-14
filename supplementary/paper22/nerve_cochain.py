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
    def gen(seed,n_lag):
        ALL=list(range(1,SZ)); rng=random.Random(seed)
        def rl():
            b=[];sp={0}
            for _ in range(N):
                c=[v for v in ALL if v not in sp and all(symp(v,x)==0 for x in b)]
                if not c: return None
                v=rng.choice(c); b.append(v); sp=xspan(b)
            return frozenset(x for x in sp if x)
        lags=[];ls=set();t=time.time()
        while len(lags)<n_lag and time.time()-t<60:
            L=rl()
            if L and L not in ls: ls.add(L); lags.append(L)
        adj=[set() for _ in lags]
        for i in range(len(lags)):
            for j in range(i+1,len(lags)):
                if len(lags[i]&lags[j])==1: adj[i].add(j); adj[j].add(i)
        return lags,adj
    def k5s(lags,adj,cap):
        n=len(lags);out=[]
        for i in range(n):
            if len(out)>=cap: break
            for j in adj[i]:
                if j<=i: continue
                aij=adj[i]&adj[j]
                for k in aij:
                    if k<=j: continue
                    aijk=aij&adj[k]
                    for l in aijk:
                        if l<=k: continue
                        for m in (aijk&adj[l]):
                            if m<=l: continue
                            five=[lags[x] for x in (i,j,k,l,m)];sh={};ok=True
                            for a in range(5):
                                for b in range(a+1,5):
                                    it=five[a]&five[b]
                                    if len(it)!=1: ok=False;break
                                    sh[(a,b)]=next(iter(it))
                                if not ok: break
                            if not ok or len(set(sh.values()))!=10: continue
                            out.append((five,sh))
                            if len(out)>=cap: return out
        return out
    def mu_triple(La,Lb,Lc):
        for x in La:
            for y in Lb:
                if (x^y) in Lc and symp(x,y): return 1
        return 0
    return symp,gen,k5s,mu_triple

def experiment(N,n_lag,max_k5,nseed):
    symp,gen,k5s,mu_triple=build(N)
    inter5=Counter()       # dim of intersection of all 5 Lagrangians
    nerve_hollow=0; tot=0
    na_eq_dmu=0; nanti_parity=Counter()
    dmu_sum_nonzero=0
    for s in range(nseed):
        lags,adj=gen(1000+7*s,n_lag)
        for five,sh in k5s(lags,adj,max_k5):
            tot+=1
            # intersection of all 5
            int=set(five[0])
            for L in five[1:]: int&=set(L)
            d=(len(int)+1).bit_length()-1 if ((len(int)+1)&(len(int)))==0 else -1
            inter5[d]+=1
            if len(int)==0: nerve_hollow+=1
            # rays
            ray={}
            for a in range(5):
                for b in range(a+1,5): ray[(a,b)]=sh[(a,b)]
            # na_m
            na=[]
            for m in range(5):
                rest=[x for x in range(5) if x!=m]; a,b,c,dd=rest
                prs=[((a,b),(c,dd)),((a,c),(b,dd)),((a,dd),(b,c))]
                na.append(sum(1 for (p,q) in prs if symp(ray[tuple(sorted(p))],ray[tuple(sorted(q))])))
            Nanti=sum(na)
            nanti_parity[Nanti%2]+=1
            # mu on all 10 triples
            mu={}
            for (a,b,c) in combinations(range(5),3):
                mu[(a,b,c)]=mu_triple(five[a],five[b],five[c])
            # delta mu on each tetrahedron (complement of m)
            dmu=[]
            for m in range(5):
                rest=tuple(x for x in range(5) if x!=m)
                faces=list(combinations(rest,3))
                dmu.append(sum(mu[f] for f in faces)%2)
            if all((na[m]%2)==dmu[m] for m in range(5)): na_eq_dmu+=1
            if sum(dmu)%2!=0: dmu_sum_nonzero+=1
    print(f"  n={N}: K5 sampled={tot}")
    print(f"    intersection-of-all-5 dim distribution: {dict(sorted(inter5.items()))}")
    print(f"    nerve hollow (cap L_a = 0): {nerve_hollow}/{tot}")
    print(f"    N_anti parity (0=even,1=odd): {dict(nanti_parity)}")
    print(f"    na_m == (delta mu)_m for all m: {na_eq_dmu}/{tot}")
    print(f"    sum(delta mu) != 0 [coboundary should pair to 0]: {dmu_sum_nonzero}/{tot}")

if __name__ == "__main__":
    print("=== Paper XX experiment 1: nerve hollowness + na vs Maslov coboundary ===")
    experiment(4, 800, 60, 6)
    experiment(5, 3000, 60, 6)
