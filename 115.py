from bisect import bisect_right
from collections import defaultdict
from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)
        if t[0] not in pos:
            return 0
        prev = [1] * len(pos[t[0]])
        for ch, pre_ch in zip(t[1:], t):
            if ch not in pos:
                return 0
            j = 0
            k = 0
            next = []
            count = 0
            while k < len(pos[ch]) and j < len(pos[pre_ch]):
                while j < len(pos[pre_ch]) and pos[pre_ch][j] < pos[ch][k]:
                    count += prev[j]
                    j += 1
                next.append(count)
                k += 1
            if next[-1] == 0:
                return 0
            prev = next + [next[-1]] * (len(pos[ch]) - k)
        return sum(prev)


class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        lpos = defaultdict(list)
        for p1, ch in enumerate(s):
            lpos[ch].append(p1)
        if any(not lpos[i] for i in t):
            return 0
        c = {i: 1 for i in lpos[t[0]]}
        for ch in t[1:]:
            pos = list(c.keys())
            pos1 = lpos[ch][bisect_right(lpos[ch], pos[0]):]
            if not pos1:
                return 0
            for i, j in zip(pos, pos[1:]):
                c[j] += c[i]
            c1 = {}
            i = 0
            for p in pos1:
                while i + 1 < len(pos) and pos[i + 1] < p:
                    i += 1
                c1[p] = c[pos[i]]
            c = c1
        return sum(c.values())


# much better
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dp(i, j) -> int:
            if len(s) - i == len(t) - j:
                return int(s[i:] == t[j:])
            elif j == len(t):
                return 1
            elif s[i] == t[j]:
                return dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                return dp(i + 1, j)

        s = ''.join(i for i in s if i in set(t))
        if len(s) < len(t):
            return 0
        return dp(0, 0)


print(Solution().numDistinct('babgbag', 'bag'))
