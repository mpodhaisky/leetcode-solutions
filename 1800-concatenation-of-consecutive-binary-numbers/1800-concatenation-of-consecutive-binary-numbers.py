class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9+7
        cur =0
        for i in range(1,n+1):
            cur = (cur << i.bit_length())%MOD
            cur = (cur + i)%MOD
        return cur