from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(pos, target, acc):
            nonlocal res
            q, r = divmod(target, coins[pos])
            if r == 0:
                res = min(res, acc + q)
            elif pos < len(coins) - 1:
                for i in range(q, max(((res - acc) * coins[pos + 1] - target) // (coins[pos + 1] - coins[pos]), -1)
                if res != float('inf') else -1, -1):
                    dp(pos + 1, target - i * coins[pos], acc + i)

        coins = sorted(set(coins), reverse=True)
        res = float('inf')
        dp(0, amount, 0)
        return -1 if res == float('inf') else res


res = Solution().coinChange([186, 419, 83, 408], 6249)
