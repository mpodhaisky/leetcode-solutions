class Solution:
    def numRollsToTarget(self, N: int, K: int, target: int) -> int:
        M=10**9+7
        dp = [1]+[0]*target
        for step in range(1,N+1):
            i = min(target,step*K)
            S = sum(dp[max(0,i-K):i])
            dp[i] = S%M
            for j in range(i-1,-1,-1):
                S-=dp[j]
                if j-K >=0: S+=dp[j-K]
                dp[j]=S%M
                
        return dp.pop()