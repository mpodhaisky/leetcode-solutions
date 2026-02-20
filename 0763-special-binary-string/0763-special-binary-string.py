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
                        A, B = s[i:j+1],s[j+1:k+1]
                        if B+A  > A+B:
                            return self.makeLargestSpecial(s[:i]+B+A+s[k+1:])
        return s