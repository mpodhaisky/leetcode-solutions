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

class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        T = Trie()
        seen = SortedList()
        res = lo = 0
        pi = deque([0])
        T.add(pi[-1])
        
        for n in nums:
            seen.add(n)
            pi.append(pi[-1]^n)
            while seen[-1]-seen[0]>k:
                seen.remove(nums[lo])
                T.remove(pi.popleft())
                lo+=1
            res = max(res,T.max_xor(pi[-1]))
            T.add(pi[-1])
        return res