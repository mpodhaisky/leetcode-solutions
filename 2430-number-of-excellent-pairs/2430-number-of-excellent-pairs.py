class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(n.bit_count() for n in set(nums))
        res=0
        for n in nums:
            res+= len(nums) - bisect_left(nums,k-n)
        return res