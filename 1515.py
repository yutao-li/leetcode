from typing import List
from random import uniform
import math


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def norm(a, b):
            return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

        if len(positions) == 1:
            return 0
        cur = [uniform(0, 100), uniform(0, 100)]
        ans = sum(norm(cur, p) for p in positions)
        change = 1
        while change > 5e-7:
            num = [0, 0]
            den = 0
            for p in positions:
                dist = norm(p, cur)
                if dist == 0:
                    return 0
                num[0] += p[0] / dist
                num[1] += p[1] / dist
                den += 1 / dist
            cur = [num[0] / den, num[1] / den]
            ans1 = sum(norm(cur, p) for p in positions)
            change = ans - ans1
            ans = ans1
        return ans
