# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque([root])
        parent={}
        while any(m for n in q for m in (n.left,n.right)):
            for _ in range(len(q)):
                cur = q.popleft()
                left = cur.left
                right = cur.right
                if left:
                    parent[left]=cur
                    q.append(left)
                if right:
                    parent[right]=cur
                    q.append(right)
        
        while len(q) > 1:
            q = set(parent[n] for n in q)
        return q.pop()