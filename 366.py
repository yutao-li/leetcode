from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(node):
            l, r = node.left, node.right
            if l:
                depth = 1 + dfs(l)
                if r:
                    depth = max(depth, 1 + dfs(r))
            else:
                if r:
                    depth = 1 + dfs(r)
                else:
                    depth = 0
            res[depth].append(node.val)
            return depth

        dfs(root)
        return [res[i] for i in range(max(res) + 1)]
