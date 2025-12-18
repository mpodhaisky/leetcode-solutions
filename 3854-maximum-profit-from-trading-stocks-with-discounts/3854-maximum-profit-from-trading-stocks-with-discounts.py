class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build adjacency list for the tree
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u - 1].append(v - 1)
        
        # Helper to merge two DP arrays: new_dp[i+j] = max(new_dp[i+j], dp1[i] + dp2[j])
        # This is essentially merging two knapsacks.
        def merge(dp1, dp2):
            new_dp = [-float('inf')] * (budget + 1)
            # Optimization: only iterate through valid states
            # We collect indices where dp value is not -inf to avoid iterating full range blindly
            valid_i = [i for i, val in enumerate(dp1) if val != -float('inf')]
            valid_j = [j for j, val in enumerate(dp2) if val != -float('inf')]
            
            for i in valid_i:
                for j in valid_j:
                    if i + j <= budget:
                        if dp1[i] + dp2[j] > new_dp[i + j]:
                            new_dp[i + j] = dp1[i] + dp2[j]
            return new_dp

        # DFS function
        # Returns a tuple: (dp_if_parent_bought, dp_if_parent_skipped)
        # Each element is a list of size budget+1 where list[cost] = max_profit
        def dfs(u):
            # Base states for accumulating children results
            # Initialize with cost 0 having profit 0.
            current_buy = [-float('inf')] * (budget + 1)
            current_buy[0] = 0
            
            current_skip = [-float('inf')] * (budget + 1)
            current_skip[0] = 0
            
            # Process all children
            for v in adj[u]:
                child_res_parent_bought, child_res_parent_skipped = dfs(v)
                
                # If u buys, children see 'parent bought'
                current_buy = merge(current_buy, child_res_parent_bought)
                # If u skips, children see 'parent skipped'
                current_skip = merge(current_skip, child_res_parent_skipped)
            
            # Now calculate the two result tables for u's parent
            res_parent_bought = [-float('inf')] * (budget + 1)
            res_parent_skipped = [-float('inf')] * (budget + 1)
            
            u_full_cost = present[u]
            u_half_cost = present[u] // 2
            u_profit_base = future[u] # We subtract cost dynamically
            
            # 1. Construct res_parent_bought (u's parent bought)
            # Option A: u Skips. Cost 0. Use current_skip.
            for b in range(budget + 1):
                if current_skip[b] != -float('inf'):
                    if current_skip[b] > res_parent_bought[b]:
                        res_parent_bought[b] = current_skip[b]
            
            # Option B: u Buys (Discounted). Cost u_half_cost. Use current_buy.
            for b in range(budget + 1):
                if current_buy[b] != -float('inf'):
                    total_cost = b + u_half_cost
                    if total_cost <= budget:
                        profit = (u_profit_base - u_half_cost) + current_buy[b]
                        if profit > res_parent_bought[total_cost]:
                            res_parent_bought[total_cost] = profit

            # 2. Construct res_parent_skipped (u's parent didn't buy)
            # Option A: u Skips. Cost 0. Use current_skip.
            for b in range(budget + 1):
                if current_skip[b] != -float('inf'):
                    if current_skip[b] > res_parent_skipped[b]:
                        res_parent_skipped[b] = current_skip[b]
                        
            # Option B: u Buys (Full Price). Cost u_full_cost. Use current_buy.
            for b in range(budget + 1):
                if current_buy[b] != -float('inf'):
                    total_cost = b + u_full_cost
                    if total_cost <= budget:
                        profit = (u_profit_base - u_full_cost) + current_buy[b]
                        if profit > res_parent_skipped[total_cost]:
                            res_parent_skipped[total_cost] = profit
                            
            return res_parent_bought, res_parent_skipped

        # The root is Employee 1 (index 0). The CEO has no parent, so we use the 
        # "parent skipped" logic (paying full price if they buy).
        _, root_res_skipped = dfs(0)
        
        # The result is the max profit found in the DP array for any cost <= budget
        return max(0, max(root_res_skipped))