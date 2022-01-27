from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1
        dp = [jobDifficulty[0]]
        stack = [0]
        compare = [[[], -1] for _ in range(n)]
        for i, j in enumerate(jobDifficulty[1:], 1):
            dp.append(max(dp[-1], j))
            while stack and jobDifficulty[stack[-1]] < j:
                compare[i][0].append(stack.pop())
            if stack:
                compare[i][1] = stack[-1]
            stack.append(i)
        for i in range(1, d):
            dp1 = [0] * n
            for j in range(i, n):
                dp1[j] = dp[j - 1] + jobDifficulty[j]
                while compare[j][0] and compare[j][0][-1] < i:
                    compare[j][0].pop()
                if compare[j][0]:
                    dp1[j] = min(dp1[j], min(dp1[k] - jobDifficulty[k] + jobDifficulty[j] for k in compare[j][0]))
                if compare[j][1] >= i:
                    dp1[j] = min(dp1[j], dp1[compare[j][1]])
            dp = dp1
        return dp[-1]


print(Solution().minDifficulty(jobDifficulty=[1, 1, 1], d=3))
