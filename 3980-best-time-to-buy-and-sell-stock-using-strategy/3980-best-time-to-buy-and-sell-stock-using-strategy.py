class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        res = cur = sum(starmap(mul,zip(prices,strategy)))
        hi=lo=0
        for i, (p,s) in enumerate(zip(prices,strategy)):
            cur -= p*s
            cur +=p
            if hi <= i-k//2:
                cur-=prices[hi]
                hi+=1
            if lo <= i-k:
                cur+=prices[lo]*strategy[lo]
                lo+=1
            if i >=k-1:
                res=max(res,cur)
        return res