class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 10**9+7
        P = pow(r-l+1,k-1,MOD)
        geo =(1-pow(10,k,MOD))*pow(-9,-1,MOD)%MOD
        res = sum(range(l,r+1))*P*geo
        return res % MOD