class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(starmap(ne, zip(map(list,zip(*strs)),map(sorted,zip(*strs)))))