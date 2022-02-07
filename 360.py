from bisect import bisect_left
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            nums = [b * i + c for i in nums]
            return nums if b >= 0 else nums[::-1]
        else:
            pivot = -b / 2 / a
            rp = bisect_left(nums, pivot)
            lp = rp - 1
            n = len(nums)
            res = []
            while lp >= 0 and rp < n:
                if pivot - nums[lp] >= nums[rp] - pivot:
                    res.append(nums[rp])
                    rp += 1
                else:
                    res.append(nums[lp])
                    lp -= 1
            if lp >= 0:
                res += nums[lp::-1]
            elif rp < n:
                res += nums[rp:]
            res = [a * i ** 2 + b * i + c for i in res]
            return res if a > 0 else res[::-1]
