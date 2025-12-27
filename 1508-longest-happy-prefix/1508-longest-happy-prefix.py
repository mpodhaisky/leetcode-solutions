class Solution:
    def longestPrefix(self, s: str) -> str:
        M=1234567891
        p=29
        front=back=res=0
        for i in range(len(s)-1):
            front=(front*p)%M
            front = (front + ord(s[i])-ord("a")+1)%M
            back = (back + pow(p,i,M)*(ord(s[-i-1])-ord("a")+1))%M
            if front ==back:
                res=i+1
        return s[:res]
