class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return prod(nlargest(2,nums))-prod(nsmallest(2,nums))