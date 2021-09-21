from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = Counter(arr1)
        first = []
        for i in arr2:
            first += [i] * arr1.pop(i)
        second = []
        for i in sorted(arr1):
            second += [i] * arr1[i]
        return first + second


res = Solution().relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6])

