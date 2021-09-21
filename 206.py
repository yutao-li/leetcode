# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        for i in range(len(stack) - 1, 0, -1):
            stack[i].next = stack[i - 1]
        stack[0].next = None
        return stack[-1]
