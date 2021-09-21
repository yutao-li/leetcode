from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        i, j, k = 0, 0, 0
        for a, b, c in costs:
            i, j, k = a + min(j, k), b + min(i, k), c + min(i, j)
        return min(i, j, k)


res = Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]])
