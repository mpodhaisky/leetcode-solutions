score=[0]*(pow(10,5)+1)

for n in range(1,pow(10,5)+1):
    cnt=cur=S=1
    while cur!=n and cnt <4:
        cur = n//(n//(cur+1))
        if n%cur==0:
            cnt+=1
            S+=cur
        if cnt==4 and cur == n:
            score[n]=S

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(score[n] for n in nums)
       