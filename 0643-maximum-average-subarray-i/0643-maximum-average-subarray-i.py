class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur,res=0,-inf
        for i, n in enumerate(nums):
            cur+=n
            if i >=k:
                cur-=nums[i-k]
            if i +1 >=k:
                res = max(res,cur)
        return res/k