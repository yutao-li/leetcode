from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        distance = [[0] * m for _ in range(n)]
        num_b = sum(1 for i in range(n) for j in range(m) if grid[i][j] == 1)
        if num_b == m * n:
            return -1
        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        buildings = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
        # Optional: check buildings are inter-connected
        # seen = [[0] * m for _ in range(n)]
        # i, j = buildings[0]
        # seen[i][j] = 1
        # count = 1
        # pool = [buildings[0]]
        # while pool:
        #     pool1 = []
        #     for r, c in [(r + a, c + b) for r, c in pool for a, b in move]:
        #         if 0 <= r < n and 0 <= c < m and not seen[r][c]:
        #             seen[r][c] = 1
        #             if grid[r][c] == 0:
        #                 pool1.append((r, c))
        #             elif grid[r][c] == 1:
        #                 count += 1
        #     pool = pool1
        # if count != num_b:
        #     return -1
        #
        for empty, (i, j) in enumerate(buildings):
            pool = [(i, j)]
            dist = 1
            while pool:
                pool1 = []
                for r, c in [(r + a, c + b) for r, c in pool for a, b in move]:
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == -empty:
                        grid[r][c] -= 1
                        distance[r][c] += dist
                        pool1.append((r, c))
                pool = pool1
                dist += 1
        return min([distance[i][j] for i in range(n) for j in range(m) if grid[i][j] == -len(buildings)], default=-1)


print(Solution().shortestDistance(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
