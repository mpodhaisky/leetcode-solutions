class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        f = lambda y: max(len(list(g)) for _ , g in groupby(enumerate(sorted(y)),lambda x: x[0]-x[1]))
        return pow(1+min(f(hBars),f(vBars)),2)