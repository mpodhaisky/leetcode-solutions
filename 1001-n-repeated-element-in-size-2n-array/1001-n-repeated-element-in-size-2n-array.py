class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen=set()
        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)