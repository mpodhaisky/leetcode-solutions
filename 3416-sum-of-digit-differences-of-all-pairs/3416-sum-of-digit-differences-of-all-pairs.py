class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        N, M = len(nums), len(str(nums[0]))
        f = [[0]*10 for _ in range(M)]
        for i in range(N):
            s = str(nums[i])
            for j in range(M):
                f[j][int(s[j])]+=1
        res=M*N*(N-1) >> 1
        for row in f:
            for n in row:
                res-= n*(n-1) >> 1
        return res