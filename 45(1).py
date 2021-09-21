from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i, j, k = 0, nums[0], 1
        while j < len(nums) - 1:
            i, j, k = j, max(j + nums[j] for j in range(i + 1, j + 1)), k + 1
        return k


res = Solution().jump([2, 3, 1, 1, 4])
