class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        M=10**9+7
        A=sorted([1]+hFences+[m])
        B=sorted([1]+vFences+[n])
        def f(arr):
            A = set()
            for _ in range(len(arr)-1):
                arr = [n-arr[0] for n in arr[1:]]
                A|=set(arr)
                
            return A
        res =f(A)&f(B)
        return -1 if not res else pow(max(res),2)%M