class Solution:
    def strStr(self, t: str, s: str) -> int:
        f = lambda x: ord(x) - ord("a") + 1
        p = 29
        M = 1234567893
        dp = [0]
        for c in s:
            dp.append(((dp[-1] * p) % M + f(c)) % M)

        seen = set(dp)
        cur = lo = 0
        for i, n in enumerate(t):
            cur = ((cur * p) % M + f(n)) % M
            while cur not in seen:
                cur = (cur - ((pow(p, i - lo, M) * f(t[lo])) % M)) % M
                lo += 1
            if i - lo + 1 == len(s):
                return lo
        return -1

