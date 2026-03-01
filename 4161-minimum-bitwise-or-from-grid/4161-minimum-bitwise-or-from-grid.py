class Solution:
    def minimumOR(self, a: list[list[int]]) -> int:
        def check(m):
            for rw in a:
                if not any((val|m)==m for val in rw):
                    return False
            return True

        l, r = 0, (1 << 17) - 1
        while l <= r:
            m = l + r >> 1
            if not check(m):
                l = m + 1
            else:
                r = m - 1
        return l