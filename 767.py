from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        s = Counter(s)
        ch, freq = s.most_common(1)[0]
        if 2 * freq - 1 > n:
            return ''
        res = [0] * n
        for i in range(freq):
            res[2 * i] = ch
        i = 2 * freq
        del s[ch]
        for ch, freq in s.items():
            for _ in range(freq):
                if i >= n:
                    i = 1
                res[i] = ch
                i += 2
        return ''.join(res)


print(Solution().reorganizeString(s="aab"))
