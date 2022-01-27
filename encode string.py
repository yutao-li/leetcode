# https://leetcode.com/discuss/interview-question/1010329/goldman-sachs-online-encode-string

class Solution:
    def decode(self, s: str):
        res = [0] * 26
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                n = int(s[i:i + 2]) - 1
                i += 3
            else:
                n = int(s[i]) - 1
                i += 1
            if i < len(s) and s[i] == '(':
                j = s.find(')', i + 1)
                res[n] += int(s[i + 1:j])
                i = j + 1
            else:
                res[n] += 1
        return res


print(Solution().decode("1226#24#"))
