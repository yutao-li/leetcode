from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        que = []
        trap = 0
        for i, h in enumerate(height):
            while que and h >= que[-1][1]:
                if len(que) >= 2:
                    trap += (min(h, que[-2][1]) - que[-1][1]) * (i - que[-2][0] - 1)
                que.pop()
            que.append((i, h))
        return trap


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
