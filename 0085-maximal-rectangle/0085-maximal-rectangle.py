class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [[int(n) for n in row] for row in matrix]
        M, N = len(matrix), len(matrix[0])
        res=0
        for r in range(M):
            cur=0
            for c in range(N):
                matrix[r][c]+= 0 if (not c or not matrix[r][c]) else matrix[r][c-1]
                width=inf
                for k in range(r+1):
                    width=min(width,matrix[r-k][c])
                    res=max(res,width*(k+1))
        return res