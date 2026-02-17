class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        M = 10**9+7
        
        @cache
        def dp(n):
            res=cur=1

            for m in arr:
                if n%m == 0 and n//m in arr:
                    res = (res +dp(m)*dp(n//m))%M
            return res
        
        return sum(map(dp,arr)) %M
