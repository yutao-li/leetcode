class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0
        if target > d * (1 + f) / 2:
            target = d * (1 + f) - target
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(d):
            tmp = [0] * (target + 1)
            for i in range(1, target + 1):
                tmp[i] = tmp[i - 1] + dp[i - 1]
                if i - f - 1 >= 0:
                    tmp[i] -= dp[i - f - 1]
            dp = tmp
        return dp[-1] % (10 ** 9 + 7)


res = Solution().numRollsToTarget(d=30, f=30, target=500)
