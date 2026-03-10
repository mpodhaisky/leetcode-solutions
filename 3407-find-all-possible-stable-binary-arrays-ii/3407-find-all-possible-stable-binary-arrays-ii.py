class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        
        @cache 
        def dp2(A,B):
            if B < 0: return 0
            return (dp1(A,B) + dp2(A,B-1))%MOD

        @cache
        def dp1(A,B):
            if not A: return not B
            return (dp2(B,A-1) - dp2(B,A-min(A,limit)-1))%MOD
        
        ans =(dp1(zero,one) + dp1(one,zero))%MOD
        dp1.cache_clear()
        dp2.cache_clear()
        return ans
        