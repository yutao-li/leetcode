from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        seen = {0}
        acc = 0
        for n in nums:
            acc += n
            if acc - target in seen:
                res += 1
                seen = {0}
                acc = 0
            else:
                seen.add(acc)
        return res


res = Solution().maxNonOverlapping(nums = [-2,6,6,3,5,4,1,2,8], target = 10)
