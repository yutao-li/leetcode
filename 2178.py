from typing import List
from math import sqrt


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        end = int(sqrt(finalSum))
        if end * (end + 1) > finalSum:
            end -= 1
        split = [2 * i for i in range(1, end + 1)]
        split[-1] += finalSum - end * (end + 1)
        return split


print(Solution().maximumEvenSplit(28))
