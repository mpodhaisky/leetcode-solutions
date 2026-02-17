class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        haystack = []
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                haystack.append(1)
            elif nums[i]==nums[i-1]:
                haystack.append(0)
            else:
                haystack.append(2)

        haystack = "".join(map(str,haystack))
        pattern = "".join(map(str,[2 if n == -1 else n for n in pattern]))
        
        M = 10**9+7

        p =7 

        def convert(s):
            res = 0
            for c in s:
                res = (res*p) %M
                res += int(c)+1
            return res
        
        h = convert(pattern)

        cur =res=0
        for i in range(len(haystack)):
            cur = (cur*p) %M
            cur = (cur+convert(haystack[i]))%M
            if i >= len(pattern):
                cur = (cur-((convert(haystack[i-len(pattern)])*pow(p,len(pattern),M))%M))%M
            res+=cur==h
        return res










