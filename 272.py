from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def pre_stack_pop():
            node = pre_stack.pop()
            res.append(node.val)
            node = node.left
            while node:
                pre_stack.append(node)
                node = node.right

        def post_stack_pop():
            node = post_stack.pop()
            res.append(node.val)
            node = node.right
            while node:
                post_stack.append(node)
                node = node.left

        pre_stack, post_stack = [], []
        node = root
        while node:
            if node.val == target:
                pre_stack.append(node)
                break
            elif node.val > target:
                node = node.left
            else:
                pre_stack.append(node)
                node = node.right
        node = root
        while node:
            if node.val == target:
                post_stack.append(node)
                break
            elif node.val > target:
                post_stack.append(node)
                node = node.left
            else:
                node = node.right
        res = []
        if pre_stack and pre_stack[-1].val == target:
            pre_stack_pop()
            res = []
        while k and pre_stack and post_stack:
            if target - pre_stack[-1].val < post_stack[-1].val - target:
                pre_stack_pop()
            else:
                post_stack_pop()
            k -= 1
        if k:
            if pre_stack:
                for _ in range(k):
                    pre_stack_pop()
            else:
                for _ in range(k):
                    post_stack_pop()
        return res
