from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not (grid and grid[0]):
            return 0
        row = len(grid)
        col = len(grid[0])
        pos = 0
        count = 0

        def dfs(r, c):
            if r + 1 < row and grid[r + 1][c] == '1':
                grid[r + 1][c] = 0
                dfs(r + 1, c)
            if c + 1 < col and grid[r][c + 1] == '1':
                grid[r][c + 1] = 0
                dfs(r, c + 1)
            if r > 0 and grid[r - 1][c] == '1':
                grid[r - 1][c] = 0
                dfs(r - 1, c)
            if c > 0 and grid[r][c - 1] == '1':
                grid[r][c - 1] = 0
                dfs(r, c - 1)

        while pos < row * col:
            r, c = divmod(pos, col)
            if grid[r][c] == '1':
                count += 1
                grid[r][c] = 0
                dfs(r, c)
            pos += 1
        return count
