class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M, N = len(mat), len(mat[0])
        prefix = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                prefix[i+1][j+1]=mat[i][j]
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                prefix[i][j]+=prefix[i-1][j]
        for i in range(1,M+1):
            for j in range(1,N+1):
                prefix[i][j]+=prefix[i][j-1]
        
        def ok(k):
            for i in range(k-1,M):
                for j in range(k-1,N):
                    if prefix[i+1][j+1] + prefix[i-k+1][j-k+1] - prefix[i+1][j-k+1] - prefix[i-k+1][j+1] <= threshold:
                        return True
            return False

        lo , hi = 0, min(M,N)
        while lo <= hi:
            mid = lo + hi >> 1
            if ok(mid):
                lo = mid+1
            else:
                hi = mid-1
        return hi