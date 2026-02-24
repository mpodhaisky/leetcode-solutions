class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        def can_deliver(t):
            a = t//r1
            b = t//r2
            c = t//lcm(r2,r1)
            return max(0,d1+c-b) + max(0,d2+c-a) - (t-a-b+c) <=0
            
        return bisect_left(range(1<<40), True, key = can_deliver)