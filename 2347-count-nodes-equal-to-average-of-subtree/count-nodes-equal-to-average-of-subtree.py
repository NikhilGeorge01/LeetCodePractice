# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        @cache
        def ct(node):
            if not node:
                return 0
            else:
                return 1 + ct(node.left) + ct(node.right)
        @cache
        def sm(node):
            if not node:
                return 0
            else:
                return node.val + sm(node.left) + sm(node.right)
        @cache
        def av(node):
            if not node:
                return 0
            if sm(node)//ct(node) == node.val:
                return 1 + av(node.left) + av(node.right)
            else:
                return av(node.left) + av(node.right)
        return av(root)