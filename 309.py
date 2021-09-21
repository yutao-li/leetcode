from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        le = len(prices)
        if le < 2:
            return 0
        profit = 0
        pool = [(0, prices[0], 1)]
        while pool:
            pool1 = []
            for pr, cur, i in pool:
                p = prices[i]
                if p <= cur:
                    if i < le - 1:
                        pool1.append((pr, p, i + 1))
                    else:
                        profit = max(profit, pr)
                else:
                    if i == le - 1:
                        pr += p - cur
                        profit = max(profit, pr)
                    else:
                        if prices[i + 1] >= p:
                            pool1.append((pr, cur, i + 1))
                        else:
                            if i + 3 < le:
                                pool1.append((pr + prices[i - 1] - cur, prices[i + 1], i + 2))
                                pool1.append((pr + p - cur, prices[i + 2], i + 3))
                            else:
                                if i + 2 < le:
                                    pool1.append((pr + prices[i - 1] - cur, prices[i + 1], i + 2))
                                profit = max(profit, pr + p - cur)
                            pool1.append((pr, cur, i + 1))
            pool = pool1
        return profit


print(Solution().maxProfit([8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]))
