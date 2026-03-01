class Solution:
    def minimumOR(self, a: list[list[int]]) -> int:
        l, r = 0, (1 << 17) - 1
        while l <= r:
            m = l + (r - l) // 2
            ck = True
            for rw in a:
                ok = False
                for val in rw:
                    # Check if val is a submask of m
                    if (val | m) == m:
                        ok = True
                        break
                if not ok:
                    ck = False
                    break
            
            if not ck:
                l = m + 1
            else:
                r = m - 1
        return l