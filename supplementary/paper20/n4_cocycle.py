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
def run(N,n_lag,max_k5,nseed):
    symp,gen,k5s,mu_triple=build(N)
    nodd=Counter(); muval=Counter(); dmu_nonzero=0; tot=0
    for s in range(nseed):
        lags,adj=gen(1000+7*s,n_lag)
        for five,sh in k5s(lags,adj,max_k5):
            tot+=1
            mu={}
            for (a,b,c) in combinations(range(5),3):
                mu[(a,b,c)]=mu_triple(five[a],five[b],five[c])
            no=sum(mu.values()); nodd[no]+=1
            for v in mu.values(): muval[v]+=1
            for m in range(5):
                rest=tuple(x for x in range(5) if x!=m)
                if sum(mu[f] for f in combinations(rest,3))%2!=0: dmu_nonzero+=1; break
    print(f"  n={N}: K5={tot}  n_odd(#mu=1 of 10) dist={dict(sorted(nodd.items()))}")
    print(f"        mu value dist (all triples)={dict(muval)}")
    print(f"        configs with some delta-mu_m != 0: {dmu_nonzero}/{tot}")
print("=== mu distribution: n=4 vs n=5 ===")
run(4,800,80,6)
run(5,3000,80,6)
