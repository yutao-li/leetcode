from collections import defaultdict
from functools import reduce
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        res = []
        r, c = 0, 0
        r_shift, c_shift = -1, 1
        for _ in range(row * col):
            res.append(mat[r][c])
            r += r_shift
            c += c_shift
            if not (0 <= r < row and 0 <= c < col):
                r_shift, c_shift = -r_shift, -c_shift
            if r < 0:
                if c >= col:
                    r += 2
                    c -= 1
                else:
                    r += 1
            elif r >= row:
                c += 2
                r -= 1
            elif c < 0:
                c += 1
            elif c >= col:
                c -= 1
                r += 2
        return res


class Solution1:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        N, M = len(matrix), len(matrix[0])
        result, intermediate = [], []
        for d in range(N + M - 1):
            intermediate.clear()
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result


class Solution2:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        for i, row in enumerate(mat):
            for j, n in enumerate(row):
                diagonal[i + j].append(n)
        return reduce(lambda x, y: x + y,
                      [diagonal[i] if i % 2 else diagonal[i][::-1] for i in range(len(mat) + len(mat[0]) - 1)])


print(Solution2().findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
