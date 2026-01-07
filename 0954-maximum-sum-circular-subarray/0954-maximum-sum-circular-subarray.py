class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        seen=SortedList([0])
        q=deque([0])
        res = -inf
        for i in range(2*len(nums)):
            q.append(q[-1]+nums[i%len(nums)])

            if i >=len(nums):
                seen.remove(q.popleft())
            
            res =max(res,q[-1]-seen[0])
            seen.add(q[-1])
        return res

