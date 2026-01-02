class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        return next(a for a, b in pairwise(nums) if a==b)