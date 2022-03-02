from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find_root(node):
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node

        def union(node1, node2):
            if height[node1] > height[node2]:
                root[node2] = node1
            elif height[node2] < height[node1]:
                root[node1] = node2
            else:
                root[node1] = node2
                height[node1] += 1

        if len(edges) != n - 1:
            return False
        root = list(range(n))
        height = [0] * n
        for i, j in edges:
            i = find_root(i)
            j = find_root(j)
            if i == j:
                return False
            union(i, j)
        return True
