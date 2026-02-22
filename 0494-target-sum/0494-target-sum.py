class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = Counter({0:1})
        for n in nums:
            new_dp=Counter()
            for m in dp:
                for dm in (m-n,m+n):
                    new_dp[dm]+=dp[m]
            dp = new_dp
        return dp[target]