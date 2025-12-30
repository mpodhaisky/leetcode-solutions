class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        lo_shu = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],  
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],  
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],  
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],  
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],  
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],  
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],  
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]   
        ]
        M,N = len(grid),len(grid[0])
        res=0
        for m in lo_shu:
            for r in range(M-2):
                for c in range(N-2):
                    res+=all(grid[r+dr][c+dc]==m[dr][dc] for dr, dc in product(range(3),repeat=2))
        return res