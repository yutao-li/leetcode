from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        mdp = [[0] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            mdp[i][i] = arr[i]
            for j in range(i + 1, len(arr)):
                mdp[i][j] = max(arr[j], mdp[i][j - 1])
        dp = [[0] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr) - 2, -1, -1):
            for j in range(i + 1, len(arr)):
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] + mdp[i][k] * mdp[k + 1][j] for k in range(i, j))
        return dp[0][len(arr) - 1]


res = Solution().mctFromLeafValues([6, 2, 4])
