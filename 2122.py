from collections import Counter
from typing import List


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        l = min(nums)
        le = len(nums) // 2
        nums = Counter(nums)
        keys = sorted(nums.keys())
        ks = [max(1, (corr - l) // 2) for corr in keys[1:]]
        for k in ks:
            nums1 = dict(nums)
            res = []
            for lower in keys:
                if nums1[lower]:
                    higher = lower + 2 * k
                    if not (higher in nums1 and nums1[higher] >= nums1[lower]):
                        break
                    res += [lower + k] * nums1[lower]
                    nums1[higher] -= nums1[lower]
            if len(res) == le:
                return res


print(Solution().recoverArray([11, 6, 3, 4, 8, 7, 8, 7, 9, 8, 9, 10, 10, 2, 1, 9]))
