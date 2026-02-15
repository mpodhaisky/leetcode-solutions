class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        prefix=[[0]*26 for _ in range(len(s)+1)]
        last={}
        res = 0

        def ok(t):
            return all(not n or n >=k for n in t) 

        def sub_masks(A,B):
            return [a-b for a,b in zip(A,B)]
        
        def add_masks(A,B):
            return [a+b for a, b in zip(A,B)]

        for i , c in enumerate(s):
            n=ord(c)-ord("a")
            last[n]=i
            prefix[i+1][n]+=1
            prefix[i+1]= add_masks(prefix[i+1],prefix[i])
            cur = 0
            while not ok(sub_masks(prefix[i+1], prefix[cur])):
                tmp = sub_masks(prefix[i+1], prefix[cur])
                for j in range(26):
                    if 0<tmp[j]<k:
                        cur = last[j]+1
                        break
            res=max(res,i-cur+1)
        return res
