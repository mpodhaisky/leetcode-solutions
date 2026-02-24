class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        adj = {}

        for i, c in enumerate(s):
            if c =="(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                adj[(j,1)] = (i-1,-1)
                adj[(j,-1)] = (i+1,1)
                adj[(i,-1)] = (j+1,1)
                adj[(i,1)] = (j-1,-1)

        pos , speed = 0, 1
        res = ""
        while 0 <= pos < len(s):
            if (pos,speed) in adj:
                pos, speed = adj[(pos,speed)]
            else:
                res+=s[pos]
                pos+=speed
        return res