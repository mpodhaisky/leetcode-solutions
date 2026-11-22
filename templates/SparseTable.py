from itertools import accumulate


class SparseTable:
    """Disjoint sparse table: O(n log n) build, O(1) query for any associative op."""

    def __init__(self, arr, op, neutral=None, commutative=False):
        self.op = op
        self.neutral = neutral
        arr = list(arr)
        n = len(arr)
        # left halves are folded right-to-left; only needs swapped args if op isn't commutative
        rev_op = op if commutative else (lambda acc, x: op(x, acc))
        self.st = [arr]

        for i in range(1, max(1, (n - 1).bit_length()) + 1):
            size = 1 << i
            half = size >> 1
            row = []

            for start in range(0, n, size):
                mid = start + half
                if mid >= n:  # no right half -> never queried at this level
                    row += arr[start:]
                    break
                end = start + size
                left = list(accumulate(arr[mid - 1 : start - 1 if start else None : -1], rev_op))
                left.reverse()
                row += left
                row += accumulate(arr[mid:end], op)

            self.st.append(row)

    def query(self, a, b):
        if b < a:
            return self.neutral
        if a == b:
            return self.st[0][a]

        row = self.st[(a ^ b).bit_length()]
        return self.op(row[a], row[b])
