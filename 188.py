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
            profit = 0
            cur = prices[0]
            i = 1
            while i < len(prices) - 1:
                if cur >= prices[i]:
                    cur = prices[i]
                    i += 1
                else:
                    if prices[i + 1] >= prices[i]:
                        i += 1
                    else:
                        profit += prices[i] - cur
                        cur = prices[i + 1]
                        i += 2
            if prices[-1] > cur:
                profit += prices[-1] - cur
            return profit


print(Solution().maxProfit(1000000000, []))
