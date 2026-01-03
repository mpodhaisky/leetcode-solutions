class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        dp = {}
        @cache
        def size(parent,cur):
            dp[cur] =1+ sum(size(cur,m) for m in adj[cur] if m!=parent)
            return dp[cur]
        size(-1,0)

        q=[(0,0)]
        seen={0}
        res=[0]*n
        for step, node in q:
            for m in adj[node]:
                if m not in seen:
                    seen.add(m)
                    res[0]+=step+1
                    q.append((step+1,m))
        
        
        seen={0}
        q=[0]
        for i in q:
            for j in adj[i]:
                if j not in seen:
                    seen.add(j)
                    res[j] = res[i]-2*dp[j]+n
                    q.append(j)

        return res