# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, acc):
            nonlocal res
            acc = 10 * acc + node.val
            if node.left:
                dfs(node.left, acc)
            if node.right:
                dfs(node.right, acc)
            if not (node.left or node.right):
                res += acc

        res = 0
        dfs(root, 0)
        return res
