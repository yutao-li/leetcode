class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        ori = s[:]
        s = s + '#' + s[::-1]
        pos = [-1] * (len(s) + 1)
        for i in range(1, len(pos)):
            j = pos[i - 1]
            while j != -1 and s[i - 1] != s[j]:
                j = pos[j]
            pos[i] = j + 1
        return ori[pos[-1]:][::-1] + ori


print(Solution().shortestPalindrome('abcd'))
