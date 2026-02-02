class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k-=1
        res = inf
        cur = 0
        sl = SortedList()
        for i,n in enumerate(nums[1:],1):
            if len(sl)<k:
                cur+=n
            elif n < sl[k-1]:
                cur-=sl[k-1]
                cur+=n
            sl.add(n)
            if i >=dist+2:
                if sl.index(nums[i-dist-1]) <k:
                    cur-=nums[i-dist-1]
                    sl.remove(nums[i-dist-1])
                    cur+=sl[k-1]
                else:
                    sl.remove(nums[i-dist-1])
            if len(sl)>=k:
                res=min(res,cur+nums[0])
        return res
