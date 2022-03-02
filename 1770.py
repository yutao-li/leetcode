from functools import lru_cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(None)
        def dp(begin, end):
            im = begin + ln - 1 - end
            if im == lm - 1:
                return max(multipliers[im] * nums[begin], multipliers[im] * nums[end])
            return max(multipliers[im] * nums[begin] + dp(begin + 1, end),
                       multipliers[im] * nums[end] + dp(begin, end - 1))

        ln = len(nums)
        lm = len(multipliers)
        return dp(0, ln - 1)


class Solution1:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        lm = len(multipliers)
        dp = [0] * (lm + 1)
        for im in range(lm - 1, -1, -1):
            dp = [max(multipliers[im] * nums[i] + dp[i + 1], multipliers[im] * nums[-im - 1 + i] + dp[i]) for i in
                  range(im + 1)]
        return dp[0]


print(Solution1().maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]))
