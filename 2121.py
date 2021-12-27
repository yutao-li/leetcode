from collections import defaultdict
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i, n in enumerate(arr):
            pos[n].append(i)
        res = [0] * len(arr)
        for v in pos.values():
            res[v[0]] = sum(abs(v[0] - i) for i in v)
            for i, (p, pre) in enumerate(zip(v[1:], v), 1):
                res[p] = res[pre] + (2 * i - len(v)) * (p - pre)
        return res
