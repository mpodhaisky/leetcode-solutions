M = 10**9+7
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [factorial(i)%M for i in range(n)]
        for d in range(k-1):
            dp.pop()
            for i in range(1,len(dp)):
                dp[i]=(dp[i-1]*(i+d+1)+dp[i])%M
        return dp[-1]