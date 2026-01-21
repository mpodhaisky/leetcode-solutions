class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        def f(n):
            if n%2==0: return -1
            return n ^(((n | (n+1))^n)>>1)
        return [f(n) for n in nums]