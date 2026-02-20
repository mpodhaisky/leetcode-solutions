class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0
        def expand(i, j, d=1):
            if i < 0 or j >= n:
                return d if i >= 0 or j < n else 0
            if s[i] == s[j]:
                return 2 + expand(i - 1, j + 1, d)
            if d:
                return 1 + max(expand(i - 1, j, d - 1), expand(i, j + 1, d - 1))
            return 0
        ans = 0
        for i in range(n):
            ans = max(ans, expand(i - 1, i + 1) + 1)
            ans = max(ans, expand(i, i + 1))
        return ans