from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def helper(i, j):
            if j == len(p):
                return i == len(s)
            match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                return helper(i, j + 2) or (match and helper(i + 1, j))
            else:
                return match and helper(i + 1, j + 1)

        return helper(0, 0)


print(Solution().isMatch("aa", 'a'))
