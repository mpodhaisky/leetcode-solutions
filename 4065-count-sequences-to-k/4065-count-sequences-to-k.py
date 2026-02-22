class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        ones= nums.count(1)
        fives = nums.count(5)
        nums= [n for n in nums if n not in (1,5)]

        five_k=0
        while k%5==0:
            five_k+=1
            k//=5
        
        @cache
        def dp(i,cnt):
            if i >= fives: return cnt == five_k
            return dp(i+1,cnt) + dp(i+1,cnt-1) + dp(i+1,cnt+1)
        
        def g(a,b):
            G = gcd(a,b)
            return a//G, b//G
        
        @cache
        def dfs(i,num,den):
            if i >= len(nums): return num%den ==0 and num //den == k
            return dfs(i+1,num,den) + dfs(i+1,*g(num * nums[i], den)) + dfs(i+1,*g(num, den*nums[i]))

        return dfs(0,1,1) * pow(3,ones) * dp(0,0)