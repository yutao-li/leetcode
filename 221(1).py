from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        dp = [0] * (len(matrix[0]) + 1)
        side = 0
        for row in matrix:
            dp1 = [0] * (len(matrix[0]) + 1)
            for j in range(len(matrix[0])):
                if row[j] == '1':
                    dp1[j + 1] = min(dp1[j], dp[j], dp[j + 1]) + 1
                    side = max(side, dp1[j + 1])
            dp = dp1
        return side ** 2
