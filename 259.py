from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        ln = len(nums)
        for i, n in enumerate(nums):
            t = target - n
            right = ln - 1
            left = i + 1
            while left < right:
                if nums[left] + nums[right] < t:
                    res += right - left
                    left += 1
                else:
                    right -= 1
            if left == i + 1:
                break
        return res


print(Solution().threeSumSmaller([3, 1, 0, -2], 4))
