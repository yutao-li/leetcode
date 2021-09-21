from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.matrix = matrix
        self.bit = [[0] * (len(matrix[0]) + 1)] + [[0] + row for row in matrix]
        for row in range(1, len(self.bit)):
            row = self.bit[row]
            power = 2
            while power < len(self.bit[0]):
                i = 1
                while i * power < len(self.bit[0]):
                    row[i * power] += row[i * power - power // 2]
                    i += 1
                power *= 2
        for col in range(1, len(self.bit[0])):
            power = 2
            while power < len(self.bit):
                i = 1
                while i * power < len(self.bit):
                    self.bit[i * power][col] += self.bit[i * power - power // 2][col]
                    i += 1
                power *= 2

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        row += 1
        col += 1
        while row < len(self.bit):
            c = col
            while c < len(self.bit[0]):
                self.bit[row][c] += diff
                c += c & (-c)
            row += row & (-row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def sum(row: int, col: int):
            res = 0
            while row:
                c = col
                while c:
                    res += self.bit[row][c]
                    c -= c & (-c)
                row -= row & (-row)
            return res

        return sum(row2 + 1, col2 + 1) + sum(row1, col1) - sum(row2 + 1, col1) - sum(row1, col2 + 1)


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3))
