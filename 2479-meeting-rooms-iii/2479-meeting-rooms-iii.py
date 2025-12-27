class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heapify(meetings)
        busy = []
        free = list(range(n))
        f = Counter()

        while meetings:
            while busy  and busy[0][0] < meetings[0][0]:
                _, slot = heappop(busy)
                heappush(free,slot)
            if free:
                _, end = heappop(meetings)
                f[free[0]]+=1
                heappush(busy,(end-1,heappop(free)))
            else:
                end, slot = heappop(busy)
                delay = end-meetings[0][0]
                f[slot]+=1
                heappush(busy,(heappop(meetings)[1]+delay,slot))
                while busy and meetings and busy[0][0] >meetings[0][0]:
                    end, slot = heappop(busy)
                    delay = end-meetings[0][0]
                    f[slot]+=1
                    heappush(busy,(heappop(meetings)[1]+delay,slot))

        return max(f, key = lambda x: (f[x],-x))