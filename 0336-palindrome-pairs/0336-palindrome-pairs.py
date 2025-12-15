"""
â â â â â â â¢â£â£â£â£¤â£¤â£¤â£¤â£¤â£¤â£¤â£¤â£¤â£¤â£¤â£¤â£¤â£â£â â â â â 
â â â â â â â£¾â â â â â â â â â â â£â â â â â¢â â â¡â â â â 
â â â â â â â£¿â â â â â â â â â â â£â¡â â â â â â â¡â â â â 
â£â£â£â â â â£¿â â â â â â â â â ¸â¢°â¡â â ³â£â °â â â¢°â£·â ¶â â£§â 
â¢»â¡â â â ²â¡â£¿â â â â â â â â  â â¢¸â â â â â â â â â â â â£¿â 
â â »â£â â â â£¿â â â â â â â¢ â â£°â â â¢â¡â¢ â â â â â£ â  â¡â â¢§
â â â â â¢¦â£â£¿â â â¢ â¡â â â â â£¯â â â â â â â  â¢¦â â â â â â¢¸
â â â â â â â£¿â â â â¢ â â â¢ â â ¹â£â â â â ¢â¢¤â  â â ¤â¡ â â â¢â¡¾
â â â â â â¢â¡¿â ¦â¢¤â£¤â£¤â£¤â£¤â£¤â£¤â£¤â¡¼â£·â ¶â ¤â¢¤â£¤â£¤â¡¤â¢¤â¡¤â ¶â â â 
â â â â â â ¸â£¤â¡´â â ¸â£â£ â ¼â â â â â ¹â£â£ â â â¢¾â¡â£ â â â â â 
â â â â â â â â â â â â â â â â â â â â â â â â â â â â â â 
"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        M = 1234567891
        p = 29
        f = lambda x: ord(x)-ord("a")+1

        def hash(s):
            cur=0
            for c in s:
                cur = (cur*p)%M
                cur = (cur+f(c))%M
            return cur

        seen=defaultdict(list)
        for i , w in enumerate(words):
            seen[w].append(i)

        res= set()
        for i in range(len(words)):
            cur=rev=0

            for k in range(len(words[i])+1):
                if k >0:
                    cur = (cur*p)%M
                    cur = (cur+f(words[i][k-1]))%M
                    rev = (rev + f(words[i][k-1])*pow(p,k-1,M))%M
                if cur == rev:
                    for j in seen[words[i][k:][::-1]]:
                        if i!=j:
                            res.add((j,i))
            cur=rev=0
            for k in range(len(words[i])+1):
                if k >0:
                    cur = (cur*p)%M
                    cur = (cur+f(words[i][len(words[i])-k]))%M
                    rev = (rev + f(words[i][len(words[i])-k])*pow(p,k-1,M))%M
                if cur == rev:
                    for j in seen[words[i][:len(words[i])-k][::-1]]:
                        if i!=j:
                            res.add((i,j))
                

        return list(map(list,res))