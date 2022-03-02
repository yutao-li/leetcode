from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)
        n = len(s)
        res = 0
        for indices in pos.values():
            for i, j, k in zip([-1] + indices, indices, indices[1:] + [n]):
                res += (j - i) * (k - j)
        return res
