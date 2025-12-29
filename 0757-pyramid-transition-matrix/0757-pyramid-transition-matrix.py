class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed=set(allowed)
        @cache
        def dfs(word):
            print(word)
            if len(word) <=1: return True
            ret=[]
            for i in range(1,len(word)):
                ret.append([])
                for c in "ABCDEF":
                    if word[i-1]+word[i]+c in allowed:
                        ret[-1].append(c)
            return any(dfs("".join(row)) for row in product(*ret))
        return dfs(bottom)