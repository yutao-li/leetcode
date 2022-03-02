from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        distance = 0
        i = j = 0
        m, n = len(grid), len(grid[0])
        while grid[i][j] != '*':
            j += 1
            if j == n:
                j = 0
                i += 1
        pool = [(i, j)]
        visited[i][j] = 1
        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while pool:
            distance += 1
            pool1 = []
            adjs = [(i + r, c + j) for i, j in pool for r, c in move]
            for i, j in adjs:
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 'X' and not visited[i][j]:
                    if grid[i][j] == '#':
                        return distance
                    visited[i][j] = 1
                    pool1.append((i, j))
            pool = pool1
        return -1
