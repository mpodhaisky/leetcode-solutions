class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(n for n in balance if n >0) < sum(-n for n in balance if n<0): return -1
        res=0
        for i in range(len(balance)):
            if balance[i]>=0: continue
            for k in range(1,len(balance)+1):
                for j in ((i-k)%len(balance),(i+k)%len(balance)):
                    if balance[j]<=0:continue
                    delta = min(-balance[i],balance[j])
                    balance[i]+=delta
                    balance[j]-=delta
                    res+=delta*k
                    if not balance[i]:
                        return res
        return 0

        