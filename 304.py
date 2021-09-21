from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in self.matrix:
            for col in range(1, len(matrix[0])):
                row[col] += row[col - 1]
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                self.matrix[row][col] += self.matrix[row - 1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 -= 1
        col1 -= 1
        res = self.matrix[row2][col2]
        if row1 >= 0:
            res -= self.matrix[row1][col2]
        if col1 >= 0:
            res -= self.matrix[row2][col1]
        if row1 >= 0 and col1 >= 0:
            res += self.matrix[row1][col1]
        return res

    # Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
