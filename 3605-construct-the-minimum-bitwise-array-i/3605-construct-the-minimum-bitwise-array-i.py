class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in nums:
            for m in range(1000):
                if m | (m+1) == n:
                    ans.append(m)
                    break
            else:
                ans.append(-1)
        return ans