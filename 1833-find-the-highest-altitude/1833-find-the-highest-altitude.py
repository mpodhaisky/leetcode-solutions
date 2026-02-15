class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=cur=0
        for n in gain:
            cur+=n
            res=max(res,cur)
        return res