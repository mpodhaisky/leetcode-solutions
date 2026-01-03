class Solution:
    def numOfWays(self, n: int) -> int:
        M=10**9+7
        dp=[i%3 != (i//3)%3 and (i//3)%3 != (i//9)%3 for i in range(27)]
        for _ in range(n-1):
            dp[:] = [sum(dp[j] for j in range(27) if dp[i] and i%3!=j%3 and (i//3)%3 != (j//3)%3 and (i//9)%3!=(j//9)%3) %M for i in range(27)]
        return sum(dp)%M
