class Solution:
    def numRollsToTarget(self, N: int, K: int, target: int) -> int:
        M=10**9+7
        dp = [1]+[0]*target
        for step in range(1,N+1):
            for i in range(min(target,step*K),-1,-1):
                dp[i]=sum(dp[max(0,i-K):i])%M
        return dp.pop()