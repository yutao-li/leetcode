from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        s0 = float('-inf')
        s1 = -prices[0]
        s2 = 0
        for price in prices[1:]:
            s0, s1, s2 = s1 + price, max(s1, s2 - price), max(s0, s2)
        return max(s0, s2)


print(Solution().maxProfit([1, 2, 4]))
