class Solution:
    def numSteps(self, s: str) -> int:
        if s.count("1") == 1:
            return len(s)-1
        else:
            return 1 + len(s) + s.count("0") - len(list(takewhile(lambda x: x=="0", s[::-1])))