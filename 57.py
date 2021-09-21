from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        c, d = newInterval
        for i, (a, b) in enumerate(intervals):
            if b < c:
                continue
            left = min(a, c)
            for j, (e, f) in enumerate(intervals[i:], i):
                if f < d:
                    continue
                if d >= e:
                    return intervals[:i] + [[left, f]] + intervals[j + 1:]
                else:
                    return intervals[:i] + [[left, d]] + intervals[j:]
            return intervals[:i] + [[left, d]]
        return intervals + [newInterval]


res = Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
