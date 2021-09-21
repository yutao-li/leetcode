from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:] for p in perms for i in range(len(p) + 1)]
        return perms


res = Solution().permute([1, 2, 3])
