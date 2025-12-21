class Solution:
    def lastInteger(self, n: int) -> int:

        def dfs(start, end, step):
            if start ==end:
                return start
            
            if abs(start-end) //abs(step) & 1:
                return dfs(end-step,start, -2*step)
            else:
                return dfs(end, start, -2*step)

        return dfs(1,n,1)