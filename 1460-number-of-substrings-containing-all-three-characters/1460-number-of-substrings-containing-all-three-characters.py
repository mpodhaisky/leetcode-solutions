class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lo=res=0
        seen=Counter()
        for c in s:
            seen[c]+=1
            while seen[s[lo]]>1:
                seen[s[lo]]-=1
                lo+=1
            if len(seen)==3:
                res+=lo+1
        return res