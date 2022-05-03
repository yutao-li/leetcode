from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(i1, i2):
            if i1 == n1:
                return s2[i2:] == s3[i1 + i2:]
            if i2 == n2:
                return s1[i1:] == s3[i1 + i2:]
            if s1[i1] == s3[i1 + i2] and dp(i1 + 1, i2):
                return True
            if s2[i2] == s3[i1 + i2] and dp(i1, i2 + 1):
                return True
            return False

        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        return dp(0, 0)


class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [True] * (n2 + 1)
        for i2 in range(n2 - 1, -1, -1):
            dp[i2] = s2[i2] == s3[n1 + i2] and dp[i2 + 1]
        for i1 in range(n1 - 1, -1, -1):
            dp[n2] = dp[n2] and s1[i1] == s3[i1 + n2]
            for i2 in range(n2 - 1, -1, -1):
                dp[i2] = s1[i1] == s3[i1 + i2] and dp[i2] or s2[i2] == s3[i1 + i2] and dp[i2 + 1]
        return dp[0]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(Solution().isInterleave(s1, s2, s3))
