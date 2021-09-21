# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = []
        pool = [root]
        while pool:
            levels.append(sum(i.val for i in pool))
            pool = [i.left for i in pool if i.left] + [i.right for i in pool if i.right]
        return max(range(len(levels)), key=lambda x: levels[x]) + 1

