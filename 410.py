from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if m == 1:
            return sum(nums)
        acc = [0]
        for n in nums:
            acc.append(acc[-1] + n)
        dp = acc[1:]
        for w in range(m - 2):
            for i in range(len(dp) - 1, w, -1):
                dp[i] = min(max(dp[j - 1], acc[i + 1] - acc[j]) for j in range(w + 1, i + 1))
        return min(max(dp[j - 1], acc[-1] - acc[j]) for j in range(m - 1, len(dp)))


res = Solution().splitArray([1, 2147483646], 1)
