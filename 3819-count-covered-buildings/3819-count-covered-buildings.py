class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        XS, YS = defaultdict(lambda: (inf,-inf)),defaultdict(lambda: (inf,-inf))

        for x, y in buildings:
            YS[x] = min(YS[x][0],y),max(YS[x][1],y)
            XS[y] = min(XS[y][0],x),max(XS[y][1],x)
        
        return sum(x not in XS[y] and y not in YS[x] for x, y in buildings)