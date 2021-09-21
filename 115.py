from collections import defaultdict


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


print(Solution().numDistinct('babgbag', 'bag'))
