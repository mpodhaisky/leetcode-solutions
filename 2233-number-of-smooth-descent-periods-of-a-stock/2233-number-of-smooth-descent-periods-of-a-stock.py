class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res,lo= 1, 0
        for i in range(1,len(prices)):
            if prices[i]!=prices[i-1]-1:
                lo=i
            res+=(i-lo+1)
        return res
            
        
