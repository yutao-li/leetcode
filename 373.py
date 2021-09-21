from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        res = []
        heap = [(n + nums2[0], n, nums2[0], 0) for n in nums1]
        for _ in range(k):
            if not heap:
                break
            a, b, c, d = heap[0]
            res.append([b, c])
            if d == len(nums2) - 1:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (b + nums2[d + 1], b, nums2[d + 1], d + 1))
        return res


res = Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
