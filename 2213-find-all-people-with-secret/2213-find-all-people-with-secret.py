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
    
    def component(self,x):
        return [i for i in range(len(self.parent)) if self.find(i)==self.find(x)]

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dsu=DSU(n)
        adj = defaultdict(list)
        for x, y, t in [[0,firstPerson,0]]+meetings:
            adj[x].append((t,y))
            adj[y].append((t,x))
        q=[(0,0,firstPerson)]
        t=0
        while q:
            t,x,y = heappop(q)
            dsu.union(x,y)
            for dt, dy in adj[y]:
                if dt>=t:
                    heappush(q,(dt,y,dy)) 
            adj[y].clear()
        return dsu.component(0)