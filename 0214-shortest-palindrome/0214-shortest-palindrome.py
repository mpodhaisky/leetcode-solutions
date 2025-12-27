class Solution:
    def shortestPalindrome(self, s: str) -> str:
        M = 1234567891
        p = 29
        L=len(s)
        res = L
        rev=cur=0
        for i, c in enumerate(s,1):
            rev=(rev+((ord(c)-ord("a")+1)*pow(p,i-1,M))%M)%M
            cur = (cur*p)%M
            cur = (cur +(ord(c)-ord("a")+1))%M
            if rev==cur:
                res= L -i
        
        return s[len(s)-res:][::-1]+s
                
