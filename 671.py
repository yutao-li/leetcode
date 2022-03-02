from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        second = 1 << 31
        node = root
        while node.left and node.right:
            if node.left.val == node.right.val:
                l_second = self.findSecondMinimumValue(node.left)
                if l_second != -1:
                    second = min(second, l_second)
                node = node.right
            elif node.left.val < node.right.val:
                second = min(second, node.right.val)
                node = node.left
            else:
                second = min(second, node.left.val)
                node = node.right
        return second if second != 1 << 31 else -1
