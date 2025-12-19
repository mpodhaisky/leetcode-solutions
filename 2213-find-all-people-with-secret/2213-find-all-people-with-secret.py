class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)
        for x, y, t in [[0,firstPerson,0]]+meetings:
            adj[x].append((t,y))
            adj[y].append((t,x))
        res=set()
        q=[(0,0,firstPerson)]
        t=0
        while q:
            t,x,y = heappop(q)
            for dt, dy in adj[y]:
                if dt>=t:
                    heappush(q,(dt,y,dy)) 
            adj[y].clear()
            res.add(x)
        return list(res)