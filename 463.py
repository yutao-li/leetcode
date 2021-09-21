from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        i, j = 0, 0
        while grid[i][j] == 0:
            if j + 1 < len(grid[0]):
                j += 1
            elif i + 1 < len(grid):
                j = 0
                i += 1
        perimeter = 0
        queue = []
        if i < len(grid):
            queue.append((i, j))
            visited[i][j] = True
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.pop()
            for r, c in moves:
                i1 = i + r
                j1 = j + c
                if i1 < 0 or i1 == len(grid) or j1 < 0 or j1 == len(grid[0]) or grid[i1][j1] == 0:
                    perimeter += 1
                elif 0 <= i1 < len(grid) and 0 <= j1 < len(grid[0]) and grid[i1][j1] == 1 and not visited[i1][j1]:
                    visited[i1][j1] = True
                    queue.append((i1, j1))
        return perimeter


print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]))
