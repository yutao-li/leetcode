class Solution:
    def numDecodings(self, s: str) -> int:
        a0, a1, c1 = 0, 1, ''
        for ch in s[::-1]:
            if ch != '0':
                if int(ch + c1) <= 26:
                    a2 = a0 + a1
                else:
                    a2 = a1
            else:
                a2 = 0
            a1, a0, c1 = a2, a1, ch
            if a1 == a0 == 0:
                return 0
        return a1


res = Solution().numDecodings('226')
