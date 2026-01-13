class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        lo, hi = 0, 10**9+1
        while abs(lo-hi)>pow(10,-6):
            mid = (lo + hi)/2
            area=0
            for x, y, l in squares:
                if y>=mid:
                    area-=l*l
                elif y+l <=mid:
                    area+=l*l
                else:
                    area+=l*(mid-y)
                    area-=l*(y+l-mid)
            

            if area >= 0:
                hi = mid - pow(10,-6)
            else:
                lo = mid + pow(10,-6)
        

        return mid



