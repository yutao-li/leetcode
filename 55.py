from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            if i + nums[i] >= len(nums) - 1:
                return True
            reach = max(i + nums[i], reach)
        return False


res = Solution().canJump([3, 2, 1, 0, 4])
