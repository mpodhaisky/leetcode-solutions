from typing import List


class SegTreeMax:
    """
    Segment tree over y-coordinate segments.
    Supports range add (+1/-1) and query global max coverage.
    """
    __slots__ = ("n", "mx", "lz")

    def __init__(self, n: int):
        self.n = n
        self.mx = [0] * (4 * n)
        self.lz = [0] * (4 * n)

    def _push(self, idx: int):
        if self.lz[idx] != 0:
            v = self.lz[idx]
            li = idx * 2
            ri = idx * 2 + 1
            self.mx[li] += v
            self.lz[li] += v
            self.mx[ri] += v
            self.lz[ri] += v
            self.lz[idx] = 0

    def _add(self, idx: int, l: int, r: int, ql: int, qr: int, val: int):
        if ql <= l and r <= qr:
            self.mx[idx] += val
            self.lz[idx] += val
            return
        self._push(idx)
        mid = (l + r) // 2
        if ql < mid:
            self._add(idx * 2, l, mid, ql, qr, val)
        if qr > mid:
            self._add(idx * 2 + 1, mid, r, ql, qr, val)
        self.mx[idx] = self.mx[idx * 2] if self.mx[idx * 2] >= self.mx[idx * 2 + 1] else self.mx[idx * 2 + 1]

    def add(self, l: int, r: int, val: int):
        """
        add val on [l, r) in segment indices
        """
        if l >= r:
            return
        self._add(1, 0, self.n, l, r, val)

    def max_all(self) -> int:
        return self.mx[1]


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        # compute upper bound for side length: maximum possible inside any rectangle
        hi = 0
        for i in range(n):
            w = topRight[i][0] - bottomLeft[i][0]
            h = topRight[i][1] - bottomLeft[i][1]
            if w < h:
                if w > hi:
                    hi = w
            else:
                if h > hi:
                    hi = h

        # check if exists square of side s inside intersection of at least two rectangles
        def ok(s: int) -> bool:
            events = []
            ys = []

            # Build feasible rectangles in (x,y) for bottom-left corner of the square
            for i in range(n):
                ax, ay = bottomLeft[i]
                cx, cy = topRight[i]
                if cx - ax < s or cy - ay < s:
                    continue

                x1 = ax
                x2 = cx - s
                y1 = ay
                y2 = cy - s

                # bottom-left coordinates can be any point in [x1,x2] x [y1,y2] inclusive,
                # which is a closed rectangle. For sweep + compression we use half-open:
                # [x1, x2+1) and [y1, y2+1) (integer lattice).
                #
                # Because coords are ints and s is int, it's safe.
                xL = x1
                xR = x2 + 1
                yL = y1
                yR = y2 + 1

                if xL >= xR or yL >= yR:
                    continue

                events.append((xL, +1, yL, yR))
                events.append((xR, -1, yL, yR))
                ys.append(yL)
                ys.append(yR)

            if len(events) < 4:
                return False  # <2 feasible rects or nothing meaningful

            ys = sorted(set(ys))
            # Need at least one segment
            if len(ys) <= 1:
                return False

            # map y value to index
            y_id = {v: i for i, v in enumerate(ys)}

            # segment tree over segments between consecutive ys:
            # segments count = len(ys)-1
            segN = len(ys) - 1
            st = SegTreeMax(segN)

            # sort events by x
            events.sort()

            # sweep
            i = 0
            m = len(events)
            while i < m:
                x = events[i][0]

                # apply all events at this x
                while i < m and events[i][0] == x:
                    _, typ, yL, yR = events[i]
                    l = y_id[yL]
                    r = y_id[yR]
                    # update on segment indices [l, r-1] == segments in [yL,yR)
                    st.add(l, r - 1 + 1, typ)
                    i += 1

                # if any y has coverage >= 2 at this x-line, then there exists an overlap region
                # Note: because we used half-open in x, if overlap exists for any x in some interval,
                # it will be seen right after processing entering events.
                if st.max_all() >= 2:
                    return True

            return False

        # Binary search max side length
        lo, ans = 0, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans * ans