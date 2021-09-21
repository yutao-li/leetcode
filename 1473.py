from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {(houses[0], 1): 0} if houses[0] else {(i, 1): j for i, j in enumerate(cost[0], start=1)}
        for h in range(1, m):
            dp1 = dict()
            candi = [(houses[h], 0)] if houses[h] else [(i, j) for i, j in enumerate(cost[h], start=1)]
            for col, cos in candi:
                for (col1, t1), c1 in dp.items():
                    new_t = t1 + (col != col1)
                    if new_t > target or new_t + m - 1 - h < target:
                        continue
                    if (col, new_t) not in dp1:
                        dp1[col, new_t] = c1 + cos
                    else:
                        dp1[col, new_t] = min(dp1[col, new_t], c1 + cos)
            dp = dp1
        return min((c for _, c in dp.items()), default=-1)


res = Solution().minCost([2, 3, 0], [[5, 2, 3], [3, 4, 1], [1, 2, 1]], 3, 3, 3)
