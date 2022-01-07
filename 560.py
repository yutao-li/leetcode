from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc = 0
        d = defaultdict(int)
        d[0] = 1
        res = 0
        for n in nums:
            acc += n
            if acc - k in d:
                res += d[acc - k]
            d[acc] += 1
        return res


print(Solution().subarraySum(nums=[1, 2, 3], k=3))
