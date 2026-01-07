class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res=-inf
        cur=0

        for n in nums:
            cur+=n
            res = max(cur,res)
            cur = max(0,cur)

        S = sum(nums)
        cur=0
        cnt=0
        for n in nums:
            cnt+=1
            cur+=n
            if cnt !=len(nums):
                res = max(res, S-cur)
            if cur >= 0:
                cur = 0
                cnt=0
            
        
        return res