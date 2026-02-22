class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        ones= nums.count(1)
        nums= [n for n in nums if n !=1]

        def g(a,b):
            G = gcd(a,b)
            return a//G, b//G
        
        @cache
        def dfs(i,num,den):
            if i >= len(nums): return num%den ==0 and num //den == k
            return dfs(i+1,num,den) + dfs(i+1,*g(num * nums[i], den)) + dfs(i+1,*g(num, den*nums[i]))

        return dfs(0,1,1) * pow(3,ones)