from heapq import heapify, heapreplace, heappop
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            i = heappop(sticks)
            merged = i + sticks[0]
            cost += merged
            heapreplace(sticks, merged)
        return cost
