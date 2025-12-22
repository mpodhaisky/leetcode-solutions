class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = ["a"+w for w in strs]
        
        @cache
        def dp(prev, cur):
            if cur == len(strs[0]): return 0
            ret = 1+ dp(prev,cur+1)
            if all(strs[i][cur]>=strs[i][prev] for i in range(len(strs))):
                ret = min(ret,dp(cur, cur+1))
            return ret
        
        ans=dp(0,1)
        dp.cache_clear()
        
        return ans