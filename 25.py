from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head:
            return head
        right = head
        pre_end = None
        while right:
            left = right
            for _ in range(k - 1):
                right = right.next
                if not right:
                    if pre_end:
                        pre_end.next = left
                    return head
            if pre_end:
                pre_end.next = right
            else:
                head = right
            pre_end = left
            pre = left
            cur = left.next
            while cur != right:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            right = right.next
            cur.next = pre
        pre_end.next = None
        return head


class Solution1:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        tail = res
        while head:
            stack = []
            for _ in range(k):
                if not head:
                    tail.next = stack[0]
                    return res.next
                stack.append(head)
                head = head.next
            for _ in range(k):
                tail.next = stack.pop()
                tail = tail.next
        tail.next = None
        return res.next


nodes = [ListNode(i) for i in range(1, 3)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
res = Solution().reverseKGroup(nodes[0], 2)
