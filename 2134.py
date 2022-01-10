from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        if n == s or s == 0:
            return 0
        acc = s - sum(nums[:s])
        res = acc
        for i in range(n):
            acc += (not nums[(i + s) % n]) - (not nums[i])
            res = min(res, acc)
        return res


print(Solution().minSwaps(nums=[1, 1, 0, 0, 1]))
