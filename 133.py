# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        n2c = dict()
        pool = [node]
        while pool:
            pool1 = []
            for n in pool:
                n2c[n] = Node(n.val)
                for neigh in n.neighbors:
                    if neigh not in n2c:
                        pool1.append(neigh)
            pool = pool1
        for n, cloned in n2c.items():
            cloned.neighbors = [n2c[i] for i in n.neighbors]
        return n2c[node]
