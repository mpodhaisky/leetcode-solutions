class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen=Counter()
        lo=res=0
        for c in s:
            seen[c]+=1
            while seen.total()-max(seen.values())>k:
                seen[s[lo]]-=1
                lo+=1
            res=max(res,seen.total())
        return res