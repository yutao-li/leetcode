from typing import List
from math import log2


class LooseMedian:
    def __init__(self):
        self.count = 0
        self.segmentTree = [0] * 128

    def insert(self, n: int):
        if n < 0:
            return
        if n == 0:
            n += 1
        i = int(log2(n)) + 64
        self.count += 1
        while i:
            self.segmentTree[i] += 1
            i //= 2

    def get(self) -> int:
        median = self.segmentTree[1] // 2 + 1
        i = 1
        for _ in range(6):
            i *= 2
            if median > self.segmentTree[i]:
                median -= self.segmentTree[i]
                i += 1
        return 2 ** (i - 64)

    def getPercentile(self, percentile: int) -> int:
        rank = int(self.segmentTree[1] * percentile / 100) + 1
        i = 1
        for _ in range(6):
            i *= 2
            if rank > self.segmentTree[i]:
                rank -= self.segmentTree[i]
                i += 1
        return 2 ** (i - 64)


looseMedian = LooseMedian()
looseMedian.insert(3)
print(looseMedian.get())
looseMedian.insert(4)
print(looseMedian.get())
looseMedian.insert(5)
print(looseMedian.get())
