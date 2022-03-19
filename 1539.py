from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in arr:
            if i <= k:
                k += 1
            else:
                return k
        return k
