class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            q, r = divmod(i - 1, 2)
            for j in range(q):
                dp[i] += dp[j] * dp[i - 1 - j]
            dp[i] *= 2
            dp[i] += (r + 1) * dp[i - 1 - q] * dp[q]
        return dp[-1]


res = Solution().numTrees(3)
