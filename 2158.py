from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        jump = [0] * (10 ** 5 + 1)
        area = [0] * len(paint)
        for i, (start, end) in enumerate(paint):
            while start < end:
                if jump[start] == 0:
                    area[i] += 1
                nextPos = max(start + 1, jump[start])
                jump[start] = max(end, jump[start])
                start = nextPos
        return area
