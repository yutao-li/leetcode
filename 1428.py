# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
mat = [[0, 0], [1, 1]]


class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        return mat[row][col]

    def dimensions(self) -> list:
        return [len(mat), len(mat[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        res = col
        for i in range(row):
            left, right = 0, res
            while left < right:
                mid = (left + right) // 2
                ele = binaryMatrix.get(i, mid)
                if ele == 1:
                    right = mid
                else:
                    left = mid + 1
            res = right
            if res == 0:
                return 0
        return res if res != col else -1


res = Solution().leftMostColumnWithOne(BinaryMatrix())

