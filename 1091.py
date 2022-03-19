from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not (grid[0][0] == 0 and grid[-1][-1] == 0):
            return -1
        n = len(grid)
        if n == 1:
            return 1
        seen = [[0] * n for _ in range(n)]
        seen[0][0] = 1
        pool = [(0, 0)]
        distance = 1
        move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while pool:
            pool1 = []
            for r, c in pool:
                for r1, c1 in move:
                    r_ = r + r1
                    c_ = c + c1
                    if r_ == n - 1 and c_ == n - 1:
                        return distance + 1
                    if 0 <= r_ < n and 0 <= c_ < n and grid[r_][c_] == 0 and seen[r_][c_] == 0:
                        seen[r_][c_] = 1
                        pool1.append((r_, c_))
            distance += 1
            pool = pool1
        return -1


print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
