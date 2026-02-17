class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        M = 10**9+7
        pi1=[0]
        pi2=[0]
        pi3 = [0] +list(accumulate( n!="0" for n in s))

        for c in s:
            n = int(c)
            if n:
                pi1.append(((pi1[-1]*10)%M + n)%M)
                pi2.append((pi2[-1]+n)%M)
            else:
                pi1.append(pi1[-1])
                pi2.append(pi2[-1])
        res = []
        for l, r in queries:
            x = pi1[r+1]-pi1[l]*pow(10,pi3[r+1]-pi3[l],M)
            S = pi2[r+1]-pi2[l]
            res.append((x*S)%M)
        return res
