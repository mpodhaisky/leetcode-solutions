class PrefixSums2d:
    def __init__(self, grid):
        self.M, self.N = len(grid),len(grid[0])
        diamond = [[0 for _ in range(self.M + self.N-1)] for _ in range(self.M + self.N -1)]

        for i in range(self.M):
            for j in range(self.N):
                diamond[i-j+self.N-1][i+j] = grid[i][j]
        
        self.prefix = self._construct_prefix(grid)
        self.diamond_prefix = self._construct_prefix(diamond)
    
    def _construct_prefix(self,grid):
        M, N = len(grid),len(grid[0])
        prefix = [[0 for _ in range(N+1)] for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                prefix[i+1][j+1] = grid[i][j] + prefix[i+1][j]+prefix[i][j+1]-prefix[i][j]
        return prefix

    def quad_sum(self,r1,c1,r2,c2):
        return self.prefix[r2+1][c2+1] + self.prefix[r1][c1] - self.prefix[r2+1][c1] - self.prefix[r1][c2+1]
    
    def chebychev_sum(self,r,c,k):
        if k == -1: return 0
        return self.quad_sum(max(0,r-k),max(0,c-k),min(r+k,self.M-1),min(c+k,self.N-1))
    
    def manhattan_sum(self, r, c, k):
        if k == -1: return 0
        r, c = r - c + self.N - 1, r + c
        max_idx = self.M + self.N - 2
        r_max, r_min = min(r + k, max_idx), max(0, r - k)
        c_max, c_min = min(c + k, max_idx), max(0, c - k)
        
        return (self.diamond_prefix[r_max + 1][c_max + 1] 
            + self.diamond_prefix[r_min][c_min] 
            - self.diamond_prefix[r_max + 1][c_min] 
            - self.diamond_prefix[r_min][c_max + 1])
