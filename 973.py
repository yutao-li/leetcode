from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def select(low, high):
            start = low
            end = high
            low += 1
            while low <= high:
                if points[low] <= points[start]:
                    low += 1
                else:
                    points[low], points[high] = points[high], points[low]
                    high -= 1
            points[low - 1], points[start] = points[start], points[low - 1]
            if low - 1 <= K <= low:
                return [i for _, i in points[:K]]
            elif K < low - 1:
                return select(start, low - 2)
            else:
                return select(low, end)

        points = [(a ** 2 + b ** 2, [a, b]) for a, b in points]
        return select(0, len(points) - 1)


print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
