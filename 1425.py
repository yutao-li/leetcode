from typing import List
import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        heap = sorted([(0, 0), (-nums[-1], len(nums) - 1)])
        for i in range(len(nums) - 2, -1, -1):
            while heap[0][1] - i > k:
                heapq.heappop(heap)
            dp[i] = nums[i] - heap[0][0]
            heapq.heappush(heap, (-dp[i], i))
        return max(dp)


res = Solution().constrainedSubsetSum([10, -2, -10, -5, 20], 2)
