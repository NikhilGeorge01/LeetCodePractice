# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node,p,q):
            if not node:
                return False
            if node == p or node == q:
                return node
            right = lca(node.right,p,q)
            left = lca(node.left,p,q)
            if left and right:
                return node
            return left or right
        return lca(root,p,q)
            

        