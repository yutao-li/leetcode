from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1
        candies = [0] * len(ratings)
        if ratings[0] <= ratings[1]:
            candies[0] = 1
            filled = 0
        else:
            filled = -1
        i = 1
        while i < len(ratings) - 1:
            if ratings[i] <= ratings[i + 1]:
                if ratings[i] <= ratings[i - 1]:
                    candies[i] = 1
                    if filled < i - 1:
                        for j in range(i - 1, filled + 1, -1):
                            candies[j] = candies[j + 1] + 1
                        candies[filled + 1] = max(candies[filled + 2] + 1, candies[filled + 1])
                else:
                    candies[i] = 1 + candies[i - 1]
                filled = i
            else:
                if ratings[i] > ratings[i - 1]:
                    candies[i] = candies[i - 1] + 1
            i += 1
        if ratings[-1] > ratings[-2]:
            candies[-1] = candies[-2] + 1
        else:
            candies[-1] = 1
            if filled < len(ratings) - 2:
                for j in range(len(ratings) - 2, filled + 1, -1):
                    candies[j] = candies[j + 1] + 1
                candies[filled + 1] = max(candies[filled + 2] + 1, candies[filled + 1])
        return sum(candies)


class Solution1:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        for i in sorted(range(n), key=lambda i: ratings[i]):
            if i > 0 and ratings[i - 1] < ratings[i]:
                res[i] = max(res[i], res[i - 1] + 1)
            if i < n - 1 and ratings[i + 1] < ratings[i]:
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)


print(Solution().candy([29, 51, 87, 87, 72, 12]))
