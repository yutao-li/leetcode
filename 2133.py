from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in matrix:
            if not (len(set(row)) == n and sum(row) == (1 + n) * n // 2):
                return False
        for i in range(len(matrix)):
            col = [matrix[j][i] for j in range(len(matrix))]
            if not (len(set(col)) == n and sum(col) == (1 + n) * n // 2):
                return False
        return True
