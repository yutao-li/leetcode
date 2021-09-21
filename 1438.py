from typing import List
import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        w = 1
        left = right = 0
        maxh = [(-nums[0], 0)]
        minh = [(nums[0], 0)]
        while right + 1 < len(nums):
            right += 1
            heapq.heappush(maxh, (-nums[right], right))
            heapq.heappush(minh, (nums[right], right))
            while -maxh[0][0] - minh[0][0] > limit:
                left += 1
                while maxh[0][1] < left:
                    heapq.heappop(maxh)
                while minh[0][1] < left:
                    heapq.heappop(minh)
            w = max(w, right - left + 1)
        return w


res = Solution().longestSubarray([4,2,2,2,4,4,2,2], 0)
