class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        if k ==0: return 0
        cur=k
        while comb(cur, k)< n: cur+=1
        return (1<<(cur-1)) + self.nthSmallest(n-comb(cur-1, k),k-1)