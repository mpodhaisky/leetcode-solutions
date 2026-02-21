
class Solution:
    def makeLargestSpecial(self, s: str, i= 0, j = -1) -> str:
        j %= len(s)
        q = [i-1]
        cur = 0
        for k in range(i,j+1):
            cur += 1 if s[k]=="1" else -1
            if not cur:
                q.append(k)
        if len(q)==2:
            return "1" + self.makeLargestSpecial(s,i+1,j-1) + "0"
        else:
            return "".join(sorted(self.makeLargestSpecial(s,a+1,b) for a, b in pairwise(q))[::-1])