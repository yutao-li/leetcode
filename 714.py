from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        s0 = 0
        s1 = -prices[0]
        for price in prices[1:]:
            s0, s1 = max(s1 + price - fee, s0), max(s0 - price, s1)
        return max(s0, s1)


print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
