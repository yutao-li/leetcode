from typing import List, Optional


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.divide(lists)

    def divide(self, lists):
        if len(lists) == 1:
            return lists[0]
        elif len(lists) > 2:
            mid = len(lists) // 2
            l1 = self.divide(lists[:mid])
            l2 = self.divide(lists[mid:])
        else:
            l1 = lists[0]
            l2 = lists[1]
        merge = []
        i1 = 0
        i2 = 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] < l2[i2]:
                merge.append(l1[i1])
                i1 += 1
            else:
                merge.append(l2[i2])
                i2 += 1
        if i1 == len(l1):
            merge += l2[i2:]
        else:
            merge += l1[i1:]
        return merge


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        return self.divide(lists)

    def divide(self, lists):
        if len(lists) == 1:
            return lists[0]
        elif len(lists) > 2:
            mid = len(lists) // 2
            l1 = self.divide(lists[:mid])
            l2 = self.divide(lists[mid:])
        else:
            l1 = lists[0]
            l2 = lists[1]
        tmp = ListNode(0)
        start = tmp
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 is None:
            tmp.next = l2
        else:
            tmp.next = l1
        return start.next


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            l1, l2 = lists[0], lists[1]
        else:
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
