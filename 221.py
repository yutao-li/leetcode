from typing import List
from bisect import bisect


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        side = 0
        pool = []
        horizon = [[] for _ in range(len(matrix))]
        straight = [[] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    pool.append((i, j))
                else:
                    horizon[i].append(j)
                    straight[j].append(i)

        while pool:
            side += 1
            pool1 = []
            for i, j in pool:
                if i + side < len(matrix) and j + side < len(matrix[0]) and matrix[i + side][j] == '1' and matrix[i][
                    j + side] == '1' and matrix[i + side][j + side] == '1':
                    hpos = bisect(horizon[i + side], j)
                    hnext0 = horizon[i + side][hpos] if hpos < len(horizon[i + side]) else len(matrix[0])
                    vpos = bisect(straight[j + side], i)
                    vnext0 = straight[j + side][vpos] if vpos < len(straight[j + side]) else len(matrix)
                    if hnext0 - j >= side and vnext0 - i >= side:
                        pool1.append((i, j))
            pool = pool1
        return side ** 2


res = Solution().maximalSquare([["0", "1"]])
