class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # dp = [[[-inf for _ in range(3)] for _ in range(k+1) ] for _ in range(len(prices))]

        #for i in range(len(prices)-2,-1,-1):

        @cache
        def dp(i, k, mode):
            if i == len(prices)-1:
                return prices[i]*mode
            res=max(dp(i+1,k,mode),mode*prices[i] + dp(i+1,k-bool(mode),0))

            if k and not mode:
                res = max(res,prices[i] + dp(i+1,k,-1), -prices[i]+ dp(i+1,k,1))
            return res
        res=dp(0,k,0)
        dp.cache_clear()
        return res