class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        ones= nums.count(1)
        nums= [n for n in nums if n !=1]

        @cache
        def dfs(i,num,den):
            if i >= len(nums): return num%den ==0 and num //den == k
            res = dfs(i+1,num,den)
            a , b= num * nums[i], den
            a, b =a//gcd(a,b), b//gcd(a,b)
            
            res+= dfs(i+1,a,b)
            a, b = num, den*nums[i]
            a, b =a//gcd(a,b), b//gcd(a,b)
            
            res+= dfs(i+1,a,b)

            return res

        return dfs(0,1,1) * pow(3,ones)