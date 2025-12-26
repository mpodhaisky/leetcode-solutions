class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=defaultdict(lambda : -inf)
        for i, n in enumerate(nums):
            if i-seen[n] <=k: return True
            seen[n]=i
        return False    
