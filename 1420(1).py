class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for _ in range(n):
            dp1 = [[0] * (k + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(k + 1):
                    dp1[i][j] = i * dp[i][j]
                    if j > 0:
                        dp1[i][j] += sum(dp[pre][j - 1] for pre in range(i + 1, m + 1))
            dp = dp1
        return dp[0][k] % (10 ** 9 + 7)


res = Solution().numOfArrays(50, 100, 25)
