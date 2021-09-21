from functools import lru_cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def dfs(dice, t):
            res = 0
            if dice == d - 1:
                return int(t <= f)
            for i in range(1, min(t, f + 1)):
                res += dfs(dice + 1, t - i)
            return res

        return dfs(0, target) % (10 ** 9 + 7)


res = Solution().numRollsToTarget(d=30, f=30, target=500)

