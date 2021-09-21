class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        s = [ord(c) for c in s]
        diff = abs(ord('a') - ord('A'))
        while i < len(s) - 1:
            if abs(s[i] - s[i + 1]) == diff:
                s.pop(i)
                s.pop(i)
                if i > 0:
                    i -= 1
            else:
                i += 1
        return ''.join(chr(i) for i in s)


res = Solution().makeGood(s="leEeetcode")

