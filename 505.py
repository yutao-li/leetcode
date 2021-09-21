from typing import List
import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        queue = [(0, start[0], start[1])]
        dists = dict()
        dists[tuple(start)] = 0
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            d, i, j = heapq.heappop(queue)
            while d > dists[i, j]:
                d, i, j = heapq.heappop(queue)
            pool = []

            for r, c in moves:
                i1, j1 = i, j
                while 0 <= i1 + r < len(maze) and len(maze[0]) > j1 + c >= 0 == maze[i1 + r][j1 + c]:
                    i1 += r
                    j1 += c
                pool.append((i1, j1))

            for i1, j1 in pool:
                d1 = d + abs(i1 + j1 - i - j)
                if (i1, j1) not in dists or dists[i1, j1] > d1:
                    if [i1, j1] == destination:
                        return d1
                    dists[i1, j1] = d1
                    heapq.heappush(queue, (d1, i1, j1))
        return -1


print(Solution().shortestDistance([[0, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 1, 0],
                                   [1, 1, 0, 1, 1],
                                   [0, 0, 0, 0, 0]],
                                  [0, 4], [4, 4]))
