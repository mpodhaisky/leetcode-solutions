class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        prefix=[[0]*26 for _ in range(len(s)+1)]
        last={}

        res = 0
        def ok(t):
            return all(not n or n >=k for n in t) 

        def substract(A,B):
            return [a-b for a,b in zip(A,B)]

        for i , c in enumerate(s):
            last[ord(c)-ord("a")]=i
            for j in range(26):
                prefix[i+1][j] = prefix[i][j] + (ord(c)-ord("a")==j)

            cur = 0

            while not ok(substract(prefix[i+1], prefix[cur])):
                tmp = substract(prefix[i+1], prefix[cur])
                for j in range(26):
                    if 0<tmp[j]<k:
                        cur = last[j]+1
                        break
                
            res=max(res,i-cur+1)
        return res
