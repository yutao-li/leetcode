from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        health = [[0] * n for _ in range(m)]
        health[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for r in range(m - 2, -1, -1):
            health[r][-1] = max(1, health[r + 1][-1] - dungeon[r][-1])
        for c in range(n - 2, -1, -1):
            health[-1][c] = max(1, health[-1][c + 1] - dungeon[-1][c])
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                health[r][c] = max(1, min(health[r][c + 1], health[r + 1][c]) - dungeon[r][c])
        return health[0][0]


class Solution1:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        health = [float('inf')] * (n + 1)
        health[-2] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                health[c] = max(1, min(health[c + 1], health[c]) - dungeon[r][c])
        return int(health[0])


print(Solution1().calculateMinimumHP(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
