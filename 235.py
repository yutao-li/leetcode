# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        if p_val > q_val:
            p_val, q_val = q_val, p_val
        node = root
        while True:
            if node.val < p_val:
                node = node.right
            elif node.val > q_val:
                node = node.left
            else:
                return node
