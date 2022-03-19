from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val <= high:
                return node.val + dfs(node.left) + dfs(node.right)
            else:
                return dfs(node.left)

        return dfs(root)


class Solution1:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sum_tree(node):
            if not node:
                return 0
            pool = [node]
            res = 0
            while pool:
                pool1 = []
                for n in pool:
                    res += n.val
                    if n.left:
                        pool1.append(n.left)
                    if n.right:
                        pool1.append(n.right)
                pool = pool1
            return res

        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                break
        if not root:
            return 0
        res = root.val
        node = root.left
        while node:
            if node.val >= low:
                res += node.val + sum_tree(node.right)
                node = node.left
            else:
                node = node.right
        node = root.right
        while node:
            if node.val <= high:
                res += node.val + sum_tree(node.left)
                node = node.right
            else:
                node = node.left
        return res
