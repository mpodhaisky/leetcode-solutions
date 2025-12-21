class Solution:
    def lastInteger(self, n: int) -> int:
        start, end , step = 1, n , 1
        while n != (((1<<(n.bit_length()-1))) | 1):
            if abs(start-end) //abs(step) & 1:
                start, end, step = end-step,start, -2*step
            else:
                start, end, step = end, start, -2 *step
            n = abs(start-end) //abs(step) +1
        return start if n.bit_length()&1 else end