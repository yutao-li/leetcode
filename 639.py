class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1] * len(s)
        if s[0] == '*':
            dp[0] = 9
        elif s[0] == '0':
            dp[0] = 0
        for i in range(1, len(s)):
            if s[i - 1] == '*':
                if s[i] == '*':
                    dp[i] = dp[i - 1] * 9 + 15 * dp[i - 2]
                elif '1' <= s[i] <= '6':
                    dp[i] = dp[i - 1] + 2 * dp[i - 2]
                elif s[i] == '0':
                    dp[i] = 2 * dp[i - 2]
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]
            elif s[i - 1] == '1':
                if s[i] == '*':
                    dp[i] = dp[i - 1] * 9 + 9 * dp[i - 2]
                elif s[i] == '0':
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]
            elif s[i - 1] == '2':
                if s[i] == '*':
                    dp[i] = dp[i - 1] * 9 + 6 * dp[i - 2]
                elif s[i] == '0':
                    dp[i] = dp[i - 2]
                elif '1' <= s[i] <= '6':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
            else:
                if s[i] == '*':
                    dp[i] = dp[i - 1] * 9
                elif s[i] == '0':
                    dp[i] = 0
                else:
                    dp[i] = dp[i - 1]
            dp[i] %= 1e9 + 7
        return int(dp[-1])


print(Solution().numDecodings("0"))
