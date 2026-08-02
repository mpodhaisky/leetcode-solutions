class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        A = [0] + list(accumulate([a if n&1 else -b for n in nums]))
        
        seen = SortedList()
        res = 0
        for n, m in pairwise(A):
            seen.add(n)
            res += seen.bisect_right(m)
        return res