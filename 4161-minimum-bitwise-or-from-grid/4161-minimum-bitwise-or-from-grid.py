class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:

        def can_do(row,i):
            for n in row:
                if not (n&(1<<i)):
                    return True
            return False
        
        res = 0
        for i in range(17,-1,-1):
            if all(can_do(row,i) for row in grid):
                for j , row in enumerate(grid):
                    grid[j]=[n for n in row if not (n&(1<<i))]
            else:
                res|=1<<i
        
        return res