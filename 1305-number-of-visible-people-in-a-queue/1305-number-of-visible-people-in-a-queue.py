
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        dp = [0]*len(heights)
        mono = []
        for i in range(len(heights)-1,-1,-1):
            while mono and heights[mono[-1]] <= heights[i]:
                mono.pop()
                dp[i]+=1
            dp[i]+=bool(mono)
            mono.append(i)
        return dp