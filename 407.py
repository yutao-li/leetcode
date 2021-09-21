from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        visited = [[False] * len(heightMap[0]) for _ in range(len(heightMap))]
        visited[0] = [True] * len(heightMap[0])
        visited[-1] = [True] * len(heightMap[0])
        for r in range(1, len(heightMap) - 1):
            visited[r][0] = True
            visited[r][-1] = True
        visits = 2 * len(heightMap[0]) + 2 * len(heightMap) - 4
        heap = [(h, 0, c) for c, h in enumerate(heightMap[0])] + \
               [(h, len(heightMap) - 1, c) for c, h in enumerate(heightMap[-1])] + \
               [(heightMap[r][0], r, 0) for r in range(1, len(heightMap) - 1)] + \
               [(heightMap[r][-1], r, len(heightMap[0]) - 1) for r in range(1, len(heightMap) - 1)]
        heapq.heapify(heap)
        res = 0
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        max_h = float('-inf')
        while visits < len(heightMap) * len(heightMap[0]):
            h, r, c = heapq.heappop(heap)
            max_h = max(max_h, h)
            for i, j in moves:
                r1 = r + i
                c1 = c + j
                if 0 <= r1 < len(heightMap) and 0 <= c1 < len(heightMap[0]) and not visited[r1][c1]:
                    h1 = heightMap[r1][c1]
                    if h1 < max_h:
                        res += max_h - h1
                    visited[r1][c1] = True
                    heapq.heappush(heap, (h1, r1, c1))
                    visits += 1
        return res


print(Solution().trapRainWater([[12, 13, 1, 12],
                                [13, 4, 13, 12],
                                [13, 8, 10, 12],
                                [12, 13, 12, 12],
                                [13, 13, 13, 13]]))
