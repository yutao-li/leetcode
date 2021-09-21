class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        md = int(1e9 + 7)
        dp = [[[0] * len(S) for _ in range(len(S))] for _ in range(4)]
        for i in range(len(S)):
            dp[ord(S[i]) - 97][i][i] = 1
        for i in range(len(S) - 2, -1, -1):
            for j in range(i + 1, len(S)):
                for c in range(4):
                    if ord(S[j]) - 97 != c:
                        dp[c][i][j] = dp[c][i][j - 1]
                    elif ord(S[i]) - 97 != c:
                        dp[c][i][j] = dp[c][i + 1][j]
                    else:
                        dp[c][i][j] = (2 + sum(dp[c1][i + 1][j - 1] for c1 in range(4))) % md
        return sum(dp[i][0][len(S) - 1] for i in range(4)) % md


print(Solution().countPalindromicSubsequences("bccb"))
