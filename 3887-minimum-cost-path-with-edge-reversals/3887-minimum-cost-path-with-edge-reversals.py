class Solution:
    def minCost(self, N: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for a, b, w in edges:
            adj[a].append((b,w))
            adj[b].append((a,2*w))
        
        q=[(0,0)]
        seen=defaultdict(lambda: inf)
        seen[0]=0

        while q:
            c, n = heappop(q)
            if c!=seen[n]: continue
            if n == N-1: return c
            for m, cc in adj[n]:
                if c+cc < seen[m]:
                    seen[m]=c+cc
                    heappush(q,(c+cc,m))
        return -1