class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        XS, YS = defaultdict(set),defaultdict(set)

        for x, y in buildings:
            YS[x].add(y)
            XS[y].add(x)
        
        res=0
        for x, y in buildings:
            res += x not in {min(XS[y]),max(XS[y])} and y not in {min(YS[x]),max(YS[x])}
            XS[y] = {min(XS[y]),max(XS[y])}
            YS[x] = {min(YS[x]),max(YS[x])}
        return res
