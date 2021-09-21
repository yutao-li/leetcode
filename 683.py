from typing import List
from bisect import bisect


class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        if len(bulbs) < 2:
            return -1
        on = sorted(bulbs[:2])
        if on[1] - on[0] == K + 1:
            return 2
        for d, i in enumerate(bulbs[2:], 3):
            pos = bisect(on, i)
            on.insert(pos, i)
            if pos and on[pos] - on[pos - 1] == K + 1:
                return d
            if pos < len(on) - 1 and on[pos + 1] - on[pos] == K + 1:
                return d
        return -1


print(Solution().kEmptySlots([6, 5, 8, 9, 7, 1, 10, 2, 3, 4], 2))
