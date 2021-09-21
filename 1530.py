# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node, depth):
            if node.left and node.right:
                l1, c1 = dfs(node.left, depth + 1)
                l2, c2 = dfs(node.right, depth + 1)
                count = c1 + c2
                l = l1 + l2
                for n1, d1 in l1:
                    for n2, d2 in l2:
                        if d1 + d2 - 2 * depth <= distance:
                            count += 1
            elif node.left:
                l, count = dfs(node.left, depth + 1)
            elif node.right:
                l, count = dfs(node.right, depth + 1)
            else:
                l, count = [(node, depth)], 0
            return l, count

        if not root:
            return 0
        return dfs(root, 0)[1]

