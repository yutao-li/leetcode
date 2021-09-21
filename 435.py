from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        move = 0
        end = intervals[0][1]
        for i, j in intervals[1:]:
            if i < end:
                move += 1
            else:
                end = j
        return move


res = Solution().eraseOverlapIntervals([[1,2],[2,3]])
