class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                lo , hi = 0 , len(nums)-1
                while lo < hi:
                    cur = nums[i]+nums[j]+nums[lo]+nums[hi]
                    if lo == i or lo == j or cur < target:
                        lo+=1
                    elif hi == j or hi == i or cur > target:
                        hi-=1
                    elif cur == target:
                        res.add(tuple(sorted((nums[lo],nums[hi],nums[i],nums[j]))))
                        hi-=1
                        lo+=1
        return list(map(list,res))