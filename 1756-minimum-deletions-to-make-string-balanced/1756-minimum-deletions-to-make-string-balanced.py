class Solution:
    def minimumDeletions(self, s: str) -> int:
        cur , res, cnt = 0, inf, 0
        for c in s:
            if c == "a":
                cnt+=1
                cur-=1
            else:
                cur+=1
            res=min(cur,res)
        return min(cnt,res+cnt)