# https://leetcode.com/discuss/interview-question/873231/docasap-stage-online-group-division
from typing import List


class Solution:
    def minClasses(self, levels: List[int], maxSpread: int) -> int:
        levels.sort()
        res = 0
        i = 0
        n = len(levels)
        while i < n:
            m = levels[i] + maxSpread
            while i < n and levels[i] < m:
                i += 1
            res += 1
        return res
