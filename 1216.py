class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def remove(s: str, i: int, j: int):
            if j == k:
                return s == s[::-1]
            for m in range(i, len(s)):
                if (m == i or s[m] != s[m - 1]) and remove(s[:m] + s[m + 1:], m, j + 1):
                    return True
            return s == s[::-1]

        return remove(s, 0, 0)
