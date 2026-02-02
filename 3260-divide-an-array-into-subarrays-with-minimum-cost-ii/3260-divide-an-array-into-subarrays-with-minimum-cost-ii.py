class WaveletTree:
    """
    Static wavelet tree that supports:
      sum_k_smallest(l, r, k): sum of k smallest values in arr[l..r] (0-indexed, inclusive)

    Build:  O(n log Ï)
    Query:  O(log Ï)
    Memory: O(n log Ï) in the simple implementation style (prefix arrays per node)
    """

    __slots__ = ("lo", "hi", "mid", "b", "s", "left", "right", "val_at_rank")

    def __init__(self, ranks: List[int], lo: int, hi: int, val_at_rank: List[int]):
        self.lo = lo
        self.hi = hi
        self.val_at_rank = val_at_rank  # rank -> original value

        self.left = None
        self.right = None

        # Leaf: all values are identical rank
        if lo == hi or not ranks:
            self.mid = (lo + hi) // 2
            self.b = [0] * (len(ranks) + 1)
            self.s = [0] * (len(ranks) + 1)
            return

        self.mid = (lo + hi) // 2

        # b[i] = how many of ranks[:i] go to left (<= mid)
        # s[i] = sum of original values of those left elements in ranks[:i]
        self.b = [0]
        self.s = [0]

        left_part = []
        right_part = []

        cnt = 0
        sm = 0
        for x in ranks:
            if x <= self.mid:
                left_part.append(x)
                cnt += 1
                sm += val_at_rank[x]
            else:
                right_part.append(x)
            self.b.append(cnt)
            self.s.append(sm)

        if lo <= self.mid:
            self.left = WaveletTree(left_part, lo, self.mid, val_at_rank)
        if self.mid + 1 <= hi:
            self.right = WaveletTree(right_part, self.mid + 1, hi, val_at_rank)

    def sum_k_smallest(self, l: int, r: int, k: int) -> int:
        """
        Sum of k smallest values in the subarray positions [l, r] (inclusive),
        where l/r refer to this node's current sequence indexing.
        """
        if l > r or k <= 0:
            return 0

        # If leaf: all values in this node are the same rank self.lo
        if self.lo == self.hi:
            return k * self.val_at_rank[self.lo]

        # Count how many go to left within [l, r]
        # Using prefix arrays of length n+1:
        # leftCount = b[r+1] - b[l]
        left_count = self.b[r + 1] - self.b[l]
        left_sum = self.s[r + 1] - self.s[l]

        if k <= left_count:
            # Restrict to left child
            nl = self.b[l]
            nr = self.b[r + 1] - 1
            return self.left.sum_k_smallest(nl, nr, k)
        else:
            # Take all left + remaining from right child
            # Map indices into right child:
            # right_index(i) = i - b[i]
            nl = l - self.b[l]
            nr = (r + 1 - self.b[r + 1]) - 1
            return left_sum + self.right.sum_k_smallest(nl, nr, k - left_count)


def build_wavelet_tree(arr: List[int]) -> WaveletTree:
    """
    Builds a wavelet tree with coordinate compression so hi-lo is small.
    """
    vals = sorted(set(arr))
    rank = {v: i for i, v in enumerate(vals)}
    ranks = [rank[v] for v in arr]
    return WaveletTree(ranks, 0, len(vals) - 1, vals)


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        wt = build_wavelet_tree(nums[1:])
        return nums[0] + min(wt.sum_k_smallest(i,i+dist,k-1) for i in range(len(nums)-1-dist))