from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        distance = [[0] * m for _ in range(n)]
        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        buildings = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
        num_b = len(buildings)
        for empty, (i, j) in enumerate(buildings):
            pool = [(i, j)]
            dist = 1
            count = 0
            while pool:
                pool1 = []
                for r, c in [(r + a, c + b) for r, c in pool for a, b in move]:
                    if 0 <= r < n and 0 <= c < m:
                        if grid[r][c] == -empty:
                            grid[r][c] -= 1
                            distance[r][c] += dist
                            pool1.append((r, c))
                        elif grid[r][c] == 2 * empty + 1:
                            grid[r][c] += 2
                            count += 1
                pool = pool1
                dist += 1
            if count != num_b:
                return -1
        return min([distance[i][j] for i in range(n) for j in range(m) if grid[i][j] == -len(buildings)], default=-1)


print(Solution().shortestDistance(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
