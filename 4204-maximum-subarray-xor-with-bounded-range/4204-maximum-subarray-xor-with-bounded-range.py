class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1
    
    def remove(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            child = node.children[bit]
            child.count -= 1
            node = child
    
    def max_xor(self, num):
        node = self.root
        result = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            flip = 1 - bit
            if flip in node.children and node.children[flip].count > 0:
                result |= (1 << i)
                node = node.children[flip]
            else:
                node = node.children[bit]
        return result

class MinMaxQueue:
    def __init__(self) -> None:
        self._q: Deque[T] = deque()
        self._minq: Deque[T] = deque()  # increasing
        self._maxq: Deque[T] = deque()  # decreasing

    def __len__(self) -> int:
        return len(self._q)

    def add(self, x: T) -> None:
        self._q.append(x)

        while self._minq and self._minq[-1] > x:
            self._minq.pop()
        self._minq.append(x)

        while self._maxq and self._maxq[-1] < x:
            self._maxq.pop()
        self._maxq.append(x)

    def pop(self) -> T:
        if not self._q:
            raise IndexError("pop from empty queue")

        x = self._q.popleft()

        if self._minq and self._minq[0] == x:
            self._minq.popleft()
        if self._maxq and self._maxq[0] == x:
            self._maxq.popleft()

        return x

    def min(self) -> T:
        if not self._q:
            raise IndexError("min from empty queue")
        return self._minq[0]

    def max(self) -> T:
        if not self._q:
            raise IndexError("max from empty queue")
        return self._maxq[0]

class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        T = Trie()
        seen = MinMaxQueue()
        res = lo = 0
        pi = deque([0])
        T.add(pi[-1])
        
        for n in nums:
            seen.add(n)
            pi.append(pi[-1]^n)
            while seen.max()-seen.min()>k:
                seen.pop()
                T.remove(pi.popleft())
                lo+=1
            res = max(res,T.max_xor(pi[-1]))
            T.add(pi[-1])
        return res