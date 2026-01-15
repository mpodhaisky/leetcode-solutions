class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        res=[]
        for i in range(32,-1,-1):
            costs=[]
            for n in nums:
                cur_cost=0
                for idx in res + [i]:
                    if not n & (1<<idx):
                        cur_cost += (1<<idx) - (n%(1<<idx))
                        n = 0
                heappush(costs,-cur_cost)
                if len(costs)>m:
                    heappop(costs)
                
            if -sum(costs) <=k:
                res.append(i)

        return sum(1<<i for i in res)
            