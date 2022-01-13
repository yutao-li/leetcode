from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        distance = [[0] * m for _ in range(n)]
        building = sum(1 for i in range(n) for j in range(m) if grid[i][j] == 1)
        if building == m * n:
            return -1
        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        min_dist = float('inf')
        empty = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2 * empty + 1:
                    grid[i][j] += 2
                    min_dist = float('inf')
                    bu = 1
                    pool = [(i, j)]
                    dist = 1
                    while pool:
                        pool1 = []
                        for r, c in [(r + a, c + b) for r, c in pool for a, b in move]:
                            if 0 <= r < n and 0 <= c < m:
                                if grid[r][c] == -empty:
                                    grid[r][c] -= 1
                                    distance[r][c] += dist
                                    min_dist = min(min_dist, distance[r][c])
                                    pool1.append((r, c))
                                elif grid[r][c] == 2 * empty + 1:
                                    bu += 1
                                    grid[r][c] += 2
                        pool = pool1
                        dist += 1
                    if bu != building:
                        return -1
                    empty += 1
        return min_dist if min_dist != float('inf') else -1


print(Solution().shortestDistance(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
