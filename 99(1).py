# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x = y = pred = None
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if pre.right is None:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    if pred and pred.val > root.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root
                    root = root.right
            else:
                if pred and pred.val > root.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val
