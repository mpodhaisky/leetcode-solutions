class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(A,B):
            if not A: return not B
            res = 0
            for i in range(1,min(A,limit)+1):
                res = (res+ dp(B,A-i))%MOD
            return res
        
        return (dp(zero,one) + dp(one,zero))%MOD