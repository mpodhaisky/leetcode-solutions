class Solution:
    def minimumDeletions(self, s: str) -> int:
        cur = res = s.count("a")
        for c in s:
            if c == "a":
                cur-=1
            else:
                cur+=1
            res=min(cur,res)
        return res