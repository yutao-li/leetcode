class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return s[left + 1:right + 1] == s[right:left:-1] or s[left:right] == s[right - 1:left - 1 if left else None:-1]


print(Solution().validPalindrome(
    s="eccer"))
