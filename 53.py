from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        t_sum = 0
        res = float('-inf')
        for num in nums:
            t_sum += num
            res = max(res, t_sum)
            if t_sum < 0:
                t_sum = 0
        return res
