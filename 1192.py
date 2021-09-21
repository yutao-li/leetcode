from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        res = []
        discover = [0] * n

        def dfs(prev, cur_node):
            cur = discover[cur_node] = discover[prev] + 1
            for nb in adj[cur_node]:
                if nb != prev:
                    if not discover[nb]:
                        dfs(cur_node, nb)
                    if discover[nb] < cur:
                        cur = discover[nb]
            discover[cur_node] = cur
            if cur == discover[prev] + 1:
                res.append([prev, cur_node])

        dfs(0, 0)
        return res


print(Solution().criticalConnections(10,
                                     [[1, 0], [2, 0], [3, 0], [4, 1], [5, 3], [6, 1], [7, 2], [8, 1], [9, 6], [9, 3],
                                      [3, 2], [4, 2], [7, 4], [6, 2], [8, 3], [4, 0], [8, 6], [6, 5], [6, 3], [7, 5],
                                      [8, 0], [8, 5], [5, 4], [2, 1], [9, 5], [9, 7], [9, 4], [4, 3]]))
