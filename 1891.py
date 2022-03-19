from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        low = 1
        high = sum(ribbons) // k + 1
        while low < high:
            mid = (low + high) // 2
            count = sum(r // mid for r in ribbons)
            if count < k:
                high = mid
            else:
                low = mid + 1
        return low - 1
