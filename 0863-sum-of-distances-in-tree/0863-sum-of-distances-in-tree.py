class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        dp = {}
        res=[0]*n

        def size(parent,cur):
            dp[cur] =1+ sum(size(cur,m) for m in adj[cur] if m!=parent)
            if cur!=0:
                res[0]+=dp[cur]
            return dp[cur]
        size(-1,0)
        
        seen={0}
        q=[0]
        for i in q:
            for j in adj[i]:
                if j not in seen:
                    seen.add(j)
                    res[j] = res[i]-2*dp[j]+n
                    q.append(j)

        return res