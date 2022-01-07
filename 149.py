from collections import Counter, defaultdict
from fractions import Fraction
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points = list(Counter(tuple(p) for p in points).items())
        if not points:
            return 0
        elif len(points) == 1:
            return points[0][1]
        elif len(points) == 2:
            return points[0][1] + points[1][1]
        num = 1
        for i, ((x0, y0), c0) in enumerate(points):
            counts = defaultdict(int)
            for (x, y), c in points[i + 1:]:
                counts[Fraction((y - y0), (x - x0)) if x != x0 else float('inf')] += c
            max_count = max(counts.values(), default=0) + c0
            if max_count > num:
                num = max_count
        return num


class Solution1:
    def maxPoints(self, points: List[List[int]]) -> int:
        count = defaultdict(lambda: defaultdict(int))
        for i, (x, y) in enumerate(points):
            for j, (x1, y1) in enumerate(points[i + 1:], i + 1):
                count[i][Fraction(y - y1, x - x1) if x - x1 else float('inf')] += 1
        return max((i for v in count.values() for i in v.values()), default=0) + 1


class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        count = defaultdict(lambda: defaultdict(int))
        for i, (x, y) in enumerate(points):
            for j, (x1, y1) in enumerate(points[i + 1:], i + 1):
                count[i][(y - y1) / (x - x1) if x - x1 else float('inf')] += 1
        return max((i for v in count.values() for i in v.values()), default=0) + 1


print(Solution1().maxPoints([[3, 1], [12, 3], [3, 1], [-6, -1]]))
