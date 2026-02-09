class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for l in range(3,len(nums)+1):
            for i in range(len(nums)-l+1):
                dp[i][i+l-1] = max(dp[i][k] + dp[k][i+l-1] + nums[i]*nums[k]*nums[i+l-1] for k in range(i+1,i+l-1))

        return dp[0][len(nums)-1]