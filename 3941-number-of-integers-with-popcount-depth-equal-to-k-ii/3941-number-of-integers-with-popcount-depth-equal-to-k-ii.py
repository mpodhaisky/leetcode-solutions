class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        seen = defaultdict(SortedList)
        IDX = {}

        @cache
        def depth(n):
            return 0 if n ==1 else 1+depth(n.bit_count())
        
        for i , n in enumerate(nums):
            p = depth(n)
            IDX[i]=p
            seen[p].add(i)
        
        res=[]
        for q in queries:
            if q[0]==1:
                _, l, r, k = q
                res.append(seen[k].bisect_left(r+1)-1 - seen[k].bisect_left(l)+1)
            else:
                _,  i, x = q
                seen[IDX[i]].remove(i)
                p = depth(x)
                IDX[i] = p
                seen[p].add(i)
        return res