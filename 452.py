from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        move = 0
        end = float('-inf')
        for i, j in sorted(points, key=lambda x: x[1]):
            if i > end:
                move += 1
                end = j
        return move


res = Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
