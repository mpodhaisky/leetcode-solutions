class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        @cache
        def dp(i,j):
            if i >= N and j>=M: return 0
            elif i >=N: return ord(s2[j])+dp(i,j+1)
            elif j >=M: return ord(s1[i]) + dp(i+1,j)
            elif s1[i]==s2[j]: return dp(i+1,j+1)
            else: return min(ord(s1[i]) + dp(i+1,j),ord(s2[j]) + dp(i,j+1))
        return dp(0,0)