class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res=0
        for i in range(len(bottomLeft)):
            a, b, c, d = bottomLeft[i]+topRight[i]
            for j in range(i+1,len(bottomLeft)):
                e,f,g,h = bottomLeft[j]+topRight[j]
                o1 = len(range(max(a,e),min(c,g)))
                o2 = len(range(max(b,f),min(d,h)))
                res=max(res,min(o1*o1,o2*o2))
        return res