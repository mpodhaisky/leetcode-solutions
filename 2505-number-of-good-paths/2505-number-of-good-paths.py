class DSU:
    def __init__(self, N):
        self.parent=list(range(N))
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)
    
    def components(self):
        return len(set(self.find(i) for i in range(len(self.parent))))

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        N = len(vals)
        h = []

        for a, b in edges:
            a, b = sorted((a,b), key = lambda x: vals[x])[::-1]
            heappush(h,(vals[a],vals[b],a,b))
        
        res = N
        
        dsu = DSU(N)

        for threshold in sorted(set(vals)):
            f = Counter()
            seen = set()    
            while h and h[0][0]==threshold:
                x, y, a, b = heappop(h)
                pa, pb = dsu.find(a), dsu.find(b)
                if a not in seen: f[pa]+=1
                if y == threshold and b not in seen: f[pb]+=1
                seen.add(a)
                seen.add(b)
                res+=f[pa]*f[pb]
                f[pa]=f[pb] = f[pa]+f[pb]
                dsu.union(a,b)
        return res