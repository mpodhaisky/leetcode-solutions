class DSU:

    def __init__(self, N):
        self.parent=list(range(N))
    

    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)
    
    def components(self):
        return len(set(self.find(i) for i in range(len(self.parent))))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        dsu = DSU(M*N)
        for r in range(M):
            for c in range(N):
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    if 0<=r+dr<M and 0<=c+dc<N and grid[r+dr][c+dc]==grid[r][c]:
                        dsu.union(r*N+c,(r+dr)*N+c+dc)
        res=set()
        for r in range(M):
            for c in range(N):
                if grid[r][c]=="1":
                    res.add(dsu.find(r*N+c))
        return len(res)
