class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(set(nums))==1: return 0
        i = 32
        while len(set((1<<i)&n for n in nums))==1: i-=1
        q=[(i-1,[n for n in nums if not n&(1<<i)],[n for n in nums if n&(1<<i)])]
        res=0
        for depth, left, right in q:
            if depth==-1 or len(left)==len(right)==1:
                res=max(res,left.pop()^right.pop())
                continue
            l0,l1,r0,r1=[],[],[],[]
            for n in left:
                if n & (1<<depth):
                    l1.append(n)
                else:
                    l0.append(n)
            for n in right:
                if n & (1<<depth):
                    r1.append(n)
                else:
                    r0.append(n)
            if not (l0 and r1) and not (l1 and r0):
                q.append((depth-1,left,right))
            if (l0 and r1):
                q.append((depth-1,l0,r1))
            if (l1 and r0):
                q.append((depth-1,l1,r0))
        return res
