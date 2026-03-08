class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(str(1-int(nums[i][i])) for i in range(len(nums)))