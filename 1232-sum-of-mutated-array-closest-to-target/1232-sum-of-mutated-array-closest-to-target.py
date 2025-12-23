class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        i=len(arr)-1
        S = sum(arr)
        res=inf
        out=None
        for value in range(arr[-1],-1,-1):
            while i>=0 and value < arr[i]:
                S-=arr[i]
                i-=1
            if abs((S+(len(arr)-1-i) * value) -target) <= res:
                res = abs((S+(len(arr)-1-i) * value) -target)
                out = value
        return out
        

