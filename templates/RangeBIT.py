class BIT:
    def __init__(self, arr):
        self.length = len(arr)
        self.t1 = [0] * (self.length + 1)
        self.t2 = [0] * (self.length + 1)

        for i, x in enumerate(arr):
            self.increase(i, i, x)

    def _add(self, tree, i, x):
        i += 1
        while i <= self.length:
            tree[i] += x
            i += i & -i

    def _query(self, tree, i):
        s = 0
        i += 1
        while i > 0:
            s += tree[i]
            i -= i & -i
        return s

    def increase(self, a, b, x):
        self._add(self.t1, a, x)
        self._add(self.t1, b + 1, -x)
        self._add(self.t2, a, a * x)
        self._add(self.t2, b + 1, -(b + 1) * x)

    def total(self, i):
        return ((i + 1) * self._query(self.t1, i)
                - self._query(self.t2, i))

    def sum(self, a, b):
        return self.total(b) - self.total(a - 1)

    def update(self, i, x):
        self.increase(i, i, x - self.sum(i, i))
