class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums)==1: return sum(nums)
        q=deque([(0,0)])
        cur=0
        res = -inf
        for i in range(2*len(nums)):
            cur +=nums[i%len(nums)]

            if (i-q[0][0]+1)>len(nums): q.popleft()
            
            res=max(res,cur-q[0][1])
            
            while q and q[-1][1]>=cur: q.pop()
            
            q.append((i,cur))

        return res

