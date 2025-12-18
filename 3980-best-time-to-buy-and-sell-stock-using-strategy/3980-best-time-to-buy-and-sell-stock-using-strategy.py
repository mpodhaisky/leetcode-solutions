class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        res = cur = sum(starmap(mul,zip(prices,strategy)))
        for i, (p,s) in enumerate(zip(prices,strategy)):
            cur += p-p*s
            if i >= k//2: cur-=prices[i-k//2]
            if i >= k: cur+=prices[i-k]*strategy[i-k]
            if i >=k-1: res=max(res,cur)
        return res