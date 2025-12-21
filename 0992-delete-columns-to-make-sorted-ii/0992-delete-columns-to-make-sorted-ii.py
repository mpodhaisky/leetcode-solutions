class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        transpose = lambda x: list(map(list,zip(*x)))
        res=0
        while strs != sorted(strs):
            found=False
            for i in range(len(strs)):
                for j in range(i+1,len(strs)):
                    for k in range(len(strs[0])):
                        if strs[i][k]<strs[j][k]: break
                        if strs[i][k]>strs[j][k]: 
                            strs = list(map("".join,transpose(transpose(strs)[:k] + transpose(strs)[k+1:])))
                            found=True
                            res+=1
                            break
                    if found:
                        break
                if found:
                    break
                
        
        return res
