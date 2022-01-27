from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k < len(prices) // 2:
            s = [0] + [-prices[0], 0] * k
            for price in prices[1:]:
                for i in range(k, 0, -1):
                    s[2 * i] = max(s[2 * i], s[2 * i - 1] + price)
                    s[2 * i - 1] = max(s[2 * i - 1], s[2 * i - 2] - price)
            return s[2 * k]
        else:
            return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))


print(Solution().maxProfit(1000000000, []))
