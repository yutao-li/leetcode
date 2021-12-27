from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums, 1):
            while 0 < n <= len(nums) and n != i and nums[n - 1] != n:
                nums[n - 1], n = n, nums[n - 1]
            if n != i:
                nums[i - 1] = 0
        for i, n in enumerate(nums, 1):
            if n == 0:
                return i
        return len(nums) + 1


print(Solution().firstMissingPositive([2, 4, 1]))
