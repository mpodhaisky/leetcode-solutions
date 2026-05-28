class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        
        #preprocessing
        blocks = isqrt(len(nums2))+1
        inc = [0]*blocks
        f=[Counter() for _ in range(blocks)]
        for i, n in enumerate(nums2):
            f[i//blocks][n]+=1

        #queries
        res=[]
        for q in queries:
            if q[0]==1:
                _ , x, y, val = q
                while x<=y:
                    if x%blocks==0 and x+blocks-1 <=y:
                        inc[x//blocks]+=val
                        x+=blocks
                    else:
                        f[x//blocks][nums2[x]]-=1
                        nums2[x]+=val
                        f[x//blocks][nums2[x]]+=1
                        x+=1
            else:
                _, tot = q
                res.append(0)
                for n in nums1:
                    for i in range(blocks):
                        res[-1]+=f[i][tot-inc[i]-n]
        return res
