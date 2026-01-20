class Solution:
    @cache
    def twoEggDrop(self, n: int) -> int:
        return 0 if not n else min(max(i,1+self.twoEggDrop(n-i)) for i in range(1,n+1))
