class Solution:
    def lastInteger(self, n: int) -> int:

        def dfs(start, end, step):
            if start ==end:
                return start

            if len(range(start,end+(1 if step >0 else -1),step)) % 2 ==0:
                return dfs(end-step,start, -2*step)
            else:
                return dfs(end, start, -2*step)

        return dfs(1,n,1)