from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        height = [(0, float('inf'))]
        vertical = sorted([(l, -h, r) for l, r, h in buildings] + list(set((r, 0, 0) for _, r, _ in buildings)))
        res = [[0, 0]]
        for l, neg_h, r in vertical:
            while l >= height[0][1]:
                heapq.heappop(height)
            if r:
                heapq.heappush(height, (neg_h, r))
            if res[-1][1] != -height[0][0]:
                res.append([l, -height[0][0]])
        return res[1:]


res = Solution().getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
