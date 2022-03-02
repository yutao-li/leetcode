from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cur = ones - sum(data[:ones])
        res = cur
        for i, j in zip(data, data[ones:]):
            cur = cur + i - j
            res = min(res, cur)
        return res
