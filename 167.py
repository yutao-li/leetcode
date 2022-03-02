from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pos = dict()
        for i, n in enumerate(numbers):
            if target - n in pos:
                return [pos[target - n], i + 1]
            pos[n] = i + 1
