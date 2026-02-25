class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        P = 131
        MOD = 10**9 + 7
        
        # Precompute prefix hashes for s
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        for i in range(n):
            h[i+1] = (h[i] * P + ord(s[i])) % MOD
            p[i+1] = (p[i] * P) % MOD
            
        # Precompute prefix hashes for reversed s
        rs = s[::-1]
        rh = [0] * (n + 1)
        for i in range(n):
            rh[i+1] = (rh[i] * P + ord(rs[i])) % MOD
            
        def get_hash(h_arr, l, r):
            if l > r: 
                return 0
            return (h_arr[r+1] - h_arr[l] * p[r-l+1]) % MOD
            
        def get_lcp(i, j):
            # i is the rightmost index of the left segment in s
            # j is the leftmost index of the right segment in s
            low = 1
            high = min(i + 1, n - j)
            lcp = 0
            while low <= high:
                mid = (low + high) // 2
                
                # Check reversed left part against normal right part
                h1 = get_hash(rh, n - 1 - i, n - 1 - i + mid - 1)
                h2 = get_hash(h, j, j + mid - 1)
                
                if h1 == h2:
                    lcp = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return lcp
            
        def expand_d0(i, j):
            if i < 0 or j >= n:
                return 0
            return 2 * get_lcp(i, j)
            
        def expand(i, j):
            # Base boundary check equivalent to the original `d=1` state
            if i < 0 or j >= n:
                return 1 if i >= 0 or j < n else 0
            
            # Find the Longest Common Prefix without any mismatch
            lcp = get_lcp(i, j)
            ni = i - lcp
            nj = j + lcp
            
            res = 2 * lcp
            
            # If we hit the boundary after skipping matching characters
            if ni < 0 or nj >= n:
                res += 1 if (ni >= 0 or nj < n) else 0
                return res
                
            # If d=1 is still available, branch by deleting from left or right
            opt1 = 1 + expand_d0(ni - 1, nj)
            opt2 = 1 + expand_d0(ni, nj + 1)
            
            return res + max(opt1, opt2)

        ans = 0
        for i in range(n):
            ans = max(ans, expand(i - 1, i + 1) + 1)
            ans = max(ans, expand(i, i + 1))
            
        return ans