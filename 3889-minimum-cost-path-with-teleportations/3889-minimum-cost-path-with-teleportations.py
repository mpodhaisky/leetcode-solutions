class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        pairs = sorted([(i,j) for i in range(M) for j in range(N)], key= lambda x: grid[x[0]][x[1]])
        idx = {n:i for i, n in enumerate(pairs)}
        initial={(i,j): pairs[bisect_right(pairs, grid[i][j], key = lambda x: grid[x[0]][x[1]])-1] for i, j in product(range(M),range(N))}
        @cache
        def dp(i,j,k,is_porting):
            if i == M-1 and j == N-1: return 0
            ret = inf
            if not is_porting:
                if i < M-1: ret = min(ret, grid[i+1][j] + dp(i+1,j,k,False))
                if j < N-1: ret = min(ret, grid[i][j+1] + dp(i,j+1,k,False))
                if k:
                    ret = min(ret,dp(*initial[(i,j)],k,True))
            else:
                ret = min(ret,dp(i,j,k-1,False))
                if idx[(i,j)]>0:
                    ret = min(ret,dp(*pairs[idx[(i,j)]-1],k,True))
            return ret
        ret =dp(0,0,k,False)
        dp.cache_clear()
        return ret