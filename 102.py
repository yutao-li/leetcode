from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        pool = [root]
        res = []
        while pool:
            pool1 = []
            for node in pool:
                if node.left:
                    pool1.append(node.left)
                if node.right:
                    pool1.append(node.right)
            res.append([i.val for i in pool])
            pool = pool1
        return res
