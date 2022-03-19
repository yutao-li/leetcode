from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        que = []
        trap = 0
        for i, h in enumerate(height):
            while que and h >= height[que[-1]]:
                dip = que.pop()
                if que:
                    trap += (min(h, height[que[-1]]) - height[dip]) * (i - que[-1] - 1)
            que.append(i)
        return trap


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
