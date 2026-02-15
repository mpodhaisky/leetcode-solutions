class Solution:
    def minOperations(self, s: str) -> int:
        c = min([c for c in s if c >"a"], default = "a")
        if c =="a": return 0
        return ord("z")-ord(c) +1

        