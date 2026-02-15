class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def divisors(n):
            res=cnt=cur=1
            while cur <n:
                cur = n // (n//(cur+1))
                if n % cur ==0:
                    res+=cur
                    cnt+=1
            return cnt, res
        res=0
        for n in nums:
            cnt, S = divisors(n)
            if cnt == 4:
                res+=S
        return res