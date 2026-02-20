class BinaryTrie:
    def __init__(self):
        self.trie = (T := lambda: defaultdict(T))()
        self.trie["cnt"] = 0

    def add(self, x: int) -> None:
        bits = bin(x)[2:].zfill(32)
        T = self.trie
        T["cnt"] += 1
        for b in bits:
            T = T[b]
            if "cnt" not in T:
                T["cnt"] = 0
            T["cnt"] += 1
        T["#"] = T.get("#", 0) + 1

    def remove(self, x: int) -> None:
        bits = bin(x)[2:].zfill(32)
        T = self.trie
        path = [T]
        for b in bits:
            if b not in T or T[b].get("cnt", 0) == 0:
                raise KeyError("value not present in trie")
            T = T[b]
            path.append(T)
        if T.get("#", 0) <= 0:
            raise KeyError("value not present in trie")

        path[-1]["#"] -= 1
        for node in path:
            node["cnt"] -= 1
        
        T = self.trie
        for b in bits:
            child = T[b]
            if child.get("cnt", 0) == 0:
                del T[b]
                break
            T = child

    def closest_complement(self, x: int) -> int:
        bits = bin(x)[2:].zfill(32)
        T = self.trie
        if T.get("cnt", 0) == 0:
            raise ValueError("trie is empty")

        res = []
        for b in bits:
            want = '1' if b == '0' else '0'
            if want in T and T[want].get("cnt", 0) > 0:
                res.append(want)
                T = T[want]
            else:
                res.append(b)
                T = T[b]
        return int("".join(res), 2)

class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        T = BinaryTrie()
        seen = SortedList()
        res = lo=cur=0
        pi = deque([0])
        T.add(pi[-1])
        
        for n in nums:
            seen.add(n)
            pi.append(pi[-1]^n)
            while seen[-1]-seen[0]>k:
                seen.remove(nums[lo])
                T.remove(pi.popleft())
                lo+=1
            m = T.closest_complement(pi[-1])
            res = max(res,pi[-1]^m)
            T.add(pi[-1])
        return res