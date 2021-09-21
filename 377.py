from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                elif num == i:
                    dp[i] += 1
                elif num < i:
                    dp[i] += dp[i - num]
        return dp[target]


print(Solution().combinationSum4([1, 2], 10))
