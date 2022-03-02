# https://www.lintcode.com/problem/280/
# https://leetcode.com/discuss/interview-question/1389344/interview-question-nearest-neighboring-city
from collections import defaultdict


class Solution:

    def NearestNeighbor(self, yCoordinates: [int], xCoordinates: [int], cities: [str], queriedPoints: [str]) -> [str]:
        """
        @param x: an array of integers, the x coordinates of each city[i]
        @param y: an array of integers, the y coordinates of each city[i]
        @param c: an array of strings that represent the names of each city[i]
        @param q: an array of strings that represent the names of query locations
        @return: the closest city for each query
        """
        q_len = len(queriedPoints)
        p2c = dict()
        p2xi = dict()
        p2yi = dict()
        x2y = defaultdict(list)
        y2x = defaultdict(list)
        for p, x, y in zip(cities, xCoordinates, yCoordinates):
            p2c[p] = (x, y)
            x2y[x].append(p)
            y2x[y].append(p)
        for v in x2y.values():
            v.sort(key=lambda p: p2c[p][1])
            for i, p in enumerate(v):
                p2yi[p] = i
        for v in y2x.values():
            v.sort(key=lambda p: p2c[p][0])
            for i, p in enumerate(v):
                p2xi[p] = i
        res = ["None"] * q_len
        for i, p in enumerate(queriedPoints):
            x, y = p2c[p]
            xi = p2xi[p]
            yi = p2yi[p]
            distance = float('inf')
            if xi > 0:
                prev = y2x[y][xi - 1]
                distance = abs(p2c[prev][1] - y)
                res[i] = prev
            if xi < len(y2x[y]) - 1:
                post = y2x[y][xi + 1]
                if abs(p2c[post][1] - y) < distance:
                    distance = abs(p2c[post][1] - y)
                    res[i] = post
            if yi > 0:
                prev = x2y[x][yi - 1]
                if abs(p2c[prev][0] - x) < distance:
                    distance = abs(p2c[prev][0] - x)
                    res[i] = prev
            if yi < len(x2y[x]) - 1:
                post = x2y[x][yi + 1]
                if abs(p2c[post][0] - x) < distance:
                    res[i] = post
        return res


cities = ["p1", "p2", "p3"]
xCoordinates = [30, 20, 10]
yCoordinates = [30, 20, 30]
queriedPoints = ["p3", "p2", "p1"]
print(Solution().NearestNeighbor(yCoordinates, xCoordinates, cities, queriedPoints))

cities = ["p1", "p2", "p3", "p4", "p5"]
xCoordinates = [10, 20, 30, 40, 50]
yCoordinates = [10, 20, 30, 40, 50]
queriedPoints = ["p1", "p2", "p3", "p4", "p5"]
print(Solution().NearestNeighbor(yCoordinates, xCoordinates, cities, queriedPoints))
