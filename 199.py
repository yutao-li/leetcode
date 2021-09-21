# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        pool = [root]
        while pool:
            res.append(pool[-1].val)
            tmp = []
            for node in pool:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            pool = tmp
        return res

