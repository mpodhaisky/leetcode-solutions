class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(starmap(ne, zip(map(list,zip(*A)),map(sorted,zip(*A)))))