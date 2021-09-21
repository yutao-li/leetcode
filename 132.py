class Solution:
    def minCut(self, s: str) -> int:
        cut = list(range(len(s)))
        for i in range(len(s)):
            cut[i] = min(cut[i], 1 + (cut[i - 1] if i - 1 >= 0 else -1))
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                cut[i + j] = min(cut[i + j], (cut[i - j - 1] if i - j - 1 >= 0 else -1) + 1)
                j += 1
            j = 1
            while i - j + 1 >= 0 and i + j < len(s) and s[i - j + 1] == s[i + j]:
                cut[i + j] = min(cut[i + j], (cut[i - j] if i - j >= 0 else -1) + 1)
                j += 1
        return cut[-1]


print(Solution().minCut('aab'))
