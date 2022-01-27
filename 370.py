from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for i, j, k in updates:
            res[i] += k
            if j < length - 1:
                res[j + 1] -= k
        for i in range(1, length):
            res[i] += res[i - 1]
        return res
