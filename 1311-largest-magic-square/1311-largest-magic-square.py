class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def is_magic(r,c,k):
            arr= [[grid[r+i][c+j] for i in range(k)] for j in range(k)]
            rows = set(map(sum,arr))
            cols = set(map(sum,zip(*arr)))
            d1 = sum(arr[i][i] for i in range(len(arr)))
            d2 = sum(arr[i][-1-i] for i in range(len(arr)))
            return len(rows|cols|{d1}|{d2})==1
        res=1
        M, N = len(grid), len(grid[0])
        for r in range(M):
            for c in range(N):
                for k in range(min(N-c,M-r),res,-1):
                    if is_magic(r,c,k):
                        res=k
                        break
        return res