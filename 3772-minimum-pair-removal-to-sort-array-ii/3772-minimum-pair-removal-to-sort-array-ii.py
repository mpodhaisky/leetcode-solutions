class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        sl = SortedList(enumerate(nums))
        inversions=0
        h=[]
        for i in range(len(nums)-1):
            heappush(h,(sum(nums[i:i+2]),(i,nums[i]),(i+1,nums[i+1])))
            if nums[i]>nums[i+1]:
                inversions+=1
        step=0
        while inversions:
            _,a, b = heappop(h)
            if a not in sl or b not in sl:
                continue
            sl.remove(a)
            sl.remove(b)
            mid=(a[0],a[1]+b[1])
            sl.add(mid)
            idx=sl.index(mid)
            if idx > 0:
                lo =sl[idx-1] 
                inversions+= (lo[1]>mid[1]) - (lo[1]>a[1])
                heappush(h,(lo[1]+mid[1],lo,mid))
            if idx <len(sl)-1:
                hi = sl[idx+1]
                inversions+= (hi[1]<mid[1])- (hi[1] < b[1])
                heappush(h,(mid[1]+hi[1],mid,hi))
            inversions-=a[1]>b[1]    
            step+=1

        return step