# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        t = defaultdict(list)
        pool = [(root, 0)]
        while pool:
            pool1 = []
            for node, col in pool:
                t[col].append(node.val)
                if node.left:
                    pool1.append((node.left, col - 1))
                if node.right:
                    pool1.append((node.right, col + 1))
            pool = pool1

        return [t[i] for i in range(min(t.keys()), max(t.keys()) + 1)]
