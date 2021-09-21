from functools import lru_cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @lru_cache(None)
        def dfs(pre, pos, k):
            if k == 0:
                return pre**(n - pos) % modu
            if n - pos < k or m - pre < k:
                return 0
            if pos == n - 1:
                return m - pre
            return (pre * dfs(pre, pos + 1, k) + sum(dfs(i, pos + 1, k - 1) for i in range(pre + 1, m + 1))) % modu

        if k > m or k < 1:
            return 0
        modu = 10**9+7
        return sum(dfs(i, 1, k - 1) for i in range(1, m + 1)) % modu


res = Solution().numOfArrays(50, 100, 25)
