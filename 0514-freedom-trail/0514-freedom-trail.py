class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        adj=defaultdict(list)
        for i in range(len(ring)):
            for j, m in enumerate(ring):
                adj[(i,m)].append(j)
            

        @cache
        def dp(i,j):
            if j >= len(key): return 0
            res=inf
            for neigh in adj[(i,key[j])]:
                dist=min(len(ring)-abs(neigh-i),abs(neigh-i))
                res=min(res, dist+1+dp(neigh,j+1))
            return res
        return dp(0,0)