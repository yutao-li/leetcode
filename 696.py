class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        i = s.find('0')
        pre_one = i
        if i == -1:
            return 0
        while True:
            j = s.find('1', i + 1)
            if j == -1:
                return res + min(pre_one, n - i)
            res += min(pre_one, j - i)
            next_i = s.find('0', j + 1)
            if next_i == -1:
                return res + min(n - j, j - i)
            pre_one = next_i - j
            res += min(pre_one, j - i)
            i = next_i
