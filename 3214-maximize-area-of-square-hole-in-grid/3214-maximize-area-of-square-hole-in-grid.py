class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        A = max(len(list(g)) for _ , g in groupby(enumerate(sorted(hBars)),lambda x: x[0]-x[1]))
        B = max(len(list(g)) for _, g in groupby(enumerate(sorted(vBars)),lambda x: x[0]-x[1]))
        return pow(1+min(A,B),2)
