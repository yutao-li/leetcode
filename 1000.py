from typing import List


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        def dp(i, j):
            if i == j:
                return 0
            if j - i == K - 1:
                return acc[j] - acc[i] + stones[j]
            if (i, j) in seen:
                return seen[i, j]
            cost = float('inf')
            for k in range(i, j, K - 1):
                cost = min(cost, dp(i, k) + dp(k + 1, j))
            if (j - i) % (K - 1) == 0:
                cost += acc[j] - acc[i] + stones[j]
            seen[i, j] = cost
            return cost

        if (len(stones) - 1) % (K - 1):
            return -1
        acc = [0]
        seen = dict()
        for s in stones:
            acc.append(acc[-1] + s)
        return dp(0, len(stones) - 1)


print(Solution().mergeStones([3, 5, 1, 2, 6], 3))
