class RangeMinSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.h = (self.n - 1).bit_length()
        self.tree = [inf] * (2 * self.n)
        self.lazy = [inf] * self.n

        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i << 1], self.tree[i << 1 | 1])

    def _apply(self, p, val):
        self.tree[p] = min(self.tree[p], val)
        if p < self.n:
            self.lazy[p] = min(self.lazy[p], val)

    def _push(self, p):
        for s in range(self.h, 0, -1):
            i = p >> s
            if self.lazy[i] != inf:
                self._apply(i << 1, self.lazy[i])
                self._apply(i << 1 | 1, self.lazy[i])
                self.lazy[i] = inf

    def _build(self, p):
        while p > 1:
            p >>= 1
            self.tree[p] = min(self.tree[p << 1], self.tree[p << 1 | 1])
            if self.lazy[p] != inf:
                self.tree[p] = min(self.tree[p], self.lazy[p])

    def update_range(self, l, r, val):
        l += self.n
        r += self.n + 1
        l0, r0 = l, r

        self._push(l0)
        self._push(r0 - 1)

        while l < r:
            if l & 1:
                self._apply(l, val)
                l += 1
            if r & 1:
                r -= 1
                self._apply(r, val)
            l >>= 1
            r >>= 1

        self._build(l0)
        self._build(r0 - 1)

    def query(self, l, r):
        l += self.n
        r += self.n + 1

        self._push(l)
        self._push(r - 1)

        res = inf
        while l < r:
            if l & 1:
                res = min(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = min(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res
