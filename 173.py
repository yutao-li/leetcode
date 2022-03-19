from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        node = root
        while node:
            self.nodes.append(node)
            node = node.left

    def next(self) -> int:
        node = self.nodes.pop()
        child = node.right
        while child:
            self.nodes.append(child)
            child = child.left
        return node.val

    def hasNext(self) -> bool:
        return bool(self.nodes)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
