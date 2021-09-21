class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        mid, radius = 0, 0
        i = 0
        while i + radius + 1 < len(s):
            if s[i - radius:i] == s[i + radius:i:-1]:
                while i - radius - 1 >= 0 and i + radius + 1 < len(s) and s[i - radius - 1] == s[i + radius + 1]:
                    radius += 1
                mid = i
            i += 1
        mid1, radius1 = 0, radius
        i = radius
        while i + radius1 < len(s):
            if s[i - radius1:i] == s[i + radius1 - 1:i - 1:-1]:
                while i - radius1 - 1 >= 0 and i + radius1 < len(s) and s[i - radius1 - 1] == s[i + radius1]:
                    radius1 += 1
                mid1 = i
            i += 1
        if radius >= radius1:
            return s[mid - radius:mid + radius + 1]
        else:
            return s[mid1 - radius1:mid1 + radius1]


print(Solution().longestPalindrome('babad'))
