class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        f = Counter(s).values()
        return len(set(f))==1