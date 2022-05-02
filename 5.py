class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        n = len(s)
        maxPalindrome = ''
        for i in range(n):
            palindrome = expand(i, i)
            if len(palindrome) > len(maxPalindrome):
                maxPalindrome = palindrome
            palindrome = expand(i, i + 1)
            if len(palindrome) > len(maxPalindrome):
                maxPalindrome = palindrome
        return maxPalindrome


# manacher's algorithm
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        s = '|' + '|'.join(s) + '|'
        n = len(s)
        center = 0
        palindromeRadius = [0] * n
        radius = 0
        while center < n:
            while center - (radius + 1) >= 0 and center + radius + 1 < n and s[center - (radius + 1)] == s[
                center + radius + 1]:
                radius += 1
            palindromeRadius[center] = radius
            oldCenter = center
            rightBound = center + radius
            center += 1
            radius = 0
            while center <= rightBound:
                mirroredCenter = oldCenter - (center - oldCenter)
                maxRadius = rightBound - center
                palindromeRadius[center] = min(maxRadius, palindromeRadius[mirroredCenter])
                if maxRadius == palindromeRadius[mirroredCenter]:
                    radius = maxRadius
                    break
                else:
                    center += 1
        i = max(range(n), key=lambda x: palindromeRadius[x])
        longest = s[i - palindromeRadius[i]:i + palindromeRadius[i] + 1]
        return longest.replace('|', '')


print(Solution1().longestPalindrome('babad'))
