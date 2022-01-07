from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[:] = nums[::-1]
            return
        j = i - 1
        i = len(nums) - 1
        while nums[i] <= nums[j]:
            i -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[:i:-1]


Solution().nextPermutation([1, 5, 1])
