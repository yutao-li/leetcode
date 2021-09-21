from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        fneg = lneg = -1
        count = 0
        zero = -1
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                if count % 2:
                    res = max(res, lneg - 1 - zero, i - 1 - fneg)
                else:
                    res = max(res, i - 1 - zero)
                zero = i
                fneg = lneg = -1
                count = 0
            elif n < 0:
                count += 1
                if fneg == -1:
                    fneg = i
                lneg = i
        if nums[-1]:
            if count % 2:
                res = max(res, lneg - 1 - zero, len(nums) - 1 - fneg)
            else:
                res = max(res, len(nums) - 1 - zero)
        return res


res = Solution().getMaxLen(nums=[1, -2, -3, 4])
