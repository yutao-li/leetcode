from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = 1
            for i, j in enumerate(isConnected[city]):
                if j and not visited[i]:
                    dfs(i)

        n = len(isConnected)
        res = 0
        visited = [0] * n
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res
