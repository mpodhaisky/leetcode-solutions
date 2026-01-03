class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        cur = 1
        for i in range(2,k+2):
            cur = ((cur*10)+1 )%k
            if not cur:
                return i
        return -1 