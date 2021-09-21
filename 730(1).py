class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        md = int(1e9) + 7
        S = [ord(ch) - 97 for ch in S]
        num_ch = 4
        dp = [[0] * len(S) for _ in range(len(S))]
        for i in range(len(S)):
            dp[i][i] = 1
        next_pos = [[len(S)] * num_ch for _ in range(len(S))]
        cur = [0] * num_ch
        for i, ch in enumerate(S):
            for j in range(cur[ch], i):
                next_pos[j][ch] = i
            cur[ch] = i
        rev_next_pos = [[-1] * num_ch for _ in range(len(S))]
        cur = [len(S) - 1] * num_ch
        for i in range(len(S) - 1, -1, -1):
            ch = S[i]
            for j in range(cur[ch], i, -1):
                rev_next_pos[j][ch] = i
            cur[ch] = i
        for i in range(len(S) - 2, -1, -1):
            for j in range(i + 1, len(S)):
                if S[i] == S[j]:
                    low = next_pos[i][S[i]]
                    high = rev_next_pos[j][S[i]]
                    if low > high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif low == high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                dp[i][j] = dp[i][j] + md if dp[i][j] < 0 else dp[i][j] % md
        return dp[0][-1]


print(Solution().countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
