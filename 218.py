import heapq
from heapq import heappush, heappop
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        height = [(0, float('inf'))]
        vertical = sorted([(l, -h, r) for l, r, h in buildings] + list(set((r, 0, 0) for _, r, _ in buildings)))
        res = [[0, 0]]
        for l, neg_h, r in vertical:
            while l >= height[0][1]:
                heapq.heappop(height)
            if r:
                heapq.heappush(height, (neg_h, r))
            if res[-1][1] != -height[0][0]:
                res.append([l, -height[0][0]])
        return res[1:]


class Solution1:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        l, r, h = buildings[0]
        height = [(-h, r)]
        res = [[l, h]]
        buildings.append([float('inf'), float('inf'), 0])
        for l, r, h in buildings[1:]:
            while height and height[0][1] < l:
                h1, r1 = heappop(height)
                h1 = -h1
                while height and height[0][1] <= r1:
                    heappop(height)
                if height:
                    h2 = -height[0][0]
                    if h1 > h2:
                        res.append([r1, h2])
                else:
                    res.append([r1, 0])
            if height:
                if -height[0][0] < h:
                    if res[-1][0] == l:
                        res[-1][1] = h
                    else:
                        res.append([l, h])
            else:
                res.append([l, h])
            heappush(height, (-h, r))
        return res[:-1]


res = Solution().getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
