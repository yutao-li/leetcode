from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:] for p in perms for i in range((p + [n]).index(n) + 1)]
        return perms


res = Solution().permuteUnique([1, 1, 2])
