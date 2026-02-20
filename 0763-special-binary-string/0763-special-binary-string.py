class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        def customcmp(A,B):
            if A +B == B+A: return 0
            if A + B > B + A: return -1
            else: return 1

        def dfs(i,j):
            q = [i-1]
            cur = 0
            for k in range(i,j+1):
                cur += 1 if s[k]=="1" else -1
                if not cur:
                    q.append(k)
                        
            if len(q)==2:
                return "1" + dfs(i+1,j-1) + "0"
            else:
                return "".join(sorted([dfs(a+1,b) for a, b in pairwise(q)], key= cmp_to_key(customcmp)))

        return dfs(0,len(s)-1)