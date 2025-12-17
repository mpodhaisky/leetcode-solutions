class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[0] * 3 for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i] = [0, prices[0], -prices[0]]
        for p in islice(prices, 1, None):
            for i in reversed(range(1, k + 1)):
                dp[i] = [
                    max(dp[i][0], dp[i][1] - p, dp[i][2] + p),
                    max(dp[i][1], dp[i - 1][0] + p),
                    max(dp[i][2], dp[i - 1][0] - p)
                ]
        return dp[-1][0]