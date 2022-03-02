from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = len(nums) - 1
        res = -1
        left = 0
        while left < right:
            while right > left and nums[left] + nums[right] >= k:
                right -= 1
            if right == left:
                break
            res = max(res, nums[left] + nums[right])
            left += 1
        return res
