class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects=rects

    def pick(self) -> List[int]:
        area = 0
        res = None
        for a, b, c, d in self.rects:
            cur_area = (c-a+1)*(d-b+1)
            area += cur_area
            if random.random() <= cur_area/area:
                res=(a,b,c,d)
        
        return [randint(res[0],res[2]),randint(res[1],res[3])]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()