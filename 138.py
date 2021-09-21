# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        m = dict()
        tmp = head
        while tmp:
            m[tmp] = Node(tmp.val)
            tmp = tmp.next
        tmp = head
        while tmp:
            if tmp.next:
                m[tmp].next = m[tmp.next]
            if tmp.random:
                m[tmp].random = m[tmp.random]
            tmp = tmp.next
        return m[head]
