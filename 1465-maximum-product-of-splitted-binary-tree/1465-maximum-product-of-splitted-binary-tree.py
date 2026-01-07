# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        M = 10**9+7
        S=0
        q=[root]
        for n in q:
            S+=n.val
            q+=filter(None,(n.left,n.right))
        
        def dfs(n):
            if not n: return 0, 0
            a, b = dfs(n.left)
            c, d = dfs(n.right)
            size = b + d + n.val
            return max(a,c,(S-size)*size), size
        
        return dfs(root)[0] % M