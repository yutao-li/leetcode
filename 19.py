from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        i = len(stack) - n
        if i == 0:
            node = head.next
            head.next = None
            head = node
        elif i == len(stack) - 1:
            stack[-2].next = None
        else:
            stack[i - 1].next = stack[i + 1]
            stack[i].next = None
        return head


# O(1) space
class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        for _ in range(n):
            first = first.next
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
