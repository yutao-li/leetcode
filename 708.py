from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal, None)
            node.next = node
            return node
        begin = head.next
        end = head
        while begin.val >= end.val and begin != head:
            end = begin
            begin = begin.right
        if begin.val == end.val or insertVal <= begin.val or insertVal >= end.val:
            cur = begin
            pre = end
        else:
            pre = begin
            cur = begin.right
            while cur.val < insertVal:
                pre = cur
                cur = cur.right
        node = Node(insertVal, cur)
        pre.next = node
        return head
