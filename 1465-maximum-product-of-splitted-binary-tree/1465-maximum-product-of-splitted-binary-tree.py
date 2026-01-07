# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        M = 10**9+7
        
        @cache
        def dfs1(n):
            if not n: return 0
            return n.val + dfs1(n.left)+dfs1(n.right)

        def dfs2(n):
            if not n: return 0
            res=0
            if n.left:
                res = max(dfs2(n.left),dfs1(n.left) * (dfs1(root)-dfs1(n.left)))
            if n.right:
                res = max(dfs2(n.right),res,dfs1(n.right) * (dfs1(root)-dfs1(n.right)))
            return res
        
        return dfs2(root) % M