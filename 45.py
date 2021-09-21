from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = [0, nums[0]]
        while step[-1] < len(nums) - 1:
            step.append(max(j + nums[j] for j in range(step[-2] + 1, step[-1] + 1)))
        return len(step) - 1


res = Solution().jump([2, 3, 1, 1, 4])
