class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        # weight = [1] * len(s)
        # i = 0
        # while i < len(s) - 1:
        #     if s[i] == '(' and s[i + 1] == ')':
        #         weight[i] = 2
        #         s = s[:i] + '|' + s[i + 2:]
        #         weight.pop(i + 1)
        #         i -= 1
        #     elif i < len(s) - 2 and s[i] == '(' and s[i + 1] == '|' and s[i + 2] == ')':
        #         weight[i] = 2 + weight[i + 1]
        #         s = s[:i] + '|' + s[i + 3:]
        #         weight.pop(i + 1)
        #         weight.pop(i + 1)
        #         i -= 1
        #     elif s[i] == '|' and s[i + 1] == '|':
        #         weight[i] += weight[i + 1]
        #         s = s[:i] + '|' + s[i + 2:]
        #         weight.pop(i + 1)
        #         i -= 1
        #     else:
        #         i += 1
        #     if i < 0:
        #         i = 0
        # ma = max(weight)
        # if ma == 1:
        #     ma = 0
        # return ma
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = 2 + dp[i - 2]
            elif s[i] == ')' and dp[i - 1] != 0:
                index = i - dp[i - 1] - 1
                if index >= 0 and s[index] == '(':
                    dp[i] = dp[i - 1] + 2
                    if index >= 1:
                        dp[i] += dp[index - 1]
        return max(dp)


print(Solution().longestValidParentheses("("))
print(Solution().longestValidParentheses("))())()()())))"))
