from typing import List
import sys

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int],
                  hierarchy: List[List[int]], budget: int) -> int:
        sys.setrecursionlimit(10000)
        B = budget
        NEG = -10**18
        
        # Build tree (0-based indices)
        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        def dfs(u: int):
            """
            Returns two arrays:
            f0[c] = max profit with cost exactly c in subtree of u,
                    assuming u's parent does NOT buy (so u has no discount)
            f1[c] = same, but assuming u's parent DOES buy (so u gets discount)
            """
            # Start with children combined DP for two situations:
            # children0: u not bought  -> children see parent-not-bought (use child's f0)
            # children1: u bought      -> children see parent-bought     (use child's f1)
            children0 = [NEG] * (B + 1)
            children1 = [NEG] * (B + 1)
            children0[0] = 0
            children1[0] = 0

            for v in children[u]:
                f0_v, f1_v = dfs(v)

                # Merge into children0 with f0_v (parent-not-bought)
                new0 = [NEG] * (B + 1)
                for c in range(B + 1):
                    if children0[c] == NEG:
                        continue
                    base = children0[c]
                    # add cost from v
                    rem = B - c
                    for cv in range(rem + 1):
                        if f0_v[cv] == NEG:
                            continue
                        val = base + f0_v[cv]
                        if val > new0[c + cv]:
                            new0[c + cv] = val
                children0 = new0

                # Merge into children1 with f1_v (parent-bought)
                new1 = [NEG] * (B + 1)
                for c in range(B + 1):
                    if children1[c] == NEG:
                        continue
                    base = children1[c]
                    rem = B - c
                    for cv in range(rem + 1):
                        if f1_v[cv] == NEG:
                            continue
                        val = base + f1_v[cv]
                        if val > new1[c + cv]:
                            new1[c + cv] = val
                children1 = new1

            # Now decide for node u itself
            f0 = [NEG] * (B + 1)
            f1 = [NEG] * (B + 1)

            # Option 1: u does NOT buy
            # Same for both parent states; just carry children0
            for c in range(B + 1):
                if children0[c] != NEG:
                    if children0[c] > f0[c]:
                        f0[c] = children0[c]
                    if children0[c] > f1[c]:
                        f1[c] = children0[c]

            # Option 2: u DOES buy
            # If parent not bought -> cost present[u], profit future[u] - present[u]
            cost_no_disc = present[u]
            profit_no_disc = future[u] - cost_no_disc

            if cost_no_disc <= B:
                for c in range(cost_no_disc, B + 1):
                    if children1[c - cost_no_disc] == NEG:
                        continue
                    val = children1[c - cost_no_disc] + profit_no_disc
                    if val > f0[c]:
                        f0[c] = val

            # If parent bought -> cost present[u]//2, profit future[u] - present[u]//2
            cost_disc = present[u] // 2
            profit_disc = future[u] - cost_disc

            if cost_disc <= B:
                for c in range(cost_disc, B + 1):
                    if children1[c - cost_disc] == NEG:
                        continue
                    val = children1[c - cost_disc] + profit_disc
                    if val > f1[c]:
                        f1[c] = val

            return f0, f1

        root = 0  # employee 1 (index 0)
        f0_root, f1_root = dfs(root)

        # Root has no boss, so it can never receive a discount.
        # Use only the "parent-not-bought" context (f0_root).
        ans = max(f0_root[:B + 1])
        return max(ans, 0)  # profit can't be negative if we choose to buy nothing
