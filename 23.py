from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])
        res = ListNode()
        cur = res
        while l1 and l2:
            cur.next = ListNode()
            cur = cur.next
            if l1.val > l2.val:
                cur.val = l2.val
                l2 = l2.next
            else:
                cur.val = l1.val
                l1 = l1.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return res.next
