from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        res = sorted((abs(i - median), i) for i in arr)
        return [i for _, i in res[-k:]]


res = Solution().getStrongest([-7, 22, 17, 3], 2)
