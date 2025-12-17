class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        
        dp=[[0]*(k+1),[-inf]*(k+1),[-inf]*(k+1)]

        for i in range(len(prices)-1,-1,-1):
            for a in range(k,-1,-1):
                dp[2][a] = max(dp[2][a],dp[0][a]-prices[i])
                dp[1][a] = max(dp[1][a],dp[0][a]+prices[i])
                dp[0][a]= max(dp[0][a], (max(dp[1][a-1]-prices[i],dp[2][a-1]+prices[i]) if a >=1 else 0))
        return dp[0][-1]