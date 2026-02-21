def is_prime(n):
    cnt = cur = 1
    while cur !=n:
        cur = n//(n//(cur+1))
        if n%cur ==0:
            cnt+=1    
    return cnt==2
        
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        for n in range(left,right+1):
            res+=is_prime(n.bit_count())
        return res
    