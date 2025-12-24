class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        S = sum(apple)
        h=[-n for n in capacity]
        heapify(h)
        cnt=0
        while S>0:
            S+=heappop(h)
            cnt+=1
        return cnt

        
