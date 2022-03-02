# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = [root]
        d = set()
        while stack:
            node = stack.pop()
            if k - node.val in d:
                return True
            d.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
