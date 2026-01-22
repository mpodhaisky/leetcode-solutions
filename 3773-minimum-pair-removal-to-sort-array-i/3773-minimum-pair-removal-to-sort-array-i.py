class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        steps=0
        while nums !=sorted(nums):
            steps+=1
            minsofar = target = inf
            for i in range(len(nums)-2,-1,-1):
                if nums[i]+nums[i+1]<=minsofar:
                    minsofar=nums[i]+nums[i+1]
                    target=i
            nums = nums[:target] +[minsofar] + nums[target+2:]
        return steps