class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        
        rows = 0
        # rows
        for r in range(M):
            for c in range(N + 1 >> 1):
                rows += grid[r][c]!=grid[r][-c-1]
            
        
        cols = 0
        # rows
        for c in range(N):
            for r in range(M + 1 >> 1):
                cols += grid[r][c]!=grid[-r-1][c]
        
        return min(rows,cols)