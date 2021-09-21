from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        queue = [start]
        visited.add(tuple(start))
        while queue:
            i, j = queue.pop()
            pool = []

            i1 = i
            while i1 - 1 >= 0 and maze[i1 - 1][j] == 0:
                i1 -= 1
            pool.append((i1, j))

            i1 = i
            while i1 + 1 < len(maze) and maze[i1 + 1][j] == 0:
                i1 += 1
            pool.append((i1, j))

            j1 = j
            while j1 - 1 >= 0 and maze[i][j1 - 1] == 0:
                j1 -= 1
            pool.append((i, j1))

            j1 = j
            while j1 + 1 < len(maze[0]) and maze[i][j1 + 1] == 0:
                j1 += 1
            pool.append((i, j1))

            for i1, j1 in pool:
                if (i1, j1) not in visited:
                    if [i1, j1] == destination:
                        return True
                    visited.add((i1, j1))
                    queue.append([i1, j1])
        return False


print(Solution().hasPath([[0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0],
                          [1, 1, 0, 1, 1],
                          [0, 0, 0, 0, 0]],
                         [0, 4],
                         [3, 2]))
