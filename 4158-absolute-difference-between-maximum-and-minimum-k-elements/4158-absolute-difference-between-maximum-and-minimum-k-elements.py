class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        return abs(sum(nlargest(k,nums)) - sum(nsmallest(k,nums)))