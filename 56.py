from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        start, end = intervals[0]
        for i, j in intervals[1:]:
            if i <= end:
                end = max(end, j)
            else:
                res.append([start, end])
                start, end = i, j
        res.append([start, end])
        return res
