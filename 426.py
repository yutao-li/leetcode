from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            first = last = node
            if node.left:
                first, l_l = dfs(node.left)
                node.left = l_l
                l_l.right = node
            if node.right:
                r_f, last = dfs(node.right)
                node.right = r_f
                r_f.left = node
            return first, last

        if not root:
            return None
        first, last = dfs(root)
        first.left = last
        last.right = first
        return first
