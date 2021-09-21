from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(i for i in nums if i > 0))
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            elif nums[i] > len(nums):
                nums[i] = 0
                i += 1
            elif nums[i] < i + 1:
                nums[nums[i] - 1] = 1
                nums[i] = 0
                i += 1
            else:
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[tmp - 1] = tmp
        i = 0
        while i < len(nums) and nums[i]:
            i += 1
        return i + 1


print(Solution().firstMissingPositive([2, 4, 1]))
