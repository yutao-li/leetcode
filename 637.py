# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        pool = [root]
        res = []
        while pool:
            res.append(sum(i.val for i in pool) / len(pool))
            pool = [i.left for i in pool if i.left] + [i.right for i in pool if i.right]
        return res


