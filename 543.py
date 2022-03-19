from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> (int, int):
            if not node:
                return 0, 0
            left_path, left_diameter = dfs(node.left)
            right_path, right_diameter = dfs(node.right)
            return 1 + max(left_path, right_path), max(1 + left_path + right_path, left_diameter, right_diameter)

        return dfs(root)[1] - 1
