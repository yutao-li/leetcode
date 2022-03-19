# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node.left:
                dfs(node.left)
            nodes.append(node)
            if node.right:
                dfs(node.right)

        def build_tree(i, j):
            if i > j:
                return None
            else:
                mid = (i + j) // 2
                nodes[mid].left = build_tree(i, mid - 1)
                nodes[mid].right = build_tree(mid + 1, j)
                return nodes[mid]

        nodes = []
        dfs(root)
        return build_tree(0, len(nodes) - 1)
