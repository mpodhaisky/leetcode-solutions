class Solution:
    def lastInteger(self, n: int) -> int:
        start, end , step = 1, n , 1
        while start!=end:
            n = abs(start-end)//abs(step)+1
            if (n-1).bit_count()==1 and n.bit_length()&1: 
                return start
            if abs(start-end) //abs(step) & 1:
                start, end, step = end-step,start, -2*step
            else:
                start, end, step = end, start, -2 *step
        return start