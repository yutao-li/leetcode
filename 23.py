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
    def __init__(self, x):
        self.val = x
        self.next = None


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
