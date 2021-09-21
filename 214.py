class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        pos = [-1] * (len(s) // 2)
        for i in range(1, len(pos)):
            j = pos[i - 1]
            while j != -1 and s[i - 1] != s[j]:
                j = pos[j]
            pos[i] = j + 1
        for i in range(1, len(pos)):
            while s[i] == s[pos[i]] and pos[i] != -1:
                pos[i] = pos[pos[i]]
        j = 0
        i = len(s) - 1
        while j < len(pos) and j < i:
            if j == -1:
                j = 0
                i -= 1
            elif s[j] == s[i]:
                i -= 1
                j += 1
            else:
                j = pos[j]
        le = j * 2 + 1 if j == i else 2 * j
        return s[le:][::-1] + s


print(Solution().shortestPalindrome('abcd'))
