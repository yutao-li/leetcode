from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        q = deque()
        li = []

        def clean(i):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()

        for i in range(k):
            clean(i)
            q.append(i)

        li.append(nums[q[0]])
        for i in range(k, len(nums)):
            clean(i)
            q.append(i)
            li.append(nums[q[0]])
        return li


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
