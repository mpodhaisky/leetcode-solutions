# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=[root]
        res=-inf
        i = None
        cnt=1
        while q:
            S = sum(n.val for n in q)
            if S > res:
                res=S
                i=cnt
            q= [m for n in q for m in (n.left,n.right) if m]
            cnt+=1
        return i