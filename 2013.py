from typing import List
from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.sameX = defaultdict(lambda: defaultdict(int))
        self.sameY = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.sameX[x][y] += 1
        self.sameY[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for x1, count in self.sameY[y].items():
            if x == x1:
                continue
            diff = x - x1
            if y - diff in self.sameX[x] and y - diff in self.sameX[x1]:
                res += self.sameX[x][y - diff] * self.sameX[x1][y - diff] * self.sameX[x1][y]
            if y + diff in self.sameX[x] and y + diff in self.sameX[x1]:
                res += self.sameX[x][y + diff] * self.sameX[x1][y + diff] * self.sameX[x1][y]
        return res
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
