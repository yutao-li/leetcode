class Solution:
    def maxScore(self, s: str) -> int:
        z = []
        o = []
        i = 0
        for ch in s[:-1]:
            if ch == '0':
                i += 1
            z.append(i)
        i = 0
        for ch in s[:0:-1]:
            if ch == '1':
                i += 1
            o.append(i)
        return max(a + b for a, b in zip(z, o[::-1]))


res = Solution().maxScore('1111')
