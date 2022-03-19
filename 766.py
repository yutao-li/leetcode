class Solution:
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))


class Solution1:
    def isToeplitzMatrix(self, m):
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(m, m[1:]))


# Follow up 1
class Solution2:
    def isToeplitzMatrix(self, matrix):
        buffer = matrix[0][:]
        n = len(matrix[0])
        for row in matrix[1:]:
            for i in range(n - 1, 0, -1):
                buffer[i] = row[i]
                if buffer[i] != buffer[i - 1]:
                    return False
            buffer[0] = row[0]
        return True


# Follow up 2:https://leetcode.com/problems/toeplitz-matrix/discuss/271388/Java-Solution-for-Follow-Up-1-and-2

print(Solution().isToeplitzMatrix(
    matrix=[[36, 59, 71, 15, 26, 82, 87], [56, 36, 59, 71, 15, 26, 82], [15, 0, 36, 59, 71, 15, 26]]))
