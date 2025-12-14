class Solution:
    def numberOfWays(self, corridor: str) -> int:
        M = 10**9+7
        res = 1
        lo=S=0
        for hi , n in enumerate(corridor):
            if n=="P": continue
            S+=1
            if S==2:
                lo=hi
            elif S==3:
                res = (res*(hi-lo))%M
                S=1
        return res if S==2 else 0