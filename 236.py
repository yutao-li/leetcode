# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            nonlocal res
            if not node:
                return False
            if res:
                return False
            left = find(node.left)
            right = find(node.right)
            eq = node == p or node == q
            if left + right + eq == 2:
                res = node
            return left or right or eq

        res = None
        find(root)
        return res
