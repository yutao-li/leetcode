# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = {p, q}
        while True:
            if p.parent:
                p = p.parent
                if p in visited:
                    return p
                visited.add(p)
            if q.parent:
                q = q.parent
                if q in visited:
                    return q
                visited.add(q)
