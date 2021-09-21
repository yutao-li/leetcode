# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted((i.start, i.end) for emp in schedule for i in emp)
        end = intervals[0][1]
        res = []
        for i, j in intervals[1:]:
            if i > end:
                res.append(Interval(end, i))
            end = max(end, j)
        return res
