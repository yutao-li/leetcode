# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            res = node
            l = node.left
            if l:
                res = dfs(l)
                l.left = node.right
                l.right = node
            return res

        if not root:
            return None
        res = dfs(root)
        root.left = root.right = None
        return res
