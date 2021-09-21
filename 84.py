from bisect import bisect_right


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # largest = 0
        # for i in range(len(heights)):
        #     if heights[i] == 0 or largest / heights[i] >= len(heights):
        #         continue
        #     l = i
        #     while l >= 0 and heights[i] <= heights[l]:
        #         l -= 1
        #     r = i
        #     while r < len(heights) and heights[i] <= heights[r]:
        #         r += 1
        #     area = (r - l - 1) * heights[i]
        #     if largest < area:
        #         largest = area
        # return largest
        if heights:
            return self.divide(heights, 0, len(heights) - 1)
        else:
            return 0

    def divide(self, heights, left, right):
        if left == right:
            return heights[left]
        minIndex = -1
        Min = float('inf')
        for i, h in enumerate(heights[left:right + 1]):
            if h < Min:
                Min = h
                minIndex = i + left
        area = Min * (right - left + 1)
        if minIndex - 1 >= left:
            larea = self.divide(heights, left, minIndex - 1)
        else:
            larea = 0
        if minIndex + 1 <= right:
            rarea = self.divide(heights, minIndex + 1, right)
        else:
            rarea = 0
        return max(area, larea, rarea)

    def largestRectangleArea1(self, heights):
        if not heights:
            return 0
        coordinates = [0]
        widths = {0: len(heights)}
        order = sorted((b, a) for a, b in enumerate(heights))
        largest = 0
        for h, i in order:
            left = bisect_right(coordinates, i) - 1
            width = widths[coordinates[left]]
            if width * h > largest:
                largest = width * h
            if i == coordinates[left]:
                del widths[i]
                if width > 1:
                    coordinates[left] += 1
                    widths[i + 1] = width - 1
                else:
                    coordinates.pop(left)
            else:
                widths[coordinates[left]] = i - coordinates[left]
                if coordinates[left] + width - i - 1 > 0:
                    coordinates.insert(left + 1, i + 1)
                    widths[i + 1] = coordinates[left] + width - i - 1
        return largest


class Solution1:
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


height = [2, 6]

print(Solution1().largestRectangleArea(height))
