class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mem = {(0, 0, 0): grid[0][0]}
        total = self.dp(grid, len(grid) - 1, len(grid) - 1, len(grid) - 1, mem)
        if total < 0:
            return 0
        return total

    def dp(self, grid, x0, y0, x1, mem):
        if (x0, y0, x1) in mem:
            return mem[x0, y0, x1]
        y1 = x0 + y0 - x1
        prev0 = []
        prev1 = []
        if y0 - 1 >= 0 and grid[x0][y0 - 1] != -1:
            prev0.append((x0, y0 - 1))
        if x0 - 1 >= 0 and grid[x0 - 1][y0] != -1:
            prev0.append((x0 - 1, y0))
        if y1 - 1 >= 0 and grid[x1][y1 - 1] != -1:
            prev1.append((x1, y1 - 1))
        if x1 - 1 >= 0 and grid[x1 - 1][y1] != -1:
            prev1.append((x1 - 1, y1))
        if prev0 and prev1:
            cherry = max(self.dp(grid, x00, y00, x11, mem) for x00, y00 in prev0 for x11, y11 in prev1)
        else:
            cherry = -1
        # for x00, y00 in prev0:
        #     for x11, y11 in prev1:
        #         get = self.dp(grid, x00, y00, x11, mem)
        #         if get != -1:
        #             if cherry < get:
        #                 cherry = get
        if cherry != -1:
            if x0 == x1:
                cherry += grid[x0][y0]
            else:
                cherry += grid[x0][y0] + grid[x1][y1]
        mem[x0, y0, x1] = cherry
        return mem[x0, y0, x1]


grid = [[1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1]]
print(Solution().cherryPickup(grid))
