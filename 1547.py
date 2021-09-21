from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def dfs(left, right):
            if right - left == 1:
                return 0
            else:
                return cuts[right] - cuts[left] + min(dfs(left, i) + dfs(i, right) for i in range(left + 1, right))

        cuts = [0] + sorted(cuts) + [n]
        return dfs(0, len(cuts) - 1)


res = Solution().minCost(n=9, cuts=[5, 6, 1, 4, 2])
