class BinaryTrie:
    def __init__(self):
        self.trie = (T := lambda: defaultdict(T))()

    def add(self, word: str) -> None:
        T = reduce(getitem,word,self.trie)
        if "#" in T:
            T["#"]+=1
        else:
            T["#"]=1

    def remove(self,word:str) -> None:
        reduce(getitem, word, self.trie)["#"]-=1

    def closest(self, word):
        T = self.trie
        res=""
        for c in word:
            if T.get(c,{}):
                res+=c
                T = T[c]
            else:
                res+=str(1-int(c))
                T = T[str(1-int(c))]
        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def stringify(n):
            return bin(n)[2:].zfill(32)
        res=0
        T = BinaryTrie()
        for n in nums:
            T.add(stringify(n))
            m = int(T.closest("".join(str(1-int(c)) for c in stringify(n))),2)
            res = max(res,n^m)
        return res