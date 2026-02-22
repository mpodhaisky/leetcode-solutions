class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        ones= nums.count(1)
        fives = nums.count(5)
        nums= [n for n in nums if n not in (1,5)]

        five_k=0
        while k%5==0:
            five_k+=1
            k//=5
        
        dp = Counter({0:1})
        for _ in range(fives):
            next_dp = Counter()
            for n in dp:
                for dn in range(-1,2):
                    next_dp[n+dn]+=dp[n]
            dp = next_dp

        def g(a,b):
            G = gcd(a,b)
            return a//G, b//G
        
        @cache
        def dfs(i,num,den):
            if i >= len(nums): return num%den ==0 and num //den == k
            return dfs(i+1,num,den) + dfs(i+1,*g(num * nums[i], den)) + dfs(i+1,*g(num, den*nums[i]))

        return dfs(0,1,1) * pow(3,ones) * dp[five_k]