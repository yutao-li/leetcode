from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        types = [1, 2, 3, 4]
        ft = [0] * (N + 1)
        adj = [[] for _ in range(N + 1)]
        for a, b in paths:
            adj[a].append(b)
            adj[b].append(a)
        for fl in range(1, N + 1):
            ts = [ft[i] for i in adj[fl]]
            for t in types:
                if t not in ts:
                    ft[fl] = t
                    break
        return ft[1:]


res = Solution().gardenNoAdj(N=4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]])
