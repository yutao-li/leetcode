from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            d = 1
            acc = 0
            for weight in weights:
                acc += weight
                if acc > mid:
                    acc = weight
                    d += 1
                    if d > days:
                        break
            if d > days:
                low = mid + 1
            else:
                high = mid
        return low


print(Solution().shipWithinDays(
    [180, 373, 75, 82, 497, 23, 303, 299, 53, 426, 152, 314, 206, 433, 283, 370, 179, 254, 265, 431, 453, 17, 189, 224],
    12))
