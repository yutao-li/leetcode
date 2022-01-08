from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        max_h = heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_h:
                res.append(i)
                max_h = heights[i]
        return res[::-1]
