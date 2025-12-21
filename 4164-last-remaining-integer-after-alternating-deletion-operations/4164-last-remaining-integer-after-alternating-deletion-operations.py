class Solution:
    def lastInteger(self, n: int) -> int:
        start = step = 1
        while n != (((1<<(n.bit_length()-1))) | 1):
            if n & 1:
                start, step = start+(n-1)*step, -2 *step
            else:
                start, step = start+(n-2)*step, -2 *step
            n -= n>>1
        return start if n.bit_length()&1 else start +(n-1)*step