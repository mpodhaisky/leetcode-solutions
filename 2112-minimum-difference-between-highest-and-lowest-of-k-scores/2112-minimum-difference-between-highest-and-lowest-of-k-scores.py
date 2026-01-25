class Solution:
    def minimumDifference(self, A: List[int], k: int) -> int:
        A.sort()
        return min(A[i]-A[i-k+1] for i in range(k-1,len(A)))