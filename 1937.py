from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0]
        n = len(dp)
        for row in points[1:]:
            leftMax = [0] * n
            rightMax = [0] * n
            leftMax[0] = dp[0]
            for i in range(1, n):
                leftMax[i] = max(leftMax[i - 1] - 1, dp[i])
            rightMax[-1] = dp[-1]
            for i in range(n - 2, -1, -1):
                rightMax[i] = max(rightMax[i + 1] - 1, dp[i])
            dp = [num + max(leftMax[i], rightMax[i]) for i, num in enumerate(row)]
        return max(dp)
