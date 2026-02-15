class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        seen = Counter()
        for w in arr:
            for i in range(len(w)):
                for j in range(i,len(w)):
                    seen[w[i:j+1]]+=1
        res=[]
        for w in arr:
            for i in range(len(w)):
                for j in range(i,len(w)):
                    seen[w[i:j+1]]-=1
            
            cur = ""
            for i in range(len(w)):
                for j in range(i,len(w)):
                    if not seen[w[i:j+1]] and (not cur or j-i+1 < len(cur) or (j-i+1 == len(cur) and  w[i:j+1] < cur)):
                        cur = w[i:j+1]
            res.append(cur)

            for i in range(len(w)):
                for j in range(i,len(w)):
                    seen[w[i:j+1]]+=1
        return res
