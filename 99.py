# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # iterative inorder traversal
        stack = []
        pred = None
        x = y = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and pred.val > root.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val
