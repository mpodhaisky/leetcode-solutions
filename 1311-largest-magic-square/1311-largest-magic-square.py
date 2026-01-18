def ok(arr):
    rows = set(map(sum,arr))
    cols = set(map(sum,zip(*arr)))
    d1 = sum(arr[i][i] for i in range(len(arr)))
    d2 = sum(arr[i][-1-i] for i in range(len(arr)))
    return len(rows|cols|{d1}|{d2})==1

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        res=1
        M, N = len(grid), len(grid[0])
        for r in range(M):
            for c in range(N):
                maxi = min(N-c,M-r)
                for k in range(maxi,res,-1):
                    cur = [[0]*k for _ in range(k)]
                    for i in range(pow(k,2)):
                        dr, dc = i//k, i%k
                        cur[dr][dc]=grid[r+dr][c+dc]
                    if ok(cur):
                        res=k
                        break
        return res