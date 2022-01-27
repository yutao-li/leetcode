from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        for i, j in zip([lower - 1] + nums, nums + [upper + 1]):
            if i + 1 < j - 1:
                res.append(str(i + 1) + "->" + str(j - 1))
            elif i + 1 == j - 1:
                res.append(str(i + 1))
        return res
