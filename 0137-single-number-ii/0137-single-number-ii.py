class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=b=0
        for n in nums:
            a= (a^n)&~b
            b= (b^n)&~a
        return a