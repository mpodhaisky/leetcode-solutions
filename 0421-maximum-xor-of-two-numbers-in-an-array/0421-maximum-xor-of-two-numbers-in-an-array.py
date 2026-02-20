class BinaryTrie:
    def __init__(self):
        self.trie = (T := lambda: defaultdict(T))()

    def add(self, word: str) -> None:
        word = bin(word)[2:].zfill(32)
        T = reduce(getitem,word,self.trie)
        if "#" in T:
            T["#"]+=1
        else:
            T["#"]=1

    def remove(self,word:str) -> None:
        word = bin(word)[2:].zfill(32)
        reduce(getitem, word, self.trie)["#"]-=1

    def closest_complement(self, word):
        word = "".join(str(1-int(c)) for c in bin(word)[2:].zfill(32))
        T = self.trie
        res=""
        for c in word:
            if T.get(c,{}):
                res+=c
                T = T[c]
            else:
                res+=str(1-int(c))
                T = T[str(1-int(c))]
        return int(res,2)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res=0
        T = BinaryTrie()
        for n in nums:
            T.add(n)
            m = T.closest_complement(n)
            res = max(res,n^m)
        return res