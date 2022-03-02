from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        diff = float('inf')
        nums.sort()
        ln = len(nums)
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            t = target - n
            left = i + 1
            right = ln - 1
            while left < right:
                diff1 = abs(t - nums[right] - nums[left])
                if diff > diff1:
                    if diff1 == 0:
                        return target
                    diff = diff1
                    res = n + nums[right] + nums[left]
                if nums[right] + nums[left] < t:
                    left += 1
                else:
                    right -= 1
            if left == i + 1:
                break
        return res


print(Solution().threeSumClosest([0, 2, 1, -3], 1))
