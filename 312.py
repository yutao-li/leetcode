from typing import List
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(left, right):
            if left + 1 == right:
                return 0
            else:
                return max((nums[left] if left >= 0 else 1) * (nums[right] if right < len(nums) else 1) * n +
                           dp(left, i) + dp(i, right) for i, n in enumerate(nums[left + 1:right], left + 1))

        return dp(-1, len(nums))


print(Solution().maxCoins([3, 1, 5, 8]))
