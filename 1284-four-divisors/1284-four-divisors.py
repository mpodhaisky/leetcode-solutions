N=pow(10,5)+1
S = [0]*N
C = [0]*N

for n in range(1,N+1):
    for m in range(n,N,n):
        C[m]+=1
        S[m]+=n

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(S[n] for n in nums if C[n]==4)