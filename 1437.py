from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre = float('-inf')
        for i, n in enumerate(nums):
            if n == 1:
                if i - pre <= k:
                    return False
                pre = i
        return True


res = Solution().kLengthApart([1,1,1,1,1], 0)
