class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        h=[(0,inf)]
        res=0
        for a, _, v in events:
            heappush(h,(-v,a))
            res=max(res,v)

        for _, b, v in sorted(events,key=lambda x: x[1]):
            while h[0][1]<=b:heappop(h)
            res= max(res,v-h[0][0])
        return res
            