class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        res=[]
        for a, b in pairwise(sorted(A)):
            if res and res[-1][-1]-res[-1][0] > b-a: res=[]
            if not res or b-a == res[-1][-1]-res[-1][0]: res.append([a,b])
        return res