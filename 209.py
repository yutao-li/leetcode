from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = len(nums) + 1
        left = 0
        right = -1
        su = 0
        while right < len(nums) - 1:
            if su < s:
                right += 1
                if nums[right] >= s:
                    return 1
                su += nums[right]
            if su >= s:
                while su >= s:
                    su -= nums[left]
                    left += 1
                length = min(length, right - left + 2)
        return length if length != len(nums) + 1 else 0


print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
