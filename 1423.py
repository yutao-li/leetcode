from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        width = len(cardPoints) - k
        mini = sum(cardPoints[:width])
        cur = mini
        for i in range(width, len(cardPoints)):
            cur += cardPoints[i] - cardPoints[i - width]
            if cur < mini:
                mini = cur
        return sum(cardPoints) - mini


res = Solution().maxScore([1, 1000, 1], 1)
