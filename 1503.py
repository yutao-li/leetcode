from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))


res = Solution().getLastMoment(9, [5], [4])
