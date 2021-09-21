from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            mask = 1 << (i * w + j)
            res = 1
            pool = [(i, j)]
            while pool:
                i, j = pool.pop()
                for i1, j1 in moves:
                    i1, j1 = i1 + i, j1 + j
                    index = i1 * w + j1
                    if 0 <= i1 < h and 0 <= j1 < w and grid[i1][j1] and mask & (1 << index) == 0:
                        pool.append((i1, j1))
                        res += 1
                        mask |= 1 << index
            return res

        num = sum(sum(row) for row in grid)
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        if num <= 1:
            return num
        w = len(grid[0])
        h = len(grid)
        ones = []
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    ones.append((i, j))
        if num > bfs(*ones[0]):
            return 0
        i, j = ones[0]
        grid[i][j] = 0
        if num - 1 > bfs(*ones[1]):
            return 1
        grid[i][j] = 1
        for i, j in ones[1:]:
            grid[i][j] = 0
            if num - 1 > bfs(*ones[0]):
                return 1
            grid[i][j] = 1
        return 2


res = Solution().minDays(grid=[[1, 1, 0, 1, 1],
                               [1, 1, 1, 1, 1],
                               [1, 1, 0, 1, 1],
                               [1, 1, 1, 1, 1]])
