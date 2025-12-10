class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i , n in enumerate(nums):
            if target - n in mp:
                return [i,mp[target-n]]
            mp[n]=i