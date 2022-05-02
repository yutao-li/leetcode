from typing import List
from heapq import heappush, heappop


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def reachable(height):
            seen = [[0] * n for _ in range(n)]
            pool = [(0, 0)]
            seen[0][0] = 1
            while pool:
                pool1 = []
                for i, j in pool:
                    for x, y in moves:
                        i1 = i + x
                        j1 = j + y
                        if 0 <= i1 < n and 0 <= j1 < n and grid[i1][j1] <= height and not seen[i1][j1]:
                            if i1 == j1 == n - 1:
                                return True
                            seen[i1][j1] = 1
                            pool1.append((i1, j1))
                pool = pool1
            return False

        n = len(grid)
        low = max(grid[0][0], grid[-1][-1])
        high = max(i for row in grid for i in row)
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while low < high:
            mid = (low + high) // 2
            if reachable(mid):
                high = mid
            else:
                low = mid + 1
        return low


class Solution1:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        res = grid[-1][-1]
        seen = [[0] * n for _ in range(n)]
        seen[0][0] = 1
        heap = [(grid[0][0], 0, 0)]
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while True:
            h, r, c = heappop(heap)
            res = max(res, h)
            for x, y in moves:
                i = r + x
                j = c + y
                if 0 <= i < n and 0 <= j < n and not seen[i][j]:
                    if i == j == n - 1:
                        return res
                    seen[i][j] = 1
                    heappush(heap, (grid[i][j], i, j))
