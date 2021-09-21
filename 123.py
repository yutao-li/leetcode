from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        s1 = -prices[0]
        s2 = 0
        s3 = -prices[0]
        s4 = 0
        for price in prices[1:]:
            s4 = max(s4, s3 + price)
            s3 = max(s3, s2 - price)
            s2 = max(s2, s1 + price)
            s1 = max(s1, - price)
        return s4


print(Solution().maxProfit([1, 2, 3, 4, 5]))
