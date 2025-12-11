class Solution:
    def merge(self, A, B):
        ret=[]
        i=j=0
        while i<len(A) and j<len(B):
            C=None
            if A[i][0] < B[j][0]:
                C = A[i]  
                i+=1
            else:
                C=B[j]
                j+=1
            if not ret or ret[-1][-1]< C[0]-1:
                ret.append(C)
            else:
                ret[-1][-1]=max(ret[-1][-1],C[1])
        for a,b in A[i:]+B[j:]:
            if not ret or ret[-1][-1] < a-1:
                ret.append([a,b])
            else:
                ret[-1][-1]=max(ret[-1][-1],b)
        return ret
                

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) &1: return False
        dp = [[0,0]]
        for n in nums:
            dp = self.merge(dp,[[a+n,b+n] for a, b in dp])

        return any(a<=(sum(nums)>>1)<=b for a, b in dp)