from bisect import bisect_right


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        largest = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            area = self.largestRectangleArea(heights)
            if area > largest:
                largest = area
        return largest

    def largestRectangleArea(self, heights):
        heights.append(0)
        res = 0
        stack = [-1]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                res = max(res, h * w)
            stack.append(i)
        return res

    def maximalRectangle1(self, matrix):
        if not (matrix and matrix[0]):
            return 0
        largest = 0
        v_interval = [0] * len(matrix[0])
        for col in range(len(matrix[0])):
            start = []
            end = []
            row = 0
            while row < len(matrix):
                if matrix[row][col] == '0':
                    row += 1
                else:
                    start.append(row)
                    row += 1
                    while row < len(matrix) and matrix[row][col] == '1':
                        row += 1
                    end.append(row)
            v_interval[col] = (start, end)

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == '1':
                    width = 1
                    height = float('inf')
                    while True:
                        curCol = y + width - 1
                        index = bisect_right(v_interval[curCol][0], x) - 1
                        height = min(v_interval[curCol][1][index] - x, height)
                        if width * height > largest:
                            largest = width * height
                        curCol += 1
                        width += 1
                        if curCol == len(matrix[0]) or matrix[x][curCol] != '1':
                            break
        return largest


matrix = [["0"]]
print(Solution().maximalRectangle1(matrix))
