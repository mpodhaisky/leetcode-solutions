class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        def ok(A):
            for i in range(1,len(A)):
                if A[i] <=A[i-1]:
                    return False
            return True
        for p in range(1,len(nums)-2):
            for q in range(p+1,len(nums)-1):
                if ok(nums[:p+1]) and ok(nums[p:q+1][::-1]) and ok(nums[q:]):
                    return True
        return False