class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum("".join(row)!="".join(sorted(row)) for row in zip(*strs))