class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        
        def special(i,j):
            cnt = 0
            for k in range(i,j+1):
                if cnt < 0: return False
                cnt+= 1 if s[k]=="1" else -1
            return not cnt
        
        for i in range(len(s)):
            for j in range(i+1,len(s),2):
                for k in range(j+2,len(s),2):
                    if special(i,j) and special(j+1,k):
                        m = s[:i]+s[j+1:k+1]+s[i:j+1]+s[k+1:]
                        if m > s:
                            return self.makeLargestSpecial(m)
        return s