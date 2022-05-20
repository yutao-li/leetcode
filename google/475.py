class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def hasOverlap(a, b):
    a, b = sorted([[a.left, a.right], [b.left, b.right]])
    return b[0] < a[1]


def hasOverlap1(a, b):
    a, b = sorted([[a.left, a.right], [b.left, b.right]])
    return b[0] < a[1], b[0]


def hasOverlap2(intervals):
    intervals = sorted([[i.left, i.right] for i in intervals])
    return all(a < b for (_, a), (b, _) in zip(intervals, intervals[1:]))


def numOverlap(intervals):
    leftBounds = sorted(i.left for i in intervals)
    rightBounds = sorted(i.right for i in intervals)
    rightI = 0
    count = 0
    for leftI, left in enumerate(leftBounds):
        while left >= rightBounds[rightI]:
            rightI += 1
        count += leftI - rightI
    return count


def computeAdjMatrix(intervals):
    n = len(intervals)
    adjMatrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if hasOverlap(i, j):
                adjMatrix[i][j] = 1
    return adjMatrix


a = Interval(1, 3)
b = Interval(2, 4)
c = Interval(3, 5)
print(numOverlap([c, b, a, a]))
