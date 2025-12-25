class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(max(0,n-i) for i, n in enumerate(sorted(happiness,reverse=True)[:k]))