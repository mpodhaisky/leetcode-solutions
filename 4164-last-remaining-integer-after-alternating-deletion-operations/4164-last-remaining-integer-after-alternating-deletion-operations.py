class Solution:
    def lastInteger(self, n: int) -> int:
        mask = 0xAAAAAAAAAAAAAAAAAAAAAA
        return ((n-1)&mask)+1

