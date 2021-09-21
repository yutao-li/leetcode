class Solution:
    def numSub(self, s: str) -> int:
        w = []
        i = 0
        while i < len(s):
            if s[i] != '1':
                i += 1
            else:
                j = i + 1
                while j < len(s) and s[j] == '1':
                    j += 1
                w.append(j - i)
                i = j + 1
        return sum(i * (i + 1) // 2 for i in w) % (10 ** 9 + 7)



