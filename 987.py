# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        pool = [(root, 0)]
        layer = 0
        while pool:
            pool1 = []
            for node, col in pool:
                d[col].append((layer, node.val))
                if node.left:
                    pool1.append((node.left, col - 1))
                if node.right:
                    pool1.append((node.right, col + 1))
            pool = pool1
            layer += 1
        return [[j for _, j in sorted(d[i])] for i in sorted(d.keys())]
