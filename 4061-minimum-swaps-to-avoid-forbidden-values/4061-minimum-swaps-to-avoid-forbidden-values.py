class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:

        A, B = Counter(nums), Counter(forbidden)

        for n in A:
            if A[n] > len(nums)-B[n]:
                return -1

        f = Counter()
        for a, b in zip(nums, forbidden):
            if a == b:
                f[a] += 1

        if len(f)<=1:
            return f.total()
        
        diff= sub(*nlargest(2,f.values()))
        for n in sorted(f.values())[::-1][2:]:
            delta = min(n,diff)
            n-=delta
            diff-=delta
            diff+=n%2
        return (f.total()-diff)//2 + diff