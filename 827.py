from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def connect(i, j):
            s = 1
            grid[i][j] = 2
            pool = [(i, j)]
            peri = set()
            res = 0
            while pool:
                pool1 = []
                for r, c in pool:
                    for r1, c1 in [(r + a, c + b) for a, b in move]:
                        if grid[r1][c1] < 1:
                            peri.add((r1, c1))
                        elif grid[r1][c1] == 1:
                            grid[r1][c1] = 2
                            s += 1
                            pool1.append((r1, c1))
                pool = pool1
            for r, c in peri:
                grid[r][c] -= s
                res = max(res, 1 - grid[r][c])
            return res

        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n = len(grid)
        grid = [[0] * (n + 2)] + [[0] + row + [0] for row in grid] + [[0] * (n + 2)]
        res = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if grid[i][j] == 1:
                    res = max(res, connect(i, j))
        return min(n * n, res)


print(Solution().largestIsland([[1, 0, 0, 1, 1], [1, 0, 0, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 1, 0]]))
