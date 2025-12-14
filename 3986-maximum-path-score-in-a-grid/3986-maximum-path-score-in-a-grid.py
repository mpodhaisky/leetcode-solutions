class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        if k - (grid[0][0]>0) <0: return -1
        k-=(grid[0][0] >0)
        M,N = len(grid), len(grid[0])
        @cache        
        def dp(i,j,k):
            if (i,j)==(M-1,N-1): return 0
            res=-inf
            if i < M-1 and k-(grid[i+1][j]>0) >=0:
                res=grid[i+1][j]+dp(i+1,j,k-(grid[i+1][j]>0))
            if j < N-1 and k-(grid[i][j+1]>0) >=0:
                res=max(res,grid[i][j+1]+dp(i,j+1,k-(grid[i][j+1]>0)))
            return res
        ret=dp(0,0,k)
        return -1 if ret==-inf else ret
