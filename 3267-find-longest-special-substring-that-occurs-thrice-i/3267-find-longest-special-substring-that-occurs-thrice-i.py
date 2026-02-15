class Solution:
    def maximumLength(self, s: str) -> int:
        def ok(l):
            if not l: return False
            seen = Counter()
            for i in range(l-1,len(s)):
                if len(set(s[i-l+1:i+1])) == 1:
                    seen[s[i-l+1:i+1]]+=1
            return not any(n>=3 for n in seen.values())
        
        res = bisect_left(range(len(s)), True, key = ok)-1
        return -1 if not res else res