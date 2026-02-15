class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        res=S=0
        seen=set()

        def dfs(r,c):
            nonlocal res, S
            S+=grid[r][c]
            res = max(res,S)
            res= max(res,sum(grid[r][c] for r,c in seen))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0<=r+dr<M and 0<=c+dc<N and (r+dr,c+dc) not in seen and grid[r+dr][c+dc]:
                    seen.add((r+dr,c+dc))
                    dfs(r+dr,c+dc)
                    seen.remove((r+dr,c+dc))
            S-=grid[r][c]
        
        for r in range(M):
            for c in range(N):
                if grid[r][c]:
                    seen.add((r,c))
                    dfs(r,c)
                    seen.remove((r,c))
        return res