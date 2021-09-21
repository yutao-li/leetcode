from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        if len(costs[0]) == 1:
            return costs[0][0]
        res = [0] * len(costs[0])
        first, second = 0, 0
        for row in costs:
            res1 = [0] * len(costs[0])
            for i, j in enumerate(row):
                res1[i] = (res[first] if i != first else res[second]) + j
            res = res1
            first, second = (0, 1) if res[0] < res[1] else (1, 0)
            for i, j in enumerate(res[2:], start=2):
                if j <= res[first]:
                    first, second = i, first
                elif j < res[second]:
                    second = i
        return res[first]


res = Solution().minCostII([[1, 5, 3], [2, 9, 4]])
