class SortedPrefixSumList:
    def __init__(self,k):
        self.k = k
        self.sl = SortedList()
        self.S = 0
    
    def add(self,x):
        if len(self.sl)<self.k:
            self.S+=x
        elif x < self.sl[self.k-1]:
            self.S+=x-self.sl[self.k-1]
        self.sl.add(x)
    
    def remove(self,x):
        if self.sl.index(x) < self.k:
            self.S-=x
            self.sl.remove(x)
            self.S+=self.sl[self.k-1]
        else:
            self.sl.remove(x)
    
    def query(self):
        return self.S


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        sl = SortedPrefixSumList(k-1)
        res = inf
        for i,n in enumerate(nums[1:],1):
            sl.add(n)
            if i >= dist+2:
                sl.remove(nums[i-dist-1])
            if i+1 >=k:
                res=min(res,sl.query()+nums[0])
        return res
