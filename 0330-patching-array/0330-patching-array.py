class Solution:
    def merge(self,A,B):
        ret=[]
        i=j=0
        while i<len(A) and j<len(B):
            C=None
            if A[i]<B[j]:
                C=A[i]
                i+=1
            else:
                C=B[j]
                j+=1
            if not ret or C[0] > ret[-1][-1]+1:
                ret.append(C)
            else:
                ret[-1][-1]=max(ret[-1][-1],C[1])
        for a, b in A[i:]+B[j:]:
            if not ret or a>ret[-1][-1]+1:
                ret.append([a,b])
            else:
                ret[-1][-1]=max(ret[-1][-1],b)
        return ret


    def minPatches(self, nums: List[int], N: int) -> int:
        dp=[[0,0]]

        for n in nums:
            dp = self.merge(dp,[[a+n,b+n] for a, b in dp])
        
        cnt=0
        
        while dp[0][1]<N:
            cnt+=1
            dp=self.merge(dp,[[a+dp[0][1]+1,b+dp[0][1]+1] for a, b in dp])
            print(dp)
        return cnt
