from typing import List
from collections import deque


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxArray(nums, k):
            if k == len(nums):
                return nums
            arr = []
            le = len(nums)
            for i, n in enumerate(nums):
                while arr and arr[-1] < n and len(arr) - 1 + le - i >= k:
                    arr.pop()
                if len(arr) < k:
                    arr.append(n)
            return arr

        def merge(a1, a2):
            a1, a2 = deque(a1), deque(a2)
            return [max(a1, a2).popleft() for _ in range(len(a1) + len(a2))]

        res = [0] * k
        for i in range(max(k - len(nums2), 0), min(k, len(nums1)) + 1):
            a1 = maxArray(nums1, i)
            a2 = maxArray(nums2, k - i)
            arr = merge(a1, a2)
            if arr > res:
                res = arr
        return res


print(Solution().maxNumber([], [1], 1))
