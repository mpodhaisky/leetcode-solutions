class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        res=0
        for c in set(s):
            cur = ord(c)
            maxsofar = 0
            for cc in s+"Z":
                if (ord(cc) - cur) %26 == 0:
                    cur+=1
                else:
                    maxsofar=max(maxsofar,cur-ord(c))
                    cur = ord(c) if c != cc else ord(c)+1
            res+=maxsofar
        return res
