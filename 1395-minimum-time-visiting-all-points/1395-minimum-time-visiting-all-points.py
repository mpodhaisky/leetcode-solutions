class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(a-c),abs(b-d)) for (a,b) , (c, d) in pairwise(points))