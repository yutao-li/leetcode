from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        cur = prices[0]
        for p in prices[1:]:
            if p > cur:
                profit += p - cur
                cur = p
            elif p < cur:
                cur = p
        return profit


print(Solution().maxProfit([7, 6, 4, 3, 1]))
