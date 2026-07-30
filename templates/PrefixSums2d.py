class PrefixSums2d:
    def __init__(self, grid):
        M, N = len(grid),len(grid[0])
        self.prefix = [[0 for _ in range(N+1)] for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                self.prefix[i+1][j+1] = grid[i][j]
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                self.prefix[i][j] += self.prefix[i][j-1]
    
        for i in range(1,M+1):
            for j in range(1,N+1):
                self.prefix[i][j] += self.prefix[i-1][j]

    def quad_sum(self,r1,c1,r2,c2):
        return self.prefix[r2+1][c2+1] + self.prefix[r1][c1] - self.prefix[r2+1][c1] - self.prefix[r1][c2+1]
