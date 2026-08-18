class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums) == k: return max(nums)
        if k == 1: return max([k for k,v in Counter(nums).items() if v ==1],default=-1)
        if nums[0] in nums[1:] and nums[-1] in nums[:-1]: return -1
        if nums[0] in nums[1:]: return nums[-1]
        if nums[-1] in nums[:-1]: return nums[0]
        return max(nums[0],nums[-1])
        