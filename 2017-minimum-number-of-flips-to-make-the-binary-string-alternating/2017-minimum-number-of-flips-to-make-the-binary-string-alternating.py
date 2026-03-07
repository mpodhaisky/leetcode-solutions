class Solution:
    def minFlips(self, s: str) -> int:
        A = list(map(int,s))
        @cache
        def dp(i,prev,skip):
            if i >= len(A): return 0
            res = inf
            if skip:
                res = dp(i+1,prev,False)
            if A[i] != prev:
                return min(res, dp(i+1,A[i],skip))
            else:
                return min(res, 1+ dp(i+1,1-A[i], skip))
        
        return min(dp(0,0,len(s)&1),dp(0,1,len(s)&1))
        