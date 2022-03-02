from collections import defaultdict
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        def dfs(i):
            layer[i] = -1
            max_l = 0
            for j in dep[i]:
                if layer[j] == -1:
                    return False
                if layer[j] == 0:
                    if not dfs(j):
                        return False
                max_l = max(max_l, layer[j])
            layer[i] = 1 + max_l
            return True

        dep = defaultdict(list)
        for i, j in relations:
            dep[i].append(j)
        layer = [0] * (n + 1)
        for i in range(1, n + 1):
            if layer[i] == 0:
                if not dfs(i):
                    return -1
        return max(layer)


print(Solution().minimumSemesters(n=3, relations=[[1, 2], [2, 3], [3, 1]]))
