from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node):
            nonlocal pathS, pathD
            if not node:
                return
            if pathS and pathD:
                return
            if node.val == startValue:
                pathS = list(path)
            elif node.val == destValue:
                pathD = list(path)
            path.append('L')
            dfs(node.left)
            path.pop()
            path.append('R')
            dfs(node.right)
            path.pop()

        path = []
        pathS = pathD = None
        dfs(root)
        i = 0
        while i < len(pathS) and i < len(pathD) and pathS[i] == pathD[i]:
            i += 1
        return 'U' * (len(pathS) - i) + ''.join(pathD[i:])
