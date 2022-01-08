from random import randrange
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        left = 0
        right = len(nums) - 1
        while True:
            i = randrange(left, right + 1)
            nums[i], nums[left] = nums[left], nums[i]
            i = left + 1
            j = right
            while i <= j:
                if nums[i] < nums[left]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    i += 1
            nums[left], nums[i - 1] = nums[i - 1], nums[left]
            if i - 1 == k:
                return nums[i - 1]
            elif i - 1 > k:
                right = i - 2
            else:
                left = i


print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
