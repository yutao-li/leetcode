# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs1(node):
            if node.left and node.right:
                node.level = 1 + max(dfs1(node.left), dfs1(node.right))
            elif node.left:
                node.level = 1 + dfs1(node.left)
            elif node.right:
                node.level = 1 + dfs1(node.right)
            else:
                node.level = 0
            return node.level

        def dfs2(node):
            if node.left and node.right:
                if node.left.level == node.right.level:
                    return node
                elif node.left.level > node.right.level:
                    return dfs2(node.left)
                else:
                    return dfs2(node.right)
            elif node.left:
                return dfs2(node.left)
            elif node.right:
                return dfs2(node.right)
            else:
                return node

        if not root:
            return root
        dfs1(root)
        return dfs2(root)

