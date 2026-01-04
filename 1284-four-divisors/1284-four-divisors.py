class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            cnt=cur=S=1
            while cur!=n:
                cur = n//(n//(cur+1))
                if n%cur==0:
                    cnt+=1
                    S+=cur
            if cnt == 4:
                res+=S
        return res