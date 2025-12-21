class Solution:
    def lastInteger(self, n: int) -> int:
        start = step = 1
        while n-1:
            if n & 1:
                start = start+(n-1)*step
            else:
                start= start+(n-2)*step
            n -= n>>1
            step*=-2
        return start