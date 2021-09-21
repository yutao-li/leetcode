from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_dist_le(n):
            i, j = 0, 0
            res = 0
            while i < len(nums):
                if j + 1 < len(nums) and nums[j + 1] - nums[i] <= n:
                    j += 1
                else:
                    res += j - i
                    i += 1
            return res

        nums.sort()
        low, high = 0, max(nums) - min(nums)
        while low < high:
            mid = (low + high) // 2
            if count_dist_le(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return high


print(Solution().smallestDistancePair([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18))
