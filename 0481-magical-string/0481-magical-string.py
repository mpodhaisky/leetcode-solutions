class Solution:
    def magicalString(self, n: int) -> int:
        
        s = "122"
        cur = 2

        while len(s) < n:
            s+= ("1" if s[-1]=="2" else "2")*int(s[cur])
            cur+=1
        return s[:n].count("1")