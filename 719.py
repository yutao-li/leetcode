from collections import Counter
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_dist_le(n):
            i, j = 0, 0
            res = 0
            while j + 1 < len(nums):
                if nums[j + 1] - nums[i] <= n:
                    j += 1
                elif j > i:
                    res += counts[nums[i]] * sum((counts[nums[m]] for m in range(i + 1, j + 1)))
                    i += 1
                else:
                    j = i = i + 1
            if i < len(nums) - 1:
                for m in range(i, len(nums) - 1):
                    res += counts[nums[m]] * sum((counts[nums[o]] for o in range(m + 1, len(nums))))
            return res

        def count_dist_le1(n):
            i, j = 0, 0
            res = 0
            while i < len(nums) - 1:
                while j + 1 < len(nums) and nums[j + 1] - nums[i] <= n:
                    j += 1
                res += j - i
                i += 1
            return res

        T = 100
        counts = Counter(nums)
        count = sum(v * (v - 1) // 2 for v in counts.values())
        if k <= count:
            return 0
        if count < T:
            low = 0
            nums.sort()
        else:
            low = 1
            k -= count
            nums = sorted(counts)
        high = max(nums) - min(nums)
        while low < high:
            mid = (low + high) // 2
            res = count_dist_le1(mid) if count < T else count_dist_le(mid)
            if res >= k:
                high = mid
            else:
                low = mid + 1
        return high


print(Solution().smallestDistancePair([62, 100, 4], 2))
