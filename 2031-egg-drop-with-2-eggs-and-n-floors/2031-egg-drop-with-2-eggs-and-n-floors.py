class Solution:
    def twoEggDrop(self, n: int) -> int:
        return bisect_left(range(n+1), True, key = lambda k: k*(k+1)//2 >= n)
        
