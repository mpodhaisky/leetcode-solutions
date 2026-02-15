class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        
        cols = list(map(Counter,zip(*grid)))
        
        @cache
        def dp(i, prev):
            if i >= N: return 0
            res= inf
            for n in range(10):
                if n == prev: continue
                res=min(res,M - cols[i][n]+dp(i+1,n))
            return res

        ans = dp(0,-1)
        dp.cache_clear()
        return ans