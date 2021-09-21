from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        lowest = prices[0]
        for p in prices[1:]:
            if p < lowest:
                lowest = p
            elif p - lowest > profit:
                profit = p - lowest
        return profit


print(Solution().maxProfit([7, 6, 4, 3, 1]))
