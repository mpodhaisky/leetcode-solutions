class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        
        def is_magic(i,j):
            seen=((1<<10)-1)^1
            d1=grid[i][j]+grid[i-1][j-1]+grid[i-2][j-2]
            d2=grid[i-2][j]+grid[i-1][j-1]+grid[i][j-2]
            rs=[0,0,0]
            cs=[0,0,0]
            for di in range(3):
                for dj in range(3):
                    seen^=(1<<grid[i-di][j-dj])
                    rs[di]+=grid[i-di][j-dj]
                    cs[dj]+=grid[i-di][j-dj]
            return set([d1,d2]+rs+cs)=={15} and not seen
        
        return sum(is_magic(i,j) for i,j in product(range(2,M),range(2,N)))
                        

