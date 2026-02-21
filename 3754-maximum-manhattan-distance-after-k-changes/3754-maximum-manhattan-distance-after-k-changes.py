class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        f = Counter()
        res = 0
        for n in s:
            f[n]+=1
            d1 =abs(f["N"]-f["S"])
            d2 =abs(f["W"]-f["E"])
            m1 = min(f["N"],f["S"])
            m2 = min(f["W"],f["E"])
            res = max(res,d1+d2 + 2*min(k, m1+m2))
        return res