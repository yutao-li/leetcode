from typing import List
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        prod = 1
        c = Counter(nums)
        for v in c.values():
            prod *= v + 1
        res = [[]]
        for i in range(1, prod):
            nums = []
            for k, v in c.items():
                i, r = divmod(i, v + 1)
                if r:
                    nums += [k] * r
                if i == 0:
                    break
            res.append(nums)
        return res


res = Solution().subsetsWithDup([1, 2, 2])
