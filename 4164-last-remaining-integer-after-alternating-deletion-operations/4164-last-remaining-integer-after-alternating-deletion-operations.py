class Solution:
    def lastInteger(self, n: int) -> int:
        start, end , step = 1, n , 1

        while start != end:
            if abs(start-end) //abs(step) & 1:
                start, end, step = end-step,start, -2*step
            else:
                start, end, step = end, start, -2*step

        return start