class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = pow(10,9)+7
        PI = [0] + list(accumulate(nums))
        res=0
        for i in range(len(nums)):

            # min where mid >= left
            j = bisect_left(range(i+1,len(nums)-1), True, key=lambda x: 2*PI[i+1] <= PI[x+1])+i+1
            
            # max where mid <= right
            k = bisect_right(range(i+1,len(nums)-1), False, key=lambda x: 2*PI[x+1] > PI[len(nums)] + PI[i+1])+i

            res= (res + max(0,k-j+1))%MOD
        return res